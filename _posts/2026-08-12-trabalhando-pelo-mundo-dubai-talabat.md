---
layout: post
title: "Trabalhando pelo mundo #2 — Dubai: seis meses remoto do Brasil antes de pisar no deserto"
description: "Uma mensagem no LinkedIn que ficou cinco semanas sem resposta virou dois anos na Talabat, do grupo Delivery Hero. Visto de trabalho nos Emirados, meio ano em remoto acordando às 3h da manhã, 47 dias em hotel, e uma semana de trabalho que mudou de dia no meio do caminho."
date: 2026-08-12
categories: [Career]
subcategories:
  - "Career/Trabalho no Exterior"
tags: [trabalho-no-exterior, dubai, emirados-arabes-unidos, carreira-internacional, expatriado, talabat, delivery-hero, remoto, relocation, visto-de-trabalho, csharp, dotnet, aws, postgresql, sql-server, golang, microsservicos, ddd, tdd, qcommerce, on-call, salario, imposto]
reading_time: 26
cover: /assets/img/posts/trabalhando-pelo-mundo-dubai.svg
image: /assets/img/posts/trabalhando-pelo-mundo-dubai.png
series: trabalhando-pelo-mundo
series_order: 2
location:
  lat: 25.2048
  lng: 55.2708
  label: "Dubai, Emirados Árabes Unidos"
---

<p class="lead">A mensagem chegou em 26 de janeiro de 2021 e eu não respondi. Cinco semanas depois, a recrutadora insistiu — e essa insistência acabou definindo os dois anos seguintes da minha vida, mais tudo o que veio depois.</p>

Este é o segundo post da série sobre os lugares onde trabalhei mudando de país. No [primeiro capítulo]({{ site.baseurl }}/artigos/trabalhando-pelo-mundo-porto-farfetch/) eu contei sobre o Porto, a mudança que nunca aconteceu. Aqui a mudança aconteceu de verdade — só que com um intervalo curioso no meio: **seis meses trabalhando para Dubai sem sair do Brasil**.

<div class="callout callout-tip">
  <div class="callout-label">O que você vai encontrar aqui</div>
  Cinco fases de entrevista, um visto que me registrou com uma profissão que não era a minha, meio ano acordando às 3h da manhã, 47 dias morando em hotel, réveillon de quarentena com vista para o Burj Khalifa — e o que me fez ir embora depois de quase dois anos.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>De onde eu vinha</h2></div>
</div>

Eu tinha acabado de sair do banco onde trabalhei desde 2019 e, em vez de procurar um substituto, estava acumulando **dois contratos parciais em paralelo** — os dois remotos, os dois de sênior, os dois via consultoria: a **Farfetch** por uma consultoria portuguesa, em recibos verdes, com a mudança para o Porto sendo planejada; e um **grupo financeiro jamaicano**, por uma consultoria chilena, em contrato PJ pago em reais contra nota fiscal.

O capítulo anterior explica a conta em detalhe, mas o resumo é este: as duas posições **somadas** ainda ficavam abaixo do que Dubai oferecia por uma vaga um degrau abaixo na escada de carreira — a carta de oferta trazia Software Engineer II, grade IC2.

O fato de eu ainda não ter me mudado para Portugal foi o que tornou tudo possível. Não havia contrato de aluguel, mudança despachada nem vida montada para desfazer.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O processo seletivo</h2></div>
</div>

Como nos outros dois países da série, começou no **LinkedIn**.

Em **26 de janeiro de 2021**, uma recrutadora da **Talabat** — plataforma de delivery do grupo alemão **Delivery Hero**, sediada em Dubai — me mandou uma mensagem. A abordagem trazia números de escala que hoje eu reconheço como o padrão do setor: milhões de usuários diários, centenas de milhares de pedidos por dia, milhares de funcionários e dezenas de nacionalidades. E a expressão que fazia o trabalho pesado da mensagem: **salário isento de impostos**.

Eu não respondi.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a mensagem que quase não foi lida
  </div>
  <p>Não foi estratégia nem desdém. Eu tinha começado na Farfetch havia pouco mais de um mês, gostava do time, e a mudança para o Porto estava sendo planejada. Deixei para depois. O "depois" durou cinco semanas.</p>
  <p>Em <strong>4 de março</strong> ela mandou um follow-up dizendo que não tinha tido retorno. Dessa vez eu respondi em treze minutos, já com o currículo anexado. Ainda esperei mais uma semana, cobrei, e a call ficou marcada para <strong>17 de março</strong>.</p>
  <p>Isso me assusta um pouco até hoje: a decisão que definiu os anos seguintes chegou como uma notificação que eu não achei importante o suficiente para abrir. Oportunidade não chega anunciada como oportunidade — chega igualzinha ao resto do ruído.</p>
</div>

### Seis conversas até a oferta

Aqui a diferença em relação ao Porto é gritante. Na Farfetch foram duas entrevistas e nenhum teste técnico. Na Talabat foram **seis etapas**, com avaliação técnica de verdade.

