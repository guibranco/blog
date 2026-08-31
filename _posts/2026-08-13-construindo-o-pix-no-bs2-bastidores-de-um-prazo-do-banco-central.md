---
layout: post
lang: pt-BR
title: "Construindo o PIX no BS2: sete meses, um prazo do Banco Central e um AirBnB em BH"
description: "Como foi sair do time B2B em São Paulo para o time de projetos especiais do core bancário e atravessar 2020 construindo o PIX, com data de lançamento definida pelo Banco Central, plantão de sobreaviso e o mercado inteiro colaborando em grupos de WhatsApp."
date: 2026-08-13
categories: [Career]
subcategories:
  - "Career/Behind the Scenes"
tags: [pix, banco-central, central-bank, carreira, career, sistemas-financeiros, financial-systems, plantao, on-call, bastidores]
medium_tags: [pix, fintech, career, on-call, brazil]
reading_time: 24
cover: /assets/img/posts/pix-bs2-bastidores.svg
image: /assets/img/posts/pix-bs2-bastidores.png
series: pix-bs2
series_title: Desenvolvendo o PIX
series_part: 1
---

<p class="lead">Em abril de 2020 eu saí de um time B2B em São Paulo e entrei no time de projetos especiais do core bancário. A primeira coisa que me contaram na nova mesa foi que o Banco Central tinha marcado o lançamento do PIX para novembro. Não era uma meta de roadmap. Era uma data.</p>

<div class="callout callout-tip">
  <div class="callout-label">Este é o primeiro de dois textos</div>
  Aqui eu conto os <strong>bastidores humanos</strong> do projeto: a mudança de time, a remontagem do time no meio do caminho, o plantão de sobreaviso e a colaboração entre concorrentes. A arquitetura — SPI, ISO 20022, os percentis do Manual de Tempos, RabbitMQ e a iniciação de pagamentos — está na <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">segunda parte, sobre a arquitetura do PIX vista por dentro</a>.
</div>

<div class="callout callout-warn">
  <div class="callout-label">Sobre o que este texto é</div>
  Este é um relato de bastidores sobre <strong>como se constrói software com prazo regulatório</strong>. Tudo que descrevo sobre o PIX em si é público e está no material do Banco Central, linkado no final. Nomes internos de sistemas, módulos, topologia e colegas de time ficam de fora.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Abril de 2020: a mudança de mesa</h2></div>
</div>

Eu estava num time B2B em São Paulo. Era um trabalho confortável no sentido em que a régua era conhecida: cliente pedia, a gente entregava, o prazo era negociável na margem.

Antes de contar como saí dele, preciso explicar a geografia do banco, porque ela é metade da história.

A estrutura era dividida em **BUs** — *business units*, ou tribos —, e cada uma tinha marketing, comercial, produto e engenharia próprios. A BU de Pessoa Jurídica, onde eu estava, era inteiramente baseada em São Paulo, do marketing à engenharia, assim como as BUs de câmbio e investimentos. Em Belo Horizonte ficavam a BU de Pessoa Física e **todo o resto do banco**: o core bancário — com serviços financeiros dentro dele — e a estrutura de apoio, do financeiro e da tesouraria ao RH, ao marketing institucional e à publicidade.

Eu estava na squad de BaaS e API banking, dentro da BU PJ. Ou seja: o lugar para onde eu queria ir ficava a quase 600 quilômetros de onde eu trabalhava, e não por acaso — era assim que o banco estava organizado.

E eu queria ir. Já tinha manifestado interesse em atuar no core bancário antes de existir qualquer conversa sobre PIX. Meu alvo, na verdade, era o **SPB — o Sistema de Pagamentos Brasileiro**, que na época era por onde passavam TED e DOC. Eu queria entender como o dinheiro sai de uma instituição e entra em outra de verdade, no nível do protocolo. Não fazia ideia de que existia um **SPI — o Sistema de Pagamentos Instantâneos**, a infraestrutura sobre a qual o PIX ia rodar —, muito menos de que ele estava sendo construído naquele momento.

