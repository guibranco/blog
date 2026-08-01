---
layout: post
title: "Trabalhando pelo mundo #1 — Porto: a mudança que nunca aconteceu"
description: "Contratado via LinkedIn por uma consultoria portuguesa para atuar na Farfetch, no Porto, em regime de recibos verdes. Cluster de Search, C# .NET, Elasticsearch, Kafka e Cassandra. Seis meses depois pedi demissão — sem nunca ter pisado em Portugal."
date: 2026-08-05
categories: [Career]
subcategories:
  - "Career/Trabalho no Exterior"
tags: [trabalho-no-exterior, portugal, porto, carreira-internacional, expatriado, farfetch, consultoria, recibos-verdes, tech-visa, remoto, csharp, dotnet, elasticsearch, kafka, cassandra, search, e-commerce, entrevista, processo-seletivo, salario, relocation]
reading_time: 21
cover: /assets/img/posts/trabalhando-pelo-mundo-porto.svg
image: /assets/img/posts/trabalhando-pelo-mundo-porto.png
series: trabalhando-pelo-mundo
series_order: 1
location:
  lat: 41.1579
  lng: -8.6291
  label: "Porto, Portugal (a mudança que não aconteceu)"
---

<p class="lead">Em dezembro de 2020 eu assinei contrato para trabalhar no Porto. Em maio de 2021 eu pedi demissão. Entre uma coisa e outra, nunca peguei o avião — e esse é justamente o motivo pelo qual esse post abre a série.</p>

Essa é a primeira parte de uma série de três textos sobre os lugares onde trabalhei mudando de país: Porto, Dubai e Dublin. Comecei pelo Porto porque ele é o capítulo mais atípico dos três: foi o único em que a mudança física simplesmente não aconteceu. O contrato existiu, o trabalho existiu, o salário caiu na conta por seis meses — só a casa em Portugal que não.

No papel, inclusive, o modelo era **híbrido**: eu deveria estar no escritório do Porto alguns dias por semana. Na prática, os seis meses inteiros foram remotos, de São Paulo.

<div class="callout callout-tip">
  <div class="callout-label">O que você vai encontrar aqui</div>
  Como foi o processo seletivo via LinkedIn, o que significa ser contratado por recibos verdes, como funciona o modelo consultoria/cliente em Portugal, e o que a squad de Search da Farfetch fazia no dia a dia.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>De onde eu vinha</h2></div>
</div>

Antes do Porto eu estava no **Banco BS2**, contratado via **K2 Partnering** — ou seja, o modelo consultoria não era novidade para mim. Entrei em julho de 2019, na tribo de **B2B**, na squad de **API Banking**: desenvolvimento do produto de *banking as a service* do banco (devs.bs2.com), incluindo o projeto de open banking, com APIs e serviços em C# .NET Core, Dapper, Entity Framework e DDD, sistemas distribuídos em RabbitMQ, deploy em Docker, e cerimônias ágeis sobre Team Foundation Server.

Em março de 2020 passei para o **time de projetos especiais**, sediado em Belo Horizonte, já dentro da divisão de serviços financeiros do banco. Cheguei a me mudar de fato — e voltei uma semana depois, quando a quarentena fechou tudo. O time inteiro foi para o remoto e, desse jeito, meio no improviso, nós implementamos o **SPI/PIX**, o sistema de pagamentos instantâneos do Banco Central. O escopo incluía mensageria **ISO 20022** — ADMI (administração), CAMT (gestão de caixa), PACS (compensação e liquidação de pagamentos) e REDA (dados de referência) —, a arquitetura das soluções de **PIX Direto e PIX Indireto** dentro do BS2, e o sistema de contabilização dos parceiros de PIX Indireto, além de suporte direto a clientes internos no processo de integração. A stack seguia em C# .NET Core, Dapper, Entity Framework e DDD, com sistemas distribuídos em RabbitMQ, deploy em Docker e as mesmas cerimônias de Scrum/Kanban — agora sobre **Azure DevOps**. Foi um período corrido: o Banco Central com prazo fechado, o país inteiro esperando, e um time distribuído construindo integração de pagamento instantâneo de dentro de casa.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a mudança que durou uma semana
  </div>
  <p>Tem uma simetria meio absurda nessa história que eu só fui perceber muito depois. Em 2020 eu me mudei para Belo Horizonte e voltei em sete dias porque a pandemia fechou tudo. Em 2021 eu não me mudei para o Porto — também porque a pandemia fechou tudo. Duas mudanças de endereço engolidas pelo mesmo evento, com resultados opostos: uma virou remoto, a outra virou demissão.</p>
</div>

Quando o recrutador da Multivision me chamou, eu estava num lugar confortável: PJ, ganhando o equivalente a um sênior de São Paulo, remoto, num projeto que tinha acabado de entregar algo relevante. E ainda assim, no horizonte, existia a possibilidade de eu ter que me mudar para Belo Horizonte quando as coisas normalizassem.

