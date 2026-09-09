---
layout: post
lang: pt-BR
title: "A ilusão do portfólio: por que aquela página com sua foto não vai te arrumar emprego"
description: "O portfólio de dev virou dogma na pandemia, empurrado por quem vendia curso. Por que quem contrata não consegue avaliar candidato por repositório de estudo, o que a gente realmente olha, e o que fazer no lugar disso."
date: 2026-09-09
categories: [Career]
subcategories:
  - "Career/Job Market"
tags: [carreira, mercado-de-trabalho, portfolio, github, junior, estagio, primeiro-emprego, bootcamp, contratacao, open-source, projetos, pandemia]
reading_time: 14
cover: /assets/img/posts/ilusao-do-portfolio.svg
image: /assets/img/posts/ilusao-do-portfolio.png
medium_tags: [carreira, programacao, portfolio, github, mercado-de-trabalho]
---

<p class="lead">Todo mês aparece a mesma cena nos grupos: alguém posta o link de um portfólio — uma página HTML com foto, nome, três ícones de rede social e uma lista de repositórios chamados <em>todo-list</em>, <em>calculadora</em> e <em>clone-do-netflix</em> — e pergunta por que não está sendo chamado para entrevista. A resposta honesta é desconfortável: não é por causa do portfólio. É que aquilo nunca foi o instrumento que decide contratação de emprego fixo, e quem disse que era estava vendendo outra coisa.</p>

<div class="callout callout-tip">
  <div class="callout-label">Antes de qualquer coisa</div>
  Isto não é um texto contra quem estuda, contra quem faz projeto pessoal ou contra quem está tentando entrar na área. É um texto contra uma expectativa mal calibrada que fizeram você comprar. Projeto de estudo é ótimo — para estudar. O problema é o que te prometeram que ele faria por você no processo seletivo.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>De onde veio essa ideia</h2></div>
</div>

Vale começar pela parte que quase ninguém checa: **isso é recente**. Não é uma prática histórica da profissão que os iniciantes de hoje redescobriram.

O GitHub existe desde 2008. Durante a maior parte desse tempo ele foi ferramenta de trabalho e infraestrutura de projeto aberto — não vitrine de candidato. Quem entrou na área nos anos 2010 mandava currículo, fazia teste técnico e conversava sobre o que tinha feito. Ninguém montava uma landing page de si mesmo para conseguir vaga CLT, e ninguém era cobrado por não ter uma.

O hábito de publicar progresso de estudo tem uma data mais ou menos identificável: em junho de 2016, um desenvolvedor chamado Alexander Kallaway propôs um desafio pessoal — programar pelo menos uma hora por dia durante 100 dias seguidos e publicar o progresso, o que virou a hashtag #100DaysOfCode. Repare no propósito original: era **disciplina de estudo com prestação de contas pública**. Não era peça de contratação. A distorção veio depois.

O ponto de virada foi 2020. Confinamento, juros baixos, mercado de tecnologia inflacionado e uma promessa que circulou em escala industrial: seis meses de curso e você troca de vida. Os números do próprio GitHub mostram o tamanho da enxurrada — o relatório Octoverse de 2020 registrou mais de 60 milhões de novos repositórios criados no período e uma entrada expressiva de gente que não era desenvolvedora: estudantes, professores, analistas de dados, designers. A plataforma fechou aquele ano com mais de 56 milhões de contas.

E aqui está a parte que interessa. Para quem vendia curso, "monte um portfólio" resolvia um problema comercial específico:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-box-open"></i> Era a única entrega verificável</div>
    <div class="provider-detail">Curso barato não consegue prometer emprego. Mas consegue prometer um artefato ao final do módulo — e um link é a prova mais fácil de mostrar que o aluno "concluiu".</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-share-nodes"></i> Era conteúdo que se autopropaga</div>
    <div class="provider-detail">Aluno postando o print do projeto novo é anúncio grátis, com depoimento embutido, na timeline de outras pessoas que também querem trocar de carreira.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-arrows-turn-to-dots"></i> Transferia a culpa do fracasso</div>
    <div class="provider-detail">Se o emprego não veio, a explicação já estava pronta: faltou projeto, faltou README bonito, faltou commit verde. Nunca faltou nada no curso.</div>
  </div>