Ajudou que aquele não era um destino cheio de estranhos. O head de serviços financeiros era mineiro, mas vinha de ter sido PO da área de internet banking do braço PJ em São Paulo — eu já o conhecia da mesma BU, ainda que de outra squad. E o diretor de TI era o antigo head de tecnologia daquele mesmo braço PJ, promovido a CIO no começo de 2020. As duas pessoas que decidiam sobre o projeto tinham saído da estrutura de onde eu vinha.

### O convite apareceu numa conversa de demissão

Esta é a parte que eu conto em conversa de carreira e que não cabe em currículo nenhum.

Eu tinha recebido uma proposta externa de uma adquirente da Faria Lima. Salário maior. Mas a vaga era em Java, uma tecnologia que eu não usava — seria trocar de empresa e de stack ao mesmo tempo. Marquei uma conversa com o diretor de TI para **pedir demissão**.

Foi nessa conversa que o convite apareceu: um time em Belo Horizonte, dentro do core, num projeto que ele ainda não podia detalhar. Não era contraproposta genérica de salário. Era exatamente a coisa que eu tinha dito que queria, oferecida no momento exato em que eu estava saindo pela porta.

<div class="callout callout-tip">
  <div class="callout-label">Três coisas que eu tiraria daqui</div>
  <p>Dizer em voz alta, com antecedência e para as pessoas certas, para onde você quer ir muda o que te oferecem quando algo surge. Se eu nunca tivesse falado do core, aquele convite não teria como existir.</p>
  <p>Oportunidade grande raramente vem de processo seletivo interno bem divulgado. Vem de quem já viu você trabalhar e precisa de gente rápido — e as pessoas com quem você trabalhou há dois anos são o pipeline de vagas mais confiável que você tem.</p>
  <p>E a menos confortável: a conversa de saída costuma ser a primeira em que a empresa escuta você com atenção total. Isso é falha de gestão, não estratégia sua. Vale saber que acontece, e é péssimo motivo para pedir demissão de blefe — porque às vezes aceitam.</p>
</div>

Aceitei. E, como o interesse era anterior, mudar para BH não me pareceu castigo — o que não impediu que algumas pessoas da BU PJ em São Paulo me perguntassem, com preocupação sincera, se eu tinha **pedido** para ir ou se aquilo tinha sido **imposto**. Sair de São Paulo para Belo Horizonte, na cabeça de boa parte do mercado de tecnologia paulistano, só podia ser punição.

O time era o de **projetos especiais** dentro de serviços financeiros. Na prática, isso significa a camada onde a conta corrente existe de verdade: débito, crédito, saldo, lançamento, conciliação. É a parte do banco onde ninguém aplaude quando funciona e todo mundo aparece quando não funciona.

A diferença cultural entre os dois mundos foi imediata. No B2B, um bug ruim é um cliente irritado. No core, um bug ruim é dinheiro no lugar errado — e, com o PIX, dinheiro no lugar errado em menos de dez segundos, sem janela de estorno automático, no fim de semana, às três da manhã.

E tudo isso acontecendo em 2020, na primeira onda da pandemia — num projeto que ninguém tinha feito antes porque o sistema ainda não existia em lugar nenhum do mundo naquele formato. A mudança de mesa e o fechamento dos escritórios aconteceram, literalmente, na mesma semana.

<div class="divider">· · ·</div>

### A semana em Belo Horizonte

Eu ia me mudar no domingo. Perdi o voo. Cheguei em Belo Horizonte na manhã de segunda-feira e fui direto para o escritório novo à tarde.

O banco ocupava uma torre na cidade, mas o time de projetos especiais não estava em nenhum dos andares de escritório: estávamos numa **sala temporária no térreo**. Provavelmente por falta de espaço lá em cima, e por sermos um time novo, emergente e urgente ao mesmo tempo. Guardei aquela imagem por anos — o projeto que se tornaria o mais estratégico do banco começou numa sala emprestada no térreo, com gente que tinha acabado de se conhecer.

Na segunda à noite, pelos grupos de WhatsApp, ficamos sabendo que o time de São Paulo tinha ido para home office. Sobre Belo Horizonte, nada. Terça foi um dia de trabalho absolutamente normal: escritório cheio, e almoço num restaurante típico mineiro, o único por ali. Terça à noite chegou o aviso de que, a partir de quarta, BH também ficaria em casa.