Se era para mudar de cidade de qualquer forma, eu preferia mudar de continente. **Morar e trabalhar na Europa sempre foi o plano** — nunca foi uma ideia que surgiu com a vaga. A vaga só apareceu na hora em que o plano finalmente ficou viável.

Vale lembrar do momento: **fim de 2020**. Pandemia em curso, mercado de tecnologia acelerando a contratação remota e uma janela rara em que empresas europeias passaram a considerar candidatos que ainda estavam do outro lado do Atlântico. Foi exatamente essa janela que abriu a porta do Porto.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O processo seletivo</h2></div>
</div>

Como nos outros dois países da série, tudo começou no **LinkedIn**. Em **3 de novembro de 2020**, uma recrutadora da **Multivision** — consultoria de tecnologia portuguesa — me mandou uma mensagem procurando um *.NET Engineer* com conhecimento em **Kafka e Elasticsearch** para um cliente no Porto. O recrutador não era da Farfetch, e isso muda a natureza do processo: você passa por duas avaliações em sequência, uma da consultoria e outra do cliente onde vai ficar alocado.

A primeira call foi no dia seguinte, por Zoom. Ela apresentou a Multivision, apresentou a Farfetch — que eu já conhecia, por sinal, porque minha namorada na época queria uma bolsa do site — e explicou o projeto. Deixou claro desde o começo que o vínculo podia ser **contrato ou recibos verdes**, e perguntou se eu entendia a diferença entre os dois. No fim, a pergunta inevitável: pretensão salarial.

### A negociação

Eu respondi um valor deliberadamente alto — o padrão que eu vinha pesquisando para **Alemanha e Irlanda**, que eram os países onde eu já vinha me candidatando. Ela não recusou nem aceitou: disse qual era o valor que ela tinha em mãos e perguntou se eu toparia.

Levei **um ou dois dias** para responder. Não foi jogo de negociação — foi eu montando planilha e pesquisando quanto custa viver no Porto para saber se aquele número fechava a conta. Fechava. Confirmei.

<div class="callout callout-tip">
  <div class="callout-label">Pretensão salarial em processo internacional</div>
  Pedir alto e depois fazer a conta com calma foi a melhor decisão desse processo. O número que você pede ancora a negociação inteira, e você sempre pode dizer sim depois. O que você não consegue é subir depois de ter falado baixo. E "viável" não é o número da proposta — é o número da proposta menos aluguel, impostos e custo de vida <em>naquela cidade específica</em>.
</div>

O valor combinado ficou em **180 € por dia + IVA**, em recibos verdes, considerando 21 dias úteis por mês.

### As etapas

<table class="compare-table">
  <thead>
    <tr><th>Data</th><th>Etapa</th></tr>
  </thead>
  <tbody>
    <tr><td>03/11/2020</td><td>Primeiro contato da recrutadora no LinkedIn</td></tr>
    <tr><td>04/11/2020</td><td>Call de apresentação (Zoom), negociação de valor e envio do CV</td></tr>
    <tr><td>06/11/2020</td><td>Retorno: o cliente quer conversar</td></tr>
    <tr><td>12/11/2020</td><td>Entrevista técnica com a Farfetch — 15h de Lisboa, por BlueJeans</td></tr>
    <tr><td>13/11/2020</td><td>Aprovado para a fase final</td></tr>
    <tr><td>17/11/2020</td><td>Entrevista com o líder técnico — 10h30 de Lisboa, 07h30 no Brasil</td></tr>
    <tr><td>17/11/2020</td><td>Proposta, por telefone, na mesma noite</td></tr>
  </tbody>
</table>

**Quatorze dias** do primeiro "olá" à proposta. Não houve teste técnico, take-home nem live coding em nenhuma etapa — só conversa.

### A entrevista técnica

A apresentação inicial foi **em inglês**; o resto correu em português. Os temas foram exatamente os que você esperaria de uma squad de busca:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-magnifying-glass"></i> Elasticsearch a fundo</div>
    <div class="provider-detail">O que é um node, analisadores, shards e réplicas.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-stream"></i> Kafka</div>
    <div class="provider-detail">Segundo pilar da vaga, cobrado com o mesmo peso.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-code"></i> C# e fundamentos</div>
    <div class="provider-detail">Trajetória com .NET e a diferença entre SOAP e REST.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-vial"></i> Selenium</div>
    <div class="provider-detail">Testes automatizados entraram na conversa.</div>
  </div>
</div>