<table class="compare-table">
  <thead>
    <tr><th>#</th><th>Etapa</th><th>Com quem</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Screening</td><td>A recrutadora que me abordou</td></tr>
    <tr><td>2</td><td>Entrevista de RH</td><td>Outra pessoa do time de recrutamento</td></tr>
    <tr><td>3</td><td><strong>Live coding</strong></td><td>Dois engenheiros sêniores</td></tr>
    <tr><td>4</td><td><strong>System design</strong></td><td>Outros dois engenheiros sêniores</td></tr>
    <tr><td>5</td><td>Entrevista final</td><td>VP de Engenharia — mistura de tudo</td></tr>
    <tr><td>6</td><td>Conversa de alocação</td><td>O engineering manager da squad, já com a decisão tomada</td></tr>
  </tbody>
</table>

Repare na ordem da última etapa: eu só conversei com quem seria meu gestor **depois** de aprovado, quando já tinham decidido para qual squad eu iria. Não foi uma entrevista — foi uma apresentação.

<div class="callout callout-tip">
  <div class="callout-label">Dois processos, duas filosofias</div>
  Porto: duas conversas, zero código escrito, decisão em catorze dias. Dubai: quatro avaliações técnicas separadas, incluindo live coding e system design com quatro engenheiros diferentes. Nenhum dos dois é errado — mas o segundo diz muito mais sobre uma empresa que contrata em volume e precisa de um critério que escale. Se você está mirando o Golfo, prepare-se para <em>system design</em>: é a etapa que mais elimina gente com experiência de sobra.
</div>

<div class="callout callout-warn">
  <div class="callout-label">Oferta com prazo de validade</div>
  A carta de oferta chegou em <strong>21 de abril de 2021</strong> e era válida por <strong>três dias úteis</strong>. É prática comum em empresas de crescimento acelerado e funciona como instrumento de pressão: reduz o tempo de comparar propostas, consultar família e fazer a conta com calma. Se você receber uma assim, saiba que pedir extensão de prazo é normal — e que a reação a esse pedido já diz muito sobre a empresa.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Contratação, visto e burocracia</h2></div>
</div>

Aqui a diferença em relação ao capítulo anterior é enorme. No Porto eu seria **prestador de serviço** por recibos verdes, com toda a responsabilidade fiscal nas minhas costas. Em Dubai eu fui **empregado**, com contrato regido pela lei trabalhista dos Emirados.

### O que vinha no pacote

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-file-signature"></i> Vínculo</div>
    <div class="provider-detail">Empregado direto, sem consultoria no meio. Três meses de período probatório e um mês de aviso prévio, conforme a lei local.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-money-bill-wave"></i> Composição salarial</div>
    <div class="provider-detail">Salário dividido em base mais subsídios de moradia, transporte e telefone — formato padrão nos Emirados.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-plane"></i> Passagem anual</div>
    <div class="provider-detail">Benefício de passagem aérea por ano, previsto em política da empresa.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-briefcase-medical"></i> Seguro-saúde</div>
    <div class="provider-detail">Obrigatório por lei nos Emirados e custeado pelo empregador.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-suitcase-rolling"></i> Pacote de mudança</div>
    <div class="provider-detail">Passagem só de ida e cerca de um mês de hotel para quem vinha de fora.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-percent"></i> Imposto de renda</div>
    <div class="provider-detail">Zero sobre salário. Bruto e líquido praticamente coincidem.</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Por que o salário nos Emirados vem fatiado</div>
  Não é firula de contracheque. A indenização de fim de serviço — o <em>gratuity</em>, algo próximo do nosso FGTS em função — é calculada <strong>apenas sobre o salário base</strong>, não sobre o total. Duas propostas com o mesmo valor bruto podem render indenizações bem diferentes dependendo de como estão divididas. É a primeira coisa que eu olharia hoje numa oferta de lá.
</div>

Eu não vou publicar os valores da minha proposta — mas vale registrar o raciocínio, porque ele é mais útil que o número. Ao comparar uma oferta dos Emirados com uma europeia, três coisas mudam a conta inteira: **não há imposto de renda sobre salário**, o que aproxima bruto e líquido; **não há previdência pública** acumulando em seu nome, então a aposentadoria é integralmente responsabilidade sua; e **o custo de vida em Dubai é alto**, especialmente moradia, o que devolve boa parte da vantagem. O que sobra de fato no fim do mês é uma conta de três variáveis, não de uma.

### O visto — e a profissão que eu nunca exerci

Todo o processo foi **conduzido pela empresa**, com a papelada chegando por e-mail. E foi aqui que apareceu a consequência mais inesperada de um detalhe que já tinha aparecido no capítulo do Porto: **eu não tenho diploma de curso superior**.

Sem diploma, o visto emitido foi o de categoria não qualificada. Perante o governo dos Emirados, eu fiquei registrado como **Filing Clerk** — arquivista. Meu cargo na empresa, minhas responsabilidades e os valores acordados permaneceram exatamente os mesmos; a divergência existia só no papel do Ministério.