Quarta-feira eu já trabalhava do AirBnB.

Foi nesse dia que troquei mensagens com o diretor de TI para entender o que ele achava — se eu ficava ou voltava. Ele era de São Paulo, morava lá com a família e passava só a semana em BH, então o dilema era exatamente o mesmo, com dez anos a mais de bagagem. O conselho foi voltar durante a quarentena. A conta era prática: aquilo supostamente duraria quarenta dias, eu não conseguiria procurar nem alugar nada naquela situação, e ficar significava queimar dinheiro em AirBnB para trabalhar sozinho num apartamento vazio. A gente estimava o prazo olhando para os países que já estavam confinados na época — o que, em retrospecto, foi o palpite mais otimista de todos.

Arrumei as coisas, avisei o head do time e o especialista que mais tarde assumiria o lugar dele, e peguei um táxi para o aeroporto ainda na quarta, com medo de não conseguir táxi nenhum de madrugada. Meu voo era quinta, às cinco da manhã.

Na quinta-feira eu já estava trabalhando de São Paulo. E fiquei remoto dali em diante, sem interrupção, até sair do banco em 2021.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a mudança que nunca aconteceu
  </div>
  <p>Foram dois dias de escritório e uma passagem de volta. A mudança para Belo Horizonte, que em março era a grande decisão de vida do ano, simplesmente evaporou: a pandemia derrubou o argumento de "estar junto", o projeto começou a andar mesmo assim, e a proposta nunca mais foi retomada.</p>
  <p>Construí o PIX inteiro de São Paulo, remoto, com o time em BH — o que em 2020 ainda parecia uma concessão excepcional e não o padrão.</p>
  <p>Olhando de hoje, com anos morando fora, aquela semana foi um ensaio muito barato de uma coisa que eu faria de verdade depois: chegar num lugar onde você não conhece ninguém, ter poucos dias para entender como as coisas funcionam e decidir se fica. A diferença é que, das outras vezes, não teve voo de volta na quinta.</p>
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
  <div class="section-title-wrap"><h2>Quem fez o quê</h2></div>
</div>

Vale começar pelo estado em que eu encontrei o time, porque ele não era o time que entregou o PIX.

Quando cheguei, projetos especiais tinha **eu, mais um desenvolvedor, um arquiteto, dois analistas de negócio, um especialista financeiro e um head**. Poucas semanas depois, os dois analistas e o head foram desligados, e o especialista assumiu a coordenação. Sobraram o arquiteto e nós dois, olhando para um prazo publicado pelo Banco Central.

Vale traduzir esses dois cargos, porque eles não têm equivalente óbvio no vocabulário de quem trabalha em produto digital. O **especialista financeiro** acumulava a função de gerente de projetos: era quem entendia do negócio bancário e ao mesmo tempo tocava cronograma, escopo e dependências. Não havia papel de agile, product owner ou scrum master ali — aquela era uma cultura de projeto tradicional, com gerente e plano, não de squad com cerimônia. E **head**, no organograma do banco, era o gerente ou superintendente do departamento, responsável pelo time e pelo projeto perante a diretoria.

O time foi remontado durante o projeto. Entraram mais quatro desenvolvedores ao longo dos meses — alguns vinham de fora e já tinham trabalhado com gente dali em outros bancos, e um veio do próprio core, com experiência em conta corrente, débito e crédito. Esse último detalhe não é acessório: ter alguém que já sabia como o dinheiro se move dentro da instituição vale mais, num projeto desses, do que qualquer familiaridade com a especificação nova, porque a especificação todo mundo ia ter que aprender do zero de qualquer jeito.

<div class="callout callout-tip">
  <div class="callout-label">A formação final</div>
  Seis desenvolvedores — <strong>três sêniores e três plenos</strong> —, um arquiteto, um head (o antigo especialista financeiro) e um analista de negócio recontratado, acumulando o papel de analista com o de agile do time. Mais o apoio permanente de uma piloto de reserva, que com o tempo passou a fazer mais parte do time do PIX do que da operação de onde ela vinha.
</div>

