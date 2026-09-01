---
layout: post
lang: pt-BR
title: "Júnior, pleno ou sênior: a pergunta de entrevista que separa os três"
description: "Uma demanda fictícia de um PO, três candidatos e três respostas completamente diferentes. O que realmente avaliamos em uma entrevista técnica — e por que senioridade não é o tamanho da sua stack."
date: 2026-08-30
categories: [Career]
subcategories:
  - "Career/Seniority"
tags: [senioridade, entrevista-tecnica, carreira-dev, contratacao, junior-pleno-senior, mercado-de-trabalho]
reading_time: 30
cover: /assets/img/posts/junior-pleno-senior-entrevista.svg
image: /assets/img/posts/junior-pleno-senior-entrevista.png
medium_tags: [carreira, programacao, entrevista, senioridade, tecnologia]
---

<p class="lead">Três candidatos entram na mesma sala virtual, recebem exatamente a mesma demanda e têm o mesmo tempo para responder. Nenhum deles precisa escrever uma linha de código para que eu saiba, em menos de cinco minutos, em que nível cada um está. Este artigo é sobre o que acontece nesses cinco minutos.</p>

Existe uma crença muito difundida — e muito confortável — de que senioridade é um inventário: quantas linguagens você sabe, quantos frameworks você já usou, quantos certificados estão pendurados no LinkedIn. É confortável porque é acionável: basta estudar mais uma ferramenta e subir um degrau.

O problema é que não funciona assim. Já entrevistei gente com quinze tecnologias no currículo que travou na primeira pergunta ambígua, e gente com uma stack modesta que dissecou o problema como cirurgião. A diferença nunca esteve no inventário. Esteve na **vivência** — na quantidade de vezes que a pessoa já viu algo dar errado e aprendeu a farejar isso antes de acontecer.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Antes de tudo: júnior não é estudante</h2></div>
</div>

Preciso começar por aqui porque é a confusão mais cara do mercado brasileiro.

**Você não é desenvolvedor júnior porque terminou um bootcamp.** Você não é júnior porque fez três projetos no GitHub, porque concluiu a graduação ou porque assistiu a 200 horas de curso. Enquanto ninguém te contratou para exercer a função, você é **estudante** — e isso não é ofensa nenhuma, é apenas a descrição correta do estágio.

Júnior é um **cargo**. Existe a partir do momento em que uma empresa assina um contrato, coloca você dentro de um time, te dá acesso ao repositório de produção e passa a depender de você para entregar valor. Antes disso existe estudo, existe portfólio, existe potencial — mas não existe senioridade, porque senioridade se mede em situações reais, e situações reais só acontecem em produção.

<div class="callout callout-tip">
  <div class="callout-label">Por que essa distinção importa</div>
  Porque muita gente se frustra achando que "está estagnada no júnior" quando na verdade ainda não entrou. São problemas diferentes, com soluções diferentes. Quem ainda não foi contratado precisa de <strong>acesso</strong>. Quem já foi contratado precisa de <strong>exposição a problemas maiores</strong>. Confundir os dois faz a pessoa estudar a sexta linguagem quando deveria estar aplicando para vagas.
</div>

E o inverso também vale: **um júnior contratado é um profissional**, não um estagiário glorificado. Ele entra em sprint, tem demanda com prazo, participa de code review, quebra produção e conserta produção. A diferença entre ele e o pleno não é "um trabalha e o outro aprende" — os dois trabalham e os dois aprendem. A diferença é o **raio de autonomia**: o tamanho do problema que a pessoa consegue receber, cortar em pedaços e resolver sem que alguém precise cortar por ela.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>O cenário: a demanda que eu levo para a entrevista</h2></div>
</div>

Eu entro na sala vestindo o chapéu de PO. Não sou o entrevistador técnico neste momento — sou o cara que acabou de sair de uma reunião com o cliente e trouxe um pedido. E o pedido é este:

<div class="callout callout-warn">
  <div class="callout-label">A demanda, exatamente como chega</div>
  "Nosso site precisa exibir um quadrado de 10px por 10px com uma cor, a cada dia do ano."
  <br><br>
  <strong>Como você planeja executar essa tarefa?</strong>
</div>

É isso. Uma frase. Vaga de propósito, mas não injusta — é exatamente o nível de detalhe que uma demanda real chega na sua mesa numa terça-feira qualquer.

Repare no verbo que eu uso: **planeja**. Não pedi para implementar. Não pedi pseudocódigo. Pedi um plano. E a primeira coisa que observo é se a pessoa percebeu isso.

Agora, os três candidatos.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Candidato A — o júnior: o editor já está aberto</h2></div>
</div>

O candidato A não hesita. É quase admirável a velocidade. Em quinze segundos ele já está descrevendo a solução:

> "Tranquilo. Eu faço uma `div` de 10 por 10 com CSS, pego a data atual com `new Date()`, calculo o dia do ano, e uso isso como índice num array de cores. Se você quiser eu já escrevo aqui."

E ele escreve. E o código funciona. Roda no navegador, mostra um quadradinho colorido, muda de cor quando você mexe o relógio da máquina. Tecnicamente correto:

```javascript
const cores = ["#e63946", "#457b9d", "#2a9d8f" /* ... 365 cores ... */];

const inicioDoAno = new Date(new Date().getFullYear(), 0, 1);
const diferenca = new Date() - inicioDoAno;
const diaDoAno = Math.floor(diferenca / 86400000);

document.querySelector("#box").style.background = cores[diaDoAno];
```

Não há nada de burro nesse código. É a solução óbvia, direta, entregue rápido. O júnior fez exatamente o que foi pedido — e é justamente esse o ponto.

**O que ele não fez:** não perguntou nada. Aceitou a demanda como especificação completa. Assumiu, sem verbalizar, que:

- a cor pode ser diferente para cada usuário (está no cliente);
- a cor pode mudar entre um ano e outro;
- todo ano tem 365 dias;
- o dia do usuário é o dia do relógio da máquina dele;
- um dia tem sempre exatamente 86.400.000 milissegundos.

Cada uma dessas cinco suposições é uma decisão de produto disfarçada de detalhe técnico. Ele tomou todas as cinco sozinho, em silêncio, e nenhuma delas foi validada com quem trouxe a demanda.