<div class="callout callout-warn">
  <div class="callout-label">O que isso significa na prática</div>
  A classificação da sua profissão no visto não é decorativa: em vários países do Golfo ela influencia categoria de residência, possibilidade de patrocinar familiares, faixas de taxa e — dependendo do caso — o próprio processo de renovação. Se você não tem diploma, ou tem um diploma que não será atestado a tempo, pergunte <strong>antes de assinar</strong> qual categoria de visto a empresa vai solicitar e o que ela limita. No meu caso não gerou problema; mas eu descobri depois, não antes.
</div>

### Exames médicos e direitos trabalhistas

O trâmite de residência inclui uma bateria obrigatória feita em órgãos do governo local, com agendamento pela empresa:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-lungs"></i> Raio-X de tórax</div>
    <div class="provider-detail">Rastreio de tuberculose, obrigatório para o visto de residência.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-vial"></i> Exame de sangue</div>
    <div class="provider-detail">Parte do protocolo sanitário exigido de todo estrangeiro.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-scale-balanced"></i> Palestra sobre direitos trabalhistas</div>
    <div class="provider-detail">Sessão obrigatória explicando a legislação local ao trabalhador estrangeiro.</div>
  </div>
</div>

A empresa agendava tudo, mas o deslocamento até os postos era por minha conta — com exceção da palestra. É um detalhe pequeno que ilustra bem o padrão de um pacote de relocação: quase tudo coberto, e uma faixa de despesas miúdas que ninguém menciona e que fica com você.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Seis meses trabalhando para Dubai sem sair do Brasil</h2></div>
</div>

Eu comecei em **30 de maio de 2021** e passei quase **seis meses em remoto, do Brasil**. Na prática, foi uma repetição do arranjo que eu já vinha fazendo com Portugal — trabalhar para um país onde eu ainda não morava — mas com uma diferença essencial: dessa vez a mudança realmente aconteceu.

### Acordar às 3h da manhã

O fuso é o que muda tudo. Portugal está três ou quatro horas à frente do Brasil; **Dubai está sete**. Não existe manhã em comum.

A daily era às **11h de Dubai**, o que me colocava de pé por volta das **4h da manhã**. Depois o horário foi antecipado para **10h de Dubai** — porque parte do time estava em remoto na Europa e o horário de verão da Ucrânia e da Croácia empurrou a cerimônia para trás. Para mim, isso significou passar a acordar às **3h**.

<div class="callout callout-warn">
  <div class="callout-label">O custo invisível do "remoto internacional"</div>
  Quando a vaga diz "trabalho remoto para o exterior", o que raramente aparece na descrição é de quem é o ônus do fuso. Não foi negociação nem imposição — a daily existia no horário que funcionava para a maioria, e eu era a minoria. Se você está avaliando algo assim, calcule antes: acordar às 3h da manhã <strong>todos os dias úteis</strong> não é um detalhe logístico, é uma alteração estrutural na sua vida.
</div>

Havia ainda dois atritos que ninguém antecipa. O primeiro era a **semana de trabalho diferente**: nessa época os Emirados trabalhavam de domingo a quinta, então meu domingo era dia útil e minha sexta era dia morto. O segundo era mais prosaico: **queda de energia e de internet**. Algumas vezes eu simplesmente não consegui trabalhar — e quando a sua casa é o escritório de uma empresa a onze mil quilômetros, não existe "vou usar a máquina do escritório".

### O equipamento

Comecei tudo com o **meu próprio notebook**, com Windows. A empresa chegou a me enviar um **MacBook**, despachado de Dubai para o Brasil, mas eu usei pouquíssimas vezes — preferi seguir na minha máquina, no ambiente que eu já dominava.

### Como eu recebia — a parte mais complicada

Essa foi a engenharia financeira menos óbvia de toda a mudança.

<table class="compare-table">
  <thead>
    <tr><th>Fase</th><th>Como o dinheiro chegava</th></tr>
  </thead>
  <tbody>
    <tr><td>Primeiros ~2 meses</td><td>Pagamento em <strong>dólar</strong> para conta empresarial nas Ilhas Cayman, via banco correspondente americano. Bastou informar IBAN e BIC/SWIFT.</td></tr>
    <tr><td>Restante do remoto</td><td>Migrei para minha conta em <strong>Portugal</strong>, aberta ainda na época da Farfetch, e de lá remetia ao Brasil — por transferência direta ou comprando criptomoeda em corretora.</td></tr>
    <tr><td>Primeiro mês em Dubai</td><td><strong>Em dinheiro vivo</strong>, retirado numa casa de câmbio local.</td></tr>
    <tr><td>Depois disso</td><td>Conta bancária local, aberta numa agência em Dubai.</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Por que o pagamento em dólar funciona nos Emirados</div>
  O dirham é <strong>atrelado ao dólar americano</strong> a uma paridade fixa mantida há décadas. Isso torna o pagamento em USD trivial para a empresa e previsível para você: não há risco cambial entre as duas moedas. É uma das razões pelas quais arranjos internacionais de pagamento são tão comuns por lá.