A divisão foi por domínio, não por camada. Cada frente era dona de uma fatia funcional de ponta a ponta, e a conta fechava exatamente: **três frentes, cada uma com um sênior e um pleno**. A borda da RSFN não entrava nessa conta — ela ficou praticamente inteira com o arquiteto, o profissional mais sênior do time, trabalhando sozinho.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Chaves e diretório</div>
    <div class="provider-detail"><strong>Um sênior e um pleno.</strong> Registro, alteração, exclusão, consulta de vínculo, reivindicação de posse e portabilidade de chave no DICT. O primeiro entregável a ir para produção, em 5 de outubro.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Recebimento e contestação</div>
    <div class="provider-detail"><strong>Um sênior e um pleno.</strong> O outro lado do fluxo: crédito na conta do recebedor, comprovante, devolução e tratamento das contestações.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Borda RSFN</div>
    <div class="provider-detail"><strong>O arquiteto, sozinho.</strong> Toda a comunicação direta com o BACEN pela RSFN: o XML assinado, o transporte, os certificados e a tradução para o barramento interno. Único ponto do time sem par.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Iniciação e PIX Indireto</div>
    <div class="provider-detail"><strong>Um sênior e um pleno</strong> — o sênior era eu. Fazer o pagamento sair, e permitir que outras instituições fizessem pagamentos saírem através da gente. O detalhamento técnico das duas está na <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">segunda parte da série</a>.</div>
  </div>
</div>

Fora da engenharia havia mais três pessoas, e demorei a entender que elas não eram overhead — eram parte do sistema.

Dois **analistas de negócio** traduziam manual do BC em requisito. Isso parece função de cerimônia até você tentar ler o Manual de Padrões para Iniciação e descobrir que a resposta para "o que acontece se a chave existir mas a conta estiver encerrada" está espalhada em três documentos e um catálogo de erros. Ter alguém cuja função é ser dono dessa leitura poupou o time de descobrir divergência de interpretação em homologação.

A terceira era a função que mais me surpreendeu: uma **piloto de reserva**. É um cargo técnico da área financeira, não de engenharia de software. O piloto de reserva — ou operador de reservas — acompanha em tempo real os saldos da instituição junto ao Banco Central, garante que exista liquidez para cobrir as liquidações e atua nas contingências, evitando que ordens de pagamento sejam rejeitadas por falta de saldo na conta de liquidação. Ela vinha do SPB e, com o passar dos meses, acabou fazendo mais parte do nosso time do que da operação original.

<div class="callout callout-tip">
  <div class="callout-label">O requisito que não é de software</div>
  A <strong>Conta PI</strong> é a conta de Pagamentos Instantâneos que cada participante direto mantém no Banco Central, separada da conta de Reservas Bancárias usada no SPB. É contra o saldo dela que o SPI liquida, transação a transação, e é ela que o participante precisa abastecer antecipadamente — inclusive de madrugada e no fim de semana, quando o PIX opera e o SPB não. Uma transação PIX não liquida sem saldo ali, por mais correto que o seu código esteja. Alguém precisa provisionar essa liquidez 24 horas por dia, sete dias por semana, num sistema que — ao contrário do SPB tradicional — não fecha à noite nem no fim de semana. Nenhuma quantidade de arquitetura resolve isso.
</div>

Na época eu achei que aquilo fosse um improviso nosso — alguém do SPB (TED e DOC) emprestado ao SPI (PIX). Não era. A função de piloto de reserva do SPI se consolidou como cargo próprio no mercado brasileiro. Anúncios de vaga para a posição descrevem exatamente esse escopo: domínio operacional do STR, no SPB, **e** do SPI, monitoramento de saldo intradiário via RSFN, contingência e tratamento de devoluções e MED. Há inclusive provedores que vendem, como diferencial para participantes indiretos, um piloto de reservas próprio, sem depender do piloto de reservas do liquidante direto.

Vale distinguir duas coisas que eu confundia. O que a norma exige na adesão ao PIX é a indicação de um **diretor estatutário** responsável perante o Banco Central pelas questões do SPI — isso é governança. O piloto de reserva é **função operacional**, criada pela necessidade concreta de manter liquidez numa conta que liquida 24 horas por dia. Uma coisa responde ao regulador; a outra impede que a transação seja rejeitada às três da manhã de domingo.

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Plantão: a primeira vez que fiquei de sobreaviso</h2></div>
</div>

