---
layout: post
lang: pt-BR
title: "Repositório não é arquitetura: separar frontend e backend não é microserviço"
description: "Dividir o código em dois repositórios é uma decisão de logística. Monólito e microserviços são decisões de runtime. Confundir as duas coisas é o erro mais repetido nos grupos de tecnologia — e sai caro."
date: 2026-08-11
categories: [Coding]
subcategories:
  - "Coding/Architecture"
tags: [arquitetura, microservicos, monolito, monorepo, deploy, boas-praticas]
reading_time: 13
cover: /assets/img/posts/repositorio-nao-e-arquitetura.svg
image: /assets/img/posts/repositorio-nao-e-arquitetura.png
---

<p class="lead">Toda semana aparece a mesma thread em algum grupo de Facebook, Discord ou Telegram de programação: "aqui na empresa a gente migrou pra microserviços — separamos o repositório do front do repositório da API". Não migrou. Você tem o mesmo sistema de antes, com um <code>git remote</code> a mais.</p>

<div class="callout callout-warn">
  <div class="callout-label">A confusão em uma frase</div>
  Quantidade de repositórios é uma decisão sobre <strong>como o código é armazenado e versionado</strong>. Monólito versus microserviços é uma decisão sobre <strong>como o sistema roda e é implantado em produção</strong>. São dois eixos independentes, e é perfeitamente possível estar em qualquer combinação dos dois.
</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>O mito e suas três variações</h2></div>
</div>

O erro nunca aparece exatamente igual, mas sempre com a mesma raiz — usar a contagem de repositórios como proxy para maturidade arquitetural. As três versões mais comuns:

**"Separei o front do back, agora é microserviço."** Não. Você separou duas camadas técnicas de uma mesma aplicação. Isso é arquitetura cliente-servidor, algo que já existia antes de a palavra "microserviço" ser cunhada.

**"Está tudo num repositório só, então é monólito."** Também não. Google, Meta e Uber rodam milhares de serviços independentes a partir de um único repositório. O monorepo é sobre onde o código mora, não sobre o que roda em produção.

**"Temos 12 repositórios, temos arquitetura distribuída madura."** Talvez. Ou talvez você tenha 12 repositórios que precisam subir juntos, na mesma janela de deploy, contra o mesmo banco de dados. Isso tem nome, e não é elogio: monólito distribuído.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Dois eixos, quatro quadrantes</h2></div>
</div>

A maneira mais rápida de matar a discussão é desenhar a matriz. Repositórios em um eixo, unidades de deploy no outro:

<table class="compare-table">
  <thead>
    <tr>
      <th>Cenário</th>
      <th>Repositórios</th>
      <th>Unidades de deploy</th>
      <th>É microserviço?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laravel/Rails servindo HTML, tudo junto</td>
      <td>1</td>
      <td>1</td>
      <td><span class="cross">✗</span></td>
    </tr>
    <tr>
      <td>SPA em React + API .NET, um repo cada</td>
      <td>2</td>
      <td>2</td>
      <td><span class="cross">✗</span></td>
    </tr>
    <tr>
      <td>40 serviços de domínio dentro de um monorepo</td>
      <td>1</td>
      <td>40</td>
      <td><span class="check">✓</span></td>
    </tr>
    <tr>
      <td>12 repositórios que sobem no mesmo release coordenado</td>
      <td>12</td>
      <td>1 (na prática)</td>
      <td><span class="cross">✗</span></td>
    </tr>
    <tr>
      <td>8 serviços, 8 repos, 8 bancos, deploy independente</td>
      <td>8</td>
      <td>8</td>
      <td><span class="check">✓</span></td>
    </tr>
  </tbody>
</table>

Repare que a coluna de repositórios não prevê a última coluna em nenhuma linha. Ela simplesmente não carrega essa informação.

O mesmo sistema, exatamente com a mesma arquitetura de runtime, pode ser guardado dos dois jeitos:

```text
# Layout A — monorepo
plataforma/
├── services/
│   ├── catalog/        → container próprio, banco próprio, deploy próprio
│   ├── checkout/       → container próprio, banco próprio, deploy próprio
│   └── notifications/  → container próprio, banco próprio, deploy próprio
├── web/                → bundle estático servido por CDN
└── libs/contracts/     → contratos compartilhados

# Layout B — polirepo
org/service-catalog        → container próprio, banco próprio, deploy próprio
org/service-checkout       → container próprio, banco próprio, deploy próprio
org/service-notifications  → container próprio, banco próprio, deploy próprio
org/web-app                → bundle estático servido por CDN
org/contracts              → pacote versionado no registry
```