<div class="callout callout-tip">
  <div class="callout-label">E isso está previsto, formalmente</div>
  Na matriz de competências da Talabat, o tema "Dealing with ambiguity" — lidar com ambiguidade — tem uma entrada explícita para o nível IC1: <strong>"n/a (not applicable at this level)"</strong>. Não é esquecimento nem indulgência. A empresa escreveu, com todas as letras, que não se espera que um júnior lide com ambiguidade. Ela aparece só a partir do IC2, e ainda assim limitada ao escopo pessoal de trabalho. Cobrar isso do candidato A seria avaliá-lo por um nível que ele não ocupa.
</div>

<div class="callout callout-warn">
  <div class="callout-label">O que isso me diz como avaliador</div>
  Não me diz que ele é ruim. Me diz que ele ainda enxerga a demanda como <strong>enunciado de exercício</strong> — algo que tem uma resposta certa esperando ser digitada. É exatamente o reflexo que a faculdade, os cursos e o LeetCode treinam durante anos. Desaprender isso é literalmente o trabalho dos primeiros anos de carreira.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Candidato B — o pleno: duas perguntas que mudam a arquitetura</h2></div>
</div>

O candidato B fica em silêncio por uns segundos. Depois vira a mesa:

> "Antes de pensar em código, tenho duas dúvidas. Primeira: **a cor precisa ser a mesma para todos os usuários?** Se sim, essa definição tem que sair do servidor, porque se eu gerar no cliente cada navegador pode chegar num resultado diferente. Segunda: **em 15 de março do ano que vem, a cor tem que ser a mesma de 15 de março deste ano?** Se sim, isso não é um cálculo, é um dado — precisa estar persistido em algum lugar."

Estas duas perguntas não são detalhes. Elas decidem a arquitetura inteira antes de qualquer linha ser escrita:

<table class="compare-table">
  <thead>
    <tr>
      <th>Resposta do PO</th>
      <th>Consequência arquitetural</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cor igual para todos</td>
      <td>Fonte da verdade no servidor (ou paleta fixa distribuída no bundle). Não pode ser aleatória no cliente.</td>
    </tr>
    <tr>
      <td>Cor pode variar por usuário</td>
      <td>Cliente resolve sozinho. Mas então "cor do dia" vira "cor do dia <em>de quem olha</em>" — e isso muda o texto da UI.</td>
    </tr>
    <tr>
      <td>Repete todo ano</td>
      <td>Paleta versionada e persistida. É conteúdo, e conteúdo tem dono, tem migração e tem changelog.</td>
    </tr>
    <tr>
      <td>Muda a cada ano</td>
      <td>Função determinística com semente por ano. Precisa ser reprodutível para debug e para suporte.</td>
    </tr>
  </tbody>
</table>

O pleno entendeu a coisa mais importante da profissão: **ambiguidade na demanda não é problema do PO, é risco do time**. Ele não devolveu a demanda; ele a refinou. Fez as perguntas cujas respostas ele sabia que mudariam o desenho.

O que ele ainda não fez: olhou para as bordas do calendário e do planeta.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a virada do "faz" para o "por quê"
  </div>
  <p>A transição de júnior para pleno, na minha cabeça, tem uma data — não no calendário, mas num code review. Eu tinha entregue uma feature exatamente como pediram, e o tech lead comentou: "está certo, mas você não perguntou o que acontece quando o campo vem nulo, e ele vem nulo em 30% dos registros da base". Não era uma questão de sintaxe. Era que eu tinha entregue código sem entender o dado. A partir dali eu passei a abrir toda demanda pelo mesmo lado: primeiro os casos que quebram, depois a solução.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Candidato C — o sênior: as perguntas que ninguém queria ouvir</h2></div>
</div>

O candidato C começa exatamente igual ao pleno. Faz as mesmas duas perguntas, na mesma ordem, quase com as mesmas palavras. E aí continua.

> "E o **ano bissexto**? Se a paleta tem 365 cores e o índice é o dia do ano, em 2028 tudo depois de 29 de fevereiro anda uma casa. O 1º de março passa a exibir a cor que era do dia 28. E o dia 29 em si — ele tem cor própria, ou herda alguma?"
>
> "E **fuso horário**? Dois usuários podem abrir a página exatamente no mesmo instante e estarem em dias diferentes. Alguém em Auckland às 10h da manhã e alguém no Havaí no mesmo segundo estão separados por um dia inteiro de calendário. Qual dos dois está 'certo'? A cor é do dia **do servidor**, do dia **do usuário**, ou do dia **de um fuso de referência do negócio**?"
>
> "Se a resposta for 'fuso do usuário', então não posso cachear essa página numa CDN sem cuidado — o HTML gerado às 23h59 em Lisboa está errado para quem abre às 00h01. Se for 'fuso do servidor', preciso escrever isso na UI, porque senão vou ter ticket de suporte de gente dizendo que a cor não mudou à meia-noite."

Aqui está a diferença que não cabe em currículo. O sênior não sabe mais JavaScript que o pleno. Ele já **levou porrada** de ano bissexto, de horário de verão, de cache que serviu conteúdo de ontem, de bug que só reproduzia entre 21h e 00h para usuário do Acre.

E tem mais uma coisa que ele viu, e que quase ninguém verbaliza:

```javascript
// O bug silencioso do candidato A:
const diaDoAno = Math.floor(diferenca / 86400000);
```

Nem todo dia tem 86.400.000 milissegundos. Em países com horário de verão — Irlanda, Portugal, boa parte da Europa — existe um dia por ano com 23 horas e outro com 25. O desvio que isso introduz é de exatamente uma hora, 3.600.000 milissegundos: nada de dramático em si. O problema é o `Math.floor`. Uma hora de defasagem é suficiente para o índice cair na casa anterior, e o efeito não é uma hora de erro — é **um dia inteiro de cor errada**. Na Irlanda, entre o último domingo de março e o último de outubro, quem abrir a página entre meia-noite e 1h da manhã continua vendo a cor de ontem. É o tipo de bug que só existe numa janela de 60 minutos, some sozinho quando o relógio volta, e ninguém consegue reproduzir às 15h de uma quarta-feira.

A versão do sênior troca aritmética por calendário:

```javascript
// Chave de calendário explícita, no fuso que o negócio decidiu.
function chaveDoDia(instante, fuso) {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: fuso,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(instante); // -> "2028-02-29"
}

const chave = chaveDoDia(new Date(), "Europe/Dublin").slice(5); // -> "02-29"
const cor = paleta[chave] ?? paleta["02-28"]; // fallback explícito para bissexto
```

Repare no que mudou conceitualmente: o índice deixou de ser **um número sequencial** e passou a ser **uma chave de calendário**. Com isso, 29 de fevereiro deixa de deslocar o resto do ano, o horário de verão deixa de importar, e o comportamento do dia extra vira uma decisão explícita e visível no código — não um acidente.

<div class="callout callout-tip">
  <div class="callout-label">O detalhe que fecha a conta</div>
  Perguntar sobre bissexto e fuso não é "viajar na maionese". São as duas únicas fontes de erro que <strong>não aparecem em teste</strong>: o ambiente de desenvolvimento roda num fuso só, e o ano bissexto acontece a cada quatro anos. Ou você prevê no planejamento, ou você descobre em produção — e o custo entre as duas coisas é de duas ordens de grandeza.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>O fluxograma: como cada um percorre o mesmo problema</h2></div>
</div>

Colocando os três caminhos lado a lado, o padrão fica visível. Não é que um pense "melhor" — é que cada um **para em um ponto diferente** antes de começar a executar.

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-fluxograma-tres-niveis.svg"
  alt="Fluxograma: júnior chega ao código na etapa 3 de 4; o sênior, na etapa 6 de 6"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

O júnior tem **quatro** etapas e chega ao código na terceira. O sênior tem **seis** e só chega ao código na última. Isso não significa que o sênior é mais lento — significa que ele gasta o tempo antes, e não depois, quando o custo do erro já multiplicou.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>As camadas do problema — e até onde cada um desce</h2></div>
</div>

Toda demanda tem camadas. A superfície é o que foi pedido; embaixo dela existem regras de negócio, estado, tempo, entrega e manutenção. Senioridade, na prática, é a **profundidade média** que a pessoa alcança sozinha, sem que alguém puxe.

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-camadas-problema.svg"
  alt="As seis camadas da mesma demanda e até qual delas cada nível desce sozinho"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Note uma coisa importante: **as camadas 1 e 2 são idênticas para os três**. O código do júnior não é pior. É que ele só existe nas duas primeiras camadas — e as quatro de baixo continuam lá, esperando alguém.

<table class="compare-table">
  <thead>
    <tr>
      <th>Pergunta levantada espontaneamente</th>
      <th>Jr</th>
      <th>Pl</th>
      <th>Sr</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Qual o tamanho e onde fica o box?</td><td><span class="check">✓</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Todos os usuários veem a mesma cor?</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>A cor de um dia repete no ano seguinte?</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>De onde vem a paleta — dado ou função?</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>O que acontece em 29 de fevereiro?</td><td><span class="cross">✗</span></td><td><span class="partial">~</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>O "dia" é de qual fuso horário?</td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Horário de verão quebra o cálculo?</td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Cache/CDN serve conteúdo de ontem?</td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Contraste/acessibilidade da cor sorteada</td><td><span class="cross">✗</span></td><td><span class="partial">~</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Como o suporte vai debugar um relato?</td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
  </tbody>
</table>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Senioridade é vivência, não inventário</h2></div>
</div>

Aqui está o ponto central do artigo, e vou ser direto: **nenhuma das perguntas do sênior exige conhecimento de framework.**

Ano bissexto é ensinado no ensino fundamental. Fuso horário é ensinado no ensino fundamental. `Intl.DateTimeFormat` está na documentação. Nada disso é conhecimento raro.

O que é raro é **lembrar de perguntar**. E você não lembra porque leu — você lembra porque um dia às 2h da manhã de um domingo de outubro o relatório de fechamento saiu duplicado, e você passou seis horas descobrindo que o servidor tinha vivido a mesma hora duas vezes.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Inventário</div>
    <div class="provider-detail">"Sei React, Vue, Angular, Node, Go, Kubernetes, Terraform, Kafka." Mede <strong>exposição a ferramentas</strong>. Acumula com estudo.</div>
    <div class="provider-price">Cresce em meses</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Vivência</div>
    <div class="provider-detail">"Já vi isso quebrar assim, e por isso eu pergunto X antes." Mede <strong>exposição a consequências</strong>. Só acumula com tempo e produção.</div>
    <div class="provider-price">Cresce em anos</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O que a entrevista mede</div>
    <div class="provider-detail">A segunda. Inventário eu leio no currículo em 40 segundos — e ele envelhece. Vivência só aparece quando você coloca a pessoa diante de ambiguidade.</div>
    <div class="provider-price">O diferencial real</div>
  </div>
</div>

### A matriz que prova isso sozinha

A matriz de competências da Talabat avalia **27 temas** distribuídos em cinco áreas: habilidades técnicas, entrega, feedback e comunicação, liderança e impacto estratégico. Cada tema tem uma descrição própria para cada um dos seis níveis, de IC1 a IC6.

Com uma exceção. Exatamente **um** dos 27 temas para de evoluir depois do sênior. Nos três níveis acima — Staff, Principal, Senior Principal — a célula não traz um texto novo. Traz duas palavras: *"see IC3"*.

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-horizonte-planejamento.svg"
  alt="Horizonte de planejamento por nível: 1 a 5 dias no júnior, 1 a 4 semanas no pleno, 1 a 3 meses no sênior, 3 a 6 meses no Staff, 6 a 12 meses no Principal e 1 a 2 anos no Senior Principal"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

<div class="callout callout-warn">
  <div class="callout-label">O tema que congela é "Writing code"</div>
  Escrever código é a única competência das 27 que <strong>atinge o teto no sênior</strong>. A partir dali, a empresa formalmente não espera que você escreva código melhor — espera que você faça outras 26 coisas melhor. Um Principal Engineer e um sênior têm, no papel, exatamente a mesma expectativa de qualidade de código. Toda a distância entre os dois está em ambiguidade, arquitetura, alinhamento, mentoria, visão de produto e horizonte de decisão.
</div>