Um sistema que liquida 24 horas por dia, sete dias por semana, não tem noite. Essa frase é óbvia no papel e brutal na prática: significa que alguém precisa estar acordável às três da manhã de domingo. Foi a primeira vez na minha carreira que entrei numa escala de sobreaviso.

O desenho do pareamento foi a parte mais inteligente. Ficávamos **em duplas, de preferência com pessoas de duas frentes diferentes**, e cada um precisava ter conhecimento básico das outras duas frentes. A lógica é direta: às três da manhã você não quer descobrir que o único problema possível é exatamente o da frente que ninguém da dupla conhece. Não era rodízio de especialista, era cobertura cruzada deliberada.

<table class="compare-table">
  <thead>
    <tr><th>Regime</th><th>Jornada</th><th>Sobreaviso no dia útil</th><th>Fim de semana</th></tr>
  </thead>
  <tbody>
    <tr><td>PJ (meu caso)</td><td>8 h</td><td>16 h</td><td>24 h</td></tr>
    <tr><td>CLT</td><td>9 h — 8 de trabalho e 1 de almoço</td><td>15 h</td><td>24 h</td></tr>
  </tbody>
</table>

A semana de plantão começava à meia-noite de sábado para domingo e terminava às 23h59min59s do sábado seguinte. Sete dias corridos de disponibilidade, com os fins de semana cobertos integralmente.

A recomendação era ficar perto do notebook ou andar com ele, e evitar lugares de onde não desse para atuar. Na prática, era uma semana sem cinema, sem viagem, sem trilha, sem nada que te deixasse longe de uma tomada e de uma conexão decente. E aqui vem a parte que eu acho importante registrar, porque muita empresa faz o oposto: **isso era remunerado**. O sobreaviso pagava por si só, e o acionamento pagava a mais.

<div class="callout callout-tip">
  <div class="callout-label">Os números do meu contrato</div>
  Um terço do valor-hora por hora de sobreaviso, e uma vez e meia o valor-hora em caso de acionamento fora do horário de trabalho. Vale notar que o primeiro número não saiu do nada: a CLT define, no artigo 244, §2º, que as horas de sobreaviso são contadas à razão de um terço do salário normal — regra originalmente dos ferroviários, estendida às demais categorias pela Súmula 428 do TST, que reconhece o sobreaviso de quem fica em regime de plantão aguardando chamado por meio telemático. Meu contrato era PJ, mas o parâmetro veio da lei.
</div>

Não foi imposto. A escala foi apresentada, discutida, questionada e **votada antes de entrar em operação**, e os valores foram negociados diretamente com as respectivas consultorias. Isso parece detalhe e não é: em muito lugar, plantão aparece como "expectativa da senioridade" e nunca vira linha em contrato. Ser pago para ficar em casa numa semana, e mais ainda para trabalhar de madrugada, é o mínimo que torna a coisa sustentável.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — explicando ao RH do banco
  </div>
  <p>Eu era o único PJ do time do PIX. Todos os outros também eram terceirizados, mas contratados em regime CLT pelas suas respectivas consultorias.</p>
  <p>Numa semana de plantão, lancei 16 horas de sobreaviso por dia na planilha. O sistema esperava 15. Resultado: recebi um questionamento do RH do próprio banco, e tive que ser eu — o PJ, terceiro, de fora — a explicar ao RH da instituição por que o meu número era diferente do dos meus colegas. A conta era simples: os CLTs tinham jornada de 9 horas porque a hora de almoço entra na janela, e eu, PJ, não tinha intervalo contratual, então trabalhava 8 e ficava disponível 16.</p>
  <p>Era uma diferença de um único número numa planilha, mas ela expunha duas relações de trabalho distintas convivendo no mesmo time. E tinha sido conferida com a minha consultoria antes.</p>
</div>

Essa diferença tinha um componente geográfico que eu só entendi com o tempo. **Todas as consultorias do time eram de Belo Horizonte, e todas contratavam em CLT.** As consultorias e os prestadores de São Paulo, de onde eu vinha, preferiam quase sempre o modelo PJ. Não era coincidência: era cultura regional de contratação em tecnologia naquele momento.

