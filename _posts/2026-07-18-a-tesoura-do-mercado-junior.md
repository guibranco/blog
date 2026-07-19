---
layout: post
title: "A tesoura do mercado júnior: vagas, candidatos e hype (2019–2026)"
description: "Com dados do Indeed, SignalFire, LinkedIn e layoffs.fyi: como as vagas de dev despencaram do pico de 2022, por que a fila de iniciantes explodiu — e por que a escassez sempre foi sênior, nunca júnior."
date: 2026-07-18
categories: [Career]
tags: [mercado-de-trabalho, junior, pandemia, layoffs, llm, trabalho-remoto, carreira, tecnologia, contratacao, emprego, dev, big-tech, startups, sênior, inteligencia-artificial, remoto, hibrido, bootcamp]
reading_time: 12
cover: /assets/img/posts/capa-tesoura-mercado-junior.svg
image: /assets/img/posts/capa-tesoura-mercado-junior-og.png
---

<p class="lead">Se você tentou entrar na área de desenvolvimento nos últimos anos, sentiu na pele: processos com centenas de candidatos, busca de emprego levando de 5 a 6 meses e gente aplicando para 200+ posições antes de conseguir uma entrevista. O que aconteceu não foi um evento só — foi uma sequência: pandemia, dinheiro barato, boom de bootcamps, layoffs, retorno ao escritório e, por fim, as LLMs. Este artigo conta essa história com dados reais.</p>

<div class="callout callout-tip">
  <div class="callout-label">Nota metodológica</div>
  Os gráficos usam dados publicados pelo <strong>Indeed Hiring Lab</strong> (índice de vagas, EUA), <strong>SignalFire</strong> (contratação de recém-formados, base LinkedIn), <strong>layoffs.fyi</strong> (demissões) e <strong>LinkedIn Economic Graph</strong> (trabalho remoto). Onde a série é anual, os valores são médias aproximadas dos pontos publicados. O único trecho sem base quantitativa pública — a composição do perfil dos candidatos — está explicitamente marcado como estimativa qualitativa. Links nas referências ao final.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Antes de tudo: a escassez nunca foi júnior</h2></div>
</div>

Existe um mito de que, antes da pandemia, "sobrava vaga para dev". Os números da época alimentavam isso: em novembro de 2019 falava-se em mais de 920 mil posições de TI abertas nos EUA, e o "developer shortage" aparecia como risco emergente nos relatórios do Gartner.

Mas o detalhe que quase ninguém lia: **a escassez era de profissionais experientes**. Posições de TI exigindo 2+ anos de experiência eram cerca de 40% mais difíceis de preencher que as de entrada. No nível júnior, a conta sempre foi inversa: mesmo em 2019, recém-formados representavam apenas 15% das contratações das big techs — com taxas de aceitação abaixo de 1% nos processos mais concorridos — e estágios em empresas conhecidas já acumulavam ordens de grandeza mais candidatos que posições.

<div class="callout callout-warn">
  <div class="callout-label">O que o ciclo 2020–2026 realmente fez</div>
  Já havia mais gente que vaga no nível de entrada <strong>antes da pandemia</strong>. A tesoura deste artigo não nasceu em 2022; ela existia em versão branda. O que os anos seguintes fizeram foi escalar brutalmente os dois lados: menos vagas de entrada e muito, muito mais gente na fila. A escassez real — essa sim documentada — seguiu sendo sênior, e continua sendo em 2026.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O ciclo completo: boom, pico e colapso das vagas</h2></div>
</div>

<img src="{{ site.baseurl }}/assets/img/posts/grafico-vagas-dev-indeed.svg" alt="Índice de vagas de desenvolvimento de software no Indeed, 2019 a 2026" style="width:100%;border-radius:8px;margin:1rem 0;">

O índice de vagas de desenvolvimento de software do Indeed (EUA, base 100 = fev/2020) conta o ciclo inteiro:

<table class="compare-table">
  <thead>
    <tr><th>Período</th><th>O que aconteceu</th><th>Índice / variação</th></tr>
  </thead>
  <tbody>
    <tr><td>2019 (pré-pandemia)</td><td>Mercado estável, próximo da linha de base</td><td>≈ 100</td></tr>
    <tr><td>2020–2022 (pico)</td><td>Digitalização forçada + juros zero disparam contratações</td><td>+120% no pico (fev/2022)</td></tr>
    <tr><td>2022–2025 (correção)</td><td>Alta de juros derruba o índice; software engineer −49%; devs especializados −60%+</td><td>−69% do pico → 61 pts (maio/2025)</td></tr>
    <tr><td>2025–2026 (retomada parcial)</td><td>Vagas de software sobem ~15%; mas 71% dos ganhos em posições sênior</td><td>+15% desde fev/2025</td></tr>
  </tbody>
