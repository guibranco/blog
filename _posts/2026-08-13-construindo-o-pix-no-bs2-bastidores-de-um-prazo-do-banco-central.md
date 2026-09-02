---
layout: post
lang: pt-BR
title: "Construindo o PIX no BS2: oito meses, um prazo do Banco Central e um AirBnB em BH"
description: "Como foi sair do time B2B em São Paulo para o time de projetos especiais do core bancário e atravessar 2020 construindo o PIX, com data de lançamento definida pelo Banco Central, um time remontado no meio do caminho e o mercado inteiro colaborando em grupos de WhatsApp."
date: 2026-08-13
categories: [Career]
subcategories:
  - "Career/Behind the Scenes"
tags: [pix, banco-central, central-bank, carreira, career, sistemas-financeiros, financial-systems, bastidores, pandemia]
medium_tags: [pix, fintech, career, on-call, brazil]
reading_time: 26
cover: /assets/img/posts/pix-bs2-bastidores.svg
image: /assets/img/posts/pix-bs2-bastidores.png
series: pix-bs2
series_title: Desenvolvendo o PIX
series_part: 1
---

<p class="lead">Em março de 2020 eu saí de um time B2B em São Paulo e entrei no time de projetos especiais do core bancário. A primeira coisa que me contaram na nova mesa foi que o Banco Central tinha marcado o lançamento do PIX para novembro. Não era uma meta de roadmap. Era uma data.</p>

<div class="callout callout-tip">
  <div class="callout-label">Este é o primeiro de três textos</div>
  Aqui eu conto os <strong>bastidores humanos</strong> do projeto: a mudança de time, a remontagem do time no meio do caminho e a colaboração entre concorrentes. A anatomia financeira do meu contrato — valor fixo, sobreaviso e o mês de sete dias por semana — está na <a href="{{ site.baseurl }}/artigos/contrato-do-pix-valor-fixo-sobreaviso-e-a-hora-que-nao-existia/">segunda parte, sobre o contrato do PIX</a>. A arquitetura — SPI, ISO 20022, os percentis do Manual de Tempos, RabbitMQ e a iniciação de pagamentos — está na <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">terceira parte, sobre a arquitetura do PIX vista por dentro</a>.
</div>

<div class="callout callout-warn">
  <div class="callout-label">Sobre o que este texto é</div>
  Este é um relato de bastidores sobre <strong>como se constrói software com prazo regulatório</strong>. Tudo que descrevo sobre o PIX em si é público e está no material do Banco Central, linkado no final. Nomes internos de sistemas, módulos, topologia e colegas de time ficam de fora — cito apenas o CIO da época, pelo papel público que ocupava. Os demais aparecem pelo cargo. As datas e os horários vêm do meu próprio histórico de localização da época.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Março de 2020: a mudança de mesa</h2></div>
</div>

Eu estava num time B2B em São Paulo. Era um trabalho confortável no sentido em que a régua era conhecida: cliente pedia, a gente entregava, o prazo era negociável na margem.

Antes de contar como saí dele, preciso explicar a geografia do banco, porque ela é metade da história.

A estrutura era dividida em **BUs** — *business units*, ou tribos —, e cada uma tinha marketing, comercial, produto e engenharia próprios. A BU de Pessoa Jurídica, onde eu estava, era inteiramente baseada em São Paulo, do marketing à engenharia, assim como as BUs de câmbio e investimentos. Em Belo Horizonte ficavam a BU de Pessoa Física e **todo o resto do banco**: o core bancário — com serviços financeiros dentro dele — e a estrutura de apoio, do financeiro e da tesouraria ao RH, ao marketing institucional e à publicidade.

Eu estava na squad de BaaS e API banking, dentro da BU PJ. Ou seja: o lugar para onde eu queria ir ficava a quase 600 quilômetros de onde eu trabalhava, e não por acaso — era assim que o banco estava organizado.

E eu queria ir. Já tinha manifestado interesse em atuar no core bancário antes de existir qualquer conversa sobre PIX. Meu alvo, na verdade, era o **SPB — o Sistema de Pagamentos Brasileiro**, que na época era por onde passavam TED e DOC. Eu queria entender como o dinheiro sai de uma instituição e entra em outra de verdade, no nível do protocolo. Não fazia ideia de que existia um **SPI — o Sistema de Pagamentos Instantâneos**, a infraestrutura sobre a qual o PIX ia rodar —, muito menos de que ele estava sendo construído naquele momento.