Vale separar as duas camadas dessa história. Do ponto de vista estritamente legal, contratar em CLT é o caminho correto e sem zona cinzenta — a pejotização de trabalho subordinado é justamente o ponto contestado. Do ponto de vista de quem estava sendo contratado, em São Paulo a prática já era costume consolidado, e eu preferia o modelo PJ — assunto que eu destrincho com calma em <a href="{{ site.baseurl }}/artigos/clt-vs-pj-qual-devo-escolher/">CLT, PJ ou MEI: qual devo escolher</a> — e ainda prefiro, **desde que o valor seja coerente com o que ele custa em direitos abdicados**. Essa ressalva não é decorativa: PJ com valor de CLT é só CLT sem férias, sem 13º, sem FGTS e sem estabilidade.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>O mercado inteiro no mesmo grupo de WhatsApp</h2></div>
</div>

Se eu tivesse que escolher a coisa mais atípica daquele projeto, não seria técnica. Seria o fato de que **os concorrentes conversavam entre si, todos os dias, em grupos de WhatsApp**.

Não era um grupo. Eram vários, com gente de instituições financeiras e instituições de pagamento diferentes, e neles se discutia o que o manual do Banco Central queria dizer numa passagem ambígua, que código de erro o SPI devolvia numa situação específica, se alguém já tinha conseguido passar em determinada etapa de teste, o que o BC tinha respondido a uma dúvida formal. Havia também eventos online promovidos pelos próprios PSPs, para alinhar expectativas e planejamento com o que estava sendo determinado pelo regulador.

<div class="callout callout-tip">
  <div class="callout-label">Por que a colaboração fazia sentido econômico</div>
  Ninguém ganhava nada com o vizinho falhando. Um sistema de pagamentos instantâneos só tem valor se a rede inteira funciona — um PIX que sai do meu banco precisa chegar no banco do outro. A concorrência real estava no produto, na tarifa e na experiência; a interpretação da norma era custo comum. Foi a demonstração mais clara que eu já vi de que colaborar e competir não são opostos.
</div>

E, para nós, aquilo virou networking de um tipo que não se constrói em conferência. Você passa meses resolvendo um problema difícil junto com pessoas de outras empresas, sob a mesma pressão, e sai dali sabendo quem é bom, quem responde e quem entende do assunto. Boa parte das conexões profissionais que eu levei do Brasil vieram daqueles grupos.

### Primeiro homologado, e a semana seguinte no LinkedIn

A homologação junto ao Banco Central tinha três etapas: teste de capacidade e performance, teste de funcionalidade do registro de chaves e aprovação do novo projeto do aplicativo — aquele mesmo anteprojeto da Carta-Circular 4.056 que abriu este texto. O banco passou nas três e a notícia saiu no fim de setembro e no começo de outubro de 2020: primeira instituição financeira digital com plataforma PIX totalmente homologada pelo Bacen.

Um número dessa etapa vale ser posto ao lado do <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">gráfico dos percentis do Manual de Tempos, na segunda parte</a>. O teste de performance de liquidação exigia responder em até 2,3 segundos. A plataforma respondeu em 242 milissegundos — cerca de dez vezes abaixo do exigido. É exatamente a linha "autorização pelo PSP do recebedor, P95, 2,3 s" daquela tabela, vista do lado de quem estava sendo medido.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o efeito colateral da notícia
  </div>
  <p>Na semana em que a notícia foi publicada, praticamente todo mundo do time recebeu convite de entrevista no LinkedIn. E não eram abordagens genéricas de recrutador: eram propostas tentadoras, de empresas que sabiam exatamente o que aquele time tinha acabado de fazer.</p>
  <p>Foi a primeira vez que eu vi, na prática, o mercado precificar uma linha de currículo em tempo real. Ninguém tinha ficado melhor como engenheiro em sete dias. O que mudou foi a prova pública de que aquele grupo tinha entregue algo difícil, com prazo regulatório, antes de todo mundo.</p>
  <p>Guardo isso como a lição mais desconfortável do projeto: competência é necessária, mas é a evidência verificável dela que abre porta. Trabalhar em coisa que aparece — ou em coisa cujo resultado alguém consegue conferir — muda a sua carreira mais rápido do que trabalhar bem em silêncio.</p>
