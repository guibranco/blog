---
layout: post
title: "Construindo o PIX no BS2: sete meses, um prazo do Banco Central e um AirBnB em BH"
description: "Como foi sair do time B2B em São Paulo para o time de projetos especiais do core bancário e construir a iniciação de pagamentos e o PIX Indireto de um participante direto, com data de lançamento definida pelo Banco Central."
date: 2026-08-13
categories: [Career, Coding]
subcategories:
  - "Career/Behind the Scenes"
  - "Coding/Architecture"
tags: [pix, banco-central, central-bank, arquitetura, architecture, sistemas-financeiros, financial-systems, dotnet, rabbitmq, iso-20022, carreira, career]
medium_tags: [pix, fintech, software-architecture, dotnet, career]
reading_time: 22
cover: /assets/img/posts/pix-bs2-bastidores.svg
image: /assets/img/posts/pix-bs2-bastidores.png
---

<p class="lead">Em abril de 2020 eu saí de um time B2B em São Paulo e entrei no time de projetos especiais do core bancário. A primeira coisa que me contaram na nova mesa foi que o Banco Central tinha marcado o lançamento do PIX para novembro. Não era uma meta de roadmap. Era uma data.</p>

<div class="callout callout-tip">
  <div class="callout-label">Sobre o que este texto é</div>
  Este é um relato de bastidores sobre <strong>como se constrói software com prazo regulatório</strong>. Tudo que descrevo aqui sobre o PIX em si — mensagens, componentes, cronograma — é público e está no material do Banco Central, linkado no final. Nomes internos de sistemas, módulos, topologia e colegas de time ficam de fora, e o diagrama de arquitetura deste post foi redesenhado do zero para ilustrar o conceito, não a implementação de ninguém.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Abril de 2020: a mudança de mesa</h2></div>
</div>

Eu estava num time B2B em São Paulo. Era um trabalho confortável no sentido em que a régua era conhecida: cliente pedia, a gente entregava, o prazo era negociável na margem.

O convite foi para o time de **projetos especiais** dentro de serviços financeiros — o core bancário. Na prática, isso significa a camada onde a conta corrente existe de verdade: débito, crédito, saldo, lançamento, conciliação. É a parte do banco onde ninguém aplaude quando funciona e todo mundo aparece quando não funciona.

A diferença cultural entre os dois mundos foi imediata. No B2B, um bug ruim é um cliente irritado. No core, um bug ruim é dinheiro no lugar errado — e, com o PIX, dinheiro no lugar errado em menos de dez segundos, sem janela de estorno automático, no fim de semana, às três da manhã.

E tudo isso acontecendo em abril de 2020. Segunda quinzena da primeira onda da pandemia, escritório fechado, time inteiro remoto de um dia para o outro, num projeto que ninguém tinha feito antes porque o sistema ainda não existia em lugar nenhum do mundo naquele formato.

<div class="divider">· · ·</div>

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a semana em Belo Horizonte
  </div>
  <p>O time de core ficava em Belo Horizonte. A conversa inicial incluía mudança: eu iria de São Paulo para BH e o projeto seria tocado de lá.</p>
  <p>Cheguei a ir. Uma semana num AirBnB, conhecendo o time presencialmente, entendendo o sistema, mapeando quem sabia o quê. E voltei para São Paulo.</p>
  <p>A mudança nunca aconteceu. Entre a pandemia, que tornou o argumento de "estar junto" muito mais fraco, e o fato de que o projeto começou a andar mesmo assim, a proposta simplesmente perdeu urgência e nunca mais foi retomada. Trabalhei no PIX de São Paulo, remoto, com o time em BH — o que, em 2020, ainda parecia uma concessão e não o padrão.</p>
  <p>Olhando de hoje, com quase seis anos morando fora, aquela semana de AirBnB foi um ensaio muito barato de uma coisa que eu faria de verdade depois: chegar num lugar onde você não conhece ninguém, ter uma semana para entender como as coisas funcionam e decidir se fica.</p>
</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O prazo não era do time. Era do Banco Central.</h2></div>
</div>

