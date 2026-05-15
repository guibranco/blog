---
layout: post
title: "Quais testes são de responsabilidade do desenvolvedor e quais são do QA?"
description: "Entenda a divisão de responsabilidades entre desenvolvedores e QAs nos testes de software — unit test, integration test e load test versus E2E e UAT — e a diferença entre caixa branca e caixa preta."
date: 2026-05-15
categories: [Coding, Testing]
tags: [dev, developer, desenvolvedor, qa, quality-assurance, automation, automation-engineer, software-engineer, testes, tests, user-acceptance, testing, unit-test, integration-test, load-test, e2e-test, uat, qa, qualidade, white-box, end-to-end, black-box, desenvolvedor, pirâmide-de-testes]
reading_time: 6
image: /assets/img/posts/dev-vs-qa-testes.svg
---

<p class="lead">Uma dúvida muito comum entre desenvolvedores e times de QA é: quem é responsável por escrever quais testes? A resposta passa por entender dois conceitos fundamentais — caixa branca e caixa preta — e como cada papel no time se relaciona com eles.</p>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Caixa branca vs Caixa preta</h2></div>
</div>

Antes de falar sobre quem testa o quê, é preciso entender a diferença entre os dois modelos de teste:

**White box (Caixa branca)** — o testador conhece e tem acesso ao código interno da aplicação. Testa a lógica, os caminhos de execução, as condições e os dados internos. É o modelo natural para quem escreveu o código, porque só quem conhece a implementação sabe exatamente quais cenários internos precisam ser cobertos.

**Black box (Caixa preta)** — o testador não conhece (e não precisa conhecer) o código interno. Testa apenas o comportamento externo da aplicação: dado uma entrada, verifica se a saída é a esperada. Simula a perspectiva do usuário final.

<div class="callout callout-tip">
  <div class="callout-label">Importante — não é uma regra exclusiva</div>
  O desenvolvedor pode escrever testes tanto de caixa branca quanto de caixa preta. Um unit test pode ser escrito como caixa preta — testando apenas a interface pública de uma função sem se importar com a implementação interna. O QA também pode escrever unit tests em caixa preta em algumas situações. A divisão mais comum no mercado é por conveniência e contexto, não por restrição técnica.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Testes de responsabilidade do desenvolvedor</h2></div>
</div>

O desenvolvedor é o único que conhece profundamente o código que escreveu — cada condição, cada caminho possível de execução, cada dependência. Por isso, cabe a ele escrever os testes que verificam a lógica interna. Isso não significa, porém, que o desenvolvedor está restrito à caixa branca — ele também pode (e deve) escrever testes de unidade no modelo caixa preta, testando apenas a interface pública de um método sem se importar com os detalhes de implementação internos.

### Unit Test (Teste unitário) — White Box ou Black Box

Testa o menor pedaço de código isoladamente — uma função, um método, uma classe. As dependências externas (banco de dados, APIs, serviços externos) são substituídas por *mocks* ou *stubs*, garantindo que o teste valide apenas aquela unidade específica.

- **White box:** o dev conhece a implementação e escreve cenários para cobrir cada ramificação interna, cada condição e cada caminho de execução.
- **Black box:** o dev (ou o QA) testa apenas a interface pública — dado esta entrada, espero esta saída — sem se importar com como o código chegou lá. É uma forma mais resiliente a refatorações.

**Por que o dev lidera?** Porque é quem tem contexto para escrever os dois tipos com profundidade — tanto os cenários de cobertura interna quanto os de comportamento externo da unidade.

**Características:** muito rápidos, altíssimo volume, executados a cada build. Formam a base da pirâmide de testes.

### Integration Test (Teste de integração)

Testa a comunicação entre dois ou mais módulos ou sistemas — por exemplo, a integração do serviço com o banco de dados, com uma API externa ou com uma fila de mensagens. Diferente do unit test, aqui a dependência real é chamada (quando isso é viável e sem impacto financeiro ou de infraestrutura).

**Por que é do dev?** Porque requer conhecimento da implementação de ambos os lados da integração — saber qual contrato é esperado, quais erros podem ocorrer e como o sistema deve se comportar em cada cenário.

**Características:** mais lentos que unit tests, menor volume, verificam que os módulos funcionam corretamente em conjunto.

### Load Test (Teste de carga)

Verifica se o código e a infraestrutura aguentam N vezes a carga normal — simulando picos de acesso para identificar gargalos de performance antes que cheguem ao usuário em produção.

**Por que é do dev?** Porque envolve entender onde a aplicação pode ter gargalos técnicos — queries lentas, conexões esgotadas, memória insuficiente — e requer conhecimento da arquitetura interna para interpretar os resultados.

**Características:** executados em ambientes que simulam produção, geralmente em ciclos de release ou após mudanças arquiteturais significativas.

<div class="callout callout-tip">
  <div class="callout-label">Colaboração entre dev e QA</div>
  O fato de o desenvolvedor liderar esses testes não significa que o QA não participa. Em times maduros, QA e dev colaboram na definição dos cenários desde o início — o QA pode inclusive escrever unit tests de caixa preta para validar contratos de API ou comportamentos esperados, enquanto o dev foca nos cenários de cobertura interna.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Testes de responsabilidade do QA</h2></div>
</div>

O QA (Quality Assurance) tem um papel complementar ao do desenvolvedor: validar que o sistema como um todo funciona corretamente do ponto de vista do usuário, sem se preocupar com os detalhes de implementação. O QA pensa em termos de fluxos, comportamentos e regras de negócio — não em funções e classes.