</div>

Cinco anos depois, o conselho continua sendo repetido por gente bem-intencionada que nunca participou de uma contratação — enquanto o volume tornou o sinal ainda mais fraco. O Octoverse de 2025 aponta mais de 180 milhões de desenvolvedores na plataforma, com cerca de 36 milhões de contas novas em um único ano e 395 milhões de repositórios públicos. Um link para um repositório não é escassez. É ruído.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O que o portfólio típico realmente prova</h2></div>
</div>

Vamos ser literais sobre o que aquele conjunto de arquivos comunica para quem está do outro lado.

Ele prova que, em algum momento da sua vida, você digitou código. Ou, dependendo do repositório, que você **copiou** código — clonou o do instrutor, seguiu o vídeo, colou a resposta do fórum ou pediu para uma IA. Não existe como distinguir uma coisa da outra olhando o resultado.

<table class="compare-table">
  <thead><tr><th>O que o portfólio de curso mostra</th><th>O que a vaga precisa saber</th><th>Coberto?</th></tr></thead>
  <tbody>
    <tr><td>Que a sintaxe compila</td><td>Se você resolve problema com restrição</td><td><span class="cross">✗</span></td></tr>
    <tr><td>Que o projeto roda no seu computador</td><td>Se aguenta dado real, sujo e em volume</td><td><span class="cross">✗</span></td></tr>
    <tr><td>Que você usou um framework da moda</td><td>Por que você escolheu ele e o que abriu mão</td><td><span class="cross">✗</span></td></tr>
    <tr><td>Que existe um README</td><td>Se você comunica decisão por escrito</td><td><span class="partial">~</span></td></tr>
    <tr><td>Que o layout está bonito</td><td>Se o código sobrevive a outra pessoa mexendo</td><td><span class="cross">✗</span></td></tr>
    <tr><td>Que você entregou o exercício</td><td>O que você fez quando quebrou em produção</td><td><span class="cross">✗</span></td></tr>
  </tbody>
</table>

E tem o argumento que encerra a discussão em 2026: **um clone de streaming, uma to-do list e um site de portfólio são exatamente o tipo de artefato que uma IA entrega em minutos**, com testes e README caprichado. Um artefato que uma máquina produz em quatro minutos não funciona como evidência de capacidade humana. Não porque a ferramenta desmerece quem estuda — mas porque a evidência deixou de discriminar. Se qualquer um consegue, ter não te diferencia de ninguém.

<img src="{{ site.baseurl }}/assets/img/posts/ilusao-do-portfolio-ninguem-liga.svg"
     alt="Ilustração: dois desenvolvedores experientes com a mão no ombro de um iniciante sentado ao notebook, com a legenda de que ninguém — nem o recrutador, nem o time da entrevista — vai abrir o e-commerce falso do portfólio"
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Isso não é desdém com o esforço de quem fez. É uma constatação de mecânica: ninguém abre o link porque não existe pergunta que aquele link responda. O avaliador precisa saber como você pensa sob restrição — e um projeto sem restrição, sem usuário e sem histórico não responde isso nem se ele passar a tarde inteira lendo.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Por que quem contrata não consegue avaliar isso</h2></div>
</div>

Esta é a parte que raramente chega até quem está estudando, porque quem está do lado de dentro não costuma escrever sobre isso. São quatro problemas práticos, e nenhum deles é má vontade.

**Não existe tempo.** Uma vaga de entrada hoje recebe centenas de candidaturas. Ler código de estranho com atenção suficiente para formar juízo leva de 20 a 40 minutos por pessoa. Ninguém tem 80 horas para gastar numa triagem — então a triagem acontece pelo que é rápido de ler: histórico, o que você fez, e a conversa.