Isso é a tese deste artigo escrita por um departamento de RH, com carimbo. Se escrever código para de diferenciar no sênior, então tudo que vem depois — e boa parte do que vem antes — é outra coisa.

E o gráfico acima mostra que outra coisa é essa. A matriz define, para cada nível, um **horizonte de planejamento**: por quanto tempo à frente aquela pessoa responde. Cinco dias no júnior. Um mês no pleno. Um trimestre no sênior. Dois anos no topo. Cada degrau multiplica o horizonte por mais ou menos quatro.

<div class="callout callout-tip">
  <div class="callout-label">Uma definição de senioridade em uma linha</div>
  Se eu tivesse que resumir o artigo inteiro numa frase, seria essa: <strong>senioridade é o tamanho do futuro pelo qual você é responsável.</strong> O júnior responde pela tarefa desta semana. O sênior responde pelo que o time vai viver daqui a três meses. É exatamente por isso que o candidato C pergunta sobre ano bissexto: o bissexto está a quatro anos de distância, e o horizonte dele alcança lá.

</div>

É por isso que um dev que passou cinco anos numa única stack, mas mantendo um produto vivo com usuários reais, costuma ser mais sênior do que alguém que passou cinco anos pulando de projeto greenfield em greenfield. **Quem nunca manteve o próprio código não viu a consequência das próprias decisões** — e é exatamente esse feedback loop que constrói a intuição.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — fuso horário não é teoria pra mim
  </div>
  <p>Morando em Dublin e trabalhando com times e sistemas que tocam o Brasil, fuso deixou de ser trivia e virou rotina. A Irlanda entra e sai do horário de verão; o Brasil não tem mais desde 2019; a diferença entre os dois oscila entre 3 e 4 horas dependendo da época do ano. Já vi agendamento disparar na hora errada, relatório diário fechar com um dia de defasagem e log com timestamp que não batia com o incidente. Depois de algumas dessas, "qual o fuso de referência?" virou a primeira pergunta que eu faço em qualquer coisa que envolva data.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Quanto tempo leva de verdade</h2></div>
</div>

Se senioridade se constrói com vivência, a pergunta óbvia é: **quantos anos?**

A resposta honesta é que depende brutalmente do tipo de empresa. O gráfico abaixo não mede quanto tempo você fica em cada nível — mede **em que ponto da carreira o título costuma chegar**. É essa leitura que expõe a distorção: a barra de "sênior" da coluna de retenção cai exatamente em cima da barra de "pleno" da big tech.

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-tempo-promocao.svg"
  alt="Linha do tempo de carreira: com quantos anos de experiência acumulada cada título costuma chegar em big tech, no mercado brasileiro e em empresas que promovem para reter"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

<div class="callout callout-tip">
  <div class="callout-label">De onde vêm esses números</div>
  As faixas de big tech vêm de trilhas de nivelamento públicas — incluindo o framework de carreira do Dropbox, que publica os tempos por nível, e a escada da Artsy, aberta no GitHub. As do mercado brasileiro vêm de levantamentos de recrutamento referenciados. Já a linha de <strong>promoção de retenção</strong> e os percentuais de aumento citados adiante são <strong>estimativas ilustrativas</strong>, baseadas em padrão observado — não em pesquisa publicada. Trate-as como ordem de grandeza, não como dado.
</div>

### Um framework que publica os números

Quase toda empresa trata a matriz de promoção como documento interno. O Dropbox publicou a dele, e isso dá uma âncora rara — números oficiais, não crowdsourced:

<table class="compare-table">
  <thead>
    <tr>
      <th>Nível (Dropbox)</th>
      <th>Tempo típico no nível — IC</th>
      <th>Tempo típico no nível — gestor</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>L1</td><td>1,5–2 anos</td><td>—</td></tr>
    <tr><td>L2</td><td>2–3 anos</td><td>—</td></tr>
    <tr><td>L3</td><td>2–4 anos</td><td>0–2 anos</td></tr>
    <tr><td><strong>L4</strong></td><td colspan="2"><strong>4+ anos — nível de carreira.</strong> A documentação diz que se espera que todo engenheiro alcance impacto de L4 ou maior, e que para muita gente L4 será o destino final, sem pressão de subir.</td></tr>
  </tbody>
</table>

Somando as faixas, uma pessoa entra no L3 com **3,5 a 5 anos** de carreira e no L4 com **5,5 a 9 anos**. Compare com a régua da seção anterior: L3 é o degrau de sênior, L4 é o de especialista. Os números batem quase exatamente com as faixas de big tech do gráfico — o que é um bom sinal, já que vieram de fontes independentes.

<div class="callout callout-tip">
  <div class="callout-label">O detalhe que quase ninguém repara</div>
  A linha do gestor em L3 é mais curta que a do IC. O motivo está escrito na própria documentação: quem migra para gestão <strong>já cresceu através de boa parte do L3 como IC</strong>. O tempo não é menor porque gestão é mais fácil — é menor porque parte do caminho já foi andado do outro lado.
</div>

### O padrão das grandes empresas

Em empresas grandes, com trilha de carreira formalizada e comitê de calibração, os números são razoavelmente estáveis. No Google, o nível de entrada (L3) costuma durar entre um ano e meio e dois anos — ficar muito além disso é lido internamente como sinal de baixa performance. O L4, o degrau seguinte, corresponde grosso modo a algo entre um e cinco anos de mercado, e o título de Senior Software Engineer (L5) normalmente é associado a uma faixa de seis a nove anos de experiência. Meta, Amazon e Microsoft operam com trilhas diferentes no nome, mas com ordens de grandeza muito parecidas.

Traduzindo para a nomenclatura brasileira:

<table class="compare-table">
  <thead>
    <tr>
      <th>Nível</th>
      <th>Experiência típica (empresa grande)</th>
      <th>Autonomia esperada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Júnior</strong></td>
      <td>0 a 2 anos</td>
      <td>Recebe uma tarefa recortada. Entrega com revisão.</td>
    </tr>
    <tr>
      <td><strong>Pleno</strong></td>
      <td>2 a 5 anos</td>
      <td>Recebe um problema. Faz o próprio recorte e entrega.</td>
    </tr>
    <tr>
      <td><strong>Sênior</strong></td>
      <td>6 anos ou mais</td>
      <td>Recebe um objetivo ambíguo. Define o problema, mapeia risco e puxa os outros junto.</td>
    </tr>
  </tbody>