Ajudou que aquele não era um destino cheio de estranhos. O head de serviços financeiros era mineiro, mas vinha de ter sido **PO da squad de internet banking e de onboarding** do braço PJ em São Paulo — a squad que cuidava do IB em si e do cadastro de clientes novos e de leads.

Eu estava em outra parte do mesmo braço. A minha squad era a de **API banking e BaaS**, e havia uma segunda squad, a da **plataforma de cobrança** — separada do internet banking, apesar de o nome sugerir o contrário para quem vê de fora. As duas dividiam o mesmo PO, porque o assunto era vizinho: quem consome API para emitir boleto costuma ser o mesmo cliente que consome API para movimentar conta. Ou seja: eu conhecia o futuro head de serviços financeiros das mesmas reuniões de priorização, mas a gente respondia a POs diferentes e olhava para produtos diferentes.

E o diretor de TI era o **Fernando Radunz**, antigo head de tecnologia daquele mesmo braço PJ, promovido a CIO no começo de 2020. As duas pessoas que decidiam sobre o projeto tinham saído da estrutura de onde eu vinha.

### O convite apareceu numa conversa de demissão — e eu fui atrás dele

Esta é a parte que eu conto em conversa de carreira e que não cabe em currículo nenhum.

Eu tinha recebido uma proposta externa de uma adquirente da Faria Lima. Salário maior. Mas a vaga era em Java, uma tecnologia que eu não usava — seria trocar de empresa e de stack ao mesmo tempo, e eu estava genuinamente em cima do muro.

Levei o caso para o meu coordenador na época, que tocava o time de engenharia do B2B/PJ. Ele conhecia a estrutura por dentro, sabia do meu interesse antigo pelo core e me deu um conselho bem específico: antes de aceitar qualquer coisa, senta com o Radunz. Não como quem pede conselho de carreira — como quem formaliza a saída.

Foi exatamente o que eu fiz. Marquei uma conversa com o CIO para **pedir demissão** já esperando que dali saísse uma proposta. Não era blefe no sentido de ameaça vazia: a oferta externa era real e eu teria aceitado. Mas eu não entrei naquela sala ingênuo, e é importante dizer isso porque a versão romântica dessa história — "eu ia embora e o destino apareceu" — é mais bonita e menos verdadeira.

E o convite apareceu: um time em Belo Horizonte, dentro do core, num projeto que ele ainda não podia detalhar. Não era contraproposta genérica de salário. Era exatamente a coisa que eu tinha dito que queria, oferecida no momento exato em que eu estava saindo pela porta — e que o meu coordenador já suspeitava que existia.

<div class="callout callout-tip">
  <div class="callout-label">Três coisas que eu tiraria daqui</div>
  <p>Dizer em voz alta, com antecedência e para as pessoas certas, para onde você quer ir muda o que te oferecem quando algo surge. Se eu nunca tivesse falado do core, aquele convite não teria como existir.</p>
  <p>Oportunidade grande raramente vem de processo seletivo interno bem divulgado. Vem de quem já viu você trabalhar e precisa de gente rápido — e as pessoas com quem você trabalhou há dois anos são o pipeline de vagas mais confiável que você tem.</p>
  <p>E a menos confortável: a conversa de saída costuma ser a primeira em que a empresa escuta você com atenção total. Isso é falha de gestão, não mérito seu. O que dá para fazer com isso é o que eu fiz — ouvir alguém que enxerga o organograma melhor do que você e escolher a porta certa para bater. O que não dá é blefar sem proposta na mão, porque às vezes aceitam o pedido e acabou a conversa.</p>
</div>

Aceitei. E, como o interesse era anterior, mudar para BH não me pareceu castigo — o que não impediu que algumas pessoas da BU PJ em São Paulo me perguntassem, com preocupação sincera, se eu tinha **pedido** para ir ou se aquilo tinha sido **imposto**. Sair de São Paulo para Belo Horizonte, na cabeça de boa parte do mercado de tecnologia paulistano, só podia ser punição.

O time era o de **projetos especiais** dentro de serviços financeiros. Na prática, isso significa a camada onde a conta corrente existe de verdade: débito, crédito, saldo, lançamento, conciliação. É a parte do banco onde ninguém aplaude quando funciona e todo mundo aparece quando não funciona.

A diferença cultural entre os dois mundos foi imediata. No B2B, um bug ruim é um cliente irritado. No core, um bug ruim é dinheiro no lugar errado — e, com o PIX, dinheiro no lugar errado em menos de dez segundos, sem janela de estorno automático, no fim de semana, às três da manhã.