</div>

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o salário que chegou em espécie
  </div>
  <p>Receber o primeiro salário de Dubai <strong>em dinheiro, no balcão de uma casa de câmbio</strong>, é uma daquelas cenas que resumem uma cidade inteira. Eu vinha de meses de transferência internacional entre três países e quatro instituições, e o primeiro pagamento presencial foi o mais analógico possível: fila, guichê, cédulas contadas na sua frente. Ainda não havia conta local, e a economia dos Emirados simplesmente tem essa camada em espécie funcionando com naturalidade.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>A mudança: um voo, uma final e 47 dias de hotel</h2></div>
</div>

### O voo que eu tentei adiar

A data estava marcada: **26 de novembro de 2021**, voo semanal de sexta-feira, de Guarulhos para Dubai, pago pela empresa. Eu pedi uma semana de adiamento. Negaram — e com uma certa razão, já que eu vinha empurrando havia seis meses.

O motivo do pedido: no dia **27 de novembro** era a **final da Libertadores**, Palmeiras contra Flamengo, no Uruguai. Eu tinha tentado ir, sem sucesso.

Aterrissei em Dubai por volta das **19h do dia 27**. Corri para o hotel, larguei as malas e fui assistir à final num bar, com um amigo que eu tinha conhecido pelos grupos de WhatsApp de brasileiros nos Emirados — alguém que, até aquele dia, eu nunca tinha visto pessoalmente.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — chegar e já ter para onde ir
  </div>
  <p>Menos de três horas depois de pousar num país onde eu nunca tinha estado, eu estava num bar assistindo meu time ganhar a Libertadores, ao lado de alguém que eu só conhecia de grupo de WhatsApp. Os grupos de brasileiros no exterior são muito subestimados: eles resolvem, em uma tarde, o problema que costuma levar meses — ter uma pessoa para chamar.</p>
  <p>Aquilo era sábado. No <strong>domingo</strong> eu já estava no escritório: a semana útil nos Emirados ia de domingo a quinta.</p>
</div>

### Os empregos que a mudança encerrou

Durante o período em remoto do Brasil, eu não estava só na Talabat. Em **junho de 2021** eu somei um contrato **CLT com a filial brasileira de uma empresa americana** — e havia ainda uma terceira frente, também parcial, num projeto de open banking. Foi a fase em que acumulei três vínculos ao mesmo tempo.

O contrato americano tem um detalhe que vale contar, porque é a melhor lição prática desta série sobre trabalho remoto internacional. O salário era acima da média de sênior no Brasil e muito abaixo da média de sênior nos Estados Unidos — o clássico **salário LATAM**: a empresa paga acima do mercado local e bem abaixo do mercado dela. E isso não era acidente, estava escrito no contrato. Exigia-se que eu estivesse **na América Latina**, por dois motivos declarados: fuso horário e custo de vida.

<div class="callout callout-warn">
  <div class="callout-label">A cláusula que ninguém lê com atenção</div>
  Contratos de "remoto internacional" quase sempre trazem uma restrição geográfica. Não é burocracia decorativa: é o que sustenta a faixa salarial. Se você pretende mudar de país em algum momento, essa cláusula precisa ser a primeira coisa que você lê — porque ela decide se aquele emprego sobrevive ou não à sua mudança.
</div>

Sendo CLT, eu precisava estar **legalmente residindo no Brasil**. Manter o vínculo morando em Dubai era impraticável: além do fuso, a empresa poderia me convocar ao escritório de São Paulo a qualquer momento. Vale registrar também o que aquele contrato **não** oferecia: nenhuma previsão de mudança para os Estados Unidos, nenhum patrocínio de visto. Não era caminho para lugar nenhum — era um emprego remoto com teto geográfico embutido.

Então o embarque de novembro resolveu a questão sozinho. **A mudança encerrou os contratos que dependiam de eu estar no Brasil**, e eu fiquei só com a Talabat.

<div class="divider">· · ·</div>

### Primeiro mês: presencial por necessidade

Meu gestor pediu que eu fosse ao escritório no primeiro mês. A justificativa tinha dois lados, e os dois faziam sentido: eu precisava me ambientar depois de meio ano conhecendo o time só por vídeo, e trabalhar de um quarto de hotel por semanas não é exatamente sustentável.

### 47 dias em dois hotéis

O pacote de contratação cobria cerca de **20 a 30 dias de hotel**, perto do escritório em **Business Bay**. Terminado o prazo, eu ainda não tinha encontrado apartamento — pedi extensão e fui transferido para um segundo hotel, mais caro, com desconto negociado. No total foram **47 dias hospedado**, entre dois hotéis, ambos em Business Bay.

Depois disso aluguei um apartamento em **JLT — Jumeirah Lake Towers**. Fazendo as contas, o valor do aluguel e o que me cobravam de diária ficaram próximos: descontado o período pago pela empresa, eu não saí perdendo com a demora.

<div class="callout callout-tip">
  <div class="callout-label">Procurar imóvel em Dubai leva mais tempo do que o pacote cobre</div>
  Um mês de hotel parece generoso até você começar a procurar. Some visitas, negociação, e a burocracia local de contrato e pagamento — que tradicionalmente envolve cheques adiantados e conta bancária local já ativa. Se for negociar um pacote de relocação para os Emirados, considere pedir um prazo maior de acomodação desde o início, em vez de depender de extensão depois.