</table>

<div class="callout callout-warn">
  <div class="callout-label">A recuperação existe — só não é para quem está entrando</div>
  Os +15% desde o fundo de fevereiro de 2025 são reais. O detalhe que mata a festa do iniciante: <strong>71% dos ganhos estão concentrados em posições sênior</strong>. O mercado está se recuperando para quem já tem experiência.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>O colapso específico da porta de entrada</h2></div>
</div>

<img src="{{ site.baseurl }}/assets/img/posts/grafico-newgrads-signalfire.svg" alt="Recém-formados como percentual das contratações em Big Tech e startups, SignalFire" style="width:100%;border-radius:8px;margin:1rem 0;">

Se o gráfico anterior mostra o mercado todo, este mostra a porta de entrada — e é aqui que a história fica feia. Segundo a **SignalFire** (análise de 650+ milhões de perfis no LinkedIn):

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Big Techs: −54%</div>
    <div class="provider-detail">Recém-formados caíram de <strong>15%</strong> das contratações em 2019 para <strong>7%</strong> em 2024 — queda de mais de metade.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Startups: −80%</div>
    <div class="provider-detail">O tombo foi ainda pior: de <strong>30%</strong> das contratações em 2019 para menos de <strong>6%</strong> em 2024.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Idade média +3 anos</div>
    <div class="provider-detail">A idade média das contratações técnicas <strong>subiu 3 anos desde 2021</strong> — as empresas pararam de investir em treinar iniciantes.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">37% preferem IA</div>
    <div class="provider-detail">37% dos gestores pesquisados afirmam <strong>preferir usar IA a contratar</strong> um profissional da geração Z.</div>
  </div>
</div>

O reflexo aparece no desemprego: devs jovens (22–27 anos) nos EUA enfrentam taxa de **~7,4%** — quase o dobro da média nacional — e o desemprego de recém-formados atingiu a maior distância da média geral já registrada.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Os layoffs: a correção que virou rotina</h2></div>
</div>

<img src="{{ site.baseurl }}/assets/img/posts/grafico-layoffs-por-ano.svg" alt="Demissões anuais em empresas de tecnologia segundo layoffs.fyi" style="width:100%;border-radius:8px;margin:1rem 0;">

Os números do **layoffs.fyi** dão a régua da correção:

<table class="compare-table">
  <thead>
    <tr><th>Ano</th><th>Demissões</th><th>Contexto principal</th></tr>
  </thead>
  <tbody>
    <tr><td>2020</td><td>≈ 80 mil</td><td>Susto inicial da pandemia</td></tr>
    <tr><td>2021</td><td>≈ 0</td><td>Auge das contratações, dinheiro barato</td></tr>
    <tr><td>2022</td><td>165 mil</td><td>Alta de juros, queda do VC, medo de recessão</td></tr>
    <tr><td>2023</td><td>≈ 264 mil <span class="check">↑ recorde</span></td><td>Correção macro + início da narrativa de IA</td></tr>
    <tr><td>2024</td><td>153 mil</td><td>Reestruturação em torno de IA</td></tr>
    <tr><td>2025</td><td>≈ 124 mil</td><td>Disciplina de custo permanente</td></tr>
    <tr><td>2026*</td><td>90 mil+ (até abril)</td><td>Consolidação + substituição por automação</td></tr>
  </tbody>
</table>

A narrativa de "corrigir contratações apressadas da pandemia" tinha fundo de verdade — empresas como Meta e Alphabet quase dobraram o quadro entre 2019 e 2022. Mas o motivo dominante da primeira onda (2022–2023) foi macroeconômico. As ondas de 2024–2026 já têm outro tempero: reestruturação em torno de IA e disciplina de custo permanente.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Quem está na fila mudou</h2></div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Estimativa qualitativa</div>
  Não existe base pública que segmente candidatos júnior por "origem". Esta seção é leitura qualitativa do fenômeno, apoiada em proxies reais.
</div>