Esse é o ponto que mais me marcou como engenheiro, e o que mais tento explicar quando alguém pergunta como era trabalhar em banco.

A maior parte dos prazos de software é ficção compartilhada. Alguém estimou, alguém dobrou a estimativa, alguém cortou escopo, a data anda. O PIX não funcionava assim. O cronograma era publicado pelo Banco Central, valia para todo o sistema financeiro nacional ao mesmo tempo, e o não cumprimento das exigências e dos prazos podia virar ação de supervisão direta sobre a instituição.

A Carta-Circular BACEN/DECEM nº 4.056, de 25 de maio de 2020, estabeleceu os procedimentos de adesão ao arranjo. Além da etapa cadastral e da homologatória, ela criou uma coisa que engenheiro nenhum estava esperando: um processo formal de aprovação da **interface do aplicativo**. As instituições tinham que enviar ao BC um anteprojeto, depois um projeto, depois a versão final — com telas ilustrativas — mostrando a dinâmica de acionamento do ambiente dedicado ao PIX, onde as funcionalidades ficariam dentro do app e como apareceriam nos menus, atalhos e botões de acesso rápido.

<div class="callout callout-warn">
  <div class="callout-label">O que isso significa na prática</div>
  Não bastava o backend liquidar em dez segundos. Onde o botão do PIX ficava na tela de login era item regulatório, sujeito a parecer do regulador. Em paralelo, a Carta-Circular nº 4.055 do mesmo dia definia o cronograma dos testes de homologação dos participantes diretos no ambiente de produção do SPI. Nós tínhamos que passar nos dois trilhos ao mesmo tempo.
</div>

O calendário público ficou assim:

<table class="compare-table">
  <thead>
    <tr><th>Data</th><th>Marco</th><th>O que estava em jogo</th></tr>
  </thead>
  <tbody>
    <tr><td>Maio/2020</td><td>Cartas-Circulares 4.055 e 4.056</td><td>Regras de adesão e de homologação</td></tr>
    <tr><td>Agosto/2020</td><td>Regulamento do PIX e manuais técnicos</td><td>Especificação fechada — o alvo para de se mexer</td></tr>
    <tr><td>05/10/2020</td><td>Início do registro de chaves</td><td>DICT em produção, com usuário real</td></tr>
    <tr><td>03/11/2020</td><td>Operação restrita (<em>soft opening</em>)</td><td>Dinheiro real, base limitada de clientes</td></tr>
    <tr><td>16/11/2020</td><td>Lançamento para toda a população</td><td>Sem plano B</td></tr>
  </tbody>
</table>

Repare no espaço entre agosto e outubro. A especificação técnica definitiva sai em agosto; o DICT precisa estar em produção em 5 de outubro. Dois meses. E o registro de chaves foi antecipado — originalmente estava previsto para 3 de novembro — justamente para dar mais tempo de rodagem ao sistema, o que do lado de dentro significou o oposto: o primeiro entregável chegou dois meses antes.

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>A arquitetura do lado do Banco Central</h2></div>
</div>

Vale começar por aqui porque tudo do lado do banco é consequência disso.

O PIX não é um sistema único. São dois sistemas principais, com papéis bem separados:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">SPI — Sistema de Pagamentos Instantâneos</div>
    <div class="provider-detail">Onde o dinheiro se move. Liquida transação a transação, sem janela de fechamento e sem ciclo de compensação. Cada participante direto mantém uma <strong>Conta PI</strong> no BC, e a transação só acontece se houver saldo nela.</div>
    <div class="provider-price">Mensageria ISO 20022 em XML</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">DICT — Diretório de Identificadores de Contas Transacionais</div>
    <div class="provider-detail">Onde as identidades são resolvidas. Guarda o vínculo entre chave (CPF/CNPJ, e-mail, telefone, chave aleatória) e conta transacional. Inclui reivindicação de posse e portabilidade de chave.</div>
    <div class="provider-price">Operado pelo próprio BC</div>
  </div>
</div>

A comunicação com essa infraestrutura acontece exclusivamente pela **RSFN** — a Rede do Sistema Financeiro Nacional. Rede dedicada, fora da internet pública, com autenticação por certificado ICP-Brasil e validação de formato e assinatura em cada mensagem.

Isso muda tudo no modelo mental de quem vem de web. Não existe "chamar uma API e tratar o erro 500". Existe um protocolo de mensageria financeira com ordem de campos, schema validado, assinatura digital e um catálogo de erros que você precisa mapear inteiro. As mensagens centrais da iniciação são a `pacs.008`, que carrega a ordem de pagamento com pagador, recebedor, valor e o `EndToEndId` — o identificador único da transação, gerado na origem e que acompanha a operação até o fim — e a `pacs.002`, que devolve o status.

Do lado da infraestrutura do próprio BC, a escolha foi pública e interessante: o edital já definia uma arquitetura distribuída baseada em Apache Kafka, e a solução contratada foi a stack open source da Red Hat — AMQ Streams (Kafka), OpenShift e Ansible Automation Platform. Em teste, com volume de 2 mil transações por segundo, 99% foram processadas em menos de quatro segundos.

<div class="callout callout-tip">
  <div class="callout-label">O detalhe que dita o resto</div>
  Tudo isso roda 24 horas por dia, todos os dias, sem janela de fechamento. E o "dez segundos" que virou slogan do PIX não é uma meta vaga: é um percentil publicado em norma, com o ciclo inteiro fatiado em marcos temporais medidos por cada participante. É esse orçamento que dita a arquitetura interna do banco — vale olhar os números antes de olhar a solução.
</div>

<div class="section-header">
  <div class="section-num">04</div>
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

Do lado do participante, o roteiro de participação direta no SPI é ainda mais específico: a instituição precisa **consumir em até 200 milissegundos no mínimo 99% das mensagens** `pacs.008` e `pacs.002` que o SPI disponibiliza. Repare no verbo — as mensagens são disponibilizadas e você as consome. Isso empurra a arquitetura para um modelo de consumo contínuo e agressivo, não de espera passiva.

E havia o teste de capacidade, que na nossa época estava na Carta Circular 4.055: enviar mensagens `pacs.008` distribuídas uniformemente ao longo de dez minutos — 10 mil, 20 mil ou 40 mil, conforme a faixa de contas transacionais do PSP — e depois receber o mesmo volume, acatando cada uma com sua `pacs.002`. Não é um teste que você passa raspando: ou a arquitetura absorve, ou você reprova e agenda de novo com o BC.

<div class="callout callout-warn">
  <div class="callout-label">O requisito que ninguém vê chegando</div>
  Para apurar esses indicadores, o Manual de Tempos exige que os relógios dos servidores dentro da instituição estejam sincronizados a ponto de não distorcer a medição — e proíbe usar relógios de instituições diferentes na apuração, justamente porque uma pequena diferença já falsearia o número. Ou seja: sincronização de tempo deixa de ser detalhe de infraestrutura e vira item de conformidade. Foi a primeira vez que eu vi NTP virar assunto de reunião com jurídico.
</div>

E, fechando o pacote, há meta de disponibilidade por porte: hoje as categorias vão de 99,5% para os maiores participantes a 95,0% para os menores, com o BC se comprometendo com 99,9% no SPI. Como o índice do participante direto **inclui as transações dos indiretos que ele liquida**, a disponibilidade de quem usa a sua infraestrutura entra na sua nota. Guarde essa frase para a seção do PIX Indireto.

<div class="section-header">
  <div class="section-num">05</div>
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
    <div class="provider-detail">Pico de volume vira profundidade de fila, não conexão recusada. E o par <em>dead-letter queue</em> mais retentativa com espera crescente resolve, com configuração, o que em chamada síncrona vira código de resiliência espalhado.</div>
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

A divisão entre os dois bancos de dados segue a mesma lógica de "cada coisa no lugar onde ela é barata". SQL Server guarda o que precisa de transação, restrição e saldo consistente: estado da operação, débito, crédito, conciliação. CouchDB guarda o que é documento — a mensagem como chegou, o payload do QR Code, a cobrança inteira. Esse material tem formato que evolui com o manual do BC, e normalizar isso em tabela é assinar um contrato de migração de schema a cada revisão. Como documento, uma versão nova simplesmente convive com a antiga, e a auditoria continua conseguindo ler o que foi trafegado exatamente como foi trafegado.