</div>

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o réveillon que eu vi pela janela
  </div>
  <p>Ainda no segundo hotel, depois da confraternização de fim de ano da minha tribo, eu peguei covid. Passei o período entre o Natal e o Ano-Novo em quarentena, sozinho, num quarto de hotel, num país onde eu tinha chegado havia um mês.</p>
  <p>A virada do ano eu assisti da janela — de frente para o Burj Khalifa, vendo a queima de fogos mais famosa do mundo do lado de fora do vidro. É uma imagem que eu não trocaria por nada, e que ao mesmo tempo resume bem o que ninguém conta sobre mudar de país: os melhores cenários costumam chegar em momentos que você não escolheu.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>A empresa, as tribos e os times</h2></div>
</div>

A **Talabat** nasceu no Kuwait em 2004 como plataforma de pedidos de comida online e, desde 2016, é subsidiária da alemã **Delivery Hero**. Opera em vários países do Oriente Médio — Kuwait, Bahrein, Emirados, Omã, Catar, Jordânia, Egito e Iraque.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-briefcase"></i> Cargo</div>
    <div class="provider-detail">Software Engineer / .NET Developer</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-sitemap"></i> Tribo</div>
    <div class="provider-detail">Groceries / qCommerce</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-building"></i> Tamanho</div>
    <div class="provider-detail">Cerca de 300 desenvolvedores; o grupo passa de 16 mil funcionários</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-handshake"></i> Vínculo</div>
    <div class="provider-detail">Contratação direta, sem intermediário</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-house-laptop"></i> Modelo</div>
    <div class="provider-detail">Híbrido — seis meses remoto do Brasil, depois presencial flexível em Dubai</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-calendar"></i> Período</div>
    <div class="provider-detail">Maio de 2021 a março de 2023 — um ano e onze meses</div>
  </div>
</div>

### Dois times, duas metades da jornada de compra

Minha passagem se dividiu quase ao meio, em dois times com escopos bem distintos.

<table class="compare-table">
  <thead>
    <tr><th>Período</th><th>Squad</th><th>Escopo</th></tr>
  </thead>
  <tbody>
    <tr><td>Mai–Dez/2021</td><td>Grocery Fulfillment</td><td>Do checkout até o entregador chegar à loja</td></tr>
    <tr><td>Jan/2022–Mar/2023</td><td>Shopping Experience<br><small>ex-FAST — Finding and Shopping Team</small></td><td>Da escolha da loja até o carrinho</td></tr>
  </tbody>
</table>

**Grocery Fulfillment** cuidava do que acontece depois que o cliente finaliza a compra: garantir que o pedido fosse separado corretamente pela equipe da loja, até o momento em que o entregador chega para retirar. É um domínio muito menos glamouroso que "busca" e muito mais brutal — porque o mundo físico não colabora. O produto acabou na prateleira. O separador não achou o item. O cliente quer substituir por outro.

**Shopping Experience** — antes chamado **FAST**, de *Finding and Shopping Team* — atuava na metade anterior: depois que o usuário escolhe a loja e antes de ele ir para o carrinho. Busca, ofertas, descontos, produtos em destaque, navegação personalizada. O carrinho e o checkout eram de outro time, e a seleção de loja de um terceiro.

<div class="callout callout-tip">
  <div class="callout-label">A anatomia de um app de delivery</div>
  Repare como o fluxo é fatiado entre times: escolher a loja, navegar e buscar, carrinho e checkout, separação do pedido, entrega. Cada fatia é um time inteiro. Isso explica por que empresas de delivery contratam tanta gente — e por que a integração entre esses pedaços é o problema mais difícil da casa.
</div>

### O mapa-múndi dentro da squad

Essa foi a maior diferença cultural em relação a tudo que eu tinha vivido. Nas duas squads, **eu nunca dividi time com alguém do mesmo país que eu** — com uma única exceção, na segunda.

<table class="compare-table">
  <thead>
    <tr><th></th><th>Engineering Manager</th><th>Engenheiros</th></tr>
  </thead>
  <tbody>
    <tr><td>Grocery Fulfillment</td><td>Nigéria</td><td>Egito, Polônia, Ucrânia, Jordânia</td></tr>
    <tr><td>Shopping Experience</td><td>Argentina, criado na Espanha</td><td>Índia, Paquistão, Brasil, Rússia</td></tr>
  </tbody>
</table>

Meus dois gestores foram um nigeriano — hoje morando em Portugal — e um argentino criado na Espanha, hoje em Varsóvia. O detalhe de onde os dois estão atualmente diz bastante sobre Dubai: é uma cidade de passagem, inclusive para quem lidera.

<div class="callout callout-tip">
  <div class="callout-label">Trabalhar sem cultura majoritária</div>
  Num time onde cada pessoa vem de um país diferente, não existe um "jeito padrão" implícito que todo mundo entende sem falar. Tudo precisa ser explicitado: o que significa um prazo, quando alguém está discordando, o que é uma pergunta e o que é uma cobrança. É mais trabalhoso — e é o ambiente onde eu mais aprendi a comunicar por escrito com clareza.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>O projeto e as tecnologias</h2></div>
