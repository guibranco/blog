---
layout: post
title: "Testes automatizados: Os diferentes tipos de testes de software"
description: "Conheça os diferentes tipos de testes automatizados — unitário, carga, estresse, E2E e integração — e entenda como cada um contribui para a qualidade e performance da sua aplicação."
date: 2022-01-17
categories: [Coding, DevOps, Testing]
tags: [testes, testing, unit-test, load-test, stress-test, e2e-test, end-to-end-test, integration-test, qualidade, performance, desenvolvimento]
reading_time: 3
image: /assets/img/posts/testing.jpg
---

<p class="lead">Veja neste artigo os diferentes tipos de testes automatizados que existem.</p>

<div class="divider">· · ·</div>

**Teste unitário (unit test)** → garantir que o código faz o que deveria fazer em todos os cenários. Testa cada pedaço de código e garante (ou deveria garantir) que todas as linhas são executadas e resultam naquilo que era esperado. Basicamente testa a lógica.

**Teste de carga (load test)** → garantir que o código e possivelmente a infraestrutura aguentam N vezes a carga normal para eventuais picos não planejados, e ver como a aplicação (código) e a infraestrutura (serviços, servidores, hardware) se comportam nessa situação. Basicamente testa a performance.

**Teste de estresse (stress test)** → ajuda a determinar a carga máxima do que está sendo testado, para determinar quando deve ser escalado vertical ou horizontalmente, ou mesmo criado um mecanismo de limitação dentro das diversas arquiteturas, lógicas e ferramentas disponíveis. Basicamente testa a robustez.

**Teste fim a fim (end-to-end test, ou E2E test** — a pronúncia de "two" e "to" é parecida, por isso se usa 2 no lugar de "to" e 4 no lugar de "for" geralmente) → garantir que o sistema como um todo (diferente do unit test) faz aquilo que era previsto, dado um determinado cenário. Testa todas as camadas da perspectiva do fluxo de um cenário. Basicamente testa os *user flows* ou *user cases*.

**Teste de integração (integration test)** → similar ao unit test, os testes de integração testam uma unidade maior — um conjunto de unidades que formam um módulo. Diferente de um E2E, que testa geralmente um *user case/scenario*, o integration test testa um módulo lógico da aplicação, como por exemplo uma integração com banco de dados ou API (REST, SOAP, etc), geralmente para garantir que a outra ponta (geralmente não criada por você) está funcionando de acordo com o esperado. Supondo que você tenha uma API de CEPs: no teste unitário você iria *mockar* as chamadas e respostas a essa API, testando seu código sem de fato chamá-la. Já no teste de integração, você iria realmente chamar a API, desde que isso seja possível e não resulte em impacto financeiro ou de infraestrutura.

<div class="divider">· · ·</div>

Isso resume a parte de testes automatizados da sua aplicação — eles te dão métricas para melhorar pontos da aplicação, entre eles, performance.

Além dos testes, uma forma de analisar performance é usar profilers de memória/CPU na aplicação ou ferramentas de APM, realizando o rastreamento de onde os picos de uso ocorrem, sob quais circunstâncias e momentos.

Alguns problemas de performance podem ocorrer por motivos variados: problema no algoritmo implementado, falta de *know-how* do desenvolvedor, gargalo em um fluxo específico, gargalo em uma dependência (banco de dados, rede, I/O, deadlock, etc) ou insuficiência de hardware para a carga da aplicação. Para determinar exatamente qual o ponto do problema e qual a solução, é necessário entender todo o contexto da aplicação e de suas dependências, e analisar os fluxos depurando ou com apoio de ferramentas como profilers e APM.
