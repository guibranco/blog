---
layout: post
title: "API/Banco de dados de feriados"
description: "Conheça dois serviços gratuitos para consultar feriados via HTTP — HolidayAPI e Calendarific — e as bibliotecas open source em C# e Rust criadas para integrá-los."
date: 2020-04-22
categories: [Coding]
tags: [api, banco-de-dados, calendarific, feriados, github, holidayapi, integracao, library, rust, sdk]
reading_time: 4
---

<p class="lead">Manter uma base atualizada com os feriados da sua região é uma necessidade cada vez mais comum — de e-commerces que estimam datas de entrega a sistemas de folha de pagamento que calculam dias úteis. Neste artigo apresento dois serviços que resolvem esse problema gratuitamente.</p>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>HolidayAPI</h2></div>
</div>

O [HolidayAPI](https://holidayapi.com){:target="_blank"} permite até **10 mil chamadas por mês** no plano grátis, cobre 250 países e retorna respostas em mais de 100 idiomas. Após o cadastro, é gerada uma chave de autenticação incluída na URL de cada requisição.

<div class="providers-grid">
  <div class="provider-card"><div class="provider-name"><code>/holidays</code></div><div class="provider-detail">Retorna os feriados mediante o ano e o país informados.</div></div>
  <div class="provider-card"><div class="provider-name"><code>/languages</code></div><div class="provider-detail">Retorna os idiomas disponíveis para retorno dos dados.</div></div>
  <div class="provider-card"><div class="provider-name"><code>/countries</code></div><div class="provider-detail">Lista os países disponíveis para pesquisa na API.</div></div>
  <div class="provider-card"><div class="provider-name"><code>/workday</code></div><div class="provider-detail">Calcula o próximo dia útil a partir de uma data e quantidade de dias.</div></div>
  <div class="provider-card"><div class="provider-name"><code>/workdays</code></div><div class="provider-detail">Calcula os dias úteis entre duas datas.</div></div>
</div>

Documentação em [holidayapi.com/docs](https://holidayapi.com/docs){:target="_blank"}. Duas das bibliotecas disponíveis são de minha autoria:

[![GuiStracini.HolidayAPI](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=GuiStracini.HolidayAPI&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/GuiStracini.HolidayAPI){:target="_blank"}
[![Holiday API Rust SDK](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=holiday-api-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/holiday-api-sdk-rs){:target="_blank"}

<div class="callout callout-warn">
  <div class="callout-label">Limitação do plano grátis</div>
  No plano gratuito você só pode pesquisar feriados <strong>retroativos</strong>. Para consultar feriados futuros, é necessário um plano pago a partir de US$16,60/mês.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Calendarific</h2></div>
</div>

O [Calendarific](https://calendarific.com/){:target="_blank"} segue os mesmos moldes da HolidayAPI, com autenticação via API key na query string.

<table class="compare-table">
  <thead><tr><th>Característica</th><th>HolidayAPI</th><th>Calendarific</th></tr></thead>
  <tbody>
    <tr><td>Requisições/mês (grátis)</td><td>10.000</td><td>1.000</td></tr>
    <tr><td>Países cobertos</td><td>250</td><td>230</td></tr>
    <tr><td>Feriados futuros (grátis)</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Plano pago a partir de</td><td>US$ 16,60/mês</td><td>US$ 10,00/mês</td></tr>
  </tbody>
</table>

SDKs em C# e Rust para o Calendarific também são de minha autoria:

[![Calendarific SDK .NET](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-dotnet&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/calendarific-sdk-dotnet/){:target="_blank"}
[![Calendarific SDK Rust](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/calendarific-sdk-rs){:target="_blank"}

<div class="conclusion">
  <h2>Qual escolher?</h2>
  <p>Para <strong>volume alto</strong> de requisições gratuitas: HolidayAPI (10× mais). Para <strong>feriados futuros sem custo</strong>: Calendarific é a única opção gratuita.</p>
</div>