</table>

Repare que a coluna que importa não é a do meio. É a da direita. Os anos são **proxy** da autonomia, não a causa dela.

### O padrão das empresas pequenas — e a armadilha

Agora a parte que ninguém coloca no material institucional.

Em empresas pequenas, consultorias de body shop e lugares que pagam abaixo do mercado, existe um padrão muito consistente: **promoção rápida com aumento pequeno**. A pessoa entra como júnior e, com menos de um ano de carreira, já é "pleno". Antes de completar três, tem cartão de visita de sênior — no mesmo ponto da linha do tempo em que uma multinacional ainda estaria assinando a promoção para pleno.

Isso raramente é generosidade. É retenção barata, e a matemática — com os números arredondados a título de ilustração — é simples:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">O que a empresa gasta</div>
    <div class="provider-detail">Um título novo (custo zero) e um aumento de 10% a 15% (custo baixo), aplicado sobre um salário que já estava abaixo do mercado.</div>
    <div class="provider-price">Custo: baixo</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O que a empresa ganha</div>
    <div class="provider-detail">Um profissional que se sente reconhecido, para de olhar vagas por mais 12 meses, e continua entregando o mesmo escopo.</div>
    <div class="provider-price">Retorno: alto</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">O que a empresa sabe</div>
    <div class="provider-detail">Que "sênior com 2 anos de carreira" não passa em processo seletivo de empresa grande. O título só tem valor lá dentro.</div>
    <div class="provider-price">Trava: efetiva</div>
  </div>
</div>

<div class="callout callout-warn">
  <div class="callout-label">O título vira uma âncora</div>
  Quando essa pessoa finalmente vai ao mercado, acontece uma das duas coisas: ou ela aplica para vagas de sênior e é reprovada em série — porque a entrevista mede vivência, não o crachá —, ou ela aceita voltar a pleno em outro lugar e sente que <em>regrediu</em>. O segundo cenário é o saudável, mas dói. E o custo emocional dessa correção é exatamente o que mantém a pessoa parada.
</div>

Como diferenciar uma promoção real de uma promoção de retenção? Pelo que **mudou além do título**:

<table class="compare-table">
  <thead>
    <tr>
      <th>Sinal</th>
      <th>Promoção real</th>
      <th>Promoção de retenção</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Aumento salarial</td><td>Salto de faixa (20%+)</td><td>Reajuste simbólico (10–15%)</td></tr>
    <tr><td>Escopo do trabalho</td><td>Muda antes ou junto do título</td><td>Continua exatamente igual</td></tr>
    <tr><td>Critérios</td><td>Existe rubrica escrita</td><td>Decisão informal do gestor</td></tr>
    <tr><td>Timing</td><td>Ciclo de avaliação</td><td>Logo depois de você mencionar outra proposta</td></tr>
    <tr><td>Referência externa</td><td>Faixa comparável ao mercado</td><td>Abaixo do piso da faixa nova</td></tr>
    <tr><td>Quem revisa seu código</td><td>Você passa a revisar o dos outros</td><td>Ninguém muda de lugar</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Um teste honesto de dois minutos</div>
  Pegue três vagas do seu nível atual em empresas do porte que você quer trabalhar. Leia os requisitos <strong>de responsabilidade</strong>, não os de tecnologia. Se você lê "lidera decisões técnicas de um domínio" e pensa "isso nunca me pediram", o título está adiantado em relação à vivência. Isso não é um julgamento — é um mapa do que buscar nos próximos dois anos.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">10</div>
  <div class="section-title-wrap"><h2>Depois do sênior, a estrada se divide</h2></div>
</div>

Até aqui eu tratei a carreira como uma escada única. Ela não é. Júnior, pleno e sênior formam um tronco comum, mas no topo desse tronco existe uma bifurcação — e muita gente descobre isso tarde demais, já tendo aceitado virar gestor por falta de alternativa visível.

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-trilhas-ic-gestao.svg"
  alt="Fluxograma da carreira: tronco comum de estudante a sênior, depois bifurcação entre trilha de especialista (Staff, Principal, Distinguished) e trilha de gestão (EM, Senior EM, Director, VP e C-level)"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Três leituras importam nesse desenho:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">A troca é lateral</div>
    <div class="provider-detail">Em escadas bem desenhadas, Staff e Engineering Manager ficam na <strong>mesma faixa salarial</strong>. Virar gestor não é subir — é mudar de ofício. Se na sua empresa gestão é o único jeito de ganhar mais, a escada está mal feita.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Dá para voltar</div>
    <div class="provider-detail">Trajetórias como Staff → EM → Senior Staff são comuns e saudáveis. Gestão não é porta de sentido único, embora muita gente a trate assim.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">A entrada direta existe</div>
    <div class="provider-detail">No Brasil é bem comum alguém entrar direto em gestão sem nunca ter tido título de IC. Funciona bem em muita gente. O que pesa não é o título que a pessoa teve, e sim quanto contexto técnico ela consegue demonstrar — sem isso, calibrar estimativa e avaliar risco vira chute, tenha ela sido IC ou não.</div>
  </div>
</div>

<h3>Trilha IC — o especialista</h3>

Em vez de inventar uma régua, vale olhar escadas reais: a da **Artsy** (aberta no GitHub), a do **Dropbox** (publicada como site), a do **Yahoo** (reconstruída por ex-funcionários em fóruns) e a da **Talabat**, que eu conheço de dentro — trabalhei lá entre 2021 e 2023, e a matriz de competências deles é o documento mais bem construído que já vi sobre isso. Elas discordam entre si de um jeito muito instrutivo:

<table class="compare-table">
  <thead>
    <tr>
      <th>Nome no BR</th>
      <th>Talabat</th>
      <th>Artsy</th>
      <th>Yahoo</th>
      <th>Google</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Estagiário</td><td>—</td><td>Intern</td><td>—</td><td>L2</td></tr>
    <tr><td><strong>Júnior</strong></td><td>Engineer I <em>(IC1)</em></td><td>Engineer 1 <em>(IC2)</em></td><td>Associate <em>(IC1)</em></td><td>L3</td></tr>
    <tr><td><strong>Pleno</strong></td><td>Engineer II <em>(IC2)</em></td><td>Engineer 2 <em>(IC3)</em></td><td>Software Engineer <em>(IC3)</em></td><td>L4</td></tr>
    <tr><td><strong>Sênior</strong></td><td>Senior Engineer <em>(IC3)</em></td><td>Senior Engineer 1–2 <em>(IC4–IC5)</em></td><td>Senior <em>(IC4)</em></td><td>L5</td></tr>
    <tr><td>Especialista</td><td>Staff <em>(IC4)</em></td><td>Staff <em>(IC6)</em></td><td>Principal <em>(IC5)</em></td><td>L6</td></tr>
    <tr><td>—</td><td>Principal <em>(IC5)</em></td><td>Senior Staff <em>(IC7)</em></td><td>Senior Principal <em>(IC6)</em></td><td>L7</td></tr>
    <tr><td>—</td><td>Sr. Principal <em>(IC6)</em></td><td>Principal <em>(IC8)</em></td><td>Distinguished <em>(IC7–IC8)</em></td><td>L8</td></tr>
  </tbody>
</table>

<div class="callout callout-warn">
  <div class="callout-label">"IC5" não quer dizer nada sozinho</div>
  Siga a linha do IC5 pelas colunas. Na Artsy, <strong>IC5 é Senior Engineer 2</strong> — sênior, ainda dentro do time. Na Talabat e no Yahoo, <strong>IC5 é Principal Engineer</strong> — dois degraus acima, com escopo de organização. A mesma sigla, em três empresas reais, descreve pessoas em estágios completamente diferentes de carreira. E o Dropbox comprime tudo em quatro níveis, onde <strong>L4 é um nível terminal</strong>: a documentação diz explicitamente que se espera que todo engenheiro chegue ao impacto de L4 <em>e possa ficar lá o resto da carreira</em>, sem pressão de subir.
</div>

A regra "Staff vem antes de Principal" vale no Google (L6 → L8), na Meta (E6 → E7), na Artsy (IC6 → IC8) e na Talabat (IC4 → IC5). Não vale no Yahoo nem na Amazon, que não têm degrau de Staff. E repare na coluna da Talabat: júnior IC1, pleno IC2, sênior IC3, Staff IC4, Principal IC5 — é a escada mais próxima da intuição brasileira que eu conheço, e existe de verdade. A régua "óbvia" não é errada; ela só não é universal.

<h3>Trilha de gestão</h3>

A Artsy é útil aqui porque publica o pareamento entre as duas trilhas — coisa que quase nenhuma empresa mostra:

<table class="compare-table">
  <thead>
    <tr>
      <th>Nome comum no BR</th>
      <th>Artsy (gestão)</th>
      <th>Par na trilha IC</th>
      <th>Escopo</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Coordenador / Tech Lead Manager</td><td>Engineering Manager 1 <em>(M2)</em></td><td>Senior Engineer 1 <em>(IC4)</em></td><td>2–4 reports</td></tr>
    <tr><td>Gerente de Engenharia</td><td>Engineering Manager 2 <em>(M3)</em></td><td>Senior Engineer 2 <em>(IC5)</em></td><td>6+ reports</td></tr>
    <tr><td>Gerente sênior</td><td>Senior Eng. Manager <em>(M4)</em></td><td>Staff <em>(IC6)</em></td><td>Começa a gerir gerentes</td></tr>
    <tr><td>Diretor de Engenharia</td><td>Director of Engineering <em>(M5)</em></td><td>Senior Staff <em>(IC7)</em></td><td>Gere gerentes</td></tr>
    <tr><td>Diretor sênior</td><td>Senior Director <em>(M6)</em></td><td>Principal <em>(IC8)</em></td><td>Impacto na empresa</td></tr>
    <tr><td colspan="4"><em>Funções executivas vizinhas — <strong>não são degraus da escada de engenharia</strong>: CIO, CISO, CDO. São pares do CTO, com escopo próprio e linha de reporte que varia por empresa.</em></td></tr>
  </tbody>
</table>

Duas coisas nessa tabela merecem atenção, e as duas contrariam o senso comum brasileiro.

**A primeira: gestão não é um atalho.** A Artsy escreve na documentação que a trilha de gestão só está disponível para quem já chegou a Senior Engineer 2. O Dropbox chega ao mesmo lugar por outro caminho: registra que o tempo de um gestor em L3 é mais curto que o de um IC justamente porque quem migra para gestão *já cresceu através de boa parte do L3 como IC*. Ou seja, nos dois frameworks a gestão começa **depois** do sênior, não em paralelo a ele.

**A segunda: o par lateral não é onde eu disse.** Eu havia afirmado que Staff e Engineering Manager sentam na mesma faixa. Na Artsy, o EM1 pareia com **Senior Engineer 1**, e é o *Senior* Engineering Manager que pareia com Staff. O EM1 lá é explicitamente transitório e interno — eles não contratam ninguém direto nesse nível, e esperam que a pessoa chegue a EM2 em uns 18 meses. A ideia de "mesma faixa" continua certa; o degrau exato, não. Varia por empresa, e é por isso que a tabela existe.

<div class="callout callout-tip">
  <div class="callout-label">Sobre a nomenclatura em si</div>
  Não existe padrão. Cada empresa usa a sua régua — L no Google, E na Meta, SDE na Amazon, ICT na Apple, IC/M na Artsy e no Yahoo, L1–L4 no Dropbox — e as siglas <strong>não são intercambiáveis entre elas</strong>. A coluna de escopo também é indicativa: o mesmo título cobre realidades muito diferentes conforme o tamanho da empresa. Se você está traduzindo seu currículo, descreva o escopo que você de fato teve; é a única coisa que o outro lado consegue ler sem precisar do manual interno da sua empresa anterior.
</div>

<h3>"Júnior" é um termo brasileiro?</h3>