A segunda entrevista, com o líder técnico, foi bem **mais interpessoal do que técnica**. É um padrão que eu veria se repetir nos processos seguintes: a última conversa raramente é sobre código — é sobre se você funciona dentro daquele time.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a recrutadora que entregou o roteiro da prova
  </div>
  <p>Na véspera da entrevista técnica, a recrutadora me mandou a lista dos assuntos que seriam cobrados. Literalmente os tópicos, um a um. Isso não é subversão do processo: consultoria só ganha quando o candidato passa, então o interesse dela era exatamente o mesmo que o meu. É uma das grandes vantagens de entrar por intermediário — do outro lado da mesa tem alguém genuinamente torcendo por você e disposto a te preparar.</p>
  <p>Eu retribuí do jeito que dava: mandei para ela dois repositórios que eu mantinha no GitHub para divulgação de vagas em Portugal, nos moldes do <em>backend-br/vagas</em>, para ajudar a encontrar outros candidatos.</p>
</div>

Quando saiu o resultado, a frase dela foi que, em Portugal inteiro, não tinham encontrado ninguém melhor — e que havia várias pessoas do Brasil no mesmo processo. Passei o resto da noite rindo sozinho.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Contratação, recibos verdes e burocracia</h2></div>
</div>

O modelo de contratação foi **recibos verdes** — o regime de trabalhador independente em Portugal, equivalente funcional do nosso PJ. Você não é empregado da empresa: você presta serviço, emite recibo pelo Portal das Finanças e é responsável pelos seus próprios impostos e contribuições.

Na prática isso significa:

<table class="compare-table">
  <thead>
    <tr><th>Item</th><th>Contrato CLT-equivalente (PT)</th><th>Recibos verdes</th></tr>
  </thead>
  <tbody>
    <tr><td>Subsídio de férias e Natal</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Férias pagas</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Segurança Social paga pela empresa</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Estabilidade / aviso prévio</td><td><span class="check">✓</span></td><td><span class="partial">~</span></td></tr>
    <tr><td>Flexibilidade e valor bruto maior</td><td><span class="partial">~</span></td><td><span class="check">✓</span></td></tr>
  </tbody>
</table>

<div class="callout callout-warn">
  <div class="callout-label">Atenção se você for pesquisar isso hoje</div>
  As regras de recibos verdes — isenção inicial de contribuições à Segurança Social, escalões de IRS, obrigatoriedade de IVA — mudaram várias vezes desde 2020. Trate os números deste post como contexto histórico e confirme sempre no Portal das Finanças e na Segurança Social antes de decidir qualquer coisa.
</div>

### A papelada que eu consegui fazer

Com a fronteira fechada, tudo o que dava para adiantar foi feito **remotamente, do Brasil**. O primeiro passo foi o **NIF** — o Número de Identificação Fiscal português, equivalente ao nosso CPF e pré-requisito para absolutamente qualquer coisa em Portugal: abrir atividade, emitir recibo, assinar contrato de aluguel, abrir conta em banco.

No começo de dezembro veio a lista de documentos para iniciar o contrato, e ela expôs o abismo de vocabulário entre os dois países. **Certificado de habilitações** é o diploma. **Comprovativo de IBAN** é o comprovante de conta bancária. Eu emperrei nos dois: não tinha diploma, e minha conta internacional só operava em dólar.

Os dois se resolveram sem drama. O diploma acabou não sendo exigido naquele momento, e a Multivision optou por **me pagar em dólares na conta que eu já tinha**, em vez de me obrigar a abrir uma conta em euros ainda do Brasil. O faturamento saía pelo **CNPJ da minha empresa brasileira**.

<div class="callout callout-tip">
  <div class="callout-label">Pequeno glossário para brasileiro</div>
  <strong>NIF</strong> = CPF · <strong>Contabilista</strong> = contador · <strong>Recibos verdes</strong> = PJ/autônomo · <strong>Certificado de habilitações</strong> = diploma · <strong>Comprovativo de IBAN</strong> = comprovante bancário · <strong>Morada</strong> = endereço · <strong>Arrendamento</strong> = aluguel · <strong>Finanças</strong> = Receita Federal · <strong>Segurança Social</strong> = INSS. Parece bobagem, mas nos primeiros meses metade do esforço é decodificar vocabulário.
</div>

### O visto: Tech Visa

O caminho previsto era o **Tech Visa**, o programa português criado para facilitar a contratação de profissionais qualificados de fora da União Europeia por empresas certificadas. O requisito que me foi comunicado era comprovar **mais de quatro anos de experiência em TI**.

Isso também rendeu uma discussão curiosa: como comprovar? No Brasil a resposta óbvia é a **carteira de trabalho** — documento que simplesmente não existe no vocabulário português e que eu precisei explicar do zero. Eu tinha oito anos registrados em carteira e mais dois como PJ, comprováveis por contrato e notas fiscais. Serviria.

Na época eu **não tinha passaporte português**. Hoje eu tenho, por descendência — mas isso veio bem depois e não teve nenhuma relação com esse trabalho. Ali eu era um brasileiro comum dependendo de visto, com consulados operando em ritmo de pandemia.

