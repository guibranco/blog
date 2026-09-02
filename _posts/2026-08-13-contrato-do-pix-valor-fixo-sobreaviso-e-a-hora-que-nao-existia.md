---
layout: post
lang: pt-BR
title: "O contrato do PIX: valor fixo, sobreaviso e a hora que o contrato aboliu e teve que reconstruir"
description: "A anatomia financeira de um contrato PJ dentro do projeto do PIX em 2020: a troca de valor-hora por valor fixo, o preço do sobreaviso, o mês de sete dias por semana que não tinha cláusula e a nota fiscal de janeiro que quase não existiu. Com os números reais das minhas notas fiscais."
date: 2026-08-13
categories: [Career]
subcategories:
  - "Career/Behind the Scenes"
tags: [pix, contrato, pj, clt, sobreaviso, on-call, carreira, career, consultoria, hora-extra, vinculo-empregaticio, banco-central]
medium_tags: [pix, contracting, career, on-call, freelancing]
reading_time: 14
cover: /assets/img/posts/pix-contrato-capa.svg
image: /assets/img/posts/pix-contrato-capa.png
series: pix-bs2
series_title: Desenvolvendo o PIX
series_part: 2
---

<p class="lead">Em março de 2020 eu troquei um contrato por hora trabalhada por um contrato de valor fixo mensal. Na hora, foi um aumento de 19%. Seis meses depois, trabalhando sete dias por semana num projeto com prazo do Banco Central, foi a cláusula que me deixou sem instrumento nenhum. Este texto é a anatomia financeira daquela decisão, com os números das minhas notas fiscais.</p>

<div class="callout callout-tip">
  <div class="callout-label">Este é o segundo de três textos</div>
  A história de como eu fui parar no projeto está na <a href="{{ site.baseurl }}/artigos/construindo-o-pix-no-bs2-bastidores-de-um-prazo-do-banco-central/">primeira parte, sobre os bastidores de um prazo do Banco Central</a>. A arquitetura — SPI, ISO 20022, os percentis do Manual de Tempos — está na <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">terceira parte. Aqui o assunto é contrato: quanto, como, quando e o que faltava estar escrito.</a>
</div>

<div class="callout callout-warn">
  <div class="callout-label">Sobre os números</div>
  Todos os valores deste texto são reais e vêm dos meus próprios contratos, aditivos e notas fiscais de serviço da época — são meus dados, e por isso posso publicá-los. O que fica de fora: o nome da consultoria pela qual eu era contratado, o nome dos colegas e a margem praticada por terceiros, que eu não conheço. Cito apenas o CIO do banco, pelo papel público que ocupava.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Fevereiro de 2020: a nota fiscal que explica a decisão</h2></div>
</div>

Eu era PJ, contratado por uma consultoria de São Paulo e alocado no time B2B de um banco digital. O contrato era simples e do tipo mais comum do mercado de tecnologia paulistano na época: **valor por hora trabalhada**.

<table class="compare-table">
  <thead>
    <tr><th>Vigência</th><th>Modelo</th><th>Valor</th><th>Jornada contratada</th></tr>
  </thead>
  <tbody>
    <tr><td>01/07/2019</td><td>Por hora</td><td>R$ 68,00/h</td><td>8 h/dia, 5 dias/semana — média de 168 h/mês</td></tr>
    <tr><td>01/03/2020</td><td>Por hora</td><td>R$ 74,80/h <em>(+10%)</em></td><td>Idem</td></tr>
    <tr><td>01/03/2020 <em>(aditivo de 31/03, retroativo)</em></td><td>Valor fixo</td><td>R$ 15.000,00/mês</td><td>Idem</td></tr>
  </tbody>
</table>

A nota fiscal que eu emiti em **02 de março de 2020**, referente ao mês de fevereiro, saiu no valor de **R$ 8.772,00**. Repare que isso é exatamente **129 horas a R$ 68,00**. Um mês cheio, pelo contrato, seriam 168 horas — **R$ 11.424,00**.

Ou seja: em fevereiro eu deixei **R$ 2.652,00 na mesa** porque tirei folga.

