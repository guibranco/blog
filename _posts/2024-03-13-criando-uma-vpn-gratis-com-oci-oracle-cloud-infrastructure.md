---
layout: post
title: "Criando uma VPN grátis com OCI (Oracle Cloud Infrastructure)"
description: "Passo a passo completo para criar sua própria VPN pessoal usando o plano Always Free da Oracle Cloud — com PiVPN (WireGuard ou OpenVPN), UFW, fail2ban e dicas de manutenção de segurança."
date: 2024-03-13
categories: [Infraestrutura]
subcategories:
  - "Infraestrutura/Cloud"
  - "Infraestrutura/DevOps"
tags: [always-free, cloud, free-tier, hospedagem, hosting, iaas, network, networking, oci, openvpn, oracle, provider, vpn, wireguard, pivpn, ubuntu, linux, ssh, ufw, fail2ban, seguranca, firewall, servidor]
reading_time: 12
image: /assets/img/posts/vpn.jpg
---

<p class="lead">Moro fora do Brasil e, em diversas situações, preciso acessar serviços brasileiros que bloqueiam conexões vindas do exterior por questões de segurança. Foi pesquisando uma solução gratuita que descobri como usar uma VM do <strong>OCI (Oracle Cloud Infrastructure)</strong> para instalar o <strong>WireGuard</strong> ou o <strong>OpenVPN</strong> via <strong>PiVPN</strong> e conseguir, sem pagar nada, um endereço de IP no país que eu precisar.</p>

<div class="callout callout-tip">
  <div class="callout-label">Cartão de crédito necessário — mas nada é cobrado</div>
  O plano Always Free exige um cartão de crédito válido <strong>(cartões pré-pagos ou de débito não são aceitos)</strong>. Uma pequena cobrança de verificação (menos de 10 unidades da moeda local) é feita e estornada automaticamente assim que a conta é validada. Enquanto você permanecer no plano Always Free e dentro dos limites, <strong>nenhum valor será cobrado</strong>. O cartão é apenas para evitar contas falsas — cada pessoa tem direito a uma conta Always Free.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>O que o plano Always Free oferece?</h2></div>
</div>

A Oracle Cloud oferece, permanentemente e sem prazo de expiração, os seguintes recursos no plano Always Free:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">2 VMs AMD</div>
    <div class="provider-detail">Instâncias <code>VM.Standard.E2.1.Micro</code> com 1 OCPU e 1 GB de RAM cada — mais que suficiente para uma VPN pessoal.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">10 TB de tráfego/mês</div>
    <div class="provider-detail">Largura de banda de saída muito acima do necessário para uso pessoal de VPN.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">IP público fixo</div>
    <div class="provider-detail">É possível reservar um endereço IP público estático — gratuito enquanto associado a uma instância ativa.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Armazenamento em bloco</div>
    <div class="provider-detail">200 GB total de armazenamento em bloco entre todas as instâncias.</div>
  </div>
</div>