Em produção, A e B são **indistinguíveis**. Mesmos containers, mesmos bancos, mesma malha de rede, mesmos SLAs. A diferença está inteiramente no fluxo de trabalho da equipe: como se abre PR, como roda CI, quem tem permissão de escrita, como se faz um refactor que cruza fronteiras.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>O que define um monólito de verdade</h2></div>
</div>

Monólito não é sinônimo de código ruim, legado ou bagunçado. A definição é técnica e bem chata:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-box"></i> Uma unidade de deploy</div>
    <div class="provider-detail">Existe um artefato — JAR, DLL, imagem, pasta — que representa a aplicação inteira. Subiu ele, subiu tudo.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-microchip"></i> Chamadas in-process</div>
    <div class="provider-detail">Os módulos conversam por chamada de método, no mesmo processo. Sem rede, sem serialização, sem timeout.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-database"></i> Um estado compartilhado</div>
    <div class="provider-detail">Um schema, uma transação ACID atravessando o domínio inteiro, um <code>JOIN</code> resolvendo qualquer consulta.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-calendar-check"></i> Um ciclo de release</div>
    <div class="provider-detail">Não existe "subir só o módulo de pagamentos". Ou vai a versão inteira, ou não vai nada.</div>
  </div>
</div>

Note que nada disso menciona repositórios. Um monólito pode estar espalhado por vinte repositórios que são montados no build — continua sendo monólito, porque o que chega em produção é um artefato só.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>O que define microserviços</h2></div>
</div>

A definição de Lewis e Fowler é bem específica: um conjunto de serviços pequenos, cada um rodando no próprio processo, comunicando-se por mecanismos leves, construídos em torno de **capacidades de negócio** e implantáveis de forma independente por maquinário automatizado.

A parte que a galera dos grupos pula é justamente a mais importante — "capacidades de negócio" e "implantáveis de forma independente". Um checklist honesto:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Deploy independente</div>
    <div class="provider-detail">Serviço A vai para produção numa terça sem que ninguém precise coordenar release com o time do serviço B.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Dados privados</div>
    <div class="provider-detail">Cada serviço é dono do próprio armazenamento. Nenhum outro serviço lê aquela tabela diretamente — só através do contrato.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Decomposição por domínio</div>
    <div class="provider-detail">Serviços recortados por capacidade de negócio (pagamento, catálogo, entrega), não por camada técnica (UI, regra, dados).</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Contrato versionado</div>
    <div class="provider-detail">Mudanças de interface são compatíveis para trás, ou versionadas. Não se muda um payload e sai avisando no Slack.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Falha isolada</div>
    <div class="provider-detail">Se um serviço cai, o resto degrada — não desaba. Timeout, circuit breaker, fallback, fila.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Autonomia de time</div>
    <div class="provider-detail">Existe um time que decide sozinho o que entra, quando sobe e em qual stack roda.</div>
  </div>
</div>

Se você riscou menos de quatro desses seis itens, o que você tem é um sistema distribuído — o que é bem diferente de ter microserviços, e traz todo o custo sem boa parte do benefício.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Frontend e backend separados são camadas, não serviços</h2></div>
</div>

Aqui está o coração do mal-entendido. Quando você separa `web-app` de `api`, você não decompôs o domínio: você separou a apresentação da regra de negócio. Isso é uma fronteira **técnica**, e ela já existia mesmo quando os dois moravam na mesma pasta — o navegador sempre foi um processo separado do servidor.

Pior: o frontend de uma SPA normalmente nem é um serviço. É um monte de arquivo estático num bucket, servido por CDN. Ele não tem banco, não tem estado do lado do servidor, não escala independentemente de nada relevante. Chamar isso de "um dos nossos microserviços" é chamar o cardápio de filial do restaurante.

<div class="callout callout-tip">
  <div class="callout-label">A analogia que costuma resolver a discussão</div>
  Separar o caixa da cozinha não transforma o restaurante numa rede de franquias. Continua sendo um restaurante — com dois balcões. Virar rede é quando cada unidade tem estoque próprio, fornecedor próprio e abre no horário que quiser, sem ligar para a matriz.
</div>

E não: a API monolítica de 400 mil linhas atrás daquela SPA não fica menos monolítica porque o React saiu de dentro dela. Ela continua sendo um único deployable, com um único banco e um único ciclo de release. Você só trocou uma chamada de renderização por uma chamada HTTP.

Existe, sim, uma versão legítima disso — **micro-frontends** —, mas o critério é o mesmo de sempre: pedaços da interface implantáveis de forma independente, cada um alinhado a um domínio de negócio, cada um com seu time. Front separado do back não é micro-frontend, do mesmo jeito que não é microserviço.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>O teste das cinco perguntas</h2></div>
</div>

Da próxima vez que aparecer a discussão, ignore o diagrama e faça estas perguntas. Elas levam menos de cinco minutos e não deixam espaço para retórica:

1. **Consigo colocar o serviço A em produção hoje sem tocar em nenhum outro repositório?**
2. **Se A cair às 3h da manhã, B continua respondendo — nem que seja degradado?**
3. **A e B têm bancos separados, e ninguém faz consulta cruzada direto no schema do vizinho?**
4. **Consigo subir a versão do framework em A sem abrir um chamado para outro time?**
5. **Existe um time que decide sozinho quando A vai para produção?**

Cinco "sim": microserviços. Alguns "não": sistema distribuído em transição, o que é uma resposta perfeitamente respeitável. Cinco "não" com doze repositórios: monólito distribuído, e vale conversar sobre isso antes que doa mais.

Repare que a pergunta "quantos repositórios vocês têm?" não aparece na lista. Ela não é diagnóstica.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Monólito distribuído: o pior dos dois mundos</h2></div>
</div>

Esse é o destino de quem confunde os dois eixos e "migra para microserviços" fatiando repositórios. Os sintomas são fáceis de reconhecer:

<table class="compare-table">
  <thead>
    <tr><th>Sintoma</th><th>O que ele revela</th></tr>
  </thead>
  <tbody>
    <tr><td>Adicionar um campo exige PR em cinco repositórios</td><td>Os serviços compartilham modelo, não contrato</td></tr>
    <tr><td>Existe uma "janela de release" com todos os times</td><td>Não há deploy independente</td></tr>
    <tr><td>Um serviço fora do ar derruba o checkout inteiro</td><td>Não há isolamento de falha</td></tr>
    <tr><td>Todos os serviços apontam para o mesmo banco</td><td>Não há propriedade de dados</td></tr>
    <tr><td>Rollback de um serviço obriga rollback dos outros</td><td>Os contratos não são versionados</td></tr>
  </tbody>
</table>

Nesse cenário, você pagou toda a fatura da arquitetura distribuída — latência de rede, falhas parciais, consistência eventual, observabilidade, service discovery, complexidade de testes de integração — e recebeu de volta exatamente zero autonomia. É estritamente pior do que o monólito bem organizado que existia antes.

A Segment documentou publicamente esse caminho: fatiaram o sistema em mais de cem serviços, viram o custo operacional explodir e voltaram para um monólito. Não porque microserviços sejam ruins, mas porque o recorte não correspondia a fronteiras reais de time e de domínio.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Monólito modular: o meio-termo que ninguém posta no grupo</h2></div>
</div>

Entre "tudo embolado" e "cem serviços" existe uma opção que resolve a maioria dos problemas reais: manter uma única unidade de deploy, mas com fronteiras internas explícitas e respeitadas — módulos com API pública definida, dependências declaradas, acesso a dados restrito ao próprio módulo.

Foi o caminho da Shopify com uma das maiores bases Rails do mundo: manter o código num único codebase, mas com limites definidos e aplicados entre componentes. Você ganha a clareza de fronteiras sem pagar a conta da rede, e — o detalhe que mais importa — se um módulo realmente precisar virar serviço depois, a fronteira já está desenhada e testada.

<div class="callout callout-tip">
  <div class="callout-label">Regra prática</div>
  Se você não consegue manter fronteiras limpas dentro de um processo só, onde o compilador e os testes estão do seu lado, você não vai conseguir mantê-las através da rede, onde o feedback vem em forma de incidente às 3h da manhã.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Então, quando separar repositórios?</h2></div>
</div>

A pergunta certa não é "monólito ou microserviço?", e sim "qual fronteira de trabalho eu quero tornar cara?". Separar repositórios encarece mudanças que cruzam a fronteira e barateia autonomia dentro dela.

<table class="compare-table">
  <thead>
    <tr><th>Critério</th><th>Monorepo</th><th>Polirepo</th></tr>
  </thead>
  <tbody>
    <tr><td>Mudança atômica cruzando fronteiras</td><td><span class="check">✓</span> um PR</td><td><span class="cross">✗</span> vários PRs coordenados</td></tr>
    <tr><td>Refactor em larga escala</td><td><span class="check">✓</span> busca e substitui</td><td><span class="cross">✗</span> migração versionada</td></tr>
    <tr><td>Permissão granular por time</td><td><span class="partial">~</span> via CODEOWNERS</td><td><span class="check">✓</span> nativo</td></tr>
    <tr><td>CI simples e rápido sem tooling extra</td><td><span class="cross">✗</span> precisa de build seletivo</td><td><span class="check">✓</span> trivial</td></tr>
    <tr><td>Versionamento independente de artefatos</td><td><span class="partial">~</span> exige convenção</td><td><span class="check">✓</span> natural</td></tr>
    <tr><td>Descoberta de código e reuso</td><td><span class="check">✓</span> tudo visível</td><td><span class="partial">~</span> depende de registry</td></tr>
    <tr><td>Contrato entre partes fica explícito</td><td><span class="partial">~</span> fácil de burlar</td><td><span class="check">✓</span> a rede força</td></tr>
  </tbody>