E tudo isso acontecendo em 2020, na primeira onda da pandemia — num projeto que ninguém tinha feito antes porque o sistema ainda não existia em lugar nenhum do mundo naquele formato. A mudança de mesa e o fechamento dos escritórios aconteceram, literalmente, na mesma semana.

<div class="divider">· · ·</div>

### A semana em Belo Horizonte

Eu ia me mudar no **domingo, 15 de março de 2020**. Cheguei em Guarulhos às nove da noite e perdi o voo — às 22h25 eu já estava de volta em São Paulo, com a mudança adiada em um dia e a sensação clássica de quem começa uma fase nova errando o primeiro passo.

Remarquei para o dia seguinte. **Segunda, 16 de março**, saí de casa às 6h02, decolei às 8h06 e pousei em Confins às 9h56. Larguei as malas no AirBnB por volta das 11h e às 14h08 estava no escritório novo. Fiquei até as 19h.

O banco ocupava uma torre na cidade, mas o time de projetos especiais não estava em nenhum dos andares de escritório: estávamos numa **sala temporária no térreo**. Provavelmente por falta de espaço lá em cima, e por sermos um time novo, emergente e urgente ao mesmo tempo. Guardei aquela imagem por anos — o projeto que se tornaria o mais estratégico do banco começou numa sala emprestada no térreo, com gente que tinha acabado de se conhecer.

Na segunda à noite, pelos grupos de WhatsApp, ficamos sabendo que o time de São Paulo tinha ido para home office. Sobre Belo Horizonte, nada.

**Terça, 17 de março**, foi um dia de trabalho absolutamente normal: cheguei ao escritório às 11h, escritório cheio, e às 11h35 saí para almoçar num restaurante típico mineiro a trezentos metros dali. Voltei às 12h28 e fiquei até as 18h39. Foi o último almoço fora que eu faria em muito tempo — e, sem que ninguém na mesa soubesse, o decreto que declarava situação de emergência em saúde pública em Belo Horizonte foi assinado naquele mesmo dia. Terça à noite chegou o aviso de que, a partir de quarta, BH também ficaria em casa.

**Quarta, 18 de março**, eu já trabalhava do AirBnB — das 8h56 às 22h44 sem sair do apartamento, segundo o meu próprio celular. No dia seguinte a prefeitura publicou o decreto que suspendia os alvarás de bares, restaurantes e shoppings da cidade. O restaurante de terça fechou na sexta.

Foi nesse dia que troquei mensagens com o diretor de TI para entender o que ele achava — se eu ficava ou voltava. Ele era de São Paulo, morava lá com a família e passava só a semana em BH, então o dilema era exatamente o mesmo, com dez anos a mais de bagagem. O conselho foi voltar durante a quarentena. A conta era prática: aquilo supostamente duraria quarenta dias, eu não conseguiria procurar nem alugar nada naquela situação, e ficar significava queimar dinheiro em AirBnB para trabalhar sozinho num apartamento vazio. A gente estimava o prazo olhando para os países que já estavam confinados na época — o que, em retrospecto, foi o palpite mais otimista de todos.

Arrumei as coisas, avisei o head do time e o especialista que mais tarde assumiria o lugar dele, e peguei um táxi para o aeroporto às 22h44 da quarta, com medo de não conseguir táxi nenhum de madrugada. Cheguei em Confins às 23h27 e virei a noite lá. Meu voo era quinta, às cinco da manhã.

**Quinta, 19 de março**, decolei às 5h01, pousei em Congonhas às 6h31 e às 7h14 estava em casa em São Paulo. Comecei a trabalhar naquela mesma manhã. E fiquei remoto dali em diante, praticamente sem interrupção, até sair do banco em 2021.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a mudança que nunca aconteceu
  </div>
  <p>Foram dois dias de escritório e uma passagem de volta. A mudança para Belo Horizonte, que em março era a grande decisão de vida do ano, simplesmente evaporou: a pandemia derrubou o argumento de "estar junto", o projeto começou a andar mesmo assim, e a proposta nunca mais foi retomada.</p>
  <p>Construí o PIX inteiro de São Paulo, remoto, com o time em BH — o que em 2020 ainda parecia uma concessão excepcional e não o padrão.</p>
  <p>Olhando de hoje, com anos morando fora, aquela semana foi um ensaio muito barato de uma coisa que eu faria de verdade depois: chegar num lugar onde você não conhece ninguém, ter poucos dias para entender como as coisas funcionam e decidir se fica. A diferença é que, das outras vezes, não teve voo de volta na quinta.</p>