Isso não significa que o desenvolvedor não pode escrever E2E ou participar de UAT. Em times menores ou com práticas mais avançadas de engenharia, o próprio dev pode automatizar cenários E2E. A diferença está em quem *lidera* e quem tem a visão mais ampla dos fluxos de negócio — papel que naturalmente recai sobre o QA.

### E2E Test (Teste fim a fim)

Testa um fluxo completo de usuário de ponta a ponta — desde a interface até o banco de dados, passando por todas as camadas do sistema. Simula exatamente o que um usuário real faria: abre a tela, preenche um formulário, clica em um botão, verifica o resultado.

**Por que o QA lidera?** Porque exige visão do fluxo de negócio e dos cenários que o usuário vai executar. Não importa como o código está estruturado internamente — só importa se o comportamento final está correto. O QA tem essa visão de ponta a ponta que o dev, focado na implementação, muitas vezes não tem.

**O dev pode escrever E2E?** Sim. Em muitos times, principalmente os que praticam DevOps e automação de qualidade, o desenvolvedor contribui ativamente na escrita de testes E2E — especialmente quando não há QA dedicado. A distinção é de liderança e responsabilidade primária, não de exclusividade técnica.

**Características:** lentos, menor volume, alto custo de manutenção. Formam o topo da pirâmide de testes.

### UAT — User Acceptance Test (Teste de aceitação do usuário)

É o teste final antes de um sistema ou funcionalidade ir para produção. O objetivo é confirmar que o que foi construído atende às necessidades reais do negócio e do usuário final — muitas vezes conduzido pelos próprios usuários ou pelo time de produto, com suporte do QA.

**Por que é do QA?** Porque o QA atua como o guardião da qualidade entre o desenvolvimento e o usuário. É o QA quem organiza os cenários, facilita as sessões de teste com stakeholders e documenta os resultados.

**Características:** geralmente manuais ou semi-automatizados, executados em ambiente de homologação, com participação direta do negócio.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>A pirâmide de testes</h2></div>
</div>

A pirâmide de testes é um modelo clássico que ilustra a proporção ideal entre os diferentes tipos de teste:

<table class="compare-table">
  <thead>
    <tr>
      <th>Nível</th>
      <th>Tipo</th>
      <th>Responsável</th>
      <th>Volume</th>
      <th>Velocidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Base</td>
      <td>Unit Test</td>
      <td>Desenvolvedor</td>
      <td>Muitos</td>
      <td>Muito rápido</td>
    </tr>
    <tr>
      <td>Meio-baixo</td>
      <td>Integration Test</td>
      <td>Desenvolvedor</td>
      <td>Médio</td>
      <td>Rápido</td>
    </tr>
    <tr>
      <td>Meio-alto</td>
      <td>Load Test</td>
      <td>Desenvolvedor</td>
      <td>Poucos</td>
      <td>Variável</td>
    </tr>
    <tr>
      <td>Alto</td>
      <td>E2E Test</td>
      <td>QA</td>
      <td>Poucos</td>
      <td>Lento</td>
    </tr>
    <tr>
      <td>Topo</td>
      <td>UAT</td>
      <td>QA + Negócio</td>
      <td>Muito poucos</td>
      <td>Manual / lento</td>
    </tr>
  </tbody>
</table>

A lógica da pirâmide é simples: quanto mais baixo o nível, mais testes você deve ter e mais rápidos eles devem ser. Quanto mais alto, menor o volume e maior o custo de criação e manutenção. Um projeto com muitos E2E e poucos unit tests tem a pirâmide invertida — o que resulta em suítes de teste lentas, frágeis e difíceis de manter.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Por que essa divisão existe?</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Contexto diferente</div>
    <div class="provider-detail">O desenvolvedor conhece o código por dentro. O QA conhece o comportamento esperado por fora. Cada um testa o que está em melhor posição de testar.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Feedback loop</div>
    <div class="provider-detail">Unit e integration tests rodam a cada commit e dão feedback em segundos. E2E e UAT rodam menos frequentemente e dão feedback em minutos ou horas. As camadas se complementam.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Custo e manutenção</div>
    <div class="provider-detail">Testes de caixa branca são mais baratos de manter — o dev os atualiza junto com o código. Testes de caixa preta são mais caros e quebrantes, por isso são poucos e estratégicos.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Qualidade real</div>
    <div class="provider-detail">Uma cobertura de unit tests alta não garante que o sistema funciona corretamente para o usuário. Por isso os testes de QA (E2E, UAT) são insubstituíveis — mesmo que sejam poucos.</div>
  </div>
</div>

<div class="conclusion">
  <h2>Responsabilidade compartilhada, papéis complementares</h2>
  <p>A divisão entre dev e QA não é uma fronteira rígida — é uma orientação baseada em contexto. O desenvolvedor <em>lidera</em> os testes de unidade, integração e carga porque conhece o código internamente. O QA <em>lidera</em> os testes E2E e UAT porque conhece os fluxos de negócio e a perspectiva do usuário.</p>
  <p>Mas o desenvolvedor pode e deve escrever unit tests de caixa preta — testando a interface pública de uma função sem depender de detalhes de implementação. Pode também contribuir com testes E2E, especialmente em times sem QA dedicado. E o QA pode escrever unit tests de caixa preta para validar contratos e comportamentos esperados.</p>
  <p>Em times maduros, a pergunta não é "quem testa o quê" — é "como garantimos juntos que o sistema tem a cobertura certa em cada camada". Quando dev e QA colaboram desde o início, definindo cenários de aceite antes de escrever a primeira linha de código, a qualidade emerge como consequência natural do processo.</p>
</div>
