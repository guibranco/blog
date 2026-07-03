---
layout: post
title: "18 serviços em 4 VMs de 1 GB: arquitetando no free tier sem sofrer"
date: 2026-07-03 22:00:00 +0100
categories: [infraestrutura]
tags: [devops, linux, nginx, arquitetura, self-hosted, free-tier]
lang: pt-BR
description: "Como distribuí quase vinte serviços PHP e .NET em quatro VMs gratuitas de 1 GB de RAM, com fila de mensagens, banco de dados, cache e hardening — sem estourar a memória."
image: /assets/img/posts/diagrama-capa.svg
---

Todo desenvolvedor com projetos pessoais chega nessa encruzilhada: os serviços se multiplicam — APIs, bots, dashboards, workers — e a conta da nuvem não pode multiplicar junto. No meu caso, o inventário chegou a **18 serviços**, entre PHP e C#/.NET, e a plataforma escolhida foi a **Oracle Cloud Infrastructure (OCI)**, rodando em **quatro instâncias VM.Standard.E2.1.Micro** — o shape AMD do free tier, com 1/8 de OCPU (burstável) e 1 GB de RAM cada.

Um gigabyte de RAM é pouco. Quatro gigabytes espalhados em quatro máquinas é menos ainda, porque cada uma paga o pedágio do sistema operacional. Este post documenta como organizei tudo: a distribuição de carga, as escolhas de middleware, a configuração de rede na OCI, o hardening antes do primeiro deploy e os ajustes de memória que fazem a diferença entre "funciona" e "o OOM killer derrubou o bot de trading às 3 da manhã".

## O free tier da OCI em números

Vale ser transparente sobre o que é gratuito de verdade. O **Always Free** da OCI inclui, em qualquer tenancy:

- **Duas** instâncias `VM.Standard.E2.1.Micro` (AMD, 1/8 OCPU burstável, 1 GB de RAM cada);
- Instâncias Ampere A1 (ARM): desde junho de 2026, o limite para tenancies Always Free caiu para o equivalente a **2 OCPUs e 12 GB de RAM** no total (eram 4 OCPUs / 24 GB — contas pagas ainda podem manter o teto antigo);
- **200 GB** de block storage no total, incluindo os boot volumes (cada VM nasce com ~47–50 GB, então quatro VMs consomem praticamente toda a cota);
- **20 GB** de Object Storage (compartilhados com o archive storage) e 10 TB/mês de egress;
- VCN, gateways, security lists e um Network Load Balancer, tudo dentro do free tier.

Repare no detalhe: o Always Free cobre **duas** E2.1.Micro. Como eu rodo quatro, a conta precisa estar no modo Pay As You Go — as duas primeiras continuam gratuitas para sempre, e as duas extras custam centavos por mês (o E2.1.Micro é o shape mais barato do catálogo). Se você quer ficar 100% no gratuito, a alternativa é trocar as quatro micro por **uma ou duas Ampere A1** — 12 GB de RAM em ARM acomodariam este stack inteiro com folga, ao custo de recompilar os binários .NET para `linux-arm64` e disputar a famosa loteria de capacidade ("out of capacity") das regiões populares.

## O sistema operacional: quanto menos, melhor

Recriei todas as VMs com a imagem **Canonical Ubuntu 24.04 Minimal** do catálogo da OCI. A imagem Minimal traz cerca de 30% menos pacotes e daemons que a padrão — e nesse cenário cada daemon ocioso é RAM que uma aplicação deixa de usar. Um detalhe que pega muita gente na hora de escolher a imagem: a variante `aarch64` é exclusiva das instâncias Ampere A1 (ARM). Nas E2.1.Micro, que são AMD x86_64, ela nem sequer inicializa.

## Dividir por papel, não por serviço

O erro clássico seria espalhar os serviços pelas máquinas até "caber". A abordagem que funcionou foi separar por **papel**: uma VM de borda, uma de dados e duas de aplicação — uma por runtime. Isso consolida os runtimes (um único pool PHP-FPM, uma única instalação do ASP.NET runtime), tira os dados da internet pública e dá a cada máquina um perfil de tuning coerente.

<figure>
  <img src="/assets/img/posts/free-tier-vms/diagrama-infraestrutura.svg" alt="Topologia da infraestrutura: VCN da OCI com sub-rede pública contendo a VM gateway e sub-rede privada com as VMs de dados, PHP e .NET" loading="lazy">
  <figcaption>Topologia da VCN: só o gateway tem IP público. Todo o resto vive em sub-rede privada.</figcaption>