</div>

Escrevi "praticamente sem interrupção" porque houve uma. Na **segunda, 27 de abril de 2020**, com São Paulo em quarentena e a cidade vazia, eu precisei ir ao escritório da Vila Olímpia por um motivo que resume bem o primeiro mês de pandemia corporativa: **resetar a senha da VPN**. A política exigia que a troca fosse feita numa máquina dentro da rede, e a rede só existia lá. Saí de casa às 12h37, fiquei **dezessete minutos** dentro do prédio e às 13h55 estava de volta. Vinte e seis quilômetros de deslocamento para um formulário.

É o tipo de detalhe que parece anedota e é, na verdade, o retrato de uma coisa séria: em março de 2020 quase nenhuma empresa tinha controle de acesso desenhado para um mundo em que ninguém entra no escritório. O ano inteiro foi essa corrida — reescrever pressupostos de segurança, de contratação e de operação que tinham sido construídos assumindo presença física.

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
    <div class="provider-detail"><strong>Um sênior e um pleno</strong> — o sênior era eu. Fazer o pagamento sair, e permitir que outras instituições fizessem pagamentos saírem através da gente. O detalhamento técnico das duas está na <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">terceira parte da série</a>.</div>
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
  <div class="section-title-wrap"><h2>O mercado inteiro no mesmo grupo de WhatsApp</h2></div>
</div>

### Antes: como a gente se comunicava dentro de casa

Para essa parte fazer sentido, vale explicar o que era normal.

No B2B, em São Paulo, a ferramenta oficial era o **Teams**. Só que era um time presencial, então o Teams servia mais para chamada e para registro do que para conversa: se você precisava de alguém, você levantava e ia até a mesa da pessoa. Chat era o que sobrava quando o outro não estava lá.

Para falar com Belo Horizonte, a ferramenta era outra: **Skype**. Nunca descobri direito o motivo — o pessoal de BH ainda não tinha migrado para o Teams, e a Microsoft ainda não tinha desligado o Skype, então as duas coisas conviviam. Na prática, dava para saber com quem você estava falando pelo aplicativo que abria. Skype significava BH; Teams significava a sua própria BU. Isso parece anedota de ferramenta e é, na verdade, uma boa métrica de quanto as duas metades do banco eram mundos separados.

E aí tinha a camada informal, que era onde o trabalho de verdade acontecia: **WhatsApp**, em camadas concêntricas.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">O grupo da squad</div>
    <div class="provider-detail">No meu caso, um grupo só para as duas squads — API banking/BaaS e plataforma de cobrança —, porque o assunto era vizinho e o PO era o mesmo.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O grupo do time de TI do B2B</div>
    <div class="provider-detail">Toda a engenharia da BU. Era onde se reportava incidente, se avisava de indisponibilidade e também onde se combinava cerveja. Profissional e social no mesmo lugar.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O grupo do B2B inteiro</div>
    <div class="provider-detail">Engenharia mais produto, marketing e comercial. A BU como unidade, não como departamento.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Os grupos com cliente</div>
    <div class="provider-detail">Um por integração, com gente das duas empresas dentro.</div>
  </div>
</div>

Os grupos com cliente são a parte que mais surpreende quem nunca trabalhou com API banking. Não era canal de suporte: era um grupo por projeto de integração, com o contato técnico do cliente, às vezes o CTO ou CIO da empresa dele, e do nosso lado eu, o meu tech lead, às vezes o coordenador — e, dependendo do tamanho da conta, o próprio CIO do banco. Numa integração com uma das maiores varejistas do país, o CTO deles estava no grupo.

<div class="callout callout-tip">
  <div class="callout-label">Por que isso funcionava</div>
  Um grupo de WhatsApp com o CTO do cliente dentro elimina, de uma vez, três camadas de telefone sem fio: o comercial que não entende o erro, o suporte que não tem acesso ao log e o gerente de projeto que traduz mal os dois. O custo é evidente — some a fronteira entre horário de trabalho e vida, e some o registro formal do que foi combinado. Mas a velocidade era incomparável, e em integração técnica velocidade de resposta é metade do produto.
</div>