<div class="callout callout-warn">
  <div class="callout-label">Antes de usar isso como referência</div>
  As regras do Tech Visa, dos escalões de IRS e das contribuições em recibos verdes mudaram várias vezes desde 2020 — e o próprio regime fiscal para estrangeiros em Portugal passou por reformulações grandes depois disso. Trate os números e procedimentos deste post como <strong>registro histórico</strong> e confirme sempre nas fontes oficiais.
</div>

E teve um personagem que não existe no vocabulário brasileiro do mesmo jeito: o **contabilista**. Em Portugal, quem trabalha por recibos verdes praticamente não sobrevive sem um — é ele quem cuida da abertura de atividade, das declarações e do calendário de obrigações.

### Como era o recibo na prática

<table class="compare-table">
  <thead>
    <tr><th>Linha</th><th>Valor</th></tr>
  </thead>
  <tbody>
    <tr><td>Serviços de consultoria — 20 dias</td><td>3.500,00 €</td></tr>
    <tr><td>Despesas</td><td>0,00 €</td></tr>
    <tr><td><strong>Valor base</strong></td><td><strong>3.500,00 €</strong></td></tr>
    <tr><td>Valor base com IVA (23%)</td><td>4.305,00 €</td></tr>
  </tbody>
</table>

### Quanto custaria morar no Porto

Enquanto a papelada corria, eu montei uma planilha de custo de vida. Não achei o arquivo original para este post, mas os números que ficaram na memória são estes:

<table class="compare-table">
  <thead>
    <tr><th>Item</th><th>Estimativa mensal</th></tr>
  </thead>
  <tbody>
    <tr><td>Arrendamento — T0 ou T1</td><td>500 a 700 €</td></tr>
    <tr><td>Alimentação</td><td>100 a 150 €</td></tr>
    <tr><td>Água, luz, gás, telefone e internet</td><td>~150 €</td></tr>
    <tr><td>Lazer, viagens e miudezas</td><td>reservado à parte</td></tr>
    <tr><td><strong>Base fixa estimada</strong></td><td><strong>750 a 1.000 €</strong></td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Decodificando os anúncios de imóvel em Portugal</div>
  <strong>T0</strong> é estúdio ou kitnet. <strong>T1</strong> tem um quarto, <strong>T2</strong> dois, <strong>T3</strong> três — o número indica quartos, não cômodos totais. Um "T2" português não é um "dois quartos" brasileiro por acaso: é exatamente isso, mas sem contar a sala.
</div>

A previsão de alimentação em 100 a 150 € parece baixa, e era proposital: como o modelo seria híbrido e eu iria pouco ao escritório, o plano era cozinhar quase tudo em casa e reservar as saídas para lazer.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>A empresa, o time e o cargo</h2></div>
</div>

A **Farfetch** é um marketplace de moda de luxo fundado por José Neves, que conecta boutiques e grifes do mundo inteiro a clientes finais. Nasceu com forte presença de engenharia em Portugal — Porto, Lisboa, Braga e Guimarães — e é hoje uma das referências de tecnologia do país.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-briefcase"></i> Cargo</div>
    <div class="provider-detail">Senior Software Engineer / .NET Developer</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-sitemap"></i> Cluster</div>
    <div class="provider-detail">Search, dentro do domínio de Consumer Products</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-users"></i> Time</div>
    <div class="provider-detail">Scouts — irmão do time de Search, com onboarding e cerimônias compartilhados</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-building"></i> Tamanho</div>
    <div class="provider-detail">Mais de 6.000 funcionários globalmente — cerca de 150 desenvolvedores na frente onde eu atuava</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-handshake"></i> Vínculo</div>
    <div class="provider-detail">Multivision (empregador) → Farfetch (cliente, onde eu ficava alocado)</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-house-laptop"></i> Modelo</div>
    <div class="provider-detail">Full-time, híbrido no papel — remoto integral na prática</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-calendar"></i> Período</div>
    <div class="provider-detail">Dezembro de 2020 a maio de 2021 — seis meses</div>
  </div>
</div>

### Como o time se organizava

A estrutura tinha várias camadas acima de mim: diretor de engenharia, head de engenharia do domínio, e então o cluster — com **engineering manager**, **group product manager** e **agile coach** próprios. O cluster de Search se dividia em duas áreas, e cada área tinha seus times. O meu era o **Scouts**.

O detalhe mais interessante do desenho é que o time **não era só de engenharia**. Cada time combinava uma célula de engenharia com uma célula de **data science e machine learning**, sob a mesma liderança técnica e nas mesmas cerimônias. Do lado de engenharia, éramos três: dois brasileiros e um português — os outros dois já morando em Portugal. Do lado de dados, o time era distribuído entre Londres e Portugal.

O **product manager** atendia de dois a três times simultaneamente, o que na prática significa que a prioridade sempre era negociada, nunca dada.

A missão do cluster era entregar os melhores resultados possíveis na busca do site e alimentar os blocos de sugestão de produto. No escopo do meu time, isso se traduzia em coisas como **ordenação de resultados por sinal de popularidade** na busca livre e um **serviço de sinônimos** consumido por vários outros projetos — o tipo de peça invisível que, quando falha, derruba a relevância inteira.