**Falta o contexto que dá sentido ao código.** Código só é avaliável junto com as restrições que o produziram: prazo, sistema legado que não podia quebrar, requisito que mudou no meio, decisão de infraestrutura que já existia, gente discordando. Projeto de estudo não tem nada disso. Ele foi escrito no vácuo, sem consequência e sem ninguém dependendo dele. Olhar aquilo e concluir alguma coisa sobre o profissional é chute com aparência de método.

**Não é comparável.** Um candidato mandou um clone de e-commerce, outro mandou um bot de Discord, o terceiro mandou uma API de biblioteca. Não existe régua comum. Processo seletivo precisa de comparabilidade — é por isso que existe teste técnico padronizado, mesmo com todos os defeitos que ele tem.

**Não há procedência.** Não dá para saber quem escreveu aquilo, com quanta ajuda e em quanto tempo. E o custo do erro é assimétrico: aprovar alguém baseado em código que a pessoa não escreveu custa muito mais caro do que reprovar alguém que escreveu.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — dos dois lados da mesa
  </div>
  <p>Trabalho com desenvolvimento desde a adolescência e hoje moro em Dublin, trabalhando em engenharia de TI. Em todas as contratações por que passei como candidato — no Brasil, em Dubai e na Irlanda —, <strong>nunca me pediram portfólio e nunca tiveram meu GitHub avaliado</strong>. Perguntaram o que eu tinha construído, o que deu errado e o que eu faria diferente.</p>
  <p>Do outro lado, participando de avaliação de candidatos, também nunca usei portfólio como critério. Não por preconceito: porque não dá. Quando eu tenho quinze pessoas para avaliar e uma hora com cada uma, o que rende é conversar sobre um problema real que a pessoa enfrentou — inclusive um problema pequeno — e ver como ela pensa. Vinte minutos disso me dizem mais do que um mês olhando repositório.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>O que a gente avalia, então</h2></div>
</div>

Se não é o portfólio, o que é?

<div class="callout callout-warn">
  <div class="callout-label"><i class="fas fa-triangle-exclamation"></i> O mal-entendido que está na raiz de tudo</div>
  <strong>Desenvolvimento não é sobre digitar código — é sobre resolver problemas.</strong> Digitar código qualquer um faz: um adolescente que gosta da área faz, e hoje uma IA faz mais rápido que os dois. O que se contrata é a capacidade de entender um problema mal explicado, escolher uma solução defensável e assumir a consequência dela. Às vezes isso acontece sem escrever uma linha sequer — a melhor solução para muita coisa é não construir nada. É por isso que um repositório, sozinho, responde a pergunta errada: ele mostra a digitação, não o raciocínio.
</div>

Grosso modo, o que a gente olha são seis coisas — e todas aparecem em conversa, não em link:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-diagram-project"></i> Raciocínio sob restrição</div>
    <div class="provider-detail">Dado um problema mal definido, você pergunta as coisas certas antes de codificar? Consegue reduzir escopo quando o prazo aperta sem entregar lixo?</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-scale-balanced"></i> Capacidade de justificar decisão</div>
    <div class="provider-detail">"Por que assim e não do outro jeito?" Quem só reproduziu tutorial trava aqui. Quem construiu de verdade tem opinião — e sabe o que sacrificou.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-bug"></i> Comportamento diante do erro</div>
    <div class="provider-detail">O que você fez quando derrubou alguma coisa? Como investigou? Avisou quem? A resposta separa profissional de estudante mais rápido que qualquer teste.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-book-open"></i> Ler código dos outros</div>
    <div class="provider-detail">A maior parte do trabalho é entender o que já existe. Escrever do zero é o caso raro — e é justamente o único que o portfólio treina.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-comments"></i> Comunicação</div>
    <div class="provider-detail">Explicar problema técnico para quem não é técnico, escrever descrição de tarefa, discordar sem brigar. Isso é metade do trabalho e quase nunca é estudado.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-briefcase"></i> Histórico verificável</div>
    <div class="provider-detail">O que você já fez, onde, com quem, com que consequência. É o sinal mais forte que existe — e o único que não dá para fabricar num fim de semana.</div>
  </div>