</figure>

Na OCI, isso se traduz numa **VCN 10.0.0.0/16** com duas sub-redes: a **pública (10.0.0.0/24)**, ligada a um Internet Gateway, onde vive apenas a vm1; e a **privada (10.0.1.0/24)**, sem IPs públicos, onde ficam vm2, vm3 e vm4. A sub-rede privada sai para a internet (atualizações de pacote, chamadas a APIs externas) através de um **NAT Gateway** — também incluído no free tier — sem jamais aceitar conexões de entrada vindas de fora.

As security lists seguem o desenho: a sub-rede pública aceita apenas 443/TCP e 51820/UDP do mundo (mais 22/TCP restrito durante o bootstrap); a privada aceita tráfego apenas do CIDR da própria VCN. Uma dica de organização: para as regras por serviço (3306 para o MariaDB, 6379 para o Redis, 5672 para a fila), **Network Security Groups** são mais limpos que security lists — você anexa o NSG à VNIC de cada instância em vez de à sub-rede inteira.

Sobre a VPN de administração: escolhi **WireGuard em vez de OpenVPN** sem hesitar. Roda no kernel, ocupa uns 4 MB, não tem pilha TLS para administrar e vira o meu plano de administração — SSH, o banco e qualquer painel interno escutam apenas na interface do túnel, nunca na internet.

Uma exceção interessante na vm1: além do papel de borda, ela hospeda o **handler de webhooks** do meu bot de automação. É o único componente do bot que precisa aceitar tráfego público não solicitado, e o trabalho dele é trivial — validar a assinatura HMAC, publicar a mensagem na fila e devolver `202`. Com isso, a VM de aplicação .NET nunca precisa de ingresso público, e um pico de webhooks estoura na fila, não no worker.

## Fila, cache e banco: o que entra e o que fica de fora

Aqui as restrições de memória decidiram quase tudo sozinhas.

**RabbitMQ ficou de fora.** A VM Erlang dele ocupa de 150 a 400 MB em repouso — inaceitável numa máquina de 1 GB que ainda precisa rodar MariaDB. A substituição foi o **LavinMQ**, que fala o mesmo protocolo AMQP 0.9.1 (ou seja: nenhum cliente muda) e fica na casa dos 30 a 100 MB. Se nem isso couber no seu cenário, uma fila gerenciada externa resolve com custo zero de RAM local.

**etcd também ficou de fora**, por outro motivo: não há problema de consenso distribuído para resolver aqui. Configuração e segredos ficam num cofre próprio (um serviço leve de *configuration & secrets management* que roda na camada .NET), então o etcd seria redundância pura ocupando ~100 MB que não existem.

**MariaDB e Redis entraram**, ambos na vm2, ambos com rédea curta: um banco por aplicação no MariaDB com `innodb_buffer_pool_size` reduzido, e Redis com `maxmemory` fixado e política `allkeys-lru` para cache e rate limiting.

<figure>
  <img src="/assets/img/posts/free-tier-vms/diagrama-servicos.svg" alt="Camadas lógicas: consumidores passam pelo edge Nginx e chegam às camadas PHP e .NET, que dependem de MariaDB, Redis e LavinMQ" loading="lazy">
  <figcaption>A visão lógica: três origens de tráfego, um edge, dois runtimes, uma camada de dados compartilhada.</figcaption>
</figure>

O fluxo assíncrono que esse desenho esconde é justamente o mais valioso: webhook chega no handler (vm1) → mensagem publicada na fila (vm2) → worker de automação (vm4) consome no ritmo que 1/8 de OCPU permite. O cofre de configurações fecha o ciclo: cada serviço busca suas connection strings e segredos nele ao subir, então as credenciais do banco existem em exatamente um lugar.

## Quem roda onde

<figure>
  <img src="/assets/img/posts/free-tier-vms/diagrama-distribuicao.svg" alt="Mapa dos serviços por VM: gateway com Nginx e handler de webhooks; VM .NET com worker, cofre, bot de trading e APIs financeiras; VM PHP com ingestão de logs e APIs de dados; VM de dados com MariaDB, Redis e LavinMQ" loading="lazy">
  <figcaption>O mapa completo: cada serviço na máquina do seu runtime.</figcaption>
</figure>

