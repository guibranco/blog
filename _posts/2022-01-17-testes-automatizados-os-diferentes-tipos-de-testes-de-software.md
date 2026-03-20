---
layout: post
title: "Testes automatizados: Os diferentes tipos de testes de software"
description: "Guia objetivo sobre os diferentes tipos de testes automatizados — unitário, integração, E2E, carga, estresse e UAT — e quando aplicar cada um."
date: 2022-01-17
categories: [Coding, DevOps, Testing]
tags: [e2e-test, end-to-end-test, integration-test, load-test, stress-test, teste, testing, unit-test, uat-test, qualidade]
reading_time: 3
---

<p class="lead">Os testes automatizados são a base de qualquer estratégia sólida de qualidade de software. Cada tipo cobre uma dimensão diferente do sistema — entender qual usar em cada situação é fundamental para construir uma suíte de testes eficiente.</p>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Os tipos de teste</h2></div>
</div>

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">UT</div>
    <div class="simbox-header-text">
      <h4>Teste unitário (Unit test)</h4>
      <span>Testa a lógica</span>
    </div>
  </div>
  <div class="simbox-body">
    <p>Garante que o código faz o que deveria fazer em <strong>todos os cenários</strong>. Testa cada pedaço de código isoladamente e garante que todas as linhas são executadas e resultam no que era esperado. As dependências externas (APIs, banco de dados) são "mockadas" — simuladas — para isolar a unidade sendo testada.</p>
  </div>
</div>

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">IT</div>
    <div class="simbox-header-text">
      <h4>Teste de integração (Integration test)</h4>
      <span>Testa módulos e integrações reais</span>
    </div>
  </div>
  <div class="simbox-body">
    <p>Similar ao unit test, mas testa uma <strong>unidade maior</strong> — um conjunto de unidades que formam um módulo. Diferente do E2E, não testa um user case completo, mas um módulo lógico específico. No teste de integração, você <strong>realmente chama</strong> a dependência externa (API, banco de dados), desde que isso seja viável e não gere impacto financeiro ou de infraestrutura.</p>
  </div>
</div>

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">E2E</div>
    <div class="simbox-header-text">
      <h4>Teste fim a fim (End-to-End / E2E)</h4>
      <span>Testa user flows completos</span>
    </div>
  </div>
  <div class="simbox-body">
    <p>Garante que o sistema como um todo faz aquilo que era previsto para um determinado cenário. Testa <strong>todas as camadas</strong> da perspectiva do fluxo de um usuário (user flow / user case) — da interface ao banco de dados e de volta. É o tipo de teste mais próximo da experiência real do usuário.</p>
  </div>
</div>

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">LT</div>
    <div class="simbox-header-text">
      <h4>Teste de carga (Load test)</h4>
      <span>Testa a performance</span>
    </div>
  </div>
  <div class="simbox-body">
    <p>Garante que o código e a infraestrutura aguentam <strong>N vezes a carga normal</strong> para eventuais picos não planejados. Verifica como a aplicação e a infraestrutura (serviços, servidores, hardware) se comportam sob pressão.</p>
  </div>
</div>

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">ST</div>
    <div class="simbox-header-text">
      <h4>Teste de estresse (Stress test)</h4>
      <span>Testa a robustez</span>
    </div>
  </div>
  <div class="simbox-body">
    <p>Ajuda a determinar a <strong>carga máxima</strong> do que está sendo testado — até onde a aplicação aguenta antes de degradar ou falhar. Essencial para definir quando escalar verticalmente, horizontalmente, ou implementar mecanismos de limitação de taxa (rate limiting, circuit breaker).</p>
  </div>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Comparativo rápido</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Tipo</th><th>O que testa</th><th>Velocidade</th><th>Usa infra real?</th></tr>
  </thead>
  <tbody>
    <tr><td>Unit test</td><td>Lógica isolada</td><td>Muito rápido</td><td><span class="cross">✗</span> Mock</td></tr>
    <tr><td>Integration test</td><td>Módulos e integrações</td><td>Médio</td><td><span class="check">✓</span> Sim</td></tr>
    <tr><td>E2E test</td><td>User flows completos</td><td>Lento</td><td><span class="check">✓</span> Sim</td></tr>
    <tr><td>Load test</td><td>Performance sob carga</td><td>Variável</td><td><span class="check">✓</span> Sim</td></tr>
    <tr><td>Stress test</td><td>Limite máximo do sistema</td><td>Variável</td><td><span class="check">✓</span> Sim</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Sobre análise de performance</div>
  Além dos testes, problemas de performance podem ser diagnosticados com <strong>profilers de memória/CPU</strong> e ferramentas de <strong>APM</strong> (Application Performance Monitoring). Causas comuns: algoritmo ineficiente, gargalo em banco de dados, I/O lento, deadlock, ou simplesmente hardware insuficiente para a carga da aplicação.
</div>