Esse número é a decisão inteira. Eu não era um profissional em conflito com a empresa, nem estava sendo prejudicado por ninguém: o contrato fazia exatamente o que dizia que ia fazer. O problema é que ele criava um incentivo que eu detestava. Toda folga tinha preço de tabela, e eu folgava — não por indisciplina, mas porque o meu ritmo naquele time era esse. Eu chegava ao escritório por volta da uma da tarde e ficava até as sete, oito da noite, oito ou nove horas por dia, só deslocado do horário comercial. Quando eu precisava de uma tarde, a tarde saía do meu faturamento.

<div class="callout callout-tip">
  <div class="callout-label">Por que isso importa mais do que parece</div>
  Contrato por hora transforma descanso em despesa. Isso é ótimo enquanto o volume de trabalho é previsível, porque você é pago exatamente pelo que entrega. Mas ele te ensina, todo mês, que parar custa dinheiro — e é uma lição que se paga com saúde antes de se pagar com produtividade.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Março: a contraproposta que veio com uma pergunta</h2></div>
</div>

O contexto está na primeira parte da série: eu tinha uma proposta externa e fui conversar com o CIO do banco para pedir demissão, já esperando que dali saísse uma contraproposta.

A proposta externa era da **Wirecard Brasil**, a antiga Moip, com escritório na Brigadeiro Faria Lima. Salário maior, mas vaga em Java — trocar de empresa e de stack ao mesmo tempo. Guardo esse detalhe com um certo carinho retrospectivo: três meses depois, em **25 de junho de 2020**, a matriz alemã pediu insolvência depois de admitir que 1,9 bilhão de euros do seu balanço simplesmente não existiam, no maior escândalo contábil do sistema financeiro europeu recente. A operação brasileira acabou vendida. Recusei aquela vaga pelo motivo errado — a linguagem de programação — e foi a melhor decisão de carreira que eu tomei naquele ano.

Na conversa, antes de oferecer qualquer coisa, o **Fernando Radunz** fez uma pergunta só: qual era o meu valor-hora. Respondi: R$ 74,80. A contraproposta veio em cima disso — **R$ 15.000,00 fixos por mês**, mesma jornada contratada, mesma vigência.

Vale fazer a conta que eu fiz na hora:

<table class="compare-table">
  <thead>
    <tr><th>Cenário</th><th>Cálculo</th><th>Mês cheio</th></tr>
  </thead>
  <tbody>
    <tr><td>Por hora, presença integral</td><td>R$ 74,80 × 168 h</td><td>R$ 12.566,40</td></tr>
    <tr><td>Por hora, um mês como fevereiro</td><td>R$ 74,80 × 129 h</td><td>R$ 9.649,20</td></tr>
    <tr><td><strong>Valor fixo proposto</strong></td><td>—</td><td><strong>R$ 15.000,00</strong></td></tr>
  </tbody>
</table>

O fixo era **19,4% acima** do que eu ganharia por hora trabalhando o mês inteiro sem faltar um dia — e mais de 50% acima do que eu tinha faturado em fevereiro. Além disso, ele resolvia o incentivo perverso: folga deixaria de custar dinheiro.

Não havia decisão difícil ali. Aceitei.

<div class="callout callout-tip">
  <div class="callout-label">Um detalhe administrativo que virou dinheiro</div>
  O aditivo foi assinado em <strong>31 de março</strong> com vigência retroativa a <strong>1º de março</strong>, e as notas eram emitidas depois do período trabalhado. Resultado: a nota de 1º de abril já saiu com os R$ 15.000,00 cheios. Eu tinha assumido que março viria pro rata pela troca no meio do mês, e não veio. Quem negocia contrato aprende rápido que a <strong>data de vigência</strong> vale mais do que a data da assinatura.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>A hora que o contrato aboliu — e teve que reconstruir</h2></div>
</div>

Aqui está a parte mais bonita, no sentido de contradição elegante, de toda essa história.

O PIX liquida 24 horas por dia, sete dias por semana. Um sistema assim não tem noite, e alguém precisa estar acordável às três da manhã de domingo. Foi a primeira vez na minha carreira que entrei numa escala de sobreaviso.

O desenho do pareamento era inteligente: ficávamos **em duplas, de preferência com pessoas de duas frentes diferentes**, e cada um precisava ter conhecimento básico das outras duas. Às três da manhã você não quer descobrir que o único problema possível é exatamente o da frente que ninguém da dupla conhece. A semana começava à meia-noite de sábado para domingo e terminava às 23h59min59s do sábado seguinte — sete dias corridos de disponibilidade, com os fins de semana cobertos integralmente. A recomendação era andar com o notebook e evitar lugares de onde não desse para atuar: uma semana sem cinema, sem viagem, sem trilha, sem nada longe de uma tomada.

