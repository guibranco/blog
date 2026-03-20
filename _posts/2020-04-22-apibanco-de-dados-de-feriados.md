---
layout: post
title: "API/Banco de dados de feriados"
description: "Ter uma base de dados com os feriados da sua região ou país é uma necessidade cada vez mais comum nos mais variados tipos de sistemas, para aumentar a precisão nos dados e informações ao usuário..."
date: 2020-04-22
categories: [Coding]
tags: [api, banco-de-dados, base-de-dados, biblioteca, c, calendarific, feriados, github, holiday, holidayapi, holidays, integracao, library, pt-br, rust, sdk, sistema]
reading_time: 4
---

Ter uma base de dados com os feriados da sua região ou país é uma necessidade cada vez mais comum nos mais variados tipos de sistemas, para aumentar a precisão nos dados e informações ao usuário final. Seja um e-commerce para estimar uma data de entrega de pedidos, seja para calcular a data de vencimento e limite de pagamento de um boleto, um sistema que trabalha com jornadas/turnos e em feriados tem expediente diferente, ou mesmo uma simples agenda que precisa saber quando um dia não será um dia útil.

Manter esta base atualizada nem sempre é uma tarefa simples de se fazer, até porque, alguns feriados não são fixos, e variam ano a ano ou até mesmo de país para país.

Neste breve artigo vou apresentar dois serviços (API) que podem ser utilizados gratuitamente para consultar os feriados através de requisições HTTP.

## HolidayAPI

Primeiramente vou falar do **[HolidayAPI](https://holidayapi.com)**, um serviço simples e que permite até 10 mil chamadas por mês no plano grátis. Possui informações de feriados de 250 países, incluindo o Brasil e é possível obter as respostas em mais de 100 diferentes idiomas.

A utilização da API é bem simples, após efetuar o cadastro é gerada uma chave de autenticação que deve ser incluída na URL sempre que for feita uma chama a API.

A API possui os seguintes endpoints:

- /holidays - Retorna os feriados, mediante o ano e o país.
- /languages - Retorna os idiomas disponíveis para retorno dos dados.
- /countries - Lista os países disponíveis para pesquisa na API.
- /workday - Calcula o próximo dia útil a partir de uma data e uma quantidade de dias.
- /workdays - Calcula os dias úteis entre duas datas.

Caso queira ver a documentação completa, ela está disponível [nesta página](https://holidayapi.com/docs)

Atualmente existem bibliotecas da **HolidayAPI** nas mais variadas linguagens, dentre elas, algumas criadas pelo criador desta API e outras pela comunidade. A lista completa de bibliotecas disponíveis vocês podem ver no final da página de documentação da API.  
P.S: Duas delas, a de [C#](https://guilherme.stracini.com.br/GuiStracini.HolidayAPI/) e [Rust](https://guilherme.stracini.com.br/holiday-api-sdk-rs/) são de minha autoria :P   
  
 [![GuiStracini.HolidayAPI](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=GuiStracini.HolidayAPI&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/GuiStracini.HolidayAPI)  [![Holiday API Rust](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=holiday-api-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/holiday-api-sdk-rs)

No plano grátis, além de limitado a 10 mil requisições por mês, você só pode pesquisar feriados retroativos, isto é, que já passaram. Caso deseje pesquisar por feriados futuros, será necessário aderir a um dos planos pagos, que começam em cerca de U$ 16,60 por mês (cobrado anualmente, no valor de U$199,00).

## Calendarific

[**Calendarific**](https://calendarific.com/) é uma API de feriados que segue os mesmos moldes da **HolidayAPI.**

Possui 3 endpoints, e também usa uma chave (API key) via parâmetro de URL (query string)

- /holidays - Que retorna os feriados, mediante o ano e o país.
- /languages - Que retorna os idiomas disponíveis para retorno dos dados.
- /countries - Que lista os países disponíveis para pesquisa na API.

A diferença do **Calendarific** é que nele o plano grátis oferece apenas 1000 requisições mensais (fazendo uma requisição por dia, e armazenando os dados, daria no máximo 31 requisições por mês), e permite consultar os feriados futuros também, não só os retroativos. Atualmente a API disponibiliza a informação de 230 países e suas subdivisões no plano gratuito, em contra-partida, a **HolidayAPI** oferece dados de 250 países (e subdivisões, apenas em um dos planos pagos).

No momento da escrita deste artigo, a **Calendarific** disponibiliza apenas bibliotecas de integração nas linguagens: Golang, Ruby, Python, PHP e JS (NodeJS). Na [documentação oficial](https://calendarific.com/client-libraries) eles não informam a existência de bibliotecas criadas pela comunidade. Porém neste exato momento estou escrevendo as versões de [C#](https://guilherme.stracini.com.br/calendarific-sdk-dotnet/) e [Rust](https://guilherme.stracini.com.br/calendarific-sdk-rs/) das bibliotecas de consumo desta API e em breve estão disponíveis em meu perfil no [GitHub](https://github.com/GuiBranco).   
  
 [![Calendarific SDK .NET](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-dotnet&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco/calendarific-sdk-dotnet/)  [![Calendarific SDK Rust](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=guibranco&repo=calendarific-sdk-rs&show_owner=true&show_forks=false&show_issues=true)](https://github.com/guibranco//calendarific-sdk-rs)

Os planos pagos desta API, que permitem um consumo mensal ilimitado, custam a partir de U$10,00.