</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>O que eu levei desse projeto</h2></div>
</div>

**Prazo externo é um tipo diferente de restrição, e é libertador.** Quando a data não é negociável, a conversa deixa de ser "quando fica pronto" e passa a ser "o que entra na primeira versão". Isso força priorização honesta muito mais rápido do que qualquer cerimônia de planejamento.

**Especificação instável é o inimigo real, não o volume de código.** Os manuais técnicos evoluíram durante o desenvolvimento. Quem tinha isolado a borda absorveu; quem tinha espalhado o formato do BC por dentro do domínio, refez.

**Em sistema financeiro, o caminho de exceção é o produto.** Confirmação é fácil. Timeout, resposta duplicada, resposta tardia, estorno de estorno — é aí que mora o trabalho, e é aí que mora o dinheiro.

**Idempotência não é otimização.** Num sistema onde a mesma mensagem pode chegar duas vezes por desenho da rede, ela é a diferença entre um sistema correto e um sistema que cria dinheiro.

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
      Agência Brasil. <strong>Começa hoje registro de chaves digitais do Pix — cronograma oficial de 5/10, 3/11 e 16/11 de 2020.</strong>
      <a href="https://agenciabrasil.ebc.com.br/economia/noticia/2020-10/comeca-hoje-registro-de-chaves-digitais-do-pix" target="_blank">agenciabrasil.ebc.com.br</a>
    </li>
    <li>
      InfoMoney. <strong>Pix: fase restrita começa em 3 de novembro com clientes e horários limitados.</strong>
      <a href="https://www.infomoney.com.br/minhas-financas/pix-fase-restrita-tem-inicio-no-dia-3-com-clientes-e-horarios-limitados-saiba-como-vai-funcionar/" target="_blank">infomoney.com.br</a>
    </li>
    <li>
      TudoCelular. <strong>BS2 é o primeiro banco digital totalmente homologado pelo Bacen para o PIX — aprovação nas três fases de teste.</strong>
      <a href="https://www.tudocelular.com/seguranca/noticias/n164085/pix-banco-bs2-primeiro-digital-homologado-bacen-banco-central.html" target="_blank">tudocelular.com</a>
    </li>
    <li>
      Seu Crédito Digital. <strong>PIX: BS2 é o primeiro banco aprovado no teste de performance do Banco Central — 242 ms contra o limite de 2,3 segundos.</strong>
      <a href="https://seucreditodigital.com.br/pix-bs2-e-o-primeiro-banco-aprovado-no-teste-de-performance-do-banco-central/" target="_blank">seucreditodigital.com.br</a>
    </li>
    <li>
      JD Consultores. <strong>O papel do piloto de reserva bancária nas instituições financeiras — monitoramento de saldos, liquidez e contingência, incluindo madrugadas e fins de semana com o Pix em operação.</strong>
      <a href="https://www.jdconsultores.com.br/piloto-de-reserva-bancaria/" target="_blank">jdconsultores.com.br</a>
    </li>
    <li>
      Conta Simples. <strong>Anúncio de vaga de analista sênior de tesouraria (piloto de reserva) — domínio operacional do STR e do SPI, saldo intradiário via RSFN, contingência, devoluções e MED. Anúncios de vaga saem do ar; consultado em agosto de 2026.</strong>
      <a href="https://contasimples.gupy.io/jobs/11034137?jobBoardSource=gupy_public_page" target="_blank">contasimples.gupy.io</a>
    </li>
    <li>
      Corner Pix. <strong>Participante indireto com piloto de reservas próprio, sem interferência do piloto de reservas do liquidante SPI direto.</strong>
      <a href="https://cornerpix.com.br/participante-indireto/" target="_blank">cornerpix.com.br</a>
    </li>
    <li>
      Tribunal Superior do Trabalho. <strong>Nova redação da Súmula 428 reconhece sobreaviso em escala com celular — aplicação analógica do art. 244, §2º da CLT.</strong>
      <a href="https://www.tst.jus.br/noticias/-/asset_publisher/89Dk/content/nova-redacao-da-sumula-428-reconhece-sobreaviso-em-escala-com-celular" target="_blank">tst.jus.br</a>
    </li>
  </ol>
</div>