A camada PHP é a mais tranquila: com PHP-FPM em `pm = ondemand` e `pm.max_children` baixo, aplicações ociosas custam praticamente zero — é por isso que uma única VM hospeda meia dúzia de APIs (ingestão de logs, APIs públicas de dados, utilitários, câmbio) sem drama.

A camada .NET é o ponto de pressão. Rodar seis ou mais processos Kestrel em 1 GB só funciona com tuning deliberado: `ServerGarbageCollection=false` (GC de workstation), `InvariantGlobalization=true`, `DOTNET_GCHeapHardLimitPercent` por serviço e **um runtime compartilhado** (publicação framework-dependent) em vez de binários self-contained, cada um carregando sua cópia do runtime. Com isso, cada API fica entre 70 e 100 MB. O bot de trading ganha proteção prioritária via systemd (`MemoryLow=`), porque é o único serviço em que um OOM kill custa dinheiro de verdade.

E se ainda assim apertar? A válvula de escape é o gateway: depois de Nginx, WireGuard e o handler, sobram uns 700 MB livres na vm1 — as duas APIs mais leves podem migrar para lá.

## Hardening antes de qualquer deploy

A ordem importa: rede e SSH primeiro, firewall depois, serviços por último. O checklist que segui em cada VM recém-criada:

1. **Security lists e NSGs na OCI** — a sub-rede pública só aceita 443/TCP e 51820/UDP; a privada só aceita tráfego do CIDR da VCN. Lembrando que na OCI o firewall tem **duas camadas** (a security list/NSG no plano de rede e o firewall dentro do host) — a porta só está aberta quando as duas concordam.
2. **SSH endurecido** — usuário próprio com chave, `PasswordAuthentication no`, `PermitRootLogin no`, `AllowUsers`, `MaxAuthTries 3`. Nas VMs privadas, o sshd escuta só na interface interna.
3. **Um dono para o firewall** — as imagens Ubuntu da OCI vêm com regras iptables persistentes pré-instaladas em `/etc/iptables/rules.v4` que rejeitam tráfego silenciosamente, brigando com o UFW. Escolha um dono (eu fiquei com o UFW), limpe as regras herdadas e configure do zero. Metade dos mistérios de "porta aberta no console da OCI mas connection refused" nasce exatamente aqui.
4. **UFW** — default deny na entrada; cada VM libera apenas as portas dos seus serviços e apenas para os CIDRs da VCN e do WireGuard. 3306 e 6379 jamais saem da rede privada.
5. **Fail2Ban só no gateway** — jails de `sshd` e Nginx. Nas VMs privadas ele é quase inútil (nada público chega lá) e a RAM economizada vale mais.
6. **Swap + zram — não pule esta** — 2 GB de swapfile com `vm.swappiness=10`, mais zram comprimido. Em VMs de 1 GB, é a diferença entre um momento lento e um serviço morto. Complementa com `MemoryMax=` e `Restart=always` nas units do systemd.
7. **Nginx + Certbot no gateway** — um `server` block por domínio, cada um com `proxy_pass` para o upstream na sub-rede privada, HTTP/2, `limit_req` nos endpoints públicos. Sobre painéis de administração do Nginx: minha recomendação é não instalar — com os configs versionados em git e `nginx -t && systemctl reload nginx`, você perde pouco e evita mais um daemon exposto na máquina mais visada.
8. **Rotina** — `unattended-upgrades` (só segurança), `chrony`, hostnames descritivos e backup noturno do MariaDB para o **OCI Object Storage** (os 20 GB do free tier dão de sobra para dumps comprimidos) via `mariadb-dump` + `rclone`.

## O que ficou de lição

Arquitetar para 1 GB de RAM é um exercício ótimo de disciplina. Cada escolha de middleware vira uma pergunta de orçamento ("esses 200 MB compram o quê?"), e a resposta quase sempre aponta para a opção mais simples: WireGuard em vez de OpenVPN, LavinMQ em vez de RabbitMQ, nenhum etcd, nenhum painel que um `git diff` substitui.

A separação por papel — borda, dados, PHP, .NET — foi o que fez o conjunto caber. E o subproduto inesperado é que a topologia final é mais segura do que a versão "cada serviço na sua VM com IP público" jamais seria: uma única porta de entrada, dados isolados, administração por VPN, e a sub-rede privada saindo para o mundo apenas pelo NAT Gateway.

Se você está montando algo parecido no free tier da OCI, espero que o mapa acima economize algumas madrugadas. E se o OOM killer visitar você mesmo assim — bem-vindo ao clube, o swap manda lembranças.
