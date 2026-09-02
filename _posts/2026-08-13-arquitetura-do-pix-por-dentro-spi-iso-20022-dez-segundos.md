---
layout: post
lang: pt-BR
title: "A arquitetura do PIX vista por dentro: SPI, ISO 20022 e um orçamento de dez segundos"
description: "Como funciona o PIX do lado do Banco Central e do lado de um participante direto: SPI, DICT, mensageria ISO 20022 sobre a RSFN, os percentis do Manual de Tempos e as decisões de arquitetura por trás de .NET, RabbitMQ, MS SQL e CouchDB."
date: 2026-08-13
categories: [Coding]
subcategories:
  - "Coding/Architecture"
tags: [pix, arquitetura, architecture, iso-20022, dotnet, rabbitmq, sistemas-financeiros, financial-systems, banco-central, central-bank]
medium_tags: [pix, software-architecture, dotnet, rabbitmq, fintech]
reading_time: 20
cover: /assets/img/posts/pix-arquitetura-capa.svg
image: /assets/img/posts/pix-arquitetura-capa.png
series: pix-bs2
series_title: Desenvolvendo o PIX
series_part: 3
---

<p class="lead">O PIX é um dos poucos sistemas em que a latência aceitável está publicada em norma, por percentil, e auditada mensalmente. Este texto é sobre o que isso faz com a arquitetura de quem precisa caber ali dentro — do lado do Banco Central e do lado de um participante direto.</p>

<div class="callout callout-tip">
  <div class="callout-label">Este é o terceiro de três textos</div>
  A história de como eu fui parar nesse projeto e como o time foi remontado no meio do caminho está na <a href="{{ site.baseurl }}/artigos/construindo-o-pix-no-bs2-bastidores-de-um-prazo-do-banco-central/">primeira parte, sobre os bastidores de um prazo do Banco Central</a>. A anatomia do contrato — valor fixo, sobreaviso e o mês de sete dias por semana — está na <a href="{{ site.baseurl }}/artigos/contrato-do-pix-valor-fixo-sobreaviso-e-a-hora-que-nao-existia/">segunda parte, sobre o contrato do PIX</a>. Aqui o assunto é técnico do início ao fim.
</div>

<div class="callout callout-warn">
  <div class="callout-label">O que é público e o que não é</div>
  Mensagens, componentes, percentis e cronograma são públicos e estão no material do Banco Central, linkado no final. Nomes internos de sistemas, módulos e topologia ficam de fora, e os diagramas deste post foram redesenhados do zero para ilustrar o conceito, não a implementação de ninguém.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>A arquitetura do lado do Banco Central</h2></div>
</div>

Vale começar por aqui porque tudo do lado do banco é consequência disso.

O PIX não é um sistema único. São dois sistemas principais, com papéis bem separados:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">SPI — Sistema de Pagamentos Instantâneos (o PIX)</div>
    <div class="provider-detail">Onde o dinheiro se move. Liquida transação a transação, sem janela de fechamento e sem ciclo de compensação. Cada participante direto mantém uma <strong>Conta PI</strong> no BC, e a transação só acontece se houver saldo nela — ver o quadro abaixo.</div>
    <div class="provider-price">Mensageria ISO 20022 em XML</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">DICT — Diretório de Identificadores de Contas Transacionais</div>
    <div class="provider-detail">Onde as identidades são resolvidas. Guarda o vínculo entre chave (CPF/CNPJ, e-mail, telefone, chave aleatória) e conta transacional. Inclui reivindicação de posse e portabilidade de chave.</div>
    <div class="provider-price">Operado pelo próprio BC</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">O que é a Conta PI, e por que ela muda tudo</div>
  <p>No <strong>SPB — Sistema de Pagamentos Brasileiro</strong>, por onde passam TED e DOC, os bancos liquidam contra a conta de <em>Reservas Bancárias</em> no Banco Central, dentro de grades de horário e com o sistema fechando à noite e no fim de semana.</p>
  <p>O <strong>SPI</strong>, arranjo sobre o qual o PIX roda, criou uma conta separada para isso: a <strong>Conta PI</strong>, de Pagamentos Instantâneos. Cada participante direto mantém a sua no BC e a abastece antecipadamente, transferindo saldo da conta de Reservas. É contra ela que o SPI debita e credita, transação a transação, sem compensação e sem ciclo de fechamento.</p>
  <p>A consequência prática é dura: <strong>não existe cheque especial no SPI</strong>. Se a Conta PI não tem saldo no instante da ordem, a transação não liquida — não importa quanto o cliente tenha na conta corrente dele nem quão correto esteja o seu código. Provisionar essa liquidez 24 horas por dia, sete dias por semana, vira função operacional permanente.</p>