</div>

O pano de fundo dos dois anos foi um só: **migração de arquitetura monolítica para microsserviços**. Todo o resto acontecia em cima disso.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-code"></i> C# .NET 5, 6 e 7</div>
    <div class="provider-detail">Base dos serviços e APIs, atravessando três versões do runtime em dois anos.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fab fa-aws"></i> AWS</div>
    <div class="provider-detail">SQS para mensageria e Lambda para processamento sob demanda.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-database"></i> SQL Server e PostgreSQL</div>
    <div class="provider-detail">Dois bancos relacionais convivendo — típico de migração em andamento.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-diagram-project"></i> KrakenD, Luna e GoLang</div>
    <div class="provider-detail">Camada de BFF e API gateway, agregando serviços para o app.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fab fa-python"></i> Python</div>
    <div class="provider-detail">Presente no ferramental e nas frentes de dados.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-vial"></i> DDD e TDD</div>
    <div class="provider-detail">Domain Driven Design nos dois times; Test Driven Development a partir do segundo.</div>
  </div>
</div>

### O que eu construí

No **Grocery Fulfillment**, três frentes que eu gosto de contar porque são problemas que só existem quando software encosta no mundo real:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-heart-pulse"></i> Heartbeat de catálogo</div>
    <div class="provider-detail">Monitoração de disponibilidade de item, permitindo ao separador marcar um produto como indisponível durante a separação.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-right-left"></i> Substituição de itens</div>
    <div class="provider-detail">Cliente, separador e retaguarda podendo trocar um item indisponível já dentro do pedido.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-phone-volume"></i> Robocalls</div>
    <div class="provider-detail">Ligações telefônicas automatizadas via integração com Asterisk.</div>
  </div>
</div>

O caso da substituição de item é o meu favorito para explicar o que é um domínio difícil: um pedido já pago, um produto que acabou, três atores diferentes com poder de alterar o mesmo carrinho ao mesmo tempo, e um entregador a caminho. Não é um problema de código — é um problema de modelagem de domínio, e é exatamente onde DDD deixa de ser sigla e vira ferramenta.

No **Shopping Experience**, o foco virou busca, ofertas e experiência de navegação, mais a construção da camada de BFF.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>A rotina</h2></div>
</div>

Se no Porto a palavra era *calma*, aqui a palavra é **elevada**. Empresa em hipercrescimento, escala grande, migração arquitetural em curso e um domínio que não perdoa erro.

### A semana que mudou de dia

Historicamente, a semana útil nos Emirados ia de **domingo a quinta-feira**, com sexta e sábado como fim de semana, porque a sexta é o dia da oração congregacional no Islã.

Em **1º de janeiro de 2022**, os Emirados mudaram para uma semana de **segunda a sexta**, com a sexta encurtada — tornando-se o primeiro país do Golfo a alinhar seu calendário ao ocidental. Eu vivi exatamente essa transição, que coincidiu quase perfeitamente com a minha troca de squad.

<table class="compare-table">
  <thead>
    <tr><th>Período</th><th>Semana útil</th><th>Fim de semana</th></tr>
  </thead>
  <tbody>
    <tr><td>Até dez/2021</td><td>Domingo a quinta</td><td>Sexta e sábado</td></tr>
    <tr><td>A partir de jan/2022</td><td>Segunda a sexta (sexta reduzida)</td><td>Sábado e domingo</td></tr>
  </tbody>
</table>

A mudança foi boa por duas razões práticas: alinhou o calendário com o resto do mundo e facilitou muito planejar viagens — quando seu fim de semana é sexta e sábado, quase todo voo e todo evento internacional cai fora dele.

E a sexta-feira nova ficou com uma personalidade própria. É comum que colegas muçulmanos parem no horário do almoço para a oração, e parte deles não retorna ao expediente. Isso transformava o dia num **dia sem reuniões**: dava para usar para foco, encerrar mais cedo por volta das 16h, ou simplesmente trabalhar normal. Sexta em Dubai passou a ter, ao mesmo tempo, cara de dia útil e clima de fim de semana.

<div class="callout callout-tip">
  <div class="callout-label">Ramadã e jornada reduzida</div>
  Durante o mês do Ramadã, a lei trabalhista dos Emirados prevê <strong>redução da jornada diária</strong> — um benefício que, na prática, se aplica a todos os funcionários, muçulmanos ou não, na maioria das empresas. É uma das coisas que mais me marcou culturalmente: o calendário religioso não é um detalhe pessoal de quem pratica, ele reorganiza o funcionamento do país inteiro.
</div>

### A semana desenhada por dia

Na segunda squad, o calendário tinha um desenho que eu passei a admirar bastante — sprints de duas semanas, com as cerimônias concentradas nas pontas:

<table class="compare-table">
  <thead>
    <tr><th>Dia</th><th>O que acontecia</th></tr>
  </thead>
  <tbody>
    <tr><td>Segunda</td><td>Reuniões de planejamento</td></tr>
    <tr><td>Terça (manhã)</td><td>Bugs sem prioridade e tickets de dívida técnica</td></tr>
    <tr><td>Terça (tarde)</td><td><strong>Chapter</strong> — encontro por especialidade</td></tr>
    <tr><td>Quinta</td><td>Dia de escritório</td></tr>
    <tr><td>Última sexta do sprint</td><td>Retrospectiva</td></tr>
  </tbody>