</table>

A heurística que uso: **separe repositórios por fronteira de propriedade e permissão, não por camada técnica.** Se o mesmo time de quatro pessoas cuida do front e do back do mesmo produto, dois repositórios só significam que toda mudança de contrato virou dois PRs, dois reviews e uma janela onde as versões estão fora de sincronia. Se são times diferentes, em fusos diferentes, com ciclos diferentes, a separação paga a si mesma.

O Google mantém a esmagadora maioria do próprio código num repositório único com bilhões de linhas — e roda milhares de serviços independentes a partir dele. É a prova por contradição mais eficiente que existe: se repositório definisse arquitetura, o Google seria o maior monólito do planeta.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — os dois extremos
  </div>
  <p>Nos últimos anos trabalhei em três empresas fora do Brasil, em domínios bem diferentes: [moda de luxo](/blog/artigos/trabalhando-pelo-mundo-porto-farfetch/), [delivery](/blog/artigos/trabalhando-pelo-mundo-dubai-talabat/) e [seguros](/blog/artigos/trabalhando-pelo-mundo-dublin-outsurance/). Passei por monorepo com dezenas de serviços dentro e por polirepo com dezenas de repositórios, e a conclusão foi a mesma nos dois casos: o layout do repositório nunca foi o que determinou se dava pra entregar rápido.</p>
  <p>O que determinou foi sempre a resposta a uma pergunta só — <em>eu consigo subir minha mudança em produção sem depender do calendário de outro time?</em> Onde a resposta era sim, o dia era bom, independentemente de o código estar em um repositório ou em trinta. Onde era não, a quantidade de repositórios só mudava quantos PRs eu precisava abrir para o mesmo bloqueio.</p>
  <p>E vi o monólito distribuído de perto: adicionar um campo em um payload exigia coordenar mudanças em vários repositórios, com uma ordem obrigatória de deploy e uma janela combinada. No papel, era arquitetura de microserviços. Na prática, era um monólito com latência de rede embutida.</p>
</div>

<div class="conclusion">
  <h2>O resumo para colar no grupo</h2>
  <p>Repositório é logística: define como o código é guardado, versionado e revisado. Arquitetura é runtime: define o que sobe em produção, em quantas peças, com quantos ciclos de vida independentes. Um não determina o outro em nenhuma direção.</p>
  <p>Separar frontend de backend é uma decisão de organização de trabalho, com prós e contras reais — e nenhum deles é "virar microserviço". Você não decompôs o domínio, decompôs a camada de apresentação. É útil, é comum, é frequentemente a escolha certa. Só não é o que a palavra significa.</p>
  <p>E, sinceramente, na maior parte dos projetos que aparecem nesses grupos, a resposta certa é um monólito modular bem desenhado, com um repositório, um deploy e fronteiras internas levadas a sério. Isso não rende post viral, mas rende sistema que sobe na sexta-feira sem ninguém prender a respiração.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Lewis, J.; Fowler, M. <strong>Microservices: a definition of this new architectural term.</strong>
      <a href="https://martinfowler.com/articles/microservices.html" target="_blank">martinfowler.com</a>
    </li>
    <li>
      Fowler, M. <strong>MicroservicePremium.</strong>
      <a href="https://martinfowler.com/bliki/MicroservicePremium.html" target="_blank">martinfowler.com</a>
    </li>
    <li>
      Fowler, M. <strong>MonolithFirst.</strong>
      <a href="https://martinfowler.com/bliki/MonolithFirst.html" target="_blank">martinfowler.com</a>
    </li>
    <li>
      Potvin, R.; Levenberg, J. <strong>Why Google Stores Billions of Lines of Code in a Single Repository.</strong> Communications of the ACM, v. 59, n. 7, 2016.
      <a href="https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/" target="_blank">research.google</a>
    </li>
    <li>
      Westeinde, K. <strong>Deconstructing the Monolith: Designing Software that Maximizes Developer Productivity.</strong> Shopify Engineering.
      <a href="https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity" target="_blank">shopify.engineering</a>
    </li>
    <li>
      Segment Engineering. <strong>Goodbye Microservices: From 100s of problem children to 1 superstar.</strong>
      <a href="https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices" target="_blank">twilio.com</a>
    </li>
    <li>
      Newman, S. <strong>Building Microservices: Designing Fine-Grained Systems.</strong> 2. ed. O'Reilly Media, 2021.
      <a href="https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/" target="_blank">oreilly.com</a>
    </li>
  </ol>
</div>