</div>

A comunicação com essa infraestrutura acontece exclusivamente pela **RSFN** — a Rede do Sistema Financeiro Nacional. Rede dedicada, fora da internet pública, com autenticação por certificado ICP-Brasil e validação de formato e assinatura em cada mensagem.

Isso muda tudo no modelo mental de quem vem de web. Não existe "chamar uma API e tratar o erro 500". Existe um protocolo de mensageria financeira com ordem de campos, schema validado, assinatura digital e um catálogo de erros que você precisa mapear inteiro. As mensagens centrais da iniciação são a `pacs.008`, que carrega a ordem de pagamento com pagador, recebedor, valor e o `EndToEndId` — o identificador único da transação, gerado na origem e que acompanha a operação até o fim — e a `pacs.002`, que devolve o status.

Do lado da infraestrutura do próprio BC, a escolha foi pública e interessante: o edital já definia uma arquitetura distribuída baseada em Apache Kafka, e a solução contratada foi a stack open source da Red Hat — AMQ Streams (Kafka), OpenShift e Ansible Automation Platform. Em teste, com volume de 2 mil transações por segundo, 99% foram processadas em menos de quatro segundos.

<div class="callout callout-tip">
  <div class="callout-label">O detalhe que dita o resto</div>
  Tudo isso roda 24 horas por dia, todos os dias, sem janela de fechamento. E o "dez segundos" que virou slogan do PIX não é uma meta vaga: é um percentil publicado em norma, com o ciclo inteiro fatiado em marcos temporais medidos por cada participante. É esse orçamento que dita a arquitetura interna do banco — vale olhar os números antes de olhar a solução.
</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O orçamento de latência, em números</h2></div>
</div>

O Banco Central não pediu "seja rápido". Ele publicou o **Manual de Tempos do Pix**, que fatia o ciclo de liquidação em marcos e define acordo de nível de serviço **por percentil** sobre a diferença entre eles. Os marcos são estes: `t0'` é quando o PSP do pagador recebe a confirmação do usuário; `t1` é quando ele cria a `pacs.008` — medido **antes** da assinatura; `t1'` é quando o SPI recebe a requisição; `t2` é quando o SPI disponibiliza a mensagem ao PSP do recebedor; `t3'` é quando o SPI recebe a `pacs.002`; `t4` é a liquidação, a troca de saldos entre as Contas PI; `t5a` é quando a `pacs.002` fica disponível para o pagador; e `t6a` é quando o pagador é notificado.

<div class="callout callout-warn">
  <div class="callout-label">Estes são os números vigentes hoje, não os de 2020</div>
  A primeira versão do Manual de Tempos saiu em 11 de agosto de 2020, no meio do projeto, e o documento já passou por sete revisões. Algumas mudaram bastante a régua: em julho de 2021 vários indicadores tiveram o percentil reduzido de 99% para 95%, e as metas de disponibilidade foram revistas. A tabela abaixo é a foto atual, útil para entender a forma do problema — não é a régua exata que estava na nossa mesa.
</div>

