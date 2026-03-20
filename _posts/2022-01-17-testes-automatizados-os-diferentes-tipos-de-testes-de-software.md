---
layout: post
title: "Testes automatizados: Os diferentes tipos de testes de software"
description: "Veja neste artigo os diferentes tipos de testes automatizados que existem. Teste unitário (unit test) - garantir que o código faz o que deveria fazer em todos os cenários. Testa cada pedaço de..."
date: 2022-01-17
categories: [Coding, DevOps, Testing]
tags: [desenvolvimento, e2e-test, end-to-end-test, integration-test, load-test, performance-test, pt-br, stress-test, teste, testing, uat-test, unit-test]
reading_time: 3
---

Veja neste artigo os diferentes tipos de testes automatizados que existem.

**Teste unitário (unit test)** -> garantir que o código faz o que deveria fazer em todos os cenários. Testa cada pedaço de código, e garante (ou deveria garantir) que todas as linhas são executadas (testadas) e resultam naquilo que era esperado. Basicamente testa a lógica.

**Teste de carga (load test)** -> garantir que o código e possivelmente a infraestrutura aguentam N vezes a carga normal para eventuais picos não planejados e ver como a aplicação (código) e a infraestrutura (serviços, servidores, hardware) se comportam nessa situação. Basicamente testa a performance.

**Testes de estresse (stress test)** -> ajuda a determinar a carga máxima do que está sendo testado, para determinar quando deve ser escalado vertical ou horizontalmente, ou mesmo criado um mecanismo de limitação dentro das diversas arquiteturas, lógicas e ferramentas disponíveis. Basicamente testa a robustez.

**Teste fim a fim** (**end-to-end test, ou E2E test** - a pronuncia de "two" e "to" é parecida, por isso se usa 2 no lugar de "to" e 4 no lugar de "for" geralmente) -> garantir que o sistema como um todo (diferente do unit test) faz aquilo que era previsto, dado um determinado cenário. Neste caso, se testa todas as camadas, da perspectiva do fluxo de um cenário. Basicamente testa os "user flows" ou "user cases".

**Teste de integração (integration test)** -> similar ao unit test, os testes de integração testam uma unidade maior, ou seja, um conjunto de unidades, que formam um módulo, diferente de um E2E, que testa geralmente um user case/scenario, o integration test testa um módulo lógico da aplicação por exemplo, uma integração com banco de dados, ou API (REST, SOAP, etc), geralmente para garantir que a outra ponta (geralmente não criada por você) está funcionando de acordo com o esperado por você.Supondo que você tenha uma API de CEPs por exemplo, no teste unitário você iria "mockar" as chamadas e resposta a essa API, de forma que você iria testar seu código que chama a API mas sem de fato chamar a API, ja no teste de integração, você iria realmente chamar a API, desde que isso seja possível e não resulte em impacto financeiro ou de infraestrutura).

Isso resume a parte de testes automatizados da sua aplicação e que de certa parte, te dão métricas para melhorar certos pontos da sua aplicação, entre eles, performance.Fora isso, e acho que de fato respondendo sua pergunta, uma forma de analisar performance, é usando profilers de memória/CPU na aplicação ou mesmo ferramentas de APM e realizando o trace/rastreamento de onde os picos de uso ocorrem, sob quais circunstancias e momentos.

Alguns problemas de performance, podem ocorrer devido aos mais variados tipos como problema no algoritmo implementado, falta de expertise/know how do desenvolvedor em adotar um determinado procedimento, gargalo em um fluxo especifico, gargalo em uma dependência (banco de dados, rede, I/O, deadlock, etc), insuficiencia de hardware para a carga da aplicação. Para você determinar exatamente qual o ponto de problema e qual solução, você precisa entender todo o contexto da aplicação e do que ela usa ("dependências") e analisar seus fluxos, depurando (debugando) ou com apoio de ferramentas como profilers e APM (ai qual e como vai depender de N fatores, como cultura da empresa, tipo de problema, tempo para solucionar, etc, etc, etc)