Parece simples de fora. Não é. Num catálogo de luxo com centenas de milhares de itens, marcas com grafias diferentes, coleções sazonais e estoque distribuído entre boutiques do mundo inteiro, relevância de busca vira um problema de engenharia bem grande — e, ao mesmo tempo, um dos que mais impacta receita diretamente.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>O projeto e as tecnologias</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-code"></i> C# .NET</div>
    <div class="provider-detail">Linguagem principal dos serviços e APIs da squad.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-magnifying-glass"></i> Elasticsearch</div>
    <div class="provider-detail">Motor de busca e relevância — indexação de catálogo, scoring, filtros facetados.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-database"></i> Apache Cassandra</div>
    <div class="provider-detail">Armazenamento distribuído de alto volume, adequado a dados de recomendação.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-stream"></i> Apache Kafka</div>
    <div class="provider-detail">Streaming de eventos — comportamento de navegação e atualizações de catálogo.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fab fa-python"></i> Python</div>
    <div class="provider-detail">Pipelines de dados e a parte mais analítica das recomendações.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fab fa-gitlab"></i> GitLab</div>
    <div class="provider-detail">Versionamento e CI/CD.</div>
  </div>
</div>

O desenho conceitual é o clássico de recomendação em e-commerce de larga escala: eventos de navegação e compra entram por **Kafka**, são processados e persistidos em **Cassandra**, viram sinal para o ranking no **Elasticsearch**, e tudo isso é exposto ao site por **APIs em C#**.

Em volta disso havia uma esteira madura, com bem mais peças do que a lista da vaga sugeria: repositório e CI, servidores de build, ferramenta de deploy separada por ambiente, análise estática de código, e três frentes de observabilidade — métricas, dashboards e agregação de logs. Havia inclusive **datacenter próprio na China**, com stack de logs separada, o que dá bem a dimensão do que significa operar um e-commerce global.

Meu trabalho ali foi essencialmente **evoluir os serviços de busca da plataforma** — melhorias incrementais em cima de uma base que já rodava em escala global.

E teve um aspecto do dia a dia que eu não esperava e que acabou sendo o mais interessante: a squad trabalhava **lado a lado com o time de Data Science**. Na divisão de trabalho, eles cuidavam dos modelos; nós fornecíamos os dados e os schemas de que eles precisavam, além de levar para produção o que saía dali.

<div class="callout callout-tip">
  <div class="callout-label">Engenharia como fornecedora de dados</div>
  Essa foi a primeira vez que eu ocupei o papel de "quem entrega dado limpo e contrato bem definido para o time de modelo". Não é escrever o algoritmo de recomendação — é garantir que o algoritmo tenha o que consumir, no formato certo e no volume certo. É um trabalho menos glamouroso e absolutamente crítico.
</div>

<div class="callout callout-tip">
  <div class="callout-label">O que eu levei dessa stack</div>
  Foi meu contato mais sério com Cassandra e com Kafka em produção de verdade, em volume de e-commerce global. Mesmo tendo sido curto, mudou bastante minha forma de pensar arquitetura orientada a eventos.
</div>

Não houve nenhum projeto novo do zero na minha passagem: o trabalho foi de **melhoria contínua** dentro do escopo do time. É o tipo de contribuição que não rende uma história bonita de "eu construí X", mas que é a realidade de quem entra numa plataforma madura que já roda em escala global — você aprende o sistema, melhora pedaço por pedaço, e a régua é não quebrar nada.

### O onboarding: um checklist gamificado

Essa foi a parte que mais me marcou tecnicamente, e é o que eu recomendaria copiar de lá. O onboarding não era "leia a wiki e boa sorte". Era um **programa baseado em conquistas**, com um documento pessoal, nominal, onde cada item virava um checkbox que só era marcado quando você demonstrava ter cumprido.

O checklist ia do trivial ao substancial:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-toolbox"></i> Ferramental</div>
    <div class="provider-detail">IDE, SDK, VPN, cliente de Kafka, plugin de Elasticsearch, extensões de Git — instalar e configurar tudo antes do "go-ahead".</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-key"></i> Acessos</div>
    <div class="provider-detail">Permissão em cada peça da esteira: repositório, CI, deploy, observabilidade, board ágil, ambientes de teste.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-comments"></i> Comunicação</div>
    <div class="provider-detail">Entrar nos canais certos — e pedir a alguém do time que explicasse a finalidade de cada um.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-graduation-cap"></i> Conhecimento</div>
    <div class="provider-detail">Fundamentos de arquitetura, processo de code review, framework de testes, padrão AAA, entrega contínua e monitoração.</div>
  </div>
</div>