Guardo isso porque explica o que vem a seguir. Quando, meses depois, apareceram os grupos de WhatsApp com gente de bancos concorrentes discutindo o manual do Banco Central, aquilo não me pareceu estranho. Era a mesma ferramenta, a mesma informalidade e a mesma lógica — só que com a fronteira uma casa mais para fora.

<div class="divider">· · ·</div>

Se eu tivesse que escolher a coisa mais atípica daquele projeto, não seria técnica. Seria o fato de que **os concorrentes conversavam entre si, todos os dias, em grupos de WhatsApp**.

Não era um grupo. Eram vários, com gente de instituições financeiras e instituições de pagamento diferentes, e neles se discutia o que o manual do Banco Central queria dizer numa passagem ambígua, que código de erro o SPI devolvia numa situação específica, se alguém já tinha conseguido passar em determinada etapa de teste, o que o BC tinha respondido a uma dúvida formal. Havia também eventos online promovidos pelos próprios PSPs, para alinhar expectativas e planejamento com o que estava sendo determinado pelo regulador.

<div class="callout callout-tip">
  <div class="callout-label">Por que a colaboração fazia sentido econômico</div>
  Ninguém ganhava nada com o vizinho falhando. Um sistema de pagamentos instantâneos só tem valor se a rede inteira funciona — um PIX que sai do meu banco precisa chegar no banco do outro. A concorrência real estava no produto, na tarifa e na experiência; a interpretação da norma era custo comum. Foi a demonstração mais clara que eu já vi de que colaborar e competir não são opostos.
</div>

E, para nós, aquilo virou networking de um tipo que não se constrói em conferência. Você passa meses resolvendo um problema difícil junto com pessoas de outras empresas, sob a mesma pressão, e sai dali sabendo quem é bom, quem responde e quem entende do assunto. Boa parte das conexões profissionais que eu levei do Brasil vieram daqueles grupos.

### Setembro: sete dias por semana

Se eu tivesse que apontar o mês em que o projeto cobrou a fatura, seria setembro de 2020. O registro de chaves entrava em produção em 5 de outubro, a homologação junto ao Banco Central corria em paralelo, e a especificação tinha fechado havia poucas semanas. O mês virou de sete dias por semana: **trabalhei três dos quatro fins de semana** — 5 e 6, 12 e 13, 26 e 27 —, além de horas extras nos dias úteis. Meu histórico de localização de setembro é quase uma linha reta: casa, casa, casa.

Com quatro exceções, todas na mesma semana.

Nos dias **17 e 18 de setembro, uma quinta e uma sexta**, eu voltei ao escritório da Vila Olímpia — dois dias cheios, das 9h26 às 20h04 e das 9h39 às 19h49. Não era visita nostálgica. Era para sentar do lado do meu antigo time, o de **B2B/Empresas**, e ajudar na integração deles com o SPI.

E não era favor informal. Aquilo foi alinhado antes com quatro pessoas: o head do meu time novo, o gerente de serviços financeiros, o gerente do B2B e o próprio CIO. Quatro assinaturas para dois dias de trabalho — o que dá a medida de quão pouco trivial era emprestar alguém do projeto do PIX naquele mês.

O motivo de ser eu era prosaico: eu conhecia aquelas pessoas e morava em São Paulo. Ninguém precisava pegar avião. Mas o detalhe diz muito sobre como um projeto de PIX se espalha dentro de um banco. O core construía a conexão com o Banco Central, mas quem tinha o cliente PJ na mão era a BU de onde eu tinha saído — e o produto deles precisava falar com a plataforma nova. Eu era, naquele momento, a única pessoa que conhecia os dois lados: o vocabulário do SPI e o jeito como aquele time pensava integração. Meses depois de ter mudado de mesa, o motivo de eu ter mudado virou a razão de eu ser útil na mesa antiga.

<div class="callout callout-tip">
  <div class="callout-label">O ativo que ninguém coloca no currículo</div>
  Quando você muda de time dentro da mesma empresa, o valor que você leva não é só técnico — é a tradução. Saber como o outro lado nomeia as coisas, quem decide o quê e onde a conversa costuma travar economiza semanas de alinhamento. É a maior vantagem prática de uma transferência interna sobre uma contratação externa, e quase nunca é reconhecida como trabalho.
</div>