E aí veio o problema. **Como se paga sobreaviso a quem tem valor fixo?**

Eu não tinha mais valor-hora. Tinha acabado de abrir mão dele três meses antes, em troca de liberdade de agenda. Mas sobreaviso é, por natureza, um custo medido em horas de disponibilidade — não em entrega.

A solução veio no *Schedule of Agreement* que eu recebi em **2 de dezembro de 2020**:

<table class="compare-table">
  <thead>
    <tr><th>Linha</th><th>Valor</th><th>Unidade</th></tr>
  </thead>
  <tbody>
    <tr><td>STD Monthly Rate</td><td>R$ 15.000,00</td><td>Mensal</td></tr>
    <tr><td>Overtime Hourly Rate <em>(hora de sobreaviso)</em></td><td>R$ 26,79</td><td>Por hora</td></tr>
    <tr><td>Horas acionadas</td><td>R$ 89,29</td><td>Por hora</td></tr>
  </tbody>
</table>

Faça a divisão: **R$ 15.000,00 ÷ 168 horas = R$ 89,2857**. O valor da hora acionada é, com arredondamento, exatamente o valor fixo dividido pela jornada contratada. Para conseguir pagar o plantão, alguém precisou reconstruir a hora que o contrato tinha abolido — e reconstruiu usando a mesma jornada que o modelo de valor fixo supostamente tinha deixado de medir.

Isso diz uma coisa importante sobre valor fixo em geral: **ele não elimina a hora, só a esconde**. Ela continua lá, dividindo o mensal pela jornada, e reaparece toda vez que alguém precisa precificar qualquer coisa fora do combinado.

### Os 30% que quase foram um terço

O segundo número merece atenção. R$ 26,79 é exatamente **30% de R$ 89,29**.

A CLT, no artigo 244, §2º, define que as horas de sobreaviso são contadas à razão de **um terço** do salário normal — regra originalmente dos ferroviários, estendida às demais categorias pela Súmula 428 do TST, que reconhece o sobreaviso de quem fica em regime de plantão aguardando chamado por meio telemático. Um terço de R$ 89,29 seria **R$ 29,76**.

Ou seja: o parâmetro usado foi 30%, não 33,3%. Uma diferença de **R$ 2,97 por hora** — que, numa semana inteira de escala, dá quase R$ 380,00.

<div class="callout callout-warn">
  <div class="callout-label">Sobre o acionamento</div>
  Eu carreguei por anos a lembrança de que o acionamento pagava <strong>uma vez e meia</strong> o valor-hora. Ao reler o documento para escrever este texto, descobri que não: pagava o valor-hora cheio, sem adicional. Faz sentido do ponto de vista de quem redigiu — eu já recebia o fixo independentemente das horas, então a hora acionada é remuneração adicional integral. Mas hoje eu negociaria 1,5× mesmo assim. Acordar às três da manhã de domingo não é a mesma coisa que trabalhar às três da tarde de terça, e o preço deveria refletir isso.
</div>

### O detalhe da planilha que expôs dois mundos

Eu era o único PJ do time do PIX. Todos os outros também eram terceirizados, mas contratados em CLT pelas suas respectivas consultorias.

Numa semana de plantão, lancei **16 horas de sobreaviso por dia** na planilha. O sistema esperava 15. Recebi um questionamento do RH do próprio banco, e tive que ser eu — o PJ, terceiro, de fora — explicar ao RH da instituição por que o meu número era diferente do dos meus colegas.

<table class="compare-table">
  <thead>
    <tr><th>Regime</th><th>Jornada</th><th>Sobreaviso no dia útil</th><th>Fim de semana</th></tr>
  </thead>
  <tbody>
    <tr><td>PJ (meu caso)</td><td>8 h</td><td>16 h</td><td>24 h</td></tr>
    <tr><td>CLT</td><td>9 h — 8 de trabalho e 1 de almoço</td><td>15 h</td><td>24 h</td></tr>
  </tbody>
</table>