Repare no padrão dos itens de conhecimento: quase todos eram *"peça a um colega do time que te explique X"*. O onboarding não terceirizava a integração para a documentação — ele **obrigava o novato a conversar com cada pessoa do time**, usando o checklist como desculpa institucional. Para alguém entrando remoto, do outro lado do Atlântico, isso vale mais do que qualquer wiki.

<div class="callout callout-tip">
  <div class="callout-label">O que eu levei desse modelo</div>
  Onboarding por conquistas resolve dois problemas de uma vez: dá ao novato uma noção clara de progresso — que é exatamente o que falta nas primeiras semanas — e transforma "conhecer o time" em tarefa explícita, em vez de deixar isso na conta da sorte e da extroversão de cada um.
</div>

### O projeto de indução

O ponto alto era um **projeto de indução**: construir, do zero, uma aplicação de *wishlist* seguindo a arquitetura de referência da casa. Solução em camadas no estilo DDD — apresentação, aplicação, domínio, dados e cross-cutting —, **Cassandra e Kafka rodando em Docker** localmente, API REST documentada com Swagger, injeção de dependência e testes de unidade em xUnit no padrão Arrange/Act/Assert.

É um exercício brilhante de onboarding porque não é um tutorial genérico: ele te força a atravessar exatamente a mesma stack e as mesmas convenções que você vai usar no trabalho real, num contexto pequeno o bastante para caber numa semana e sem risco de quebrar produção. Você termina com um repositório seu, um code review feito com o time e um merge request de verdade.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>A rotina</h2></div>
</div>

A palavra que melhor descreve o trabalho é **calma**. Não no sentido de pouco trabalho, mas de previsibilidade: escopo bem definido, ritmo sustentável, sem cultura de urgência artificial.

A rotina, essa, era qualquer coisa menos calma no começo do dia. Eu acordava entre **05h00 e 06h00** para entrar na daily no horário de Portugal. O onboarding, ainda em dezembro, já tinha sido assim — remoto, marcado para 10h30 de Lisboa. E a entrevista final tinha sido às 07h30 do horário de Brasília. O padrão se manteve por seis meses.

<div class="callout callout-tip">
  <div class="callout-label">Três ou quatro horas fazem mais diferença do que parece</div>
  Portugal fica três horas à frente de Brasília — quatro durante parte do ano, quando só um dos países está em horário de verão. Na comparação com Dubai ou com a Ásia, isso é quase nada. Mas basta para que o time inteiro comece a trabalhar enquanto você ainda está dormindo, e para que a sua manhã seja o meio do dia deles. A janela de sobreposição existe e é confortável — só que ela começa muito cedo do seu lado.
</div>

### A daily que mudava de idioma

Esse é o detalhe mais curioso da rotina, e eu nunca vi repetido em nenhum outro lugar onde trabalhei.

<table class="compare-table">
  <thead>
    <tr><th>Dias</th><th>Participantes</th><th>Idioma</th></tr>
  </thead>
  <tbody>
    <tr><td>Terça e quinta</td><td>Só engenharia</td><td>Português</td></tr>
    <tr><td>Segunda, quarta e sexta</td><td>Engenharia + machine learning</td><td>Inglês</td></tr>
  </tbody>
</table>

A lógica era puramente demográfica. O time de engenharia era composto por dois brasileiros e um português — nas terças e quintas, falar inglês entre nós seria teatro. Já o time de machine learning estava majoritariamente em **Londres**, com apenas uma analista júnior em Portugal. Nos dias em que as duas células se encontravam, o inglês era a única língua comum.

<div class="callout callout-tip">
  <div class="callout-label">Idioma como decisão de time, não como política</div>
  Eu gosto muito dessa solução porque ela é honesta: em vez de decretar "aqui se fala inglês" e produzir reuniões truncadas onde metade das pessoas se expressa pela metade, o time deixou o idioma seguir quem estava na sala. Falava-se português quando dava, inglês quando era necessário. O custo disso é ter que trocar de chave no meio da semana; o benefício é que ninguém perde nuance à toa.
</div>

### O resto do calendário

O processo era **ágil de verdade, não ágil de fachada**: cerimônias de Scrum combinadas com Kanban, tudo rodando sobre Jira, com backlog, sprint board e release board separados por time. Planning, refinamento, review e retrospectiva no ritmo padrão — e o cluster tinha até um **agile coach** dedicado, o que não é comum.

Havia também **1:1 mensal com o engineering manager**. Somado ao product manager que circulava entre dois ou três times, o desenho deixava claro onde ficava cada responsabilidade: o EM cuidava das pessoas e da carreira, o PM disputava prioridade, e o time decidia como fazer.

Foi meu primeiro emprego internacional trabalhando de casa. Curiosamente, o mais difícil da adaptação não foi o idioma nem a cultura — foi o despertador.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Por que a mudança nunca aconteceu</h2></div>
</div>

A resposta curta: **apareceu Dubai**.

### A mensagem que eu ignorei por cinco semanas

Vale contar como apareceu, porque quase não apareceu.

