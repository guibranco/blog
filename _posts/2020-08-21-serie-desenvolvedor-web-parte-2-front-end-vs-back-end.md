---
layout: post
title: "Série: Desenvolvedor web. Parte 2: Front-end vs Back-end"
description: "O que é front-end e back-end, as tecnologias de cada área, salários, e o roteiro de estudos completo para quem quer começar no desenvolvimento web."
date: 2020-08-21
categories: [Career]
tags: [back-end, backend, carreira, css, desenvolvimento, front-end, frontend, html, javascript, nodejs, php, estudos, salario]
reading_time: 8
image: /assets/img/posts/backend-vs-frontend.jpg
series: serie-desenvolvedor-web
series_title: "Série: Desenvolvedor web"
series_part: 2
---

<p class="lead">Quer entrar no mercado de TI ou só aprender por hobby mas está perdido e não sabe nem o que procurar para começar? Leia este post que vou tentar te dar um rumo!</p>

Antes de mais nada é preciso saber que na área de TI existem diversas profissões e que uma mesma profissão pode executar trabalhos diferentes conforme a empresa a qual você presta serviço. Neste artigo vou abordar especialmente as profissões de desenvolvimento: desenvolvedor web, analista de desenvolvimento, programador, back-end, front-end, e qualquer outro nome que essa mesma tarefa possa ter.

A maioria das empresas leva em consideração mais sua experiência na área do que sua formação acadêmica, por isso o curso que você fez ou faz na faculdade não fará muita diferença para um desenvolvedor. Eu mesmo abandonei a faculdade de ADS, não me formei e sempre trabalhei na área. Não estou falando para você fazer o mesmo, mas não se prenda muito à faculdade — aprendemos bem mais por fora dela do que dentro.

<div class="callout callout-warn">
  <div class="callout-label">Atenção</div>
  Se você está entrando nesta área pelo retorno financeiro, tome muito cuidado. Pessoas que ganham bem são pessoas que gostam e exercem bem suas atividades. Entrar em qualquer área por dinheiro geralmente é um erro — fazer algo que não gosta pode desmotivar e frustrar até o ponto que você desista.
</div>

> *Escolha um trabalho que você ame e não terás que trabalhar um único dia em sua vida. — Confúcio*

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Front-end</h2></div>
</div>

O front-end é a parte do sistema web que o usuário final vê — a interface gráfica. É feita por um desenvolvedor front-end, com ou sem o apoio de um UX, ou por um fullstack.

Cabe ao front-ender os conhecimentos necessários para construir uma tela responsiva que leve a melhor experiência ao usuário sem consumir recursos demasiados do navegador, internet e computador de cada pessoa.

A stack básica do front-end é composta por três tecnologias obrigatórias:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">HTML</div>
    <div class="provider-detail">HyperText Markup Language — a linguagem universal dos navegadores. Estrutura o documento e o conteúdo. Sem ela não existe interface gráfica web.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">CSS</div>
    <div class="provider-detail">Cascade Style Sheets — define a apresentação visual: responsividade, animações, temas, grid e flexbox.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">JavaScript</div>
    <div class="provider-detail">Atualmente a única linguagem de script suportada por todos os navegadores. Manipula o DOM, cria interatividade e realiza requisições ao back-end.</div>
  </div>
</div>

Além da stack básica, um front deve conhecer pelo menos uma biblioteca JS e um framework de UI:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">React</div>
    <div class="provider-detail">Biblioteca JS mantida pelo Meta. Maior ecossistema e comunidade. Padrão de mercado em 2020.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Angular</div>
    <div class="provider-detail">Framework completo mantido pelo Google. Mais opinativo, curva de aprendizado maior.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Vue</div>
    <div class="provider-detail">Curva de aprendizado menor. Popular em projetos de porte médio.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">jQuery</div>
    <div class="provider-detail">Ainda muito usada em sistemas legados. Para novos projetos o JS nativo + CSS3 já cobre praticamente tudo que antes exigia jQuery.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Bootstrap</div>
    <div class="provider-detail">Framework CSS mais popular. Rápido para começar, grid system consolidado.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Materialize / Bulma / Foundation / Semantic</div>
    <div class="provider-detail">Alternativas ao Bootstrap com abordagens visuais e filosóficas diferentes.</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Diferenciais</div>
  Conhecer técnicas de UI/UX, usabilidade, SEO, paleta de cores, teste A/B, pré-processadores CSS (Sass, Less), arquitetura CSS (BEM), e os conceitos de SPA e PWA são diferenciais importantes para um front-ender.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Back-end</h2></div>
</div>

Back-end é a parte do sistema que realiza o processamento — onde ficam a lógica e as regras de negócio. É no back-end que ocorre a conexão com banco de dados, envio de e-mails, processamento de pagamentos e integração com outros sistemas. É a parte que o usuário não pode e não deve ver.

