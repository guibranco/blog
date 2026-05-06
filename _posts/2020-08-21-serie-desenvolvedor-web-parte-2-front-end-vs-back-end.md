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

A maioria das empresas leva em consideração mais sua experiência na área do que sua formação acadêmica, por isso o curso que você fez ou faz na faculdade — sendo ele de TI ou área correlata — não fará muita diferença para um desenvolvedor. Eu mesmo abandonei a faculdade de ADS, não me formei e sempre trabalhei na área. Não estou falando para você fazer o mesmo, mas não se prenda muito à faculdade — aprendemos bem mais por fora dela do que dentro, afinal a faculdade não é só para desenvolvedores e precisa preparar o profissional para a vida e para outras profissões também.

> *Se você está entrando nesta área pelo retorno financeiro, tome muito cuidado. Pessoas que ganham bem são pessoas que gostam e exercem bem suas atividades. Entrar em qualquer área por dinheiro geralmente é um erro — fazer algo que não gosta pode desmotivar e frustrar até o ponto que você desista.*
>
> *Escolha um trabalho que você ame e não terás que trabalhar um único dia em sua vida. — Confúcio*

<div class="divider">· · ·</div>

## O que é front-end e back-end?

No desenvolvimento web separamos as partes do sistema em back-end, front-end e infraestrutura. Além de outras partes que podem ou não existir conforme o tipo e porte do sistema/empresa.

### Front-end

O front-end é a parte do sistema web que o usuário final vê — a interface gráfica. É feita por um desenvolvedor front-end, com ou sem o apoio de um UX, ou por um fullstack.

Cabe ao "front ender" os conhecimentos necessários para construir uma tela responsiva que leve a melhor experiência ao usuário sem consumir recursos demasiados do navegador, internet e computador de cada pessoa.

Geralmente um front-end domina a stack básica da web: HTML, CSS e JS. Grande parte acaba tendo conhecimento de uma linguagem de back-end também — principalmente freelancers e fullstacks — geralmente PHP ou o próprio JS via Node.js ou Deno. Não é obrigatório, porém conhecimento nunca é demais.

Além da stack básica, um front deve conhecer bibliotecas e frameworks. Recomenda-se saber pelo menos uma biblioteca JS e um framework de UI.

**Bibliotecas JS populares (2020):**

- React
- Angular
- Vue
- jQuery (ainda usada em sistemas legados; para novos projetos o JS nativo + CSS3 já fazem praticamente tudo que antes exigia jQuery)

**Frameworks CSS / UI Kits:**

- Bootstrap
- Materialize
- Bulma
- Foundation
- Semantic

Além desses, conhecer técnicas de UI/UX, usabilidade, SEO, paleta de cores, teste A/B, pré-processadores CSS (Sass, Less), arquitetura CSS (BEM), conceitos de SPA e PWA são diferenciais importantes.

### Back-end

Back-end é a parte do sistema que realiza o processamento — onde ficam a lógica e as regras de negócio. É no back-end que ocorre a conexão com banco de dados, envio de e-mails, processamento de pagamentos, envio de dados para outros sistemas. É a parte que o usuário não pode e não deve ver.

Lembrando: **tudo que está no front-end o usuário consegue alterar**, intencionalmente ou não, criando brechas de segurança. Por isso é importante fazer validações no back-end mesmo que elas já existam no front-end. No front valide apenas para melhorar a experiência do usuário e evitar requisições desnecessárias.

Para trabalhar com back-end é ideal conhecer o básico de front-end — saber como o front se comporta e vai consumir seu código é importante para criar a melhor API possível.

Diferente do front-end que tem uma stack de 3 tecnologias obrigatórias (HTML, CSS, JS), no back-end não existe padronização: praticamente qualquer linguagem de programação pode ser usada. Basicamente o que pode ser feito com uma linguagem pode ser feito com qualquer outra, mudando apenas o paradigma ou a implementação.

**Não acreditem em nenhum vídeo, artigo ou comentário falando que linguagem X ou Y vai morrer — isso são pessoas tentando direcionar você para outra linguagem que preferem, ou pura ignorância do mercado.**

Algumas das linguagens disponíveis: PHP, JS (Node.js / Deno), C#, Java, Rust, Python, Ruby, Elixir, Go, Kotlin, Clojure, F#, VB.NET, Erlang, C++, C, e muitas outras.

Partindo do princípio que você sabe zero de qualquer linguagem de programação, você vai levar em média de **6 meses a 2 anos** para estar apto a conseguir uma vaga com alguma delas. Você só precisa saber de **uma** delas para a vaga de back-end (diferente do front, que exige a stack completa — mas a stack do front dá para aprender em 3 meses a 1 ano).

PHP e JS (via [Node.js](https://nodejs.org/en){:target="_blank"} ou [Deno](https://deno.com/){:target="_blank"}) são os que têm a menor curva de aprendizado e a maior quantidade de vagas no mercado. Java e C# são mais usados no mundo corporativo — grandes empresas, e-commerces, bancos, financeiras e indústria.

### Salário

As duas profissões pagam relativamente o mesmo. O que varia é o contexto:

- **Agência de publicidade ou e-commerce** — o apelo visual é maior, você provavelmente encontrará melhores remunerações para front-end.
- **Sistemas corporativos** (ERP, WMS, TMS, CRM, sistemas bancários) — mais oferta e melhores salários para back-end.

Isso não é uma regra, é um padrão observado ao longo dos anos — não existe garantia que esse cenário permaneça para sempre.

<div class="divider">· · ·</div>

## O que estudar para começar?

Para começar como desenvolvedor web — seja front-end, back-end ou fullstack — é importante conhecer a stack básica da web: HTML, CSS e JS.

**Ordem de aprendizagem recomendada:**

**1. HTML** — *HyperText Markup Language* — A linguagem universal dos navegadores. Sem ela você não cria um sistema web com interface gráfica.
- Funcionamento básico e protocolo HTTP
- Tags e atributos
- O que é UI e UX
- Semântica
- SEO

**2. CSS** — *Cascade Style Sheets* — As definições de estilo que permitem personalizar a aparência das tags HTML.
- Seletores e atributos
- Media queries
- Pseudo classes e pseudo atributos
- Grid system e Flexbox
- BEM (Block Element Modifier)
- Pré-compiladores (Sass, Less)

**3. JS** — *JavaScript* — Atualmente a única linguagem de script suportada por todos os navegadores que seguem o padrão de mercado (não confunda JavaScript com Java — são coisas totalmente diferentes!). O JS é responsável por dar vida à página no lado do cliente e realizar interações que o CSS sozinho não é capaz.
- DOM — Document Object Model
- Tipos de dados primitivos (string, integer, boolean)
- Variáveis e escopo (`var`, `const`, `let`)
- Estruturas condicionais (`if`, `else`) e de repetição (`for`, `while`)
- Arrays e Objetos
- JSON (JavaScript Object Notation)
- Funções, Prototype e Eventos
- Requisições assíncronas — AJAX (`xmlhttp` & `fetch`)
- Promises
- Cookies, Local Storage e Session Storage
- WebSockets