</table>

O efeito colateral desse desenho é ótimo: como o sprint durava duas semanas e as cerimônias caíam numa sexta e na segunda seguinte, sobrava **uma semana inteira sem reunião de processo**. Bloco de foco de verdade, não aquele "no-meeting Wednesday" que dura até alguém marcar algo.

As **terças** eram reservadas para dívida técnica e para o *chapter* — a reunião de todos que trabalhavam na mesma especialidade, atravessando as squads, para propor soluções de alcance transversal. Havia chapter de backend (o meu), de produto, de frontend, de mobile nativo e de mobile em Flutter. O pessoal de infraestrutura, DevOps e plataforma participava de todos.

<div class="callout callout-tip">
  <div class="callout-label">Por que <em>chapters</em> funcionam</div>
  Numa organização fatiada em squads verticais, cada time resolve seus próprios problemas — e as mesmas soluções acabam sendo reinventadas cinco vezes em paralelo. O chapter é o eixo horizontal que corrige isso: um espaço fixo onde a especialidade conversa consigo mesma. Reservar <strong>uma tarde por semana</strong> para isso, com dívida técnica de manhã no mesmo dia, é uma das coisas mais saudáveis que eu vi numa empresa desse porte.
</div>

### Escritório, verão e a rotina social

O presencial era leve: em geral **um dia por semana**, normalmente às quintas. E no verão a régua caía drasticamente — algo como **uma ida a cada dois meses**, ou seja, cerca de duas vezes ao longo dos quatro meses de calor.

Faz todo sentido para quem já passou um verão no Golfo. Não é uma questão de conforto: com temperaturas que ultrapassam os 45 °C, sair de casa no meio do dia é uma decisão logística.

O verão também esvaziava a cidade. Muita gente voltava ao país de origem por semanas. Eu escolhi outra coisa: como tinha acabado de sair do Brasil, não tinha o menor interesse em voltar tão cedo, nem para visitar — usei o período para **viajar pela Europa**.

E havia um ritual que eu levo comigo: a cada um ou dois meses, um **happy hour pago pela empresa**. Algumas vezes o time chegou a fazer a retrospectiva do sprint num bar. A empresa cobria comida e narguilé; bebida alcoólica ficava por conta de cada um.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Por que eu saí</h2></div>
</div>

Não foi uma decisão tomada num dia. Foram quatro coisas se acumulando.

### 1. O projeto deixou de me interessar

A frente em que eu estava não era o tipo de trabalho que eu queria fazer nos anos seguintes. Isso, sozinho, não faz ninguém mudar de país — mas remove a razão que faz você tolerar todo o resto.

### 2. Plantão não remunerado

Essa foi a fonte de desgaste mais concreta.

O telefone tocava **toda terça-feira, às 6h da manhã** — não por incidente real, mas porque a execução de testes de carga disparava o sistema de alertas, que ligava automaticamente para quem estivesse de plantão. Um alarme previsível, recorrente e inteiramente evitável, transformado em despertador semanal.

Somava-se a isso o trabalho real durante o plantão, causado com frequência por **erros originados em outras squads, outros times e até outros países**. Você acordava de madrugada para resolver algo que não era do seu domínio, sem remuneração adicional pelo regime de sobreaviso.

<div class="callout callout-warn">
  <div class="callout-label">Pergunte sobre on-call antes de assinar</div>
  Plantão é o item que mais frequentemente fica de fora da conversa durante o processo seletivo, e o que mais afeta qualidade de vida depois. Vale perguntar explicitamente: existe escala de sobreaviso? É remunerada ou compensada em folga? Qual foi o volume real de acionamentos no último trimestre? Quantos deles eram alarmes falsos? Uma empresa que mede isso vai saber responder. Uma que não mede já respondeu.
</div>

### 3. O retorno ao presencial integral, avisado com dois dias

A empresa decidiu voltar ao escritório **cinco dias por semana**. A comunicação veio por e-mail numa **segunda-feira**, informando que a partir da **quarta** o presencial seria obrigatório.

Depois de quase dois anos de modelo híbrido — com verões de uma ida a cada dois meses —, a mudança em si já era grande. O prazo de dois dias para reorganizar a vida foi o que transformou uma decisão administrativa em sinal sobre a empresa.

### 4. O escritório ficou mais longe e mais caro

Em paralelo, a empresa mudou de prédio: saiu de **Business Bay** para o **City Walk**. O novo endereço ficava longe demais da estação de metrô para se fazer o trajeto a pé, o que empurrava a locomoção para o táxi — e encareceu o deslocamento diário.