</div>

Como já escrevi antes por aqui, [senioridade é qualidade, não quantidade](/blog/artigos/como-e-o-mercado-de-trabalho-para-desenvolvedores-ti/): não é a quantidade de tecnologias, de cursos ou de repositórios que define nível. É a profundidade do que você já teve que resolver.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Estudante não é júnior</h2></div>
</div>

Boa parte da frustração vem de uma confusão de categorias. Estudar programação não te torna júnior — te torna estudante de programação. São coisas diferentes, com expectativas diferentes.

<table class="compare-table">
  <thead><tr><th>Nível</th><th>O que se espera</th><th>Quem é</th></tr></thead>
  <tbody>
    <tr><td>Estudante</td><td>Aprender. Entregar exercício. Errar sem custo.</td><td>Não é profissional ainda — é alguém em formação</td></tr>
    <tr><td>Estagiário</td><td>Aprender <em>dentro</em> de uma empresa, com supervisão e vínculo com a instituição de ensino</td><td>Estudante matriculado, em ato educativo</td></tr>
    <tr><td>Júnior</td><td>Entregar tarefa definida com supervisão, no prazo, atravessando o ciclo inteiro: ticket, código, review, deploy, suporte</td><td>Profissional de fato, responsável por um pedaço do sistema</td></tr>
    <tr><td>Pleno</td><td>Receber problema, não tarefa. Decidir sozinho o caminho e assumir a consequência</td><td>Profissional autônomo tecnicamente</td></tr>
  </tbody>
</table>

**O júnior já é profissional.** Ele não é "o estudante que passou". Ele tem responsabilidade real: se o código dele quebra o faturamento, o problema é da empresa e o aprendizado é dele. Ninguém consegue avaliar isso em quem nunca esteve nessa posição — e é exatamente por isso que a primeira vaga é a mais difícil de todas, com ou sem portfólio.

E o estágio, no Brasil, é uma figura jurídica específica — não é "júnior barato". A Lei 11.788/2008 define estágio como ato educativo escolar supervisionado, exigindo que o estudante esteja frequentando ensino regular, com termo de compromisso assinado pelas três partes, supervisor designado e jornada limitada a 6 horas diárias e 30 semanais para o ensino superior. Sem esses requisitos, o estágio é nulo e vira vínculo empregatício com todas as obrigações trabalhistas.

Duas consequências práticas que ninguém conta para quem está começando:

<div class="callout callout-warn">
  <div class="callout-label">A maioria dos estágios não é de desenvolvimento</div>
  Estágio, historicamente, é generalista ou de suporte: atendimento, documentação, planilha, teste manual, ticket de infraestrutura, apoio administrativo à área técnica. Isso é normal e é o desenho legal da coisa — é formação, não produção. Quem entra achando que vai codar feature nova desde a primeira semana se frustra por um motivo errado.
</div>

<div class="callout callout-warn">
  <div class="callout-label">Vaga de "estágio em desenvolvimento" costuma ser júnior mascarado</div>
  Quando o anúncio pede stack completa, autonomia, entrega de feature e 30 horas semanais dedicadas a produto — mas oferece bolsa e nenhum vínculo —, aquilo não é ato educativo: é uma vaga de júnior com desconto e sem encargos. É legítimo aceitar sabendo o que é. O que não dá é confundir isso com uma porta de entrada normal e concluir que você é ruim por não conseguir passar nela.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Quem tem bom portfólio geralmente não precisa dele</h2></div>
</div>

Esse é o paradoxo que sustenta a ilusão inteira.

Existe, sim, um tipo de portfólio que impressiona: projeto com usuários reais, com issues abertas por estranhos, com histórico de manutenção de anos, com releases, com gente dependendo daquilo. Só que **quem tem isso quase nunca está procurando emprego pelo formulário**. Essa pessoa já está no mercado, já tem colegas de trabalho anteriores, já é lembrada quando abre vaga. O canal dela é indicação — o velho QI, "quem indica" — e indicação continua sendo o caminho mais rápido para uma vaga em qualquer lugar do mundo.