Em **26 de janeiro de 2021**, com pouco mais de um mês de Farfetch, uma recrutadora da **Talabat** — plataforma de delivery do grupo Delivery Hero, sediada em Dubai — me mandou mensagem no LinkedIn. A abordagem tinha tudo que um recrutador colocaria numa vitrine: escala de milhões de usuários diários, time com dezenas de nacionalidades, microsserviços e Kubernetes, e a expressão que fazia o trabalho pesado — **salário isento de impostos**.

Eu não respondi.

Não foi estratégia nem desdém. Eu tinha acabado de começar num lugar de que gostava, estava com a mudança para o Porto sendo planejada, e simplesmente deixei a mensagem para depois. O "depois" durou cinco semanas.

Em **4 de março** ela mandou um follow-up dizendo que não tinha tido retorno e perguntando se eu queria conversar. Dessa vez eu respondi — em treze minutos, e já com o currículo anexado. Ainda perdi uma semana esperando resposta, cobrei, e a call ficou marcada para **17 de março**.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a decisão que quase não foi tomada
  </div>
  <p>Isso me assusta um pouco até hoje. A mudança de país que definiu os cinco anos seguintes da minha vida chegou como uma notificação do LinkedIn que eu não achei importante o suficiente para abrir. Se aquela recrutadora não tivesse feito follow-up — e follow-up é justamente o que a maioria não faz —, eu provavelmente teria me mudado para o Porto e essa série teria dois capítulos.</p>
  <p>A lição que eu tirei não é "responda tudo". É que oportunidade não chega anunciada como oportunidade. Ela chega igualzinha a todo o resto do ruído, e você só descobre a diferença depois.</p>
</div>

### A conta que decidiu

A resposta longa exige explicar uma configuração que eu tinha naquele momento e que não é óbvia. Além do contrato com a Multivision, eu tinha em paralelo um contrato **part-time remoto** com a **Grace Kennedy Financial Group** — o maior grupo financeiro da Jamaica e do Caribe —, via a agência de recrutamento **The Bridge Social**, entre fevereiro e maio de 2021. Dois vínculos de **Senior Software Engineer / .NET Developer** ao mesmo tempo — um full-time, o outro part-time.

<div class="callout callout-tip">
  <div class="callout-label">A conta real</div>
  Mesmo somando os dois rendimentos — o full-time da Farfetch/Multivision e o part-time da Grace Kennedy —, o total ainda ficava abaixo do que a Talabat oferecia. E a vaga de Dubai não era nem de sênior — a carta de oferta trazia <strong>Software Engineer II, grade IC2</strong>, um degrau abaixo na escada de carreira de lá.
</div>

Some a isso o segundo fator: os **Emirados Árabes Unidos não cobram imposto de renda sobre salário**. Enquanto em recibos verdes eu arcaria com IRS, Segurança Social e contabilista, no Dubai bruto e líquido eram praticamente a mesma coisa.

Vale registrar o que **não** estava em jogo: o contrato com a Grace Kennedy era part-time, remoto, e não envolvia qualquer plano de mudança para o Caribe — era renda extra, não um caminho de carreira. Terminou junto com a Farfetch, em maio de 2021.

<div class="divider">· · ·</div>

Mas a parte mais decisiva não é financeira. É logística.

**O fato de eu ainda não ter me mudado foi o que tornou tudo possível.** Eu estava em São Paulo, sem contrato de aluguel no Porto, sem mudança despachada, sem nada instalado. Trocar de rumo naquele momento custava dois e-mails de desligamento — não uma vida desmontada.

Se eu já estivesse morando em Portugal, provavelmente teria dito não. Depois de atravessar visto, mudança, aluguel e adaptação, ninguém desfaz tudo isso seis meses depois por uma proposta melhor. E, sendo honesto, eu suspeito que a vaga nem teria chegado até mim: um candidato recém-instalado na Europa é bem menos disponível para um novo processo internacional do que alguém que ainda está no ponto de partida.

**A mudança que nunca aconteceu foi exatamente o que permitiu a mudança que aconteceu.** É irônico, mas é assim que funciona: o custo de mudar de rumo cresce muito rápido depois que você assina o contrato de aluguel.