<img
  src="{{ site.baseurl }}/assets/img/posts/pix-bs2-arquitetura.svg"
  alt="Diagrama conceitual da arquitetura de PIX em um participante direto: canais, serviços de iniciação, recebimento, DICT e orquestração indireta sobre um barramento RabbitMQ, com um gateway de mensageria na borda da RSFN falando com SPI e DICT"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

A decisão estrutural mais importante foi separar a **borda da RSFN** do resto. Um arquiteto cuidava exclusivamente da comunicação direta com o BACEN: tudo que estava à frente dos nossos serviços, o XML assinado, o transporte, os certificados, a tradução daquilo para uma mensagem que entrava no nosso RabbitMQ.

Isso parece um detalhe de organograma e é, na verdade, o que tornou o prazo viável. Significava que quem estava construindo iniciação de pagamento não precisava saber montar um envelope ISO 20022 assinado. Recebia e publicava mensagens numa fila, num contrato interno estável. Quando o BC publicava uma correção de schema — e publicava —, o impacto ficava contido numa camada, em vez de se espalhar por cinco times ao mesmo tempo.

<div class="callout callout-tip">
  <div class="callout-label">Padrão que eu levei para todo lugar depois</div>
  Quando existe um integrador externo que você não controla e que muda por decreto, isole-o atrás de um contrato que <em>você</em> controla. Custa uma camada a mais de tradução e paga esse custo na primeira mudança de especificação.
</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Quem fez o quê</h2></div>
</div>

O time era pequeno para o tamanho do escopo, e a divisão foi por domínio, não por camada. Cada pessoa era dona de uma fatia funcional de ponta a ponta.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Chaves e diretório</div>
    <div class="provider-detail">Uma pessoa responsável pelo DICT: registro, alteração, exclusão, consulta de vínculo, reivindicação de posse e portabilidade. O primeiro entregável a ir para produção, em 5 de outubro.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Recebimento e contestação</div>
    <div class="provider-detail">Uma pessoa responsável pelo outro lado do fluxo: crédito na conta do recebedor, comprovante, devolução e o tratamento das contestações.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Borda RSFN</div>
    <div class="provider-detail">Um arquiteto cuidando da comunicação direta com o BACEN, do XML e da tradução para o barramento interno.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Iniciação e PIX Indireto</div>
    <div class="provider-detail">A minha parte: fazer o pagamento sair, e permitir que outras instituições fizessem pagamentos saírem através da gente.</div>
  </div>
</div>

<div class="section-header">
  <div class="section-num">07</div>
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
  <div class="section-num">08</div>
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

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>O que eu levei desse projeto</h2></div>
</div>

**Prazo externo é um tipo diferente de restrição, e é libertador.** Quando a data não é negociável, a conversa deixa de ser "quando fica pronto" e passa a ser "o que entra na primeira versão". Isso força priorização honesta muito mais rápido do que qualquer cerimônia de planejamento.

**Especificação instável é o inimigo real, não o volume de código.** Os manuais técnicos evoluíram durante o desenvolvimento. Quem tinha isolado a borda absorveu; quem tinha espalhado o formato do BC por dentro do domínio, refez.

**Em sistema financeiro, o caminho de exceção é o produto.** Confirmação é fácil. Timeout, resposta duplicada, resposta tardia, estorno de estorno — é aí que mora o trabalho, e é aí que mora o dinheiro.

**Idempotência não é otimização.** Num sistema onde a mesma mensagem pode chegar duas vezes por desenho da rede, ela é a diferença entre um sistema correto e um sistema que cria dinheiro.

**Trabalhar com o resto do mercado ao mesmo tempo é raro.** Todo banco do país estava construindo a mesma coisa, contra o mesmo prazo, contra a mesma especificação. Os fóruns técnicos do período tinham um clima de cooperação que eu nunca mais vi em nenhum outro projeto — porque ninguém ganhava nada com o vizinho falhando.