Confira a lista completa de recursos gratuitos na [documentação oficial](https://docs.oracle.com/pt-br/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm){:target="_blank"}.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Passo 1 — Criar a conta no OCI</h2></div>
</div>

Acesse [oracle.com/br/cloud/free](https://www.oracle.com/br/cloud/free/){:target="_blank" rel="nofollow noopener"} e clique em **Iniciar gratuitamente**.

Durante o cadastro, preste atenção nos seguintes pontos:

**Endereço:** use exatamente o mesmo endereço cadastrado no cartão de crédito que você vai utilizar. Divergências causam falha na verificação do pagamento.

**Região do datacenter (Home Region):** esta é a escolha mais importante de todo o processo.

<div class="callout callout-warn">
  <div class="callout-label">A escolha da região NÃO pode ser alterada depois</div>
  Escolha o datacenter do país cujo IP você deseja ter. Se quiser um IP brasileiro, selecione <strong>Brazil East (São Paulo)</strong>. Para acessar serviços do Reino Unido (ex.: jogos no Xbox/PlayStation), selecione um datacenter britânico. Essa decisão é permanente para a conta.
</div>

**Verificação do cartão:** uma cobrança de verificação será feita (menos de 10 unidades da moeda local — ex: R$ 3–7, €5–7, £5). O valor é estornado automaticamente após a validação.

<div class="callout callout-tip">
  <div class="callout-label">Falha na verificação?</div>
  Se a validação do cartão falhar, envie um e-mail para o suporte da Oracle. No meu caso, resolveram em menos de 48 horas e pude continuar o cadastro normalmente.
</div>

Após criar a conta, ative o **2FA (autenticação de dois fatores)** imediatamente em Perfil → Configurações de segurança. Ative o 2FA em todos os serviços que utilizar na internet.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Passo 2 — Criar a instância de computação</h2></div>
</div>

No console da OCI, acesse **Compute → Instances → Create Instance**.

**Nome:** dê um nome descritivo, como `vpn-server`.

**Availability Domain:** clique em **Edit** na seção Placement e selecione um domínio marcado como **Always Free eligible**.

**Imagem:** clique em **Edit** em Image and Shape → Change image → selecione **Canonical Ubuntu 22.04** (ou 20.04).

**Shape:** clique em **Change shape** → selecione **VM.Standard.E2.1.Micro** (o único shape Always Free para AMD).

**Rede (VCN):** clique em **Edit** na seção Networking. Se não tiver uma VCN criada, o console oferece criar uma automaticamente. Em **Public IPv4 address**, selecione **Assign a public IPv4 address** — você vai reservar um IP fixo no próximo passo.

**Chaves SSH:** em **Add SSH keys**, clique em **Generate a key pair for me** e faça o download das chaves privada e pública. Guarde o arquivo `.key` em local seguro — ele é sua única forma de acesso à VM.

Clique em **Create** e aguarde a instância iniciar (status: **Running**).

### Reservar um IP público fixo

Por padrão, o IP público pode mudar se a instância for reiniciada. Para fixá-lo:

1. Na página da instância, acesse **Resources → Attached VNICs**
2. Clique no nome da VNIC → **IPv4 Addresses**
3. Nos três pontos ao lado do IP, clique em **Edit**
4. Selecione **Reserved IP address**, dê um nome e confirme

O IP agora é fixo e permanecerá o mesmo enquanto estiver associado à instância.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Passo 3 — Abrir as portas na VCN (Security List)</h2></div>
</div>

A OCI tem dois níveis de firewall: as **Security Lists** da VCN (controle de rede) e o **firewall da própria instância** (UFW/iptables, configurado mais à frente). Ambos precisam estar liberados.

Na página da instância, acesse **Resources → Attached VNICs → nome da subnet → Security Lists**.

Adicione as seguintes **Ingress Rules**:

<table class="compare-table">
  <thead>
    <tr><th>Protocolo</th><th>Porta</th><th>CIDR de origem</th><th>Finalidade</th></tr>
  </thead>
  <tbody>
    <tr><td>TCP</td><td>22</td><td>0.0.0.0/0</td><td>SSH</td></tr>
    <tr><td>UDP</td><td>51820</td><td>0.0.0.0/0</td><td>WireGuard</td></tr>
    <tr><td>UDP</td><td>1194</td><td>0.0.0.0/0</td><td>OpenVPN</td></tr>
    <tr><td>TCP</td><td>1194</td><td>0.0.0.0/0</td><td>OpenVPN (TCP fallback)</td></tr>
  </tbody>
</table>

Para as **Egress Rules**, adicione uma regra permitindo todo o tráfego de saída (protocolo: All, destino: 0.0.0.0/0) — normalmente já existe por padrão.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Passo 4 — Conectar via SSH</h2></div>
</div>

### Linux / macOS / Windows (PowerShell)

```bash
# Ajuste as permissões do arquivo de chave (obrigatório no Linux/macOS)
chmod 600 /caminho/para/sua-chave.key

# Conectar
ssh -i /caminho/para/sua-chave.key ubuntu@SEU_IP_PUBLICO
```

### Windows com PuTTY

1. Abra o **PuTTYgen**, clique em **Load key** e selecione o arquivo `.key` baixado
2. Clique em **Save private key** — isso gera um arquivo `.ppk`
3. Abra o **PuTTY**, informe o IP público, vá em **Connection → SSH → Auth** e selecione o `.ppk`
4. Conecte com o usuário `ubuntu`

<div class="callout callout-tip">
  <div class="callout-label">Dica para Windows — use o PowerShell</div>
  O Windows 10/11 já inclui um cliente SSH nativo. O PowerShell ou o Windows Terminal dispensam o PuTTY para a maioria dos casos.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Passo 5 — Atualizar o sistema e configurar segurança</h2></div>
</div>

### Atualizar pacotes do sistema

Sempre execute estas etapas logo após conectar em uma instância nova — e regularmente depois:

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
sudo apt-get autoclean
```

<div class="callout callout-tip">
  <div class="callout-label">Automatize as atualizações semanalmente</div>
  Adicione uma tarefa no cron para manter o sistema sempre atualizado sem intervenção manual:

```bash
sudo crontab -e
```

Adicione esta linha (executa todo domingo às 02h00):

```bash
0 2 * * 0 apt-get update && apt-get upgrade -y && apt-get autoremove -y && apt-get autoclean
```

Alternativamente, ative o <strong>unattended-upgrades</strong> para aplicar patches de segurança automaticamente:

```bash
sudo apt-get install unattended-upgrades -y
sudo dpkg-reconfigure --priority=low unattended-upgrades
```
</div>

### Configurar o UFW (Uncomplicated Firewall)

O Ubuntu inclui o UFW, que facilita a gestão do firewall local da instância.

```bash
# Instalar o UFW (geralmente já está instalado)
sudo apt-get install ufw -y

# Política padrão: bloquear tudo que entra, permitir tudo que sai
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Liberar SSH (IMPORTANTE: faça isso ANTES de ativar o UFW)
sudo ufw allow 22/tcp

# Liberar WireGuard
sudo ufw allow 51820/udp

# Liberar OpenVPN
sudo ufw allow 1194/udp
sudo ufw allow 1194/tcp

# Ativar o UFW
sudo ufw enable

# Verificar status
sudo ufw status verbose
```

<div class="callout callout-warn">
  <div class="callout-label">Instâncias OCI — iptables legado</div>
  Instâncias Ubuntu na OCI têm regras de <strong>iptables pré-configuradas</strong> que podem bloquear o tráfego da VPN mesmo com o UFW ativado e a Security List liberada. Execute os comandos abaixo para garantir que os pacotes VPN passem:

```bash
# Liberar portas via iptables (necessário no OCI)
sudo iptables -I INPUT -p udp --dport 51820 -j ACCEPT   # WireGuard
sudo iptables -I INPUT -p udp --dport 1194 -j ACCEPT    # OpenVPN UDP
sudo iptables -I INPUT -p tcp --dport 1194 -j ACCEPT    # OpenVPN TCP

# Persistir as regras entre reinicializações
sudo apt-get install iptables-persistent -y
sudo netfilter-persistent save
```
</div>

### Instalar e configurar o fail2ban

O **fail2ban** monitora os logs do sistema e bane automaticamente IPs que fazem muitas tentativas de login com falha — proteção essencial contra ataques de força bruta no SSH.

```bash
# Instalar
sudo apt-get install fail2ban -y

# Criar arquivo de configuração local (não edite o .conf original)
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
```

Localize a seção `[sshd]` e configure:

```ini
[sshd]
enabled  = true
port     = 22
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 5
bantime  = 3600
findtime = 600
```

- **maxretry:** número de falhas de login antes do ban (5 é um bom valor)
- **bantime:** duração do ban em segundos (3600 = 1 hora)
- **findtime:** janela de tempo para contar as tentativas (600 = 10 minutos)

```bash
# Reiniciar o fail2ban para aplicar as configurações
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban

# Verificar status
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Passo 6 — Instalar a VPN com PiVPN</h2></div>
</div>

O **PiVPN** ([github.com/pivpn/pivpn](https://github.com/pivpn/pivpn){:target="_blank"}) é um instalador interativo que automatiza toda a configuração do WireGuard ou OpenVPN. É a forma mais simples, segura e atualizada de instalar uma VPN em um servidor Ubuntu.

```bash
curl -L https://install.pivpn.io | bash
```

O instalador vai guiar você por um assistente interativo. As escolhas recomendadas:

<table class="compare-table">
  <thead>
    <tr><th>Etapa</th><th>WireGuard (recomendado)</th><th>OpenVPN (alternativa)</th></tr>
  </thead>
  <tbody>
    <tr><td>Protocolo</td><td>WireGuard</td><td>OpenVPN</td></tr>
    <tr><td>Porta</td><td>51820 (UDP)</td><td>1194 (UDP) ou 1194 (TCP)</td></tr>
    <tr><td>DNS</td><td>Google (8.8.8.8) ou Cloudflare (1.1.1.1)</td><td>Idem</td></tr>
    <tr><td>IP do servidor</td><td>Seu IP público reservado</td><td>Idem</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">WireGuard vs OpenVPN — qual escolher?</div>
  <strong>WireGuard</strong> é mais moderno, mais rápido, usa menos recursos e é mais simples de configurar. É a escolha certa para a maioria dos casos de uso pessoal. <strong>OpenVPN</strong> é mais compatível com redes corporativas e alguns firewalls restritivos que bloqueiam UDP — nesse caso, usar OpenVPN na porta 443/TCP pode contornar bloqueios.
</div>

### Adicionar um cliente (perfil)

Após a instalação, adicione um perfil para o seu dispositivo:

```bash
# WireGuard
pivpn wg add

# OpenVPN
pivpn ovpn add
```

O PiVPN vai gerar um arquivo de configuração (`.conf` para WireGuard, `.ovpn` para OpenVPN) e também exibir um **QR Code** no terminal — basta escanear com o aplicativo do celular.

### Listar clientes e verificar conexões

```bash
# Listar perfis criados
pivpn -l

# Verificar clientes conectados (WireGuard)
pivpn wg

# Verificar clientes conectados (OpenVPN)
pivpn ovpn
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Passo 7 — Configurar o cliente VPN</h2></div>
</div>

### Baixar o arquivo de configuração

Os perfis gerados ficam em `/home/ubuntu/configs/`. Transfira para o seu dispositivo:

**Via SCP (linha de comando):**
```bash
# No seu computador local
scp -i /caminho/sua-chave.key ubuntu@SEU_IP:/home/ubuntu/configs/meu-perfil.conf .
```

**Via FileZilla (interface gráfica):**
1. Protocolo: **SFTP**
2. Host: seu IP público
3. Porta: 22
4. Tipo de autenticação: **Arquivo de chave** → selecione o `.ppk` gerado pelo PuTTYgen
5. Navegue até `/home/ubuntu/configs/` e baixe o arquivo

### Instalar o cliente VPN

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Windows / macOS</div>
    <div class="provider-detail"><strong>WireGuard:</strong> <a href="https://www.wireguard.com/install/" target="_blank">wireguard.com/install</a><br><strong>OpenVPN:</strong> <a href="https://openvpn.net/vpn-client/" target="_blank">OpenVPN Connect</a></div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Android / iOS</div>
    <div class="provider-detail"><strong>WireGuard:</strong> disponível na Play Store e App Store<br><strong>OpenVPN:</strong> OpenVPN Connect na Play Store e App Store</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Linux</div>
    <div class="provider-detail"><code>sudo apt install wireguard</code><br>ou<br><code>sudo apt install openvpn network-manager-openvpn</code></div>
  </div>
</div>

Importe o arquivo `.conf` (WireGuard) ou `.ovpn` (OpenVPN) no cliente e conecte. Para celulares com WireGuard, o PiVPN exibe um **QR Code** diretamente no terminal — basta escanear:

```bash
pivpn wg -qr nome-do-perfil
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Manutenção contínua</h2></div>
</div>

Uma instância VPN é um servidor na internet — precisa de manutenção regular para se manter segura.

```bash
# Atualizar o sistema manualmente (execute mensalmente no mínimo)
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y

# Atualizar o PiVPN
pivpn update

# Verificar IPs banidos pelo fail2ban
sudo fail2ban-client status sshd

# Desbanir um IP específico (caso necessário)
sudo fail2ban-client set sshd unbanip 1.2.3.4

# Verificar o status dos serviços
sudo systemctl status wg-quick@wg0   # WireGuard
sudo systemctl status openvpn        # OpenVPN
sudo systemctl status fail2ban
sudo systemctl status ufw
```

<div class="callout callout-tip">
  <div class="callout-label">Cron com envio de notificação por e-mail</div>
  Se quiser receber um relatório das atualizações por e-mail, instale o <code>mailutils</code> e adicione <code>MAILTO=seu@email.com</code> no topo do crontab. Útil para confirmar que as atualizações automáticas estão funcionando.
</div>

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>VPN pessoal, gratuita e sob seu controle</h2>
  <p>Com o plano Always Free da Oracle Cloud, é possível ter um servidor VPN próprio com IP do país que você precisar — completamente gratuito, sem anúncios, sem logs e sem limites artificiais de velocidade. O PiVPN simplifica a instalação do WireGuard ou OpenVPN para alguns minutos, e a combinação de UFW + fail2ban garante que o servidor permaneça seguro contra tentativas de invasão.</p>
  <p>A mesma abordagem funciona em outros provedores de nuvem com free tier — AWS e Azure oferecem instâncias gratuitas por 12 meses, com limites de banda menores (≈ 100 GB/mês). Para uso pessoal e de longo prazo, o Always Free da OCI é a melhor opção disponível hoje.</p>
</div>