Essa é uma observação que eu carrego há anos, e vale separar o que os dados sustentam do que não sustentam.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">✗ O que se refuta</div>
    <div class="provider-detail">"Junior Software Developer" <strong>existe</strong> em vagas nos EUA e no Reino Unido. Aparece bastante em <em>defense contractors</em>, consultorias, agências de <em>staffing</em> e empresas menores. Não é um termo exclusivo do português.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">✓ O que se confirma</div>
    <div class="provider-detail">Nenhuma escada de big tech tem um degrau chamado "Junior". A entrada é numerada: L3 no Google, E3 na Meta, SDE I na Amazon, ICT2 na Apple. O título some justamente onde a trilha é formalizada.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">→ O que é de fato nosso</div>
    <div class="provider-detail"><strong>"Pleno."</strong> O inglês tem "mid-level", que é um adjetivo descritivo, não um cargo. A tríade fixa júnior/pleno/sênior como escala de três degraus é convenção lusófona — a Farfetch usar "júnior" reforça isso, já que é uma empresa portuguesa.</div>
  </div>
</div>

Ou seja: sua percepção estava mais certa do que errada, só apontando para a palavra vizinha. O que não se traduz não é "júnior" — é **"pleno"**. E isso tem uma consequência prática desagradável: quem se descreve como "pleno" num currículo em inglês está usando um rótulo que o recrutador do outro lado não consegue mapear. O termo que ele espera ler é o título do nível, não a escala.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — a matriz que mudou minha cabeça
  </div>
  <p>Passei por vários processos de avaliação em que "nível" era uma conversa subjetiva entre o gestor e o RH. A primeira vez que vi isso escrito como documento sério foi na Talabat, em Dubai, entre 2021 e 2023. Não era uma lista de tecnologias — era uma grade de 27 competências, com o horizonte de planejamento e o escopo de impacto declarados em cada degrau. Foi lendo aquilo que eu entendi por que tinha passado tanto tempo achando que precisava aprender mais uma linguagem: eu estava tentando subir na única linha da tabela que para de contar no sênior.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">11</div>
  <div class="section-title-wrap"><h2>O que a gente realmente avalia</h2></div>
</div>

Volto à sala de entrevista. Quando o cenário do quadradinho colorido termina, eu não preenchi nenhum campo chamado "sabe JavaScript". Preenchi estes:

<img
  src="{{ site.baseurl }}/assets/img/posts/senioridade-pesos-avaliacao.svg"
  alt="Peso de cada critério na avaliação: análise e decisão somam 60%, ferramentas conhecidas apenas 5%"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Traduzindo cada linha em pergunta concreta que eu me faço:

<table class="compare-table">
  <thead>
    <tr>
      <th>Critério</th>
      <th>O que eu observo na prática</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Análise</strong></td>
      <td>Ele tratou a frase como especificação ou como sintoma? Separou o que foi pedido do que foi assumido?</td>
    </tr>
    <tr>
      <td><strong>Planejamento</strong></td>
      <td>Existe uma ordem no raciocínio, ou é um monte de ideias soltas? Ele consegue dizer o que faria primeiro e por quê?</td>
    </tr>
    <tr>
      <td><strong>Pensamento crítico</strong></td>
      <td>Ele questionou a demanda em si? "Por que 10 por 10?", "isso é para quê?" — entender o objetivo às vezes mata metade do escopo.</td>
    </tr>
    <tr>
      <td><strong>Raciocínio lógico</strong></td>
      <td>Quando eu mudo uma premissa no meio, ele reconstrói a solução ou trava? Essa é a melhor pergunta de follow-up que existe.</td>
    </tr>
    <tr>
      <td><strong>Tomada de decisão</strong></td>
      <td>Diante de uma pergunta que eu recuso responder ("decide você"), ele decide e justifica, ou fica paralisado esperando autorização?</td>
    </tr>
    <tr>
      <td><strong>Comunicação</strong></td>
      <td>Ele explica para um PO ou despeja jargão? Sênior que não consegue traduzir risco técnico em risco de negócio não é sênior, é especialista isolado.</td>
    </tr>
  </tbody>
</table>

Não inventei esses seis critérios. Eles são a versão informal de eixos que aparecem nos frameworks formais. A Artsy avalia IC em quatro dimensões, e a tradução é quase direta:

<table class="compare-table">
  <thead>
    <tr>
      <th>Eixo formal (Artsy)</th>
      <th>O que ele mede</th>
      <th>Equivalente neste artigo</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>Knowledge Leadership</strong></td><td>Profundidade e amplitude técnica na área de negócio</td><td>Profundidade técnica</td></tr>
    <tr><td><strong>Impact</strong></td><td>Natureza dos problemas resolvidos e valor entregue</td><td>Tomada de decisão</td></tr>
    <tr><td><strong>Influence</strong></td><td>Efeito sobre projetos, estratégia e sobre as pessoas ao redor</td><td>Comunicação</td></tr>
    <tr><td><strong>Discretion</strong></td><td>Natureza da orientação <em>recebida</em> e da orientação <em>fornecida</em></td><td>Raio de autonomia</td></tr>
  </tbody>
</table>

O quarto eixo é o mais revelador, e é exatamente o que o cenário do quadradinho mede. "Natureza da orientação recebida" é outra forma de perguntar: **quanto do problema alguém precisou recortar por você antes de te entregar?** O júnior recebe a tarefa já cortada. O sênior recebe a frase crua e faz o próprio corte — e ainda devolve as decisões documentadas para quem pediu.

<div class="callout callout-warn">
  <div class="callout-label">Framework não é checklist</div>
  A documentação do Dropbox abre com esse aviso, e vale repetir aqui: a matriz não é uma lista de caixinhas para marcar. Eles registram inclusive que o foco migrou de "projetos complexos" para <strong>impacto</strong> — não é a complexidade do que você construiu que promove, é o que aquilo mudou. Se a sua empresa trata a matriz como checklist de tecnologias dominadas, ela está usando a ferramenta ao contrário.
</div>

<div class="callout callout-tip">
  <div class="callout-label">O follow-up que revela tudo</div>
  Depois que o candidato apresenta o plano, eu digo: <em>"o cliente mudou de ideia — agora a cor tem que ser a mesma para todos, mas cada usuário vê no fuso dele"</em>. Essa contradição aparente não tem resposta única. O que eu meço não é a solução; é se a pessoa <strong>identifica que é uma contradição</strong> e negocia, ou se sai implementando as duas coisas ao mesmo tempo sem perceber o conflito.