A conta era simples: os CLTs tinham janela de 9 horas porque a hora de almoço entra nela, e eu, PJ, não tinha intervalo contratual. Uma diferença de um único número numa planilha — que expunha duas relações de trabalho distintas convivendo no mesmo time, no mesmo plantão, com o mesmo celular do lado da cama.

E vale registrar o desfecho: **eu nunca fui acionado**. Fiquei de sobreaviso duas ou três semanas até sair do banco, e não houve uma única chamada. O sistema que a gente construiu não me acordou nenhuma vez.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Setembro: a cláusula que não existia</h2></div>
</div>

Guarde a ironia: o sobreaviso, que tinha cláusula escrita, tabela e valor por hora, **quase não me custou nada** — foram duas ou três semanas de celular por perto e zero acionamentos.

O que me custou foi setembro, que não tinha cláusula nenhuma.

O registro de chaves entrava em produção em 5 de outubro, a homologação junto ao Banco Central corria em paralelo e a especificação técnica tinha fechado havia poucas semanas. Setembro virou um mês de sete dias por semana: **trabalhei três dos quatro fins de semana do mês** — 5 e 6, 12 e 13, 26 e 27 de setembro —, além de horas extras nos dias úteis. O único fim de semana livre foi o de 19 e 20, o do churrasco do time em Confins.

E o detalhe que torna esses três fins de semana especialmente irritantes em retrospecto: eles foram, na minha frente, **trabalho braçal isolado**. Não dependiam de colaboração, de outro time nem de resposta do Banco Central. Era volume, não coordenação — o tipo de esforço que existe justamente porque a decisão de escopo foi tomada tarde demais.

E aqui está o fato que organiza este texto todo:

<div class="callout callout-warn">
  <div class="callout-label">Quem recebeu e quem não recebeu</div>
  Todo mundo que estava em <strong>contrato por hora</strong> — PJ ou CLT — recebeu as horas extras de setembro: os sábados, os domingos e também as horas extras do dia a dia. Eu, no valor fixo, recebi exatamente o mesmo que receberia num mês tranquilo. A mesma cláusula que em março tinha me dado 19% de aumento e liberdade de agenda, em setembro me deixou sem instrumento nenhum.
</div>

Valor fixo é uma aposta simétrica: você ganha nos meses tranquilos e paga nos meses de crise. O problema é que **projeto com prazo regulatório não tem mês tranquilo depois que o cronograma aperta**. Ele tem uma reta final que come, de uma vez só, todo o excedente que você acumulou no começo. Em março, com trabalho previsível, eu comprei liberdade barato. Em setembro descobri que tinha vendido o meu único mecanismo de defesa.

### O único momento de tensão

Houve um episódio que vale contar porque ele mostra onde essa assimetria aparece na prática, e não na planilha.

Numa sexta-feira e depois numa segunda, fui questionado sobre participar da *daily* nos fins de semana. Respondi que não via motivo: eu estava trabalhando horas extras que, até aquele momento, não estavam sendo pagas, e o trabalho daquelas frentes naquele momento era isolado — não dependia de colaboração, de outros times nem de resposta do Banco Central. Nada bloqueante seria resolvido num domingo de qualquer forma, e o que houvesse eu poderia reportar ao longo do dia ou na segunda.

Foi o único atrito do projeto inteiro, e resolveu-se com profissionalismo dos dois lados. Mas ele me fez, pela primeira e única vez, cogitar uma coisa que eu nunca cheguei a levar adiante: **entrar com uma ação de reconhecimento de vínculo empregatício**.

<div class="callout callout-warn">
  <div class="callout-label">Por que a ação teria fundamento</div>
  Repare no conjunto: eu era PJ, mas tinha <strong>jornada contratada</strong> (8 h/dia, 5 dias/semana), estava numa <strong>escala de plantão</strong> definida pelo time, era cobrado por <strong>presença em cerimônia</strong>, lançava horas numa <strong>planilha auditada pelo RH do cliente</strong> e respondia a um coordenador do cliente. Isso é, ponto a ponto, o desenho de subordinação que a Justiça do Trabalho usa para caracterizar vínculo. A pejotização de trabalho subordinado é exatamente esse ponto — e não é uma zona cinzenta técnica, é o ponto contestado.
</div>

