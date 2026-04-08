---
layout: post
title: "RabbitMQ gratuito: Potencialize sua arquitetura de mensageria sem custos"
description: "Como usar RabbitMQ ou LavinMQ de graça com o CloudAMQP — sem cartão de crédito, sem servidor dedicado, ideal para projetos pessoais, estudos e pequenos projetos comerciais."
date: 2024-02-21
categories: [Coding]
tags: [rabbitmq, lavinmq, cloudamqp, mensageria, message-broker, php, infraestrutura, iaas, filas, arquitetura]
reading_time: 4
image: /assets/img/posts/rabbitmq-server.jpg
---

<p class="lead">Descubra como tirar proveito do poder da mensageria com o RabbitMQ gratuitamente. Neste artigo explico como usar o RabbitMQ ou LavinMQ de graça, caso você não possua acesso a um servidor dedicado ou VPS para instalação.</p>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap">
    <h2>CloudAMQP</h2>
  </div>
</div>

O [CloudAMQP](https://www.cloudamqp.com/){:target="_blank"} é um provedor de infraestrutura como serviço (**IaaS** — *Infrastructure as a Service*) que descobri em janeiro de 2024. Ele oferece instâncias gerenciadas de dois message brokers: **RabbitMQ** e **LavinMQ**.

Se você precisar de uma ou mais instâncias do [RabbitMQ](https://www.rabbitmq.com/){:target="_blank"} — ou quiser conhecer o [LavinMQ](https://lavinmq.com/){:target="_blank"} (projeto interessante, ainda não testei na prática) — o CloudAMQP oferece um **plano gratuito** que permite usar um dos serviços de filas em projetos pessoais, de estudo ou mesmo em pequenos projetos comerciais.

Para usar, basta acessar [cloudamqp.com](https://www.cloudamqp.com/){:target="_blank"} e criar uma conta — manualmente, com sua conta do GitHub ou com o Google. Até a presente data, **não é obrigatório cadastrar cartão de crédito**. Ele será solicitado, mas não é necessário informar (a menos que deseje um plano pago).

[![Captura de tela da página de criação de instâncias do CloudAMQP mostrando o plano gratuito selecionado e o aviso de que não há cartão de crédito associado](https://blog.guilhermebranco.com.br/wp-content/uploads/2024/02/CloudAMQP-Create-free-instance-1024x535.png)](https://www.cloudamqp.com/){:target="_blank"}

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap">
    <h2>Comparativo dos planos gratuitos</h2>
  </div>
</div>

<table class="compare-table">
  <thead>
    <tr>
      <th>Limite</th>
      <th>RabbitMQ</th>
      <th>LavinMQ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Conexões simultâneas</td>
      <td>20</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Filas</td>
      <td>150</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Mensagens por mês</td>
      <td>1 milhão</td>
      <td>2 milhões</td>
    </tr>
    <tr>
      <td>Mensagens não consumidas</td>
      <td>10 mil</td>
      <td>20 mil</td>
    </tr>
    <tr>
      <td>TTL de filas sem consumo</td>
      <td>28 dias</td>
      <td>28 dias</td>
    </tr>
  </tbody>
</table>

O LavinMQ oferece exatamente o dobro de recursos em todos os limites. Se o projeto crescer e o plano gratuito do RabbitMQ não atender mais, migrar para o LavinMQ é o próximo passo natural — ainda de graça.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap">
    <h2>Um exemplo real de uso</h2>
  </div>
</div>

Para ilustrar o quanto o plano gratuito do RabbitMQ aguenta na prática, compartilho meu próprio cenário: tenho um projeto em **PHP rodando em hospedagem compartilhada** (sem RabbitMQ instalado) que publica e consome mensagens via CloudAMQP.

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">MQ</div>
    <div class="simbox-header-text">
      <h4>Carga real do projeto em produção</h4>
      <span>PHP · hospedagem compartilhada · CloudAMQP free</span>
    </div>
  </div>
  <div class="simbox-body">
    <div class="simbox-specs">
      <div class="spec-item"><div class="spec-label">Consumers 24/7</div><div class="spec-value">2</div></div>
      <div class="spec-item"><div class="spec-label">Publishers (pico)</div><div class="spec-value">0 – 8</div></div>
      <div class="spec-item"><div class="spec-label">Conexões no pico</div><div class="spec-value">~10</div></div>
      <div class="spec-item"><div class="spec-label">Mensagens/dia</div><div class="spec-value">5k – 8k</div></div>
      <div class="spec-item"><div class="spec-label">Mensagens/mês</div><div class="spec-value">150k – 240k</div></div>
      <div class="spec-item"><div class="spec-label">Uso do limite</div><div class="spec-value">&lt; 25%</div></div>
    </div>
    <p style="font-size:14px;color:#5a534a;line-height:1.65;">150k–240k mensagens mensais representam menos de um quarto do limite de 1 milhão oferecido no plano gratuito. Para um projeto de hospedagem compartilhada sem RabbitMQ instalado, é uma solução perfeita.</p>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Dica</div>
  Publishers são as conexões que recebem requisições HTTP e enfileiram mensagens para processamento assíncrono pelos consumers. Em hospedagens compartilhadas onde você não controla o servidor, o CloudAMQP resolve o problema de não ter um broker instalado localmente — sem configuração, sem manutenção.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap">
    <h2>Links úteis</h2>
  </div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.cloudamqp.com/" target="_blank">CloudAMQP</a></div>
    <div class="provider-detail">Site principal do provedor. Cadastro gratuito, sem cartão.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.cloudamqp.com/docs/index.html" target="_blank">Primeiros passos</a></div>
    <div class="provider-detail">Documentação oficial com guias de início rápido.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.cloudamqp.com/plans.html" target="_blank">Planos</a></div>
    <div class="provider-detail">Comparativo completo entre plano gratuito e pagos.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.cloudamqp.com/docs/rabbitmq-server.html" target="_blank">Docs RabbitMQ</a></div>
    <div class="provider-detail">Documentação específica do RabbitMQ no CloudAMQP.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.cloudamqp.com/docs/lavinmq-server.html" target="_blank">Docs LavinMQ</a></div>
    <div class="provider-detail">Documentação específica do LavinMQ no CloudAMQP.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.rabbitmq.com/" target="_blank">RabbitMQ oficial</a></div>
    <div class="provider-detail">Site oficial do RabbitMQ com documentação completa.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://lavinmq.com/" target="_blank">LavinMQ oficial</a></div>
    <div class="provider-detail">Site oficial do LavinMQ com docs e benchmarks.</div>
  </div>
</div>

<div class="conclusion">
  <h2>Vale a pena?</h2>
  <p>Para projetos pessoais, estudos ou aplicações de baixo volume: <strong>sim, sem dúvida</strong>. Você tem acesso a um message broker gerenciado, sem servidor para configurar, sem custo e sem cartão de crédito.</p>
  <p>O limite de 1 milhão de mensagens por mês do RabbitMQ gratuito é generoso o suficiente para cobrir a maioria dos cenários de desenvolvimento e projetos pequenos em produção. Quando crescer, o LavinMQ dobra esses limites — também de graça.</p>
</div>