Isoladamente, é um detalhe logístico. Combinado com a exigência de estar lá **todos os dias**, virou um custo diário concreto, em dinheiro e em tempo, imposto sem aviso.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a viagem que virou mudança
  </div>
  <p>Em <strong>fevereiro de 2023</strong> eu vim à Europa a passeio. Tinha combinado a viagem com uma amiga que morava em Malta: Manchester, onde vive um dos meus melhores amigos; Londres, onde eu não conhecia ninguém na época; e Dublin, onde eu tinha vários amigos, incluindo dois dos mais próximos.</p>
  <p>Eu vim como turista. Voltei tendo decidido morar aqui.</p>
</div>

### O processo, conduzido de Dubai

Do primeiro contato até eu escolher para onde ir levou cerca de **dois meses**. Dessa vez não foi o LinkedIn: cheguei através de um **recrutador indicado**, de uma consultoria de recrutamento e seleção, que cuidou de encontrar as vagas.

O processo incluiu triagem e **teste online de algoritmos** no estilo LeetCode. No fim, eu tinha três opções na mesa — entre elas a **OUTsurance** e a RetailInMotion — e precisei escolher.

Saí da Talabat em **março de 2023** e mudei para Dublin em **23 de abril de 2023**.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">10</div>
  <div class="section-title-wrap"><h2>Linha do tempo</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Quando</th><th>O quê</th></tr>
  </thead>
  <tbody>
    <tr><td>26/01/2021</td><td>Primeira mensagem da recrutadora no LinkedIn — sem resposta</td></tr>
    <tr><td>04/03/2021</td><td>Follow-up; respondo e envio o currículo</td></tr>
    <tr><td>17/03/2021</td><td>Primeira call com a Talabat</td></tr>
    <tr><td>Mar–Abr/2021</td><td>Seis etapas: screening, RH, live coding, system design, VP de Engenharia e alocação</td></tr>
    <tr><td>21/04/2021</td><td>Carta de oferta, válida por três dias úteis</td></tr>
    <tr><td>Abr–Mai/2021</td><td>Desligamento dos dois contratos paralelos</td></tr>
    <tr><td>30/05/2021</td><td>Primeiro dia na Talabat — remoto, do Brasil, acordando às 4h</td></tr>
    <tr><td>Mai–Dez/2021</td><td>Squad Grocery Fulfillment</td></tr>
    <tr><td>Jun–Nov/2021</td><td>Contrato CLT paralelo com filial brasileira de empresa americana, encerrado pela mudança</td></tr>
    <tr><td>26/11/2021</td><td>Voo de Guarulhos para Dubai, pago pela empresa</td></tr>
    <tr><td>27/11/2021</td><td>Pouso em Dubai às 19h — e final da Libertadores num bar, à noite</td></tr>
    <tr><td>28/11/2021</td><td>Primeiro dia no escritório, um domingo</td></tr>
    <tr><td>Dez/2021</td><td>Covid e quarentena entre o Natal e o Ano-Novo, no hotel</td></tr>
    <tr><td>01/01/2022</td><td>Os Emirados mudam a semana útil para segunda a sexta</td></tr>
    <tr><td>Jan/2022</td><td>Troca para a squad Shopping Experience; mudança para o apartamento em JLT</td></tr>
    <tr><td>Fev/2023</td><td>Viagem de férias a Manchester, Londres e Dublin</td></tr>
    <tr><td>Fev–Mar/2023</td><td>Processo seletivo na Irlanda, conduzido de Dubai</td></tr>
    <tr><td>Mar/2023</td><td>Saída da Talabat — um ano e onze meses</td></tr>
    <tr><td>23/04/2023</td><td>Mudança para Dublin</td></tr>
  </tbody>
</table>

<div class="conclusion">
  <h2>O que ficou desses dois anos</h2>
  <p>Dubai me deu a experiência técnica mais dura da carreira e o ambiente mais internacional em que eu já trabalhei. Um time onde ninguém compartilha a sua língua materna te obriga a comunicar de um jeito que nenhum curso ensina — e eu saí de lá escrevendo muito melhor do que entrei.</p>
  <p>Também me deu a resposta para uma pergunta que eu não sabia que estava fazendo. O plano original, lá no capítulo do Porto, era usar Portugal como porta de entrada para a Europa. Dubai foi um desvio de quase dois anos — extraordinariamente bem pago, extraordinariamente formativo — e ainda assim um desvio. Quando eu passei uma semana de férias em Dublin, em fevereiro de 2023, a resposta veio sozinha.</p>
  <p>No próximo e último post da série: entrevista e contrato feitos inteiramente por Zoom, de Dubai. Cheguei em Dublin num domingo e comecei a trabalhar na segunda.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Talabat. <strong>About us.</strong>
      <a href="https://corporate.talabat.com/about/" target="_blank">talabat.com</a>
    </li>
    <li>
      Delivery Hero. <strong>Our brands.</strong>
      <a href="https://www.deliveryhero.com/brands-countries/" target="_blank">deliveryhero.com</a>
    </li>
    <li>
      U.AE — Portal oficial do Governo dos Emirados Árabes Unidos. <strong>Working hours and leaves.</strong>
      <a href="https://u.ae/en/information-and-services/jobs/employment-in-the-private-sector/working-hours" target="_blank">u.ae</a>
    </li>
  </ol>
</div>