Não fui adiante, e não me arrependo de não ter ido. Mas registro porque a lição não é sobre aquele banco especificamente: é que **quem aceita PJ em regime de subordinação está financiando, com direitos abdicados, uma economia que o Judiciário considera irregular** — e o preço disso só aparece quando as coisas apertam.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>A nota fiscal que quase não existiu</h2></div>
</div>

Em dezembro, quando eu já tinha comunicado a minha saída, recebi uma mensagem de WhatsApp do gerente de serviços financeiros: as horas extras de setembro **seriam pagas**. Vinha junto um pedido de desculpas — o banco já sabia da minha saída, mas o gerente de contas da consultoria ainda não tinha sido informado. Uma falha de comunicação do lado da consultoria, não do banco.

Deixa eu ser explícito sobre o que isso significa. **Aquele pagamento aconteceu porque uma pessoa se lembrou.** Não havia cláusula que o obrigasse, não havia processo automático, não havia gatilho contratual. Se aquela mensagem não tivesse sido enviada, eu teria saído do projeto do PIX com três fins de semana e um mês de horas extras não remunerados, e nem instrumento eu teria para reclamar — porque, contratualmente, eu não tinha direito a nada além dos R$ 15.000,00.

Os números das duas últimas notas fiscais:

<table class="compare-table">
  <thead>
    <tr><th>Nota fiscal</th><th>Valor</th><th>Composição</th></tr>
  </thead>
  <tbody>
    <tr><td>Notas de abril a outubro</td><td>R$ 15.000,00</td><td>Somente o fixo</td></tr>
    <tr><td>Penúltima</td><td>R$ 16.071,60</td><td>Fixo + R$ 1.071,60 — 40 h de sobreaviso a R$ 26,79</td></tr>
    <tr><td><strong>Última — 05/01/2021</strong></td><td><strong>R$ 30.776,45</strong></td><td>Fixo de dezembro + sobreaviso + o extra de setembro</td></tr>
  </tbody>
</table>

A última nota merece ser aberta linha por linha, porque ela é o resumo financeiro da história inteira:

<table class="compare-table">
  <thead>
    <tr><th>Componente</th><th>Cálculo</th><th>Valor</th></tr>
  </thead>
  <tbody>
    <tr><td>Valor fixo de dezembro</td><td>—</td><td>R$ 15.000,00</td></tr>
    <tr><td>Uma semana completa de sobreaviso</td><td>128 h × R$ 26,79</td><td>R$ 3.429,12</td></tr>
    <tr><td><strong>Extra de setembro</strong></td><td>—</td><td><strong>R$ 12.347,33</strong></td></tr>
    <tr><td><strong>Total</strong></td><td>—</td><td><strong>R$ 30.776,45</strong></td></tr>
  </tbody>
</table>

Aquela semana de dezembro foi a única escala que eu cumpri integralmente — 16 horas por dia útil mais 24 horas por dia de fim de semana, os 128 h da tabela. A de novembro, na penúltima nota, foi parcial: 40 horas, menos de um terço de uma semana cheia.

E aí está a linha que interessa. O extra de setembro — **R$ 12.347,33** — equivale a **138 horas** ao meu valor-hora implícito de R$ 89,29, ou a **82% de uma mensalidade inteira**. Bate com a realidade do mês: seis dias de fim de semana trabalhados dão 48 horas, e o resto — umas 90 horas — corresponde a mais ou menos **quatro horas extras por dia útil** ao longo de setembro. É exatamente o formato de um mês de reta final.

<div class="callout callout-warn">
  <div class="callout-label">O detalhe mais desconfortável: o número não era meu</div>
  Aquele valor <strong>não foi calculado a partir das minhas horas</strong>, porque eu não tinha horas para apresentar. Contrato de valor fixo não gera apontamento — foi justamente isso que eu comprei em março. Pelo que entendi na época, o número saiu de uma <strong>média do que o resto do time lançou nas respectivas planilhas</strong>. Ou seja: a minha remuneração pelo mês mais pesado do projeto foi estimada a partir do registro dos meus colegas. Deu certo porque eles trabalharam tanto quanto eu, e porque quem fez a estimativa foi generoso. Nenhuma das duas coisas era garantida.
</div>