E, no fim daquela mesma semana, o único fim de semana livre do mês: **sábado, 19 de setembro**, voei para Belo Horizonte às 8h12 e cheguei às 9h14 para um churrasco com o time, em Confins, na região metropolitana. Foi a primeira vez que eu vi pessoalmente a maior parte daquelas pessoas — gente com quem eu falava todo dia havia cinco meses, cujas casas eu conhecia por videochamada e cujos rostos eu só tinha visto em retângulo. Voltei no domingo, dia 20, no voo das 14h39.

Não era confraternização de fim de projeto: faltavam quase dois meses para o lançamento e o pior ainda estava por vir. Era, mais precisamente, o reconhecimento de que um time que só se conhece por tela tem um limite — e que atravessar outubro e novembro ia exigir mais do que boa vontade em call.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o custo do mês inteiro
  </div>
  <p>Três fins de semana de trabalho num mês não é heroísmo, é uma escolha ruim que às vezes não tem alternativa boa. O prazo era do Banco Central, o time tinha sido remontado no meio do caminho e o escopo não cabia. A conta fechou, mas fechou no músculo.</p>
  <p>O que eu faria diferente hoje não é trabalhar menos naquele mês específico — é ter brigado mais cedo, em julho, pela conversa sobre o que ficaria de fora da primeira versão. Quando você chega em setembro precisando de sete dias por semana, a decisão errada já foi tomada semanas antes, e o esforço extra é só o preço dela.</p>
  <p>Setembro também teve um custo financeiro, e ele é específico o bastante para merecer texto próprio: eu estava em contrato de valor fixo, e quem estava por hora recebeu extra por aqueles sábados e domingos. Essa conta — com os números das minhas notas fiscais — está na <a href="{{ site.baseurl }}/artigos/contrato-do-pix-valor-fixo-sobreaviso-e-a-hora-que-nao-existia/">segunda parte da série</a>.</p>
</div>

### Primeiro homologado, e a semana seguinte no LinkedIn

A homologação junto ao Banco Central tinha três etapas: teste de capacidade e performance, teste de funcionalidade do registro de chaves e aprovação do novo projeto do aplicativo — aquele mesmo anteprojeto da Carta-Circular 4.056 que abriu este texto. O banco passou nas três e a notícia saiu no fim de setembro e no começo de outubro de 2020: primeira instituição financeira digital com plataforma PIX totalmente homologada pelo Bacen.

Um número dessa etapa vale ser posto ao lado do <a href="{{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/">gráfico dos percentis do Manual de Tempos, na terceira parte</a>. O teste de performance de liquidação exigia responder em até 2,3 segundos. A plataforma respondeu em 242 milissegundos — cerca de dez vezes abaixo do exigido. É exatamente a linha "autorização pelo PSP do recebedor, P95, 2,3 s" daquela tabela, vista do lado de quem estava sendo medido.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o efeito colateral da notícia
  </div>
  <p>Na semana em que a notícia foi publicada, praticamente todo mundo do time recebeu convite de entrevista no LinkedIn. E não eram abordagens genéricas de recrutador: eram propostas tentadoras, de empresas que sabiam exatamente o que aquele time tinha acabado de fazer.</p>
  <p>Foi a primeira vez que eu vi, na prática, o mercado precificar uma linha de currículo em tempo real. Ninguém tinha ficado melhor como engenheiro em sete dias. O que mudou foi a prova pública de que aquele grupo tinha entregue algo difícil, com prazo regulatório, antes de todo mundo.</p>
  <p>Guardo isso como a lição mais desconfortável do projeto: competência é necessária, mas é a evidência verificável dela que abre porta. Trabalhar em coisa que aparece — ou em coisa cujo resultado alguém consegue conferir — muda a sua carreira mais rápido do que trabalhar bem em silêncio.</p>
</div>

<div class="section-header">
  <div class="section-num">05</div>
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
  <p>E a mudança para Belo Horizonte, que era a grande decisão de vida em março, virou uma semana de AirBnB e uma passagem de volta. Às vezes a mudança importante do ano não é a que estava no plano.</p>
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
      Prefeitura de Belo Horizonte. <strong>Decreto nº 17.297, de 17 de março de 2020 (situação de emergência em saúde pública) e Decreto nº 17.304, de 18 de março de 2020, que suspendeu a partir de 20 de março os alvarás de bares, restaurantes, shoppings e demais atividades com potencial de aglomeração.</strong>
      <a href="https://prefeitura.pbh.gov.br/noticias/prefeito-suspende-temporariamente-funcionamento-de-estabelecimentos-comerciais" target="_blank">prefeitura.pbh.gov.br</a>
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
  </ol>
</div>