</div>

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — o candidato que "errou" e foi aprovado
  </div>
  <p>Já aprovei candidato que não conhecia metade da stack da vaga e reprovei candidato com o currículo perfeito. O aprovado, diante de um cenário parecido com esse, disse: "eu não sei como se faz isso nessa linguagem, mas o problema aqui é definir de quem é o dia — e isso eu preciso perguntar antes de escolher qualquer biblioteca". Sintaxe se aprende em duas semanas. Esse instinto leva anos.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">12</div>
  <div class="section-title-wrap"><h2>Como treinar isso de propósito</h2></div>
</div>

Vivência acumula sozinha com o tempo, mas dá para acelerar bastante. Algumas coisas que funcionam:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">1. Escreva as suposições</div>
    <div class="provider-detail">Antes de codar qualquer coisa, liste no card as premissas que você está assumindo. Só de escrever, você descobre que metade delas você não tem certeza — e essas viram perguntas.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">2. Mantenha o que você fez</div>
    <div class="provider-detail">Fugir de manutenção é fugir do feedback. O bug que você conserta um ano depois é a aula mais cara e mais eficiente disponível.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">3. Leia post-mortems</div>
    <div class="provider-detail">Relatórios públicos de incidente de grandes empresas são vivência de segunda mão. Você aprende o formato do desastre sem pagar o preço.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">4. Faça a pergunta chata</div>
    <div class="provider-detail">"E se der errado no meio?" numa reunião de refinamento vale mais que qualquer certificação. E é grátis.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">5. Colecione casos-limite</div>
    <div class="provider-detail">Data, fuso, encoding, arredondamento monetário, nome próprio, endereço, nulo, string vazia, concorrência. São sempre os mesmos suspeitos.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">6. Explique para quem não é dev</div>
    <div class="provider-detail">Se você não consegue explicar o risco para o PO, você não entendeu o risco — entendeu só a implementação.</div>
  </div>
</div>

<div class="conclusion">
  <h2>A senioridade não está no que você digita</h2>
  <p>Os três candidatos conseguiriam entregar o quadradinho colorido. Todos os três. Em qualquer linguagem, em qualquer framework. A diferença nunca foi a capacidade de produzir o código — foi <strong>quantas perguntas cada um fez antes de produzi-lo</strong>, e quantas dessas perguntas vieram de já ter visto a coisa quebrar.</p>
  <p>Por isso empilhar tecnologias não te promove. Um pleno que aprende a sétima linguagem continua pleno com sete linguagens. O que move o ponteiro é ampliar o raio do problema que você consegue receber e resolver sozinho — e isso exige alguém te dar problemas maiores, e você aguentar as consequências deles.</p>
  <p>E se você ainda não foi contratado: você não está "preso no júnior". Você ainda não entrou. São problemas diferentes, e o seu tem solução mais rápida do que parece — porque o primeiro emprego, por mais difícil que seja consegui-lo, é justamente o que destrava o único recurso que não dá para estudar em casa: <strong>situações reais, com consequências reais</strong>.</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      DesignGurus. <strong>Google Software Engineer Levels Explained: L3 to L10 and the Terminal Level.</strong>
      <a href="https://www.designgurus.io/blog/google-software-engineer-levels" target="_blank">designgurus.io</a>
    </li>
    <li>
      Candor. <strong>Google Engineering Levels Demystified.</strong>
      <a href="https://candor.co/articles/tech-careers/google-promotions-the-real-scoop-on-leveling-up" target="_blank">candor.co</a>
    </li>
    <li>
      GeekHunter. <strong>Desenvolvedor júnior, pleno ou sênior: entenda as diferenças.</strong>
      <a href="https://blog.geekhunter.com.br/senior-developer-ou-junior/" target="_blank">blog.geekhunter.com.br</a>
    </li>
    <li>
      Revelo. <strong>Desenvolvedor júnior, pleno e sênior: saiba qual contratar.</strong>
      <a href="https://blog.revelo.com.br/desenvolvedor-saiba-qual-nivel-contratar/" target="_blank">blog.revelo.com.br</a>
    </li>
    <li>
      DesignGurus. <strong>Staff Engineer vs Principal Engineer: What Changes Beyond L6.</strong>
      <a href="https://designgurus.substack.com/p/staff-engineer-vs-principal-engineer" target="_blank">designgurus.substack.com</a>
    </li>
    <li>
      DesignGurus. <strong>FAANG Software Engineer Levels Explained: Apple ICT, Google L, Meta E, Amazon SDE.</strong>
      <a href="https://www.designgurus.io/blog/understanding-faang-software-engineer-job-levels" target="_blank">designgurus.io</a>
    </li>
    <li>
      sph.sh. <strong>Understanding Career Levels in Tech Companies.</strong>
      <a href="https://sph.sh/en/posts/career-levels-tech-companies/" target="_blank">sph.sh</a>
    </li>
    <li>
      Talabat. <strong>Engineering Competency Matrix</strong> (documento interno, 2021–2023; inspirado na matriz pública da CircleCI). Consultado por experiência direta do autor.
    </li>
    <li>
      Dropbox. <strong>Engineering Career Framework — Promotion Guidelines &amp; Clarifications.</strong>
      <a href="https://dropbox.github.io/dbx-career-framework/promotion_guidelines.html" target="_blank">dropbox.github.io</a>
    </li>
    <li>
      Artsy. <strong>The Artsy Engineering Ladder.</strong>
      <a href="https://github.com/artsy/README/blob/main/careers/ladder.md" target="_blank">github.com/artsy</a>
    </li>
    <li>
      Quora. <strong>What are the different levels of software engineers at Yahoo?</strong> (relatos de ex-funcionários, não documentação oficial)
      <a href="https://www.quora.com/What-are-the-different-levels-of-software-engineers-at-Yahoo" target="_blank">quora.com</a>
    </li>
    <li>
      MDN Web Docs. <strong>Intl.DateTimeFormat.</strong>
      <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat" target="_blank">developer.mozilla.org</a>
    </li>
    <li>
      IANA. <strong>Time Zone Database.</strong>
      <a href="https://www.iana.org/time-zones" target="_blank">iana.org</a>
    </li>
  </ol>
</div>