<table class="compare-table">
  <thead>
    <tr><th>Indicador</th><th>Percentil</th><th>Tempo</th></tr>
  </thead>
  <tbody>
    <tr><td>Iniciação pelo PSP do pagador (<code>t1 − t0'</code>)</td><td>P50</td><td>0,9 s</td></tr>
    <tr><td>Iniciação pelo PSP do pagador (<code>t1 − t0'</code>)</td><td>P95</td><td>1,5 s</td></tr>
    <tr><td>Autorização pelo PSP do recebedor (<code>t3' − t2</code>)</td><td>P50</td><td>1,4 s</td></tr>
    <tr><td>Autorização pelo PSP do recebedor (<code>t3' − t2</code>)</td><td>P95</td><td>2,3 s</td></tr>
    <tr><td><strong>Experiência do usuário pagador (<code>t6a − t0'</code>)</strong></td><td>P50</td><td>6,0 s</td></tr>
    <tr><td><strong>Experiência do usuário pagador (<code>t6a − t0'</code>)</strong></td><td>P99</td><td>10,0 s</td></tr>
    <tr><td>Consulta ao DICT, visão do usuário</td><td>P99</td><td>2,0 s</td></tr>
    <tr><td>Tempo dentro do SPI (<code>t2 − t1'</code>) + (<code>t5a − t3'</code>)</td><td>P50</td><td>2,8 s</td></tr>
    <tr><td>Tempo dentro do SPI (<code>t2 − t1'</code>) + (<code>t5a − t3'</code>)</td><td>P99</td><td>4,6 s</td></tr>
    <tr><td>Consulta de chaves no DICT, lado do BC</td><td>P99</td><td>1,0 s</td></tr>
    <tr><td>Atualização de chaves no DICT, lado do BC</td><td>P99</td><td>5,0 s</td></tr>
  </tbody>
</table>

<img
  src="{{ site.baseurl }}/assets/img/posts/pix-manual-de-tempos.svg"
  alt="Gráfico de barras dos acordos de nível de serviço do Manual de Tempos do Pix. Obrigações do participante: iniciação pelo PSP do pagador, 0,9s no P50 e 1,5s no P95; autorização pelo PSP do recebedor, 1,4s no P50 e 2,3s no P95; consulta ao DICT na visão do usuário, 2,0s no P99; experiência do usuário pagador, 6,0s no P50 e 10,0s no P99. Obrigações do Banco Central: tempo dentro do SPI, 2,8s no P50 e 4,6s no P99; consulta de chaves no DICT, 1,0s no P99; atualização de chaves no DICT, 5,0s no P99. Acima de tudo, um teto duro de 40 segundos no canal primário, além do qual o SPI rejeita a transação."
  style="width:100%;max-width:900px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Vale parar na linha em negrito. Os "dez segundos" que viraram slogan do PIX são o **P99 da experiência do usuário pagador** — a mediana pactuada é 6 segundos. E existe um teto duro por cima de tudo: um PIX enviado ao canal primário de mensagens tem limite máximo de **40 segundos** entre a ordem do usuário e a liquidação. Passou disso, o próprio SPI rejeita a transação e comunica os participantes.

<div class="callout callout-tip">
  <div class="callout-label">Percentil não é média, e a diferença é o projeto inteiro</div>
  Uma média de 1,2 segundo esconde uma cauda horrível. Um P95 de 1,5 segundo, não. O P95 é onde moram pausa de garbage collector, reconexão de conexão de fila, cold start de processo, retry de DNS, lock de tabela em pico e o primeiro request depois de um deploy. Projetar para a média te dá um sistema que passa em homologação; projetar para a cauda te dá um sistema que passa em auditoria.
</div>

Do lado do participante, o roteiro de participação direta traz um número que **não é um acordo de nível de serviço permanente, e sim critério de aprovação no teste de capacidade**: durante o teste, a instituição precisava consumir em até 200 milissegundos no mínimo 99% das mensagens `pacs.008` e `pacs.002` disponibilizadas pelo SPI, além de demonstrar recebimento de pelo menos 50% das ordens em 1,4 segundo e 95% em 2,3 segundos. Ainda assim, o número diz muito sobre o desenho esperado. Repare no verbo: as mensagens são *disponibilizadas* e você as *consome*. Isso empurra a arquitetura para um modelo de consumo contínuo e agressivo, não de espera passiva.

E havia o teste de capacidade, que na nossa época estava na Carta Circular 4.055: enviar mensagens `pacs.008` distribuídas uniformemente ao longo de dez minutos — 10 mil, 20 mil ou 40 mil, conforme a faixa de contas transacionais do PSP — e depois receber o mesmo volume, acatando cada uma com sua `pacs.002`. Não é um teste que você passa raspando: ou a arquitetura absorve, ou você reprova e agenda de novo com o BC.

<div class="callout callout-warn">
  <div class="callout-label">O requisito que ninguém vê chegando</div>
  Para apurar esses indicadores, o Manual de Tempos exige que os relógios dos servidores dentro da instituição estejam sincronizados a ponto de não distorcer a medição — e proíbe usar relógios de instituições diferentes na apuração, justamente porque uma pequena diferença já falsearia o número. Ou seja: sincronização de tempo deixa de ser detalhe de infraestrutura e vira item de conformidade. Foi a primeira vez que eu vi NTP virar assunto de reunião com jurídico.
</div>

E, fechando o pacote, há meta de disponibilidade por categoria — e a categoria não é definida por porte da instituição, e sim pela **participação do participante no total de transações Pix liquidadas no SPI no ano anterior**. As faixas atuais vão de 99,5% para quem responde por mais de 2% do total a 95,0% para os demais, com o BC se comprometendo com 99,9% no SPI. Como o índice do participante direto **inclui as transações dos indiretos que ele liquida**, a disponibilidade de quem usa a sua infraestrutura entra na sua nota. Guarde essa frase para a seção do PIX Indireto.

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>A arquitetura do lado do banco</h2></div>
</div>

Do lado de dentro, a plataforma foi construída em **.NET**, com **RabbitMQ** como barramento de mensagens, **MS SQL Server** para o estado transacional e **CouchDB** para documentos e payloads — as representações inteiras de cobranças, QR Codes e mensagens, que não cabem confortavelmente num modelo relacional normalizado e que você precisa guardar exatamente como chegaram, para auditoria.

### Por que .NET

A resposta honesta é a menos glamourosa: **porque já era a stack do banco e o time inteiro era .NET**. Não houve prova de conceito, benchmark comparativo nem estudo de linguagem. Havia sete meses e um prazo publicado em norma.

Isso não é preguiça de arquitetura, é aritmética. Trocar de stack num projeto com data fixa significa gastar as primeiras semanas em curva de aprendizado, ferramental, pipeline, padrão de log, biblioteca de acesso a dados e — o mais caro — na descoberta dos modos de falha que a equipe ainda não conhece. Num sistema onde o P95 é requisito auditável, você não quer estar aprendendo o comportamento do coletor de lixo da plataforma nova em novembro. A stack que o time domina tem uma vantagem que nenhum benchmark mede: quando algo trava em produção às três da manhã, alguém sabe onde olhar.

<div class="callout callout-tip">
  <div class="callout-label">A regra que eu tiraria daqui</div>
  Prazo externo e curto é o pior momento possível para adotar tecnologia nova. A escolha "chata" — o que o time já roda, já monitora e já sabe depurar — quase sempre vence a escolha "certa" nesse contexto. Guarde a migração de stack para quando o cronograma for seu.
</div>

### Por que uma fila, e por que RabbitMQ

Aqui a decisão foi de forma, não de marca. O que o problema pedia era um **barramento de mensagens**, por quatro razões que vêm direto das restrições das seções anteriores.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Isolar a borda que muda por decreto</div>
    <div class="provider-detail">A fila é o contrato interno estável entre os serviços de domínio e o gateway RSFN. Correção de schema publicada pelo BC bate na borda, não nos cinco serviços atrás dela.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">24/7 sem janela de manutenção</div>
    <div class="provider-detail">O sistema não pode parar para deploy. Com a fila no meio, derrubar um consumidor não derruba o fluxo: as mensagens se acumulam e são drenadas quando ele volta. Sem fila, cada restart vira erro na cara do cliente.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Contrapressão e retentativa de graça</div>
    <div class="provider-detail">Pico de volume vira profundidade de fila, não conexão recusada. O broker entrega as <em>primitivas</em> — <em>dead-letter exchange</em>, TTL, reentrega —, não uma política pronta: limite de tentativas, espera crescente, tratamento de mensagem venenosa e garantia de encaminhamento continuam sendo decisão de topologia, de configuração e de código seu. E, como a reentrega é o mecanismo, a idempotência segue obrigatória.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Escala horizontal para o teste de capacidade</div>
    <div class="provider-detail">Consumidores concorrentes na mesma fila são a forma mais barata de multiplicar vazão. Quarenta mil <code>pacs.008</code> em dez minutos é um problema de quantidade de consumidores, não de otimização de código.</div>
  </div>
</div>

RabbitMQ especificamente porque roteamento era o que faltava. O tráfego não é um fluxo único: são `pacs.008` de saída, `pacs.008` de entrada, `pacs.002` nos dois sentidos, devoluções, mensagens de cadastro e avisos operacionais. Um *exchange* com chave de roteamento resolve isso declarativamente — cada tipo de mensagem chega no consumidor certo sem que ninguém escreva um `switch` gigante no meio do caminho. Some a isso que era um broker que o banco já operava, e a decisão praticamente se toma sozinha.

<div class="callout callout-warn">
  <div class="callout-label">O que a fila não resolve, e que morde depois</div>
  Broker não te dá entrega exatamente uma vez nem ordem global — te dá <em>pelo menos uma vez</em> e ordem apenas dentro de uma fila. Toda a correção do sistema volta a depender da idempotência ancorada no <code>EndToEndId</code>. E há um custo real de latência: cada salto pela fila gasta milissegundos de um orçamento em que o P50 da iniciação é 0,9 segundo. Por isso nem tudo vira mensagem — o que está no caminho síncrono da resposta ao usuário, como a consulta de chave, paga o preço de ser síncrono; o que pode ser assíncrono, como o trânsito até a borda, ganha a fila.
</div>

### O que o PIX tinha que devolver para dentro do banco

Uma coisa que eu não esperava era quanto do trabalho não tinha nada a ver com o usuário final. Um participante direto não precisa apenas mover dinheiro: precisa **prestar contas do movimento para dentro da própria instituição**, e isso vira requisito de engenharia como qualquer outro.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Antifraude e PLD/AML</div>
    <div class="provider-detail">Controles obrigatórios que entram no caminho da transação. Não são "integrações opcionais" — são condição de operar, e precisam caber no orçamento de latência.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Tesouraria</div>
    <div class="provider-detail">Precisa enxergar a posição da Conta PI para provisionar liquidez, inclusive de madrugada e no fim de semana, quando o PIX opera e o resto do banco não.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Controladoria e contabilidade</div>
    <div class="provider-detail">Balancete e fechamento dependem de que cada liquidação apareça classificada, no dia certo, batendo com o extrato.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Auditoria interna</div>
    <div class="provider-detail">Precisa de trilha completa, reproduzível, do que foi trafegado — e no formato que ela consegue consumir, não no formato que é conveniente para nós.</div>
  </div>
</div>

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o CSV numa pasta de rede
  </div>
  <p>Parte do que eu construí ali foi bem menos glamourosa que iniciação de pagamento: a geração de relatórios diários de operações, em CSV, depositados numa pasta específica da rede, para os times de tesouraria, controladoria e auditoria consumirem.</p>
  <p>Na época eu achei aquilo o item mais entediante do backlog. Um sistema de ponta, com mensageria ISO 20022 e liquidação em milissegundos, terminando num arquivo separado por vírgula numa pasta compartilhada.</p>
  <p>Anos depois, na Irlanda, me vi fazendo exatamente a mesma coisa: um ledger paralelo de conciliação cujo produto final é um CSV alimentando o ERP financeiro da empresa. Mudou o país, o setor, a moeda e a stack. Não mudou o padrão — <strong>o sistema transacional mais moderno do mundo ainda precisa entregar a verdade dele, todo dia, num formato que a área financeira consiga abrir</strong>. Hoje eu trato esse tipo de tarefa como integração de primeira classe, não como sobra de sprint.</p>
</div>

A divisão entre os dois bancos de dados segue a mesma lógica de "cada coisa no lugar onde ela é barata". SQL Server guarda o que precisa de transação, restrição e saldo consistente: estado da operação, débito, crédito, conciliação. CouchDB guarda o que é documento — a mensagem como chegou, o payload do QR Code, a cobrança inteira. Esse material tem formato que evolui com o manual do BC, e normalizar isso em tabela é assinar um contrato de migração de schema a cada revisão. Sem schema fixo, um payload no formato novo convive com um no formato antigo sem migração.

<div class="callout callout-warn">
  <div class="callout-label">Onde é fácil errar aqui</div>
  Não confunda a revisão interna do CouchDB com histórico de auditoria. O <code>_rev</code> existe para controle de concorrência e resolução de conflito na replicação — não é versionamento de aplicação, e as revisões antigas são descartadas na compactação. Quem depende disso para auditoria descobre o problema no pior momento possível. O padrão correto é <strong>persistir cada payload recebido como documento imutável, com identificador próprio</strong>, e definir explicitamente política de retenção e de compactação para garantir que o conteúdo exigido pela auditoria continue existindo.
</div>

<img
  src="{{ site.baseurl }}/assets/img/posts/pix-bs2-arquitetura.svg"
  alt="Diagrama conceitual da arquitetura de PIX em um participante direto. Camada de canais: app, APIs, PSPs indiretos e backoffice. Camada de plataforma: iniciação, recebimento, DICT, orquestração indireta e conciliação sobre um barramento RabbitMQ. Camada de dados e sistemas internos: MS SQL Server, CouchDB, controle de idempotência e core de conta corrente, e abaixo antifraude, PLD e AML, controladoria com balancete e fechamento, e relatórios de operações para auditoria. Abaixo, o gateway de mensageria na borda da RSFN, falando com o SPI e o DICT do Banco Central."
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

A decisão estrutural mais importante foi separar a **borda da RSFN** do resto. Um arquiteto cuidava exclusivamente da comunicação direta com o BACEN: tudo que estava à frente dos nossos serviços, o XML assinado, o transporte, os certificados, a tradução daquilo para uma mensagem que entrava no nosso RabbitMQ.

Isso parece um detalhe de organograma e é, na verdade, o que tornou o prazo viável. Significava que quem estava construindo iniciação de pagamento não precisava saber montar um envelope ISO 20022 assinado. Recebia e publicava mensagens numa fila, num contrato interno estável. Quando o BC publicava uma correção de schema — e publicava —, o impacto ficava contido numa camada, em vez de se espalhar por cinco times ao mesmo tempo.

<div class="callout callout-tip">
  <div class="callout-label">Padrão que eu levei para todo lugar depois</div>
  Quando existe um integrador externo que você não controla e que muda por decreto, isole-o atrás de um contrato que <em>você</em> controla. Custa uma camada a mais de tradução e paga esse custo na primeira mudança de especificação.
</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Iniciação de pagamentos</h2></div>
</div>

Iniciação é a metade do PIX que o usuário associa ao produto: alguém aperta um botão e o dinheiro sai. Havia três formas de origem, e elas convergiam para o mesmo núcleo:

- **por chave**, com consulta ao DICT para resolver a conta de destino;
- **manual**, com os dados bancários digitados — banco, agência, conta, documento;
- **por QR Code**, estático ou dinâmico, que precisa ser interpretado antes de virar uma ordem.

E dois destinos possíveis, que parecem o mesmo produto para o cliente e são coisas completamente diferentes por dentro:

<table class="compare-table">
  <thead>
    <tr><th>Cenário</th><th>Liquidação</th><th>Envolve o SPI</th><th>O que pode dar errado</th></tr>
  </thead>
  <tbody>
    <tr><td>Mesma instituição</td><td>Interna, entre contas do próprio banco</td><td><span class="cross">✗</span></td><td>Débito e crédito precisam ser atômicos</td></tr>
    <tr><td>Para outro PSP</td><td>Via SPI, contra a Conta PI</td><td><span class="check">✓</span></td><td>Tudo o mais</td></tr>
  </tbody>
</table>

O fluxo do caso interbancário, simplificado — a barra inferior mostra o orçamento de dez segundos correndo em paralelo:

<img
  src="{{ site.baseurl }}/assets/img/posts/pix-fluxo-iniciacao.svg"
  alt="Diagrama de sequência do fluxo de iniciação de um PIX interbancário: o cliente inicia por chave, QR Code ou dados manuais; o banco consulta o DICT, valida limites, gera o EndToEndId e debita o pagador; a ordem vai ao barramento, a borda RSFN monta a pacs.008 para o SPI, que a repassa ao PSP recebedor; o aceite volta como pacs.002 até a confirmação ao cliente. Ausência de pacs.002 dentro do prazo não é recusa: o caminho é consultar o status e reconciliar. O estorno, idempotente pelo EndToEndId, vale para rejeição definitiva ou para transação reconciliada como não liquidada."
  style="width:100%;max-width:900px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

O detalhe que consome mais tempo de engenharia não está no caminho feliz. Está nas duas últimas linhas.

<div class="callout callout-warn">
  <div class="callout-label">O problema difícil da iniciação</div>
  Você debita antes de saber se o pagamento vai passar. Se debitar depois, corre o risco de mandar dinheiro que não existe. A armadilha é tratar silêncio como recusa: se a <code>pacs.002</code> não chegou dentro do prazo, você não sabe se a transação falhou ou se liquidou e a resposta se perdeu. Nesse estado, o caminho é consultar o status e reconciliar, não estornar. O estorno fica reservado para rejeição definitiva ou para a transação que a reconciliação confirmou como não liquidada — e precisa ser idempotente, porque a resposta pode chegar atrasada ou duplicada. Um estorno executado duas vezes é dinheiro criado do nada; um estorno executado em cima de um PIX que liquidou é dinheiro pago duas vezes.
</div>

É por isso que o `EndToEndId` deixa de ser um campo de protocolo e vira a espinha dorsal do desenho interno: ele é a chave de idempotência de tudo. Toda operação em cima de uma transação — confirmar, estornar, consultar, conciliar — se ancora nele. Se você errar isso, o sistema funciona lindamente em homologação e produz divergência de conciliação no primeiro fim de semana de produção.

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>PIX Indireto: virar infraestrutura de outra pessoa</h2></div>
</div>

A segunda parte que eu construí foi o **PIX Indireto**, e ela é conceitualmente mais interessante que a primeira.

No desenho do arranjo, quem não se conecta diretamente ao SPI pode participar como **participante indireto**: não tem Conta PI, não fala com o BC, e suas transações são liquidadas por meio de um participante direto — que é quem registra esse indireto no SPI e atua como seu liquidante. Fintechs, instituições de pagamento e carteiras digitais oferecem PIX aos seus clientes usando a infraestrutura de um banco.

O que eu construí foi esse lado: todo o **cadastro e controle dos PSPs indiretos**, mais a orquestração das chamadas para os demais serviços quando a operação vinha em nome de um deles.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Multi-tenancy com identidade regulatória</div>
    <div class="provider-detail">Cada participante indireto tem o próprio ISPB. Ele não é "um cliente grande" — é uma instituição, e as mensagens que saem para o SPI carregam a identidade dele. Isolamento aqui não é boa prática, é requisito.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Roteamento e orquestração</div>
    <div class="provider-detail">Uma operação que chega em nome de um indireto tem que atravessar iniciação, DICT e recebimento carregando esse contexto, sem que cada serviço precise reimplementar a regra.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Conciliação em duas pontas</div>
    <div class="provider-detail">O saldo é liquidado contra a Conta PI do direto, mas o extrato precisa fechar do lado do indireto. São duas verdades que têm que bater.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Responsabilidade compartilhada</div>
    <div class="provider-detail">Se o indireto faz algo errado, o problema aparece com o nome do direto. Isso empurra controle, limite e trilha de auditoria para dentro do produto desde o primeiro dia.</div>
  </div>
</div>

Escrever software que outras instituições financeiras consomem muda o padrão de qualidade de um jeito difícil de explicar para quem nunca fez. Não existe "a gente corrige na próxima sprint". Existe uma instituição inteira cuja operação parou.

Vale registrar uma coisa que só ficou clara com os anos: a capacidade de participante indireto foi construída ali, em 2020, mas o produto comercial com esse nome só foi anunciado publicamente bem depois — segundo reportagem da Finsiders publicada no lançamento, um executivo do banco afirmou que o projeto chegou a ser engavetado por questões de responsabilidade regulatória antes de ser retomado. É uma lição sobre a diferença entre *estar pronto* e *ser lançado*, e sobre não medir o valor do que você construiu pela data em que apareceu no site.

<div class="conclusion">
  <h2>O que sobra depois da especificação</h2>
  <p>Cinco anos depois, o que eu levo desse desenho não são os nomes das mensagens. É a noção de que, quando a latência aceitável vira norma auditada, ela deixa de ser assunto de otimização e vira restrição de projeto — e todo o resto da arquitetura se organiza em volta dela.</p>
  <p>O outro aprendizado é sobre isolamento. A camada que traduzia o XML do Banco Central para o barramento interno foi o que permitiu que uma correção de especificação publicada em agosto não virasse retrabalho em cinco frentes ao mesmo tempo. Se eu tivesse que guardar uma única decisão daquele projeto, seria essa.</p>
  <p>Se você chegou aqui pela parte técnica e quer a outra metade, ela está nos dois textos anteriores: quem construiu e sob que pressão, na <a href="{{ site.baseurl }}/artigos/construindo-o-pix-no-bs2-bastidores-de-um-prazo-do-banco-central/">primeira parte</a>; e a que custo, com os números do contrato, na <a href="{{ site.baseurl }}/artigos/contrato-do-pix-valor-fixo-sobreaviso-e-a-hora-que-nao-existia/">segunda</a>.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Banco Central do Brasil. <strong>Manual de Tempos do Pix — limites máximos de tempo e indicadores de acordo de nível de serviço por percentil.</strong>
      <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/IX_ManualdeTemposdoPix.pdf" target="_blank">bcb.gov.br</a>
    </li>
    <li>
      Banco Central do Brasil. <strong>Roteiro para participação direta no SPI e abertura de Conta PI — requisitos de consumo de mensagens e testes de capacidade.</strong>
      <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/sistemapagamentosinstantaneos_docs/Roteiro_para_Participacao_Direta_no_SPI_e_abertura_de_Conta_PI.pdf" target="_blank">bcb.gov.br</a>
    </li>
    <li>
      Banco Central do Brasil. <strong>Divulgação do Sistema de Pagamentos Instantâneos (SPI) — princípios para infraestruturas do mercado financeiro.</strong>
      <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/sistemapagamentosinstantaneos_docs/principios_infraestruturas_mercado_financeiro.pdf" target="_blank">bcb.gov.br</a>
    </li>
    <li>
      Banco Central do Brasil. <strong>Carta Circular nº 4.055, de 25 de maio de 2020 — cronograma e escopo dos testes de homologação, incluindo capacidade e registro de participante indireto.</strong>
      <a href="https://normativos.bcb.gov.br/Lists/Normativos/Attachments/51046/C_Circ_4055_v1_O.pdf" target="_blank">normativos.bcb.gov.br</a>
    </li>
    <li>
      Convergência Digital. <strong>Banco Central elege open source e nuvem como bases da infraestrutura do PIX — Apache Kafka via Red Hat AMQ Streams.</strong>
      <a href="https://convergenciadigital.com.br/especial/cloud/banco-central-elege-open-source-e-nuvem-como-bases-da-infraestrutura-do-pix/" target="_blank">convergenciadigital.com.br</a>
    </li>
    <li>
      Finsiders Brasil. <strong>A nova aposta do BS2 para ampliar sua atuação no Pix — lançamento do Pix Indireto e o período em que o projeto ficou engavetado.</strong>
      <a href="https://finsidersbrasil.com.br/reportagem-exclusiva-fintechs/a-nova-aposta-do-bs2-para-ampliar-sua-atuacao-no-pix/" target="_blank">finsidersbrasil.com.br</a>
    </li>
    <li>
      Banco BS2. <strong>Participantes indiretos no Pix — regra e modelo de liquidação via participante direto.</strong>
      <a href="https://blog.bancobs2.com.br/participantes-indiretos-pix/" target="_blank">blog.bancobs2.com.br</a>
    </li>
  </ol>
</div>