O perfil de quem disputa a porta de entrada mudou visivelmente ao longo do ciclo:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Geeks/nerds por vocação</div>
    <div class="provider-detail">Dominavam o funil pré-pandemia. Esse grupo não sumiu — foi <strong>diluído</strong> pela chegada massiva de outros perfis.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Aventureiros e migrantes</div>
    <div class="provider-detail">Chegaram com força em 2020, muitos empurrados pelo desemprego do lockdown para um setor que só contratava.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">A leva dos cursos online</div>
    <div class="provider-detail">Explodiu de 2021 em diante, com a indústria do "aprenda a programar em 6 meses e ganhe 10 mil". Resultado: muito mais gente chegando ao mercado sem base sólida.</div>
  </div>
</div>

Os proxies reais desse afogamento: busca de emprego em tech levando **5–6 meses** com 200+ candidaturas; e o comportamento defensivo dos recrutadores — inflação de títulos (**25% das vagas que em 2019 eram júnior passaram a exigir senioridade**) e processos com etapas artificiais.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Remoto: pouca vaga, metade das candidaturas</h2></div>
</div>

<img src="{{ site.baseurl }}/assets/img/posts/grafico-remoto-vagas-vs-candidaturas.svg" alt="Fatia de vagas remotas versus fatia de candidaturas no LinkedIn" style="width:100%;border-radius:8px;margin:1rem 0;">

O desequilíbrio do remoto é um dos dados mais impressionantes do ciclo:

<table class="compare-table">
  <thead>
    <tr><th>Período</th><th>% de vagas remotas</th><th>% de candidaturas remotas</th></tr>
  </thead>
  <tbody>
    <tr><td>Jan/2021</td><td>&lt; 10% (LinkedIn)</td><td>—</td></tr>
    <tr><td>Fev/2022 (pico)</td><td>20%+ (LinkedIn) · 10%+ (Indeed)</td><td><strong>50%</strong> de todas as candidaturas</td></tr>
    <tr><td>Nov/2022</td><td>14%</td><td>—</td></tr>
    <tr><td>Dez/2023</td><td>≈ 10%</td><td>46% das candidaturas</td></tr>
    <tr><td>2025</td><td>≈ 20% (remoto+híbrido)</td><td><strong>60%</strong> das candidaturas</td></tr>
  </tbody>
</table>

Vagas remotas chegam a atrair até **25× mais candidatos** que vagas híbridas. Para o júnior o efeito é duplo: as poucas vagas remotas que sobraram são as mais disputadas do mercado, e a fatia sênior delas cresce — sob o argumento de que iniciante precisa de mentoria presencial.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>E as LLMs? Culpadas, mas menos do que dizem</h2></div>
</div>

O GitHub Copilot chegou ao público em 2022 e o ChatGPT em novembro do mesmo ano. "A IA acabou com as vagas júnior" virou explicação universal — especialmente entre quem não conseguiu a tão sonhada vaga.

A cronologia, porém, não fecha: o declínio das vagas nas ocupações mais expostas à IA **começou antes do lançamento do ChatGPT**. O gatilho foi o fim do dinheiro barato. O que as LLMs fizeram de fato foi:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">1. Narrativa conveniente</div>
    <div class="provider-detail">"Aumentamos a produtividade com IA" soa melhor para o acionista do que "erramos o dimensionamento". A IA deu cobertura para não recontratar.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">2. Comprimir as tarefas de entrada</div>
    <div class="provider-detail">CRUD, boilerplate, testes, tarefas rotineiras — exatamente o degrau onde o júnior aprendia. Estima-se que <strong>50%+ das tarefas de entrada</strong> são automatizáveis, ≈5× o risco de posições sênior.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">3. Inflar ainda mais a fila</div>
    <div class="provider-detail">Currículos e candidaturas gerados por IA transformaram aplicar em vaga num jogo de spam, degradando o sinal para os dois lados.</div>
  </div>
</div>

E há um dado que complica a narrativa simplista: desde o lançamento das ferramentas de código agênticas (fev/2025), as vagas de software **subiram ~15%** enquanto o mercado geral caiu. As ocupações mais expostas à IA, que mais caíram, agora lideram a recuperação.

<div class="callout callout-warn">
  <div class="callout-label">O risco real é mais silencioso</div>
  Cortar a base da pirâmide melhora a margem hoje e cria uma <strong>crise de sucessão de talento em 5–10 anos</strong>. Se ninguém contrata júnior, de onde sairão os sêniores de 2032?