<div class="conclusion">
  <h2>Cinco anos depois</h2>
  <p>O PIX virou infraestrutura pública invisível. Ninguém mais lembra que aquilo era um projeto com risco de não sair, e é exatamente esse o sinal de que deu certo: sistema financeiro bem-feito é aquele em que ninguém pensa.</p>
  <p>Do meu lado, foi o projeto que mais me ensinou por unidade de tempo em toda a carreira no Brasil. Não pela stack — .NET, RabbitMQ e SQL Server eu já conhecia — mas pela combinação de prazo inegociável, especificação em movimento e consequência real do erro. Um mês depois do lançamento eu embarquei para o Porto — <a href="{{ site.baseurl }}/artigos/trabalhando-pelo-mundo-porto-farfetch/">a primeira vez que saí do Brasil para trabalhar</a>, e boa parte da confiança para aceitar aquilo veio de ter atravessado 2020 dentro do core de um banco.</p>
  <p>E a mudança para Belo Horizonte, que era a grande decisão de vida em abril, virou uma semana de AirBnB e uma passagem de volta. Às vezes a mudança importante do ano não é a que estava no plano.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Banco Central do Brasil. <strong>Carta Circular nº 4.056, de 25 de maio de 2020 — procedimentos para adesão ao arranjo de pagamentos instantâneos (PIX).</strong>
      <a href="https://normativos.bcb.gov.br/Lists/Normativos/Attachments/51047/C_Circ_4056_v1_O.pdf" target="_blank">normativos.bcb.gov.br</a>
    </li>
    <li>
      Banco Central do Brasil. <strong>Carta Circular nº 4.055, de 25 de maio de 2020 — cronograma dos testes de homologação dos participantes diretos no SPI.</strong>
      <a href="https://normativos.bcb.gov.br/Lists/Normativos/Attachments/51046/C_Circ_4055_v1_O.pdf" target="_blank">normativos.bcb.gov.br</a>
    </li>
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
      Agência Brasil. <strong>Começa hoje registro de chaves digitais do Pix (cronograma oficial: 5/10, 3/11 e 16/11 de 2020).</strong>
      <a href="https://agenciabrasil.ebc.com.br/economia/noticia/2020-10/comeca-hoje-registro-de-chaves-digitais-do-pix" target="_blank">agenciabrasil.ebc.com.br</a>
    </li>
    <li>
      InfoMoney. <strong>Pix: fase restrita começa em 3 de novembro com clientes e horários limitados.</strong>
      <a href="https://www.infomoney.com.br/minhas-financas/pix-fase-restrita-tem-inicio-no-dia-3-com-clientes-e-horarios-limitados-saiba-como-vai-funcionar/" target="_blank">infomoney.com.br</a>
    </li>
    <li>
      Convergência Digital. <strong>Banco Central elege open source e nuvem como bases da infraestrutura do PIX (Apache Kafka / Red Hat AMQ Streams).</strong>
      <a href="https://convergenciadigital.com.br/especial/cloud/banco-central-elege-open-source-e-nuvem-como-bases-da-infraestrutura-do-pix/" target="_blank">convergenciadigital.com.br</a>
    </li>
    <li>
      Finsiders Brasil. <strong>A nova aposta do BS2 para ampliar sua atuação no Pix — lançamento do Pix Indireto e o período em que o projeto ficou engavetado.</strong>
      <a href="https://finsidersbrasil.com.br/reportagem-exclusiva-fintechs/a-nova-aposta-do-bs2-para-ampliar-sua-atuacao-no-pix/" target="_blank">finsidersbrasil.com.br</a>
    </li>
    <li>
      Banco BS2. <strong>Participantes indiretos no Pix: entenda a regra e o modelo de liquidação via participante direto.</strong>
      <a href="https://blog.bancobs2.com.br/participantes-indiretos-pix/" target="_blank">blog.bancobs2.com.br</a>
    </li>
  </ol>
</div>
