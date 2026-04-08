---
layout: post
title: "API/Banco de dados de feriados"
description: "Conheça dois serviços gratuitos para consultar feriados via HTTP — HolidayAPI e Calendarific — incluindo endpoints disponíveis, limitações do plano grátis e SDKs em C# e Rust."
date: 2020-04-22
categories: [Coding]
tags: [api, feriados, holidayapi, calendarific, sdk, csharp, rust, integracao, banco-de-dados, library]
reading_time: 4
image: /assets/img/posts/calendar.jpg
---

<p class="lead">Ter uma base de dados com os feriados da sua região ou país é uma necessidade cada vez mais comum nos mais variados tipos de sistemas, para aumentar a precisão nos dados e informações ao usuário final. Seja um e-commerce para estimar uma data de entrega de pedidos, seja para calcular a data de vencimento e limite de pagamento de um boleto, um sistema que trabalha com jornadas/turnos e em feriados tem expediente diferente, ou mesmo uma simples agenda que precisa saber quando um dia não será um dia útil.</p>

Manter esta base atualizada nem sempre é uma tarefa simples de se fazer, até porque alguns feriados não são fixos e variam ano a ano ou até mesmo de país para país.

Neste breve artigo vou apresentar dois serviços (API) que podem ser utilizados gratuitamente para consultar os feriados através de requisições HTTP.

<div class="divider">· · ·</div>

## HolidayAPI

O [**HolidayAPI**](https://holidayapi.com){:target="_blank"} é um serviço simples que permite até **10 mil chamadas por mês** no plano grátis. Possui informações de feriados de 250 países, incluindo o Brasil, e é possível obter as respostas em mais de 100 diferentes idiomas.

A utilização da API é bem simples: após efetuar o cadastro é gerada uma chave de autenticação que deve ser incluída na URL sempre que for feita uma chamada à API.

A API possui os seguintes endpoints:

- `/holidays` — Retorna os feriados, mediante o ano e o país.
- `/languages` — Retorna os idiomas disponíveis para retorno dos dados.
- `/countries` — Lista os países disponíveis para pesquisa na API.
- `/workday` — Calcula o próximo dia útil a partir de uma data e uma quantidade de dias.
- `/workdays` — Calcula os dias úteis entre duas datas.

A documentação completa está disponível em [holidayapi.com/docs](https://holidayapi.com/docs){:target="_blank"}.

Atualmente existem bibliotecas da HolidayAPI nas mais variadas linguagens — algumas criadas pelo autor da API e outras pela comunidade. A lista completa pode ser vista no final da página de documentação.

*P.S: Duas delas, a de [C#](https://guilherme.stracini.com.br/GuiStracini.HolidayAPI/){:target="_blank"} e a de [Rust](https://guilherme.stracini.com.br/holiday-api-sdk-rs/){:target="_blank"}, são de minha autoria. :P*

[![GuiStracini.HolidayAPI](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=GuiStracini.HolidayAPI&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/GuiStracini.HolidayAPI){:target="_blank"} [![Holiday API Rust SDK](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=holiday-api-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/holiday-api-sdk-rs){:target="_blank"}

No plano grátis, além de limitado a 10 mil requisições por mês, você só pode pesquisar feriados **retroativos**, isto é, que já passaram. Para pesquisar feriados futuros, é necessário aderir a um dos planos pagos, que começam em cerca de US$ 16,60 por mês (cobrado anualmente, no valor de US$ 199,00).

<div class="divider">· · ·</div>

## Calendarific

O [**Calendarific**](https://calendarific.com/){:target="_blank"} é uma API de feriados que segue os mesmos moldes da HolidayAPI.

Possui 3 endpoints e também usa uma chave (API key) via parâmetro de URL (query string):

- `/holidays` — Retorna os feriados, mediante o ano e o país.
- `/languages` — Retorna os idiomas disponíveis para retorno dos dados.
- `/countries` — Lista os países disponíveis para pesquisa na API.

A diferença do Calendarific é que no plano grátis são oferecidas apenas **1.000 requisições mensais**, mas ele permite consultar os feriados **futuros** também, não só os retroativos. A API disponibiliza informações de 230 países e suas subdivisões no plano gratuito — em contrapartida, a HolidayAPI oferece dados de 250 países (subdivisões apenas em planos pagos).

No momento da escrita deste artigo, a Calendarific disponibiliza bibliotecas de integração oficiais nas linguagens: Golang, Ruby, Python, PHP e JS (Node.js). A [documentação oficial](https://calendarific.com/client-libraries){:target="_blank"} não informa a existência de bibliotecas criadas pela comunidade. Porém estou escrevendo as versões de [C#](https://guilherme.stracini.com.br/calendarific-sdk-dotnet/){:target="_blank"} e [Rust](https://guilherme.stracini.com.br/calendarific-sdk-rs/){:target="_blank"} e em breve estarão disponíveis no meu [GitHub](https://github.com/GuiBranco){:target="_blank"}.

[![Calendarific SDK .NET](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-dotnet&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/calendarific-sdk-dotnet/){:target="_blank"} [![Calendarific SDK Rust](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/calendarific-sdk-rs){:target="_blank"}

Os planos pagos desta API, que permitem um consumo mensal ilimitado, custam a partir de US$ 10,00.