O valor é justo. E chegou **quatro meses depois**, num pagamento único, numa nota emitida cinco dias depois de eu já ter saído.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o que eu senti ao emitir aquela nota
  </div>
  <p>Alívio, e um incômodo que demorou anos para eu conseguir nomear. Alívio porque o dinheiro era significativo e eu estava juntando para sair do Brasil. Incômodo porque eu tinha acabado de descobrir que a minha remuneração por um mês inteiro de trabalho excepcional dependia da boa memória de um gestor.</p>
  <p>Não foi má-fé de ninguém — pelo contrário, a pessoa que se lembrou fez isso por conta própria, com pedido de desculpas incluído, quando já não tinha obrigação nenhuma comigo. É justamente aí que mora a lição: <strong>quando o seu pagamento depende de alguém ser decente, você não tem um contrato, você tem sorte</strong>. E eu tive.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>A camada que ninguém vê: a consultoria no meio</h2></div>
</div>

Nada disso acontecia numa relação direta com o banco. Eu era PJ contratado por uma consultoria de São Paulo, que me alocava no cliente — cheguei lá, aliás, por indicação de um conhecido que já trabalhava no banco pela mesma consultoria, que é como boa parte desse mercado funciona de verdade.

O mapa de contratação valia um estudo sociológico:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">O time B2B, em São Paulo</div>
    <div class="provider-detail">Quatro ou cinco consultorias diferentes convivendo no mesmo time — e não só desenvolvedores: até o designer de UI/UX era terceirizado. O modelo predominante era <strong>PJ</strong>.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O time do PIX, em Belo Horizonte</div>
    <div class="provider-detail">Também terceirizado, mas por consultorias mineiras — e todas contratavam <strong>CLT</strong>. Cultura regional de contratação, não coincidência.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Os funcionários do banco</div>
    <div class="provider-detail">Alguns contratados diretos, e exatamente <strong>um</strong> PJ direto — um profissional do core com quase vinte anos de casa, exceção histórica que o banco queria encerrar justamente por risco trabalhista.</div>
  </div>
</div>

Eu nunca soube a margem da consultoria. Uma pessoa da equipe de recrutamento chegou a comentar comigo uma vez, e eu não guardei o número — lembro que era alto o suficiente para fazer diferença. Mas é honesto reconhecer que aquele valor nunca seria meu: o banco não me contrataria como PJ direto de jeito nenhum. A única porta realista era virar funcionário CLT — caminho que dois colegas do time, o arquiteto e o head, seguiram depois do lançamento do PIX.

E eu não queria. Não por desprezo pela CLT, mas porque o meu objetivo não era carreira no Brasil.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>O que eu negociaria hoje</h2></div>
</div>

Nada aqui é "nunca aceite valor fixo". Valor fixo foi a decisão certa em março de 2020, com a informação que existia em março de 2020. O que faltava era um punhado de linhas que ninguém escreveu:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">1. Teto de esforço</div>
    <div class="provider-detail">Acima de X horas no mês, ou de N dias trabalhados, volta a valer valor-hora. É a cláusula que faltava no meu contrato, e é a única que teria mudado setembro.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">2. A hora de referência, escrita desde o início</div>
    <div class="provider-detail">Se o mensal dividido pela jornada vai ser usado para precificar sobreaviso e acionamento, que ele esteja no contrato desde o primeiro dia — e não só num aditivo nove meses depois.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">3. Sobreaviso como cláusula permanente</div>
    <div class="provider-detail">Não como aditivo emergencial quando o plantão vira necessidade. E com o parâmetro legal como piso: um terço, não 30%.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">4. Acionamento com adicional</div>
    <div class="provider-detail">1,5× o valor-hora, no mínimo, para chamada fora do horário. O incômodo de madrugada tem que ter preço próprio, senão ele é gratuito para quem escala.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">5. Prazo de pagamento de extras</div>
    <div class="provider-detail">Extra apurado no mês X é pago até o mês X+1. Sem isso, o seu dinheiro vira uma linha na cabeça de alguém — e quatro meses de atraso não é exceção, é o padrão de quem não escreveu prazo.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">6. Apontamento mesmo sem valor-hora</div>
    <div class="provider-detail">Valor fixo dispensa você de bater ponto, não de <strong>anotar</strong>. Se eu tivesse mantido um registro simples das minhas horas em setembro, o extra teria sido calculado com o meu número — e não com a média do que os outros lançaram.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name">7. Reajuste com gatilho, não com conversa</div>
    <div class="provider-detail">Meu aumento de 10% em fevereiro veio porque alguém foi generoso. Funcionou, mas não é mecanismo — é sorte com outro nome.</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">A regra que eu levo comigo</div>
  Toda a diferença entre o sobreaviso e o mês de setembro está numa frase: <strong>o sobreaviso foi remunerado porque alguém sentou e escreveu a regra antes de precisar dela</strong>. Setembro não foi, porque ninguém escreveu. Não era má-fé, era ausência. Em contrato, ausência sempre custa para o lado mais fraco.