Ou seja: o portfólio forte é **consequência** de já estar na área, não causa de entrar nela. Quem precisa desesperadamente do portfólio é justamente quem ainda não tem o que colocar dentro dele.

Isso não quer dizer que ele nunca conte. Conta — só que em contexto diferente do que te venderam:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-laptop-code"></i> Freelancer e autônomo: pesa muito</div>
    <div class="provider-detail">O cliente compra entregável, não processo. Ele quer ver cinco sites parecidos com o que ele quer, no ar, funcionando. Aqui portfólio é o principal instrumento de venda — e sempre foi.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-building"></i> Empresa pequena: pesa um pouco</div>
    <div class="provider-detail">Quem contrata sem processo estruturado usa o que tem à mão. <a href="https://www.hackerrank.com/research/developer-skills/2018" target="_blank">Pesquisa do HackerRank (2018)</a> mostrou o portfólio valendo mais em empresa pequena (80%) do que em grande (66%) — mas experiência anterior liderando em qualquer tamanho.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-city"></i> Emprego fixo estruturado: quase nada</div>
    <div class="provider-detail">Onde existe processo — triagem, teste padronizado, entrevista técnica, painel —, o portfólio no máximo desempata dois finalistas. Ele não entra na conta antes disso.</div>
  </div>
</div>

Guarde a assimetria: **um portfólio excelente raramente decide uma contratação, mas um portfólio ruim consegue atrapalhar** — link quebrado, repositório abandonado, código copiado sem crédito, README com erro grosseiro. Se não vai cuidar, é melhor não linkar.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>O iceberg: por que o curso barato só ensina a ponta</h2></div>
</div>

Existe um motivo estrutural para o descompasso entre o que se estuda e o que se cobra. Escrever código é a única parte da profissão que dá para ensinar em vídeo, avaliar por exercício e vender por R$ 30. Todo o resto exige uma coisa que nenhum curso consegue fabricar: **consequência real**.

<img src="{{ site.baseurl }}/assets/img/posts/ilusao-do-portfolio-iceberg-carreira.svg"
     alt="Diagrama de iceberg: acima da linha d'água, escrever código (sintaxe, framework, CRUD); abaixo, requisito ambíguo, código legado, code review, testes, CI/CD, observabilidade, plantão, migrations, dado sujo, prazo, escopo, custo de infra, segurança, dívida técnica, documentação, comunicação escrita e trabalhar com gente"
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Ninguém aprende a lidar com um deploy que derrubou o sistema às duas da manhã fazendo exercício. Ninguém aprende a estimar prazo sem já ter errado estimativa na frente de alguém que dependia dela. Ninguém aprende a mexer em código legado de dez anos, escrito por gente que saiu da empresa, sem ter uma empresa com código legado de dez anos por perto.

Não é falha do professor nem má-fé do bootcamp — é limite do formato. O problema é vender a ponta do iceberg como se fosse o iceberg inteiro, e depois deixar o aluno concluir que o que falta é mais um projeto no GitHub.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Para que serve um portfólio de verdade</h2></div>
</div>

Portfólio, na origem da palavra, é **pasta de trabalhos publicados** — coisas que existiram no mundo, para outras pessoas. Arquiteto mostra prédio construído, não maquete de faculdade. Fotógrafo mostra ensaio entregue ao cliente, não exercício de curso de fotografia.

A regra de bolso é essa:

<div class="callout callout-tip">
  <div class="callout-label">O teste do usuário estranho</div>
  Existe pelo menos <strong>uma pessoa que você não conhece</strong> usando isso e que ficaria irritada se amanhã parasse de funcionar? Se a resposta for sim, é portfólio. Se for não, é estudo — e estudo é excelente, só não é evidência para terceiros.
</div>