Quando a viagem para Dubai finalmente se concretizou, eu encerrei os dois vínculos — o de recibos verdes com a Multivision e o part-time remoto com a Grace Kennedy, onde fiquei quatro meses.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — pedir demissão de um lugar onde nunca cheguei
  </div>
  <p>A comunicação saiu entre abril e maio, e só depois de eu já ter <strong>contrato assinado com a Talabat</strong> — não antes. Essa ordem não é detalhe: quando a mudança depende de visto, de fronteira e de país estrangeiro, você não abre mão do que tem com base em promessa verbal. Só avisei quando não havia mais cenário em que eu ficasse.</p>
  <p>Houve uma ironia adicional no caminho. A recrutadora que tinha conduzido todo o meu processo saiu da Multivision em janeiro de 2021, e o meu acompanhamento passou para outra equipe. Quem me contratou com tanto entusiasmo — que tinha comemorado comigo pelo telefone, torcido antes das entrevistas, me preparado para a prova — não estava mais lá para ouvir que eu ia embora. Eu me despedi de pessoas que mal me conheciam, de um escritório que eu nunca vi, numa cidade onde eu nunca morei.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Linha do tempo</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Quando</th><th>O quê</th></tr>
  </thead>
  <tbody>
    <tr><td>Julho de 2019</td><td>Entrada no Banco BS2 via K2 Partnering — squad de API Banking, tribo B2B, São Paulo</td></tr>
    <tr><td>Março de 2020</td><td>Passagem para o time de projetos especiais (BH) — mudança de uma semana e volta para SP pela quarentena</td></tr>
    <tr><td>2020</td><td>Implementação do SPI/PIX, com o time todo em remoto</td></tr>
    <tr><td>03/11/2020</td><td>Primeiro contato da recrutadora da Multivision no LinkedIn</td></tr>
    <tr><td>12 e 17/11/2020</td><td>Entrevistas com a Farfetch — técnica e com o líder técnico</td></tr>
    <tr><td>17/11/2020</td><td>Proposta aceita, por telefone</td></tr>
    <tr><td>Dezembro de 2020</td><td>Documentação, onboarding virtual e início no time Scouts</td></tr>
    <tr><td>Dezembro de 2020</td><td>NIF, contabilista e planejamento da mudança para o Porto</td></tr>
    <tr><td>12/01/2021</td><td>A recrutadora que conduziu meu processo deixa a Multivision</td></tr>
    <tr><td>26/01/2021</td><td>Primeira mensagem da Talabat no LinkedIn — que eu não respondi</td></tr>
    <tr><td>Fevereiro de 2021</td><td>Início do contrato part-time remoto com a Grace Kennedy Financial Group (Jamaica), via The Bridge Social — em paralelo com a Farfetch</td></tr>
    <tr><td>04/03/2021</td><td>Follow-up da recrutadora de Dubai — dessa vez eu respondo</td></tr>
    <tr><td>17/03/2021</td><td>Primeira call com a Talabat</td></tr>
    <tr><td>21/04/2021</td><td>Carta de oferta da Talabat — válida por três dias úteis</td></tr>
    <tr><td>Abril–Maio de 2021</td><td>Comunicação de saída dos dois vínculos, já com o contrato assinado</td></tr>
    <tr><td>Maio de 2021</td><td>Fim da passagem pela Farfetch e do contrato com a Grace Kennedy — sem nunca ter me mudado para Portugal</td></tr>
    <tr><td>30/05/2021</td><td>Primeiro dia na Talabat — ainda remoto, do Brasil</td></tr>
    <tr><td>14/06/2021</td><td>Início de um novo contrato CLT paralelo (filial brasileira de empresa americana) — já durante os primeiros meses remotos na Talabat, sem relação com a decisão do Porto</td></tr>
  </tbody>
</table>

<div class="conclusion">
  <h2>O que ficou desses seis meses</h2>
  <p>Meu plano sempre foi usar Portugal como porta de entrada para a Europa. E, no fim das contas, foi mais ou menos o que aconteceu — só que fora de ordem, com um desvio de quase dois anos pelo deserto no meio do caminho. Hoje eu moro na Irlanda. Cheguei lá, só não pelo roteiro que estava na planilha.</p>
  <p>Foi a passagem mais curta da minha carreira internacional e, ainda assim, formativa em um aspecto específico: foi ali que eu descobri, na prática, que trabalhar para uma empresa de fora não é a mesma coisa que morar fora. São dois projetos diferentes, com burocracias diferentes, e um não implica automaticamente o outro.</p>
  <p>Também foi onde eu entendi a diferença real entre ser contratado <em>por</em> uma empresa e ser alocado <em>em</em> uma empresa. Nos dois capítulos seguintes da série — Dubai e Dublin — o vínculo foi direto, sem intermediário, e a experiência mudou completamente de textura.</p>
  <p>No próximo post: a mensagem que eu quase não respondi, o processo que correu inteiro por Zoom, seis meses trabalhando do Brasil para o Oriente Médio — e depois um ano e meio morando no deserto.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Farfetch. <strong>About Farfetch.</strong>
      <a href="https://www.farfetch.com/" target="_blank">farfetch.com</a>
    </li>
    <li>
      Autoridade Tributária e Aduaneira. <strong>Portal das Finanças — trabalhadores independentes.</strong>
      <a href="https://info.portaldasfinancas.gov.pt/" target="_blank">portaldasfinancas.gov.pt</a>
    </li>
    <li>
      Segurança Social. <strong>Regime dos trabalhadores independentes.</strong>
      <a href="https://www.seg-social.pt/" target="_blank">seg-social.pt</a>
    </li>
  </ol>
</div>