</div>

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>O que fica</h2>
  <p>A tesoura já existia antes da pandemia — mais candidatos que vagas no nível de entrada era a norma mesmo em 2019. O ciclo 2020–2026 multiplicou os dois lados dela.</p>
  <p>A escassez documentada sempre foi <strong>sênior</strong> — e a recuperação atual (71% dos ganhos em posições sênior) reforça isso. A porta de entrada encolheu para menos da metade: 15% → 7% das contratações em big tech, 30% → 6% em startups. A janela do remoto para iniciantes praticamente fechou: pouca vaga, demanda recorde.</p>
  <p>LLMs mudaram <em>o que</em> um júnior faz mais do que <em>se</em> ele existe — mas estão redesenhando o degrau de entrada. Quem domina fundamentos e usa IA como alavanca segue empregável; quem só copia resposta de chat compete com o próprio chat.</p>
</div>

<div class="divider">· · ·</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Indeed Hiring Lab. <strong>The US Tech Hiring Freeze Continues</strong> (jul/2025). Tech postings −36% vs 2020; software engineer −49%; devs especializados −60%+.
      <a href="https://www.hiringlab.org/2025/07/30/the-us-tech-hiring-freeze-continues/" target="_blank">hiringlab.org</a>
    </li>
    <li>
      Indeed Hiring Lab. <strong>AI and Job Postings: From Destruction to Creation?</strong> (jul/2026). Rebote de ~15% nas vagas de software desde fev/2025; declínio das ocupações expostas à IA começou antes do ChatGPT.
      <a href="https://www.hiringlab.org/2026/07/08/ai-and-job-postings-from-destruction-to-creation/" target="_blank">hiringlab.org</a>
    </li>
    <li>
      SignalFire. <strong>State of Tech Talent Report</strong> (2025 e 2026). Recém-formados de 15% → 7% em big tech; startups 30% → &lt;6%; idade média +3 anos; 37% dos gestores preferem IA a contratar Gen Z.
      <a href="https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025" target="_blank">2025</a> ·
      <a href="https://www.signalfire.com/blog/signalfire-state-of-talent-report-2026" target="_blank">2026</a>
    </li>
    <li>
      layoffs.fyi. <strong>Demissões em tech por ano</strong>: 165 mil (2022), ~264 mil (2023), 153 mil (2024), ~124 mil (2025).
      <a href="https://layoffs.fyi" target="_blank">layoffs.fyi</a>
    </li>
    <li>
      LinkedIn Economic Graph / Talent Blog. <strong>Remoto</strong>: pico de 20%+ dos anúncios (mar/2022); 50,1% das candidaturas com 19,4% das vagas (fev/2022); 46% das candidaturas com 10% das vagas (dez/2023).
      <a href="https://www.linkedin.com/business/talent/blog/talent-acquisition/remote-jobs-attract-majority-applications-first-time" target="_blank">linkedin.com</a>
    </li>
    <li>
      Indeed / Axios. <strong>Remoto</strong>: 2,6% dos anúncios em 2019 → 10%+ em mai/2022 → 7,6% em jul/2024.
      <a href="https://www.axios.com/2024/08/16/indeed-job-listings-remote-decline" target="_blank">axios.com</a>
    </li>
    <li>
      Federal Reserve Bank of New York. <strong>Desemprego de recém-formados</strong>: devs de 22–27 anos com ~7,4%.
      <a href="https://www.newyorkfed.org/research/college-labor-market" target="_blank">newyorkfed.org</a>
    </li>
    <li>
      Datapeople. <strong>Inflação de títulos</strong>: 25% das vagas júnior de 2019 reclassificadas como sênior.
      <a href="https://datapeople.io/blog/recruiting-trends-post-pandemic-tech-industry/" target="_blank">datapeople.io</a>
    </li>
    <li>
      Brookings Institution. <strong>Automação</strong>: 50%+ das tarefas de posições de entrada automatizáveis — ≈5× o risco de posições sênior.
    </li>
    <li>
      DistantJob. <strong>Contexto pré-pandemia</strong>: concentração da escassez em posições com 2+ anos de experiência.
      <a href="https://distantjob.com/blog/the-talented-developer-shortage-is-a-lie/" target="_blank">distantjob.com</a>
    </li>
  </ol>
</div>