O que muda um projeto de "exercício" para "trabalho":

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Problema de outra pessoa</div>
    <div class="provider-detail">Alguém tinha uma dor concreta — a planilha do salão da esquina, o controle de escala do time de futebol da várzea, o relatório que sua área faz na mão toda sexta.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Restrição real</div>
    <div class="provider-detail">Orçamento zero, celular velho, internet ruim, prazo do cliente, dado que chega errado. Restrição é o que gera decisão — e decisão é o que dá para avaliar.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Manutenção</div>
    <div class="provider-detail">Você continuou mexendo depois do "pronto": corrigiu bug que outra pessoa reportou, migrou versão, quebrou compatibilidade e resolveu. Isso é o que separa quem entrega de quem sustenta.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Registro da decisão</div>
    <div class="provider-detail">Um texto curto explicando por que você escolheu aquele caminho e o que descartou. Comunicação escrita é raríssima e altamente avaliável — vale mais que mais um repositório.</div>
  </div>
</div>

Caminhos que produzem esse tipo de material, em ordem de facilidade:

1. **Automatize alguma coisa do seu trabalho atual**, mesmo que ele não seja de TI. Quem trabalha em logística, contabilidade, atendimento ou estoque tem acesso a um problema real que ninguém resolveu — e a um usuário exigente: você mesmo e seus colegas. Isso é experiência de produção, com contexto e consequência.
2. **Resolva o problema de alguém próximo** e assuma o suporte. Sistema pequeno de verdade vale mais que aplicação grande de mentira.
3. **Contribua em projeto aberto que você já usa.** Comece pequeno: corrigir documentação, reproduzir bug, escrever teste que faltava. Interagir com mantenedor e passar por code review de estranho é exatamente a habilidade que a vaga quer ver.
4. **Escreva sobre o que você resolveu.** Um post curto — o problema, as opções, a escolha, o que quebrou depois — demonstra raciocínio de um jeito que nenhum repositório demonstra.

E continue fazendo clone de Netflix, se isso te ensina. Só chame pelo nome: é treino. Treino vai na sua pasta de estudos, não na apresentação profissional.

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>O atalho que não existe</h2>
  <p>A ilusão do portfólio sobreviveu porque ela é confortável dos dois lados. Para quem vende curso, é uma entrega barata que parece resultado. Para quem estuda, é uma tarefa clara e controlável — muito mais agradável do que a verdade, que é: a primeira vaga depende de escassez, de rede de contatos e de sorte de timing, em proporções que você não controla.</p>
  <p>O que você controla é o tipo de evidência que constrói. Um repositório a mais com exercício de curso não move nada. Um problema real resolvido para alguém real, mantido por seis meses e explicado por escrito, move — não porque impressiona, mas porque cria assunto para a única coisa que decide contratação: uma conversa em que você tem o que contar.</p>
  <p>Não é mais rápido. Mas é a diferença entre acumular link e acumular repertório.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>GitHub. <strong>The State of the Octoverse 2020.</strong> <a href="https://octoverse.github.com/2020/" target="_blank">octoverse.github.com</a></li>
    <li>GitHub. <strong>Octoverse 2025: a new developer joins GitHub every second.</strong> <a href="https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/" target="_blank">github.blog</a></li>
    <li>freeCodeCamp. <strong>The #100DaysOfCode Challenge, its history, and why you should try it.</strong> <a href="https://www.freecodecamp.org/news/the-crazy-history-of-the-100daysofcode-challenge-and-why-you-should-try-it-for-2018-6c89a76e298d/" target="_blank">freecodecamp.org</a></li>
    <li>Brasil. <strong>Lei nº 11.788, de 25 de setembro de 2008 (Lei do Estágio).</strong> <a href="https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm" target="_blank">planalto.gov.br</a></li>
    <li>HackerRank. <strong>2018 Developer Skills Report.</strong> <a href="https://www.hackerrank.com/research/developer-skills/2018" target="_blank">hackerrank.com</a></li>
  </ol>
</div>