</div>

<div class="conclusion">
  <h2>E, mesmo assim, PJ foi a escolha certa</h2>
  <p>Parece contraditório terminar um texto sobre os buracos de um contrato PJ defendendo a escolha por ele, mas as duas coisas convivem — e é exatamente esse o ponto.</p>
  <p>Do ponto de vista estritamente legal, contratar em CLT é o caminho correto e sem zona cinzenta, e a pejotização de trabalho subordinado é indefensável. Do ponto de vista de quem estava sendo contratado, em São Paulo a prática já era costume consolidado, e eu preferia o modelo — o assunto está destrinchado em <a href="{{ site.baseurl }}/artigos/clt-vs-pj-qual-devo-escolher/">CLT, PJ ou MEI: qual devo escolher</a>. Ainda prefiro, <strong>desde que o valor seja coerente com o que ele custa em direitos abdicados</strong>. PJ com valor de CLT é só CLT sem férias, sem 13º, sem FGTS e sem estabilidade.</p>
  <p>No meu caso, o cálculo tinha um objetivo que a maioria dos meus colegas não tinha: eu não estava construindo carreira no Brasil. Desde 2016 eu planejava um intercâmbio na Europa, e entrei naquele banco por três motivos na ordem — o desafio de trabalhar em mercado financeiro, a remuneração, e o fato de ser PJ, que era o que tornava a meta possível. O plano original era sair no fim do contrato de um ano, com o dinheiro do intercâmbio guardado. A pandemia matou o plano do intercâmbio e abriu outro caminho: um mês depois do lançamento do PIX eu embarquei para o Porto — <a href="{{ site.baseurl }}/artigos/trabalhando-pelo-mundo-porto-farfetch/">a primeira vez que saí do Brasil para trabalhar</a> —, com emprego e visto, e não como estudante. Depois vieram Dubai e a Irlanda, onde estou há três anos e meio.</p>
  <p>Ou seja: aquele contrato, com todos os defeitos que este texto descreve, cumpriu o que eu pedi dele. O que eu não sabia negociar em 2020 não era o valor. Era o que fazer quando o combinado deixasse de valer.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Presidência da República. <strong>Decreto-Lei nº 5.452/1943 (CLT), art. 244, §2º — horas de sobreaviso contadas à razão de 1/3 do salário normal.</strong>
      <a href="https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm" target="_blank">planalto.gov.br</a>
    </li>
    <li>
      Tribunal Superior do Trabalho. <strong>Nova redação da Súmula 428 reconhece sobreaviso em escala com celular — aplicação analógica do art. 244, §2º da CLT.</strong>
      <a href="https://www.tst.jus.br/noticias/-/asset_publisher/89Dk/content/nova-redacao-da-sumula-428-reconhece-sobreaviso-em-escala-com-celular" target="_blank">tst.jus.br</a>
    </li>
    <li>
      Startups. <strong>A insolvência da Wirecard — pedido apresentado em 25 de junho de 2020, após a companhia admitir que US$ 2,1 bilhões do caixa não existiam.</strong>
      <a href="https://startups.com.br/negocios/a-insolvencia-da-wirecard-e-o-problema-de-olhar-para-o-outro-lado/" target="_blank">startups.com.br</a>
    </li>
    <li>
      Diário Oficial do Estado de São Paulo. <strong>Wirecard Brazil S.A. ("MOIP") — sede na Av. Brigadeiro Faria Lima, 3064, Itaim Bibi; aquisição pelo PagSeguro aprovada pelo Banco Central em 02/12/2020.</strong>
      <a href="https://diariooficial.imprensaoficial.com.br/doflash/prototipo/2021/Abril/15/empresarial/pdf/pg_0038.pdf" target="_blank">imprensaoficial.com.br</a>
    </li>
  </ol>
</div>