<div class="callout callout-warn">
  <div class="callout-label">Segurança</div>
  Tudo que está no front-end o usuário consegue alterar, intencionalmente ou não — criando brechas de segurança. Por isso é fundamental fazer validações no back-end mesmo que elas já existam no front-end. No front valide apenas para melhorar a experiência do usuário e evitar requisições desnecessárias.
</div>

Diferente do front-end que tem uma stack de 3 tecnologias obrigatórias, no back-end não existe padronização — praticamente qualquer linguagem pode ser usada. O que pode ser feito com uma pode ser feito com qualquer outra, mudando apenas o paradigma ou a implementação.

<div class="callout callout-warn">
  <div class="callout-label">Mito a combater</div>
  Não acreditem em nenhum vídeo, artigo ou comentário falando que linguagem X ou Y vai morrer — isso são pessoas tentando direcionar você para outra linguagem que preferem, ou pura ignorância do mercado.
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">PHP</div>
    <div class="provider-detail">Menor curva de aprendizado. Maioria das vagas de júnior no mercado. Muito usado em agências, e-commerces e sistemas de pequeno porte.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">JavaScript (Node.js / Deno)</div>
    <div class="provider-detail">O mesmo JS do front-end, agora no back. Funciona também no mobile e desktop. Grande volume de vagas e curva de aprendizado baixa.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Python</div>
    <div class="provider-detail">Fácil de aprender, forte em dados e ML. Menos vagas web para júnior comparado a PHP e JS.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">C# (.NET)</div>
    <div class="provider-detail">Dominante em grandes empresas, fintechs e sistemas corporativos. Curva de aprendizado maior.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Java</div>
    <div class="provider-detail">Padrão em bancos, indústria e enterprise. Verboso, mas extremamente maduro e estável.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Rust / Go / Elixir / Ruby / Kotlin / outros</div>
    <div class="provider-detail">Cada uma com seu nicho e paradigma. Menos vagas para iniciantes, mas crescimento acelerado em diferentes segmentos.</div>
  </div>
</div>

Partindo do princípio que você sabe zero de qualquer linguagem, você vai levar em média **6 meses a 2 anos** para estar apto a conseguir uma vaga. Você só precisa saber de **uma** linguagem para a vaga de back-end — diferente do front, que exige a stack completa (mas o front dá para aprender em 3 meses a 1 ano).

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Salários e mercado</h2></div>
</div>

As duas profissões pagam relativamente o mesmo. O que varia é o contexto:

<table class="compare-table">
  <thead><tr><th>Contexto</th><th>Tende a pagar mais para</th></tr></thead>
  <tbody>
    <tr><td>Agências de publicidade, e-commerce, marketing digital</td><td>Front-end (apelo visual maior)</td></tr>
    <tr><td>Sistemas corporativos (ERP, WMS, TMS, CRM, bancos)</td><td>Back-end (lógica e performance)</td></tr>
    <tr><td>Startups, SaaS</td><td>Fullstack ou equilibrado</td></tr>
  </tbody>
</table>

Lembrando que isso não é uma regra — é um padrão observado ao longo dos anos. Não existe garantia que esse cenário permaneça para sempre.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>O que estudar para começar</h2></div>
</div>

Para começar como desenvolvedor web — seja front-end, back-end ou fullstack — é importante conhecer a stack básica. Recomendo a seguinte ordem de aprendizagem:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">1. HTML</div>
    <div class="provider-detail">Funcionamento básico · Protocolo HTTP · Tags e atributos · UI e UX · Semântica · SEO</div>
    <div class="provider-price">3 a 4 semanas</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">2. CSS</div>
    <div class="provider-detail">Seletores · Atributos · Media queries · Pseudo classes · Grid system · Flexbox · BEM · Sass/Less</div>
    <div class="provider-price">4 a 8 semanas</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">3. JavaScript</div>
    <div class="provider-detail">DOM · Tipos primitivos · Variáveis e escopo · Condicionais e loops · Arrays e Objetos · JSON · Funções · Eventos · AJAX/fetch · Promises · WebSockets</div>
    <div class="provider-price">2 a 6 meses</div>
  </div>
</div>

<div class="conclusion">
  <h2>A barreira do primeiro emprego</h2>
  <p>O mercado é competitivo para quem está entrando — isso é real. Mas depois que você quebra a barreira do primeiro emprego, fica muito mais fácil. O que importa nessa fase não é o salário, é o aprendizado.</p>
  <p>Escolha a área que mais te atrai, estude com consistência, construa um portfólio com projetos reais e fuja de atalhos. Não existe caminho mágico.</p>
</div>
