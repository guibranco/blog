---
layout: post
lang: pt-BR
title: "A parede de 50 metros: a IA barateou o tijolo, não a fundação"
description: "Um pedido de uma linha, a mesma IA e dois construtores. Por que as duas paredes saem idênticas na foto, o que só aparece em corte — e o que os dados de 2026 dizem sobre experiência, vibe coding e código gerado por IA."
date: 2026-11-05
categories: [Career]
subcategories:
  - "Career/Seniority"
tags: [inteligencia-artificial, vibe-coding, senioridade, engenharia-de-software, carreira-dev, llm, arquitetura, boas-praticas, qualidade, seguranca, junior-pleno-senior]
cover: /assets/img/posts/parede-de-50-metros/cover.svg
image: /assets/img/posts/parede-de-50-metros/cover.png
medium_tags: [inteligencia-artificial, vibe-coding, programacao, carreira, engenharia-de-software]
---

<p class="lead">Alguém pede: “construa uma parede de 50 metros”. Só isso. Dois construtores recebem o mesmo pedido, têm a mesma inteligência artificial à disposição e, no fim do dia, entregam duas paredes que saem idênticas na foto. Este texto é sobre a diferença entre elas — a que não aparece na foto — e sobre por que ela virou a parte mais valiosa do trabalho de quem escreve software.</p>

O jeito mais comum de contar essa história coloca dois pedreiros lado a lado: um experiente e outro "com IA". É uma comparação torta, porque o experiente também usa IA. Na pesquisa de 2026 do Stack Overflow, com mais de 30 mil respostas, só 17,2% disseram não usar nenhuma ferramenta do tipo.

Então o experimento aqui é outro: **o mesmo pedido, a mesma IA, o mesmo prazo**. A única variável é quem está segurando a ferramenta.

<div class="callout callout-warn">
  <div class="callout-label">O pedido, exatamente como chega</div>
  “Construa uma parede de 50 metros.”
</div>

Uma frase. Vaga de propósito, mas não injusta: é com esse nível de detalhe que demanda de verdade chega numa terça-feira qualquer. Já usei a mesma estrutura — uma demanda de uma linha e respostas muito diferentes — para mostrar [o que separa júnior, pleno e sênior numa entrevista]({{ site.baseurl }}/artigos/junior-pleno-senior-diferencas-praticas-entrevista/). A diferença é que agora todo mundo tem ao lado uma máquina que assenta tijolo mais rápido do que qualquer um de nós.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Construtor A: a parede sobe em uma tarde</h2></div>
</div>

O construtor A faz o que o nome *vibe coding* promete. O termo é de Andrej Karpathy, de fevereiro de 2025: um jeito de programar em que você "se entrega totalmente às vibes" e "esquece que o código sequer existe". Em novembro do mesmo ano, virou a palavra do ano do dicionário Collins.

Ele repassa o pedido. O prompt é o pedido, palavra por palavra. A IA faz o que foi pedido — e faz bem. Em uma tarde a parede está de pé, reta, bonita na foto. Entregue.

Não há nada de burro nisso. É a resposta óbvia e direta, e ela funciona. O ponto é o que **não** aconteceu: ninguém perguntou nada. Para aquela parede existir, alguém teve de decidir que:

- "50 metros" era altura — ou comprimento, tanto faz: alguém escolheu;
- a parede não vai segurar nada além dela mesma;
- o chão aguenta;
- não venta;
- ninguém vai abrir uma porta nela depois.

Naquela entrevista, eram decisões que o júnior tomava sozinho, em silêncio. Aqui acontece algo um pouco pior: elas não foram tomadas por ninguém. A IA preencheu cada lacuna com o que era mais provável para um pedido daquele tamanho — e, quando ninguém diz o contrário, o mais provável é o caso feliz.

<div class="callout callout-tip">
  <div class="callout-label">Justiça seja feita</div>
  Uma IA bem instruída faz essas perguntas: basta pedir. Mas alguém precisa saber respondê-las — e perceber quando a resposta veio errada. O construtor A não sabe que elas existem.
</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Construtor B: sete perguntas antes do primeiro tijolo</h2></div>
</div>

O construtor B usa a mesma IA. Só que, antes do primeiro tijolo, ele pergunta — ao cliente, à IA e a si mesmo:

1. **50 metros de quê?** Altura ou comprimento?
2. **Pra quê?** Muro de divisa, parede de galpão, fachada de prédio, arrimo segurando barranco?
3. **O que vai se apoiar nela?** Um telhado, outro andar, nada?
4. **Que chão é esse?** Alguém fez sondagem?
5. **Venta? Chove? Fica exposta?**
6. **Quem cuida depois?** Vai ter porta, janela, um segundo andar no ano que vem?
7. **Como ela fica de pé enquanto é construída?**

Nenhuma dessas perguntas é sobre assentar tijolo. E cada resposta muda o projeto inteiro — às vezes a ponto de acabar com ele, quando a pergunta 2 revela que o cliente só precisava de uma cerca.

Repare no que **não** mudou: o construtor B não assenta tijolo melhor que o A. Os dois usam a mesma máquina. A diferença acontece antes do primeiro tijolo — e continua depois do último.

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Uma parede de 50 metros não é uma de 5 metros esticada</h2></div>
</div>

Não sou engenheiro civil, então fico na ordem de grandeza — mas ela já basta para mostrar por que "pra quê?" não é filosofia.

A norma brasileira de alvenaria estrutural (NBR 16868-1) limita a esbeltez de uma parede não armada — a altura efetiva dividida pela espessura efetiva — a 24. E, se a parede estiver solta no topo, a altura efetiva conta em dobro.

<div class="callout callout-tip">
  <div class="callout-label">A conta, com um bloco comum de 14 cm</div>
  Travada em cima e embaixo: 24 × 0,14 m = <strong>3,36 m</strong>, mais ou menos um andar. Solta no topo: metade disso, <strong>1,68 m</strong>. Solta e com 50 metros: (2 × 50) ÷ 24 ≈ <strong>4,2 m de espessura</strong> — antes de qualquer conta de vento. É a leitura simplificada de um único critério da norma: serve para dar escala, não para projetar.
</div>

É por isso que o motivo decide tudo. Se os 50 metros são a fachada de um prédio, a parede ganha uma laje a cada três metros e deixa de ser uma parede de 50: vira umas dezessete paredes de três, travadas uma em cima da outra. Se ela fica sozinha, muda de formato.

Os exemplos reais deixam isso visível. O Monadnock Building, em Chicago, é considerado o prédio mais alto do mundo com paredes portantes de tijolo: dezesseis andares, 65,5 metros — e paredes com 1,8 m de espessura no térreo, afinando até 30 cm no último andar. Uma das estruturas de tijolo mais altas do mundo, a chaminé da antiga fundição de Anaconda, nos Estados Unidos, tem 178 metros e é um tubo que afina: 23 metros de diâmetro interno na base, 18 no topo.

Acima de certa altura, parede reta e fina simplesmente não existe: ou ela ganha travamento, ou engrossa na base, ou vira pirâmide e cone. E se os 50 metros forem de comprimento, é outra obra: fundação corrida, pilar de travamento a cada poucos metros, junta de dilatação para o muro não rachar com o calor.

O número era o mesmo. As obras, não.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>No dia da entrega, as duas estão de pé</h2></div>
</div>

Seria fácil escrever este texto dizendo que a parede do construtor A sai torta e cai no primeiro dia. Não é verdade — e quem repete isso perde a discussão para a primeira demo que funciona. De frente, as duas paredes são iguais. Código gerado sem critério compila, passa no teste do caminho feliz e roda bonito na apresentação.

<img src="{{ site.baseurl }}/assets/img/posts/parede-de-50-metros/frente-e-corte.svg"
     alt="Duas paredes de tijolo idênticas vistas de frente no dia 1. Em corte, a parede do construtor A está apoiada direto no chão, sem motivo, fundação, armação nem travamento; a do construtor B tem sapata e estacas, base mais larga, cinta no topo e uma laje a cada andar."
     style="width:100%;max-width:600px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

A diferença está no corte — o que tem embaixo e dentro da parede — e só aparece com o tempo:

- **o vento**: produção de verdade, com carga, concorrência, serviço de terceiro fora do ar e gente mal-intencionada;
- **o segundo andar**: o sistema que cresce e passa a sustentar coisas que ninguém previu;
- **a porta nova**: o requisito que muda e exige abrir um buraco na parede sem derrubá-la.

Existe um dado que mede exatamente essa distância. A Veracode testa modelos de IA em 80 tarefas de código, em quatro linguagens, com prompts que não falam de segurança — ou seja, o pedido de uma linha. Na atualização de março de 2026, a taxa de código que compila tinha subido de cerca de 50%, em 2023, para cerca de 95%. A taxa de código seguro ficou onde sempre esteve: 55%. Quase metade das tarefas saiu com uma vulnerabilidade conhecida.

<div class="callout callout-warn">
  <div class="callout-label">A frente melhorou. O corte, não.</div>
  O resumo do próprio relatório, em tradução livre: os modelos ficaram excelentes em escrever código que compila e falharam em escrever código que é seguro. Os modelos da série GPT-5 com raciocínio estendido se saíram melhor, com 70% a 72% — o que ainda deixa mais de uma tarefa em cada quatro com falha.
</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Traduzindo a obra</h2></div>
</div>

A analogia só presta se der para traduzir. Esta é a minha tradução:

<table class="compare-table">
  <thead>
    <tr><th>Na obra</th><th>No software</th><th>A pergunta</th></tr>
  </thead>
  <tbody>
    <tr><td>O motivo da parede</td><td>O problema de negócio por trás da tarefa</td><td>Pra quê?</td></tr>
    <tr><td>“50 metros” — de quê?</td><td>Número sem unidade: “50 mil usuários” cadastrados, simultâneos ou por dia?</td><td>Quanto, medido como?</td></tr>
    <tr><td>Sondagem do terreno</td><td>Legado, dados reais, integrações que já existem</td><td>Onde isso vai pisar?</td></tr>
    <tr><td>Fundação</td><td>Modelo de dados, contratos entre sistemas, arquitetura</td><td>O que não dá para trocar depois?</td></tr>
    <tr><td>Pilares, vigas e cintas</td><td>Autorização, validação, transações, limites entre módulos</td><td>O que segura o quê?</td></tr>
    <tr><td>Escoras e andaimes</td><td>Testes, feature flags, ambientes separados, rollback</td><td>Como fica de pé durante a obra?</td></tr>
    <tr><td>Prumo e nível a cada fiada</td><td>Revisão de código, CI, ler o que a IA gerou</td><td>Quem conferiu?</td></tr>
    <tr><td>Vento e chuva</td><td>Produção: carga, concorrência, falha de terceiro, ataque</td><td>O que acontece quando dá errado?</td></tr>
    <tr><td>Porta e janela depois</td><td>Manutenção e mudança de requisito</td><td>Quem mexe nisso daqui a um ano?</td></tr>
    <tr><td>A assinatura na ART</td><td>Responsabilidade: quem atende o plantão</td><td>Quem responde se cair?</td></tr>
  </tbody>
</table>

Duas linhas merecem um parágrafo.

**O vento.** Em alguns sistemas ele vem escrito. No PIX, a latência aceitável é publicada em norma, por percentil, e auditada todo mês — contei isso em [A arquitetura do PIX vista por dentro]({{ site.baseurl }}/artigos/arquitetura-do-pix-por-dentro-spi-iso-20022-dez-segundos/). Ali ninguém precisou adivinhar para quanto vento projetar. Na maioria dos sistemas ninguém escreveu nada, e é o construtor B quem tem de perguntar.

**A assinatura.** No Brasil, obra de engenharia tem ART: a Anotação de Responsabilidade Técnica, criada pela Lei 6.496, de 1977, que define quem são os responsáveis técnicos por ela. A IA não assina ART. No software ninguém assina, mas alguém sempre atende o telefone às três da manhã.

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>A mesma parede, em código</h2></div>
</div>

Saindo do canteiro. O pedido agora é este:

<div class="callout callout-warn">
  <div class="callout-label">O pedido</div>
  “Crie um endpoint que exporta os pedidos em CSV.”
</div>

Uma resposta plausível para o pedido como ele chegou — de uma IA ou de qualquer um de nós com pressa:

```csharp
app.MapGet("/pedidos/exportar", async (LojaDbContext db) =>
{
    var pedidos = await db.Pedidos.ToListAsync();

    var csv = new StringBuilder("Id,Cliente,Email,Total\n");
    foreach (var p in pedidos)
        csv.AppendLine($"{p.Id},{p.NomeCliente},{p.EmailCliente},{p.Total}");

    return Results.Text(csv.ToString(), "text/csv");
});
```

De frente, está pronto: compila, devolve um CSV, abre no Excel. Na demo, com cinquenta pedidos de teste, é impecável. Agora o corte:

<table class="compare-table">
  <thead>
    <tr><th>O que a frente não mostra</th><th>Quando aparece</th><th>A pergunta que faltou</th></tr>
  </thead>
  <tbody>
    <tr><td>O endpoint não exige autorização: quem tiver a URL baixa nome e e-mail de todos os clientes</td><td>No primeiro curioso — ou no primeiro incidente de LGPD</td><td>Quem pode exportar isso?</td></tr>
    <tr><td><code>ToListAsync()</code> carrega a tabela inteira na memória</td><td>Com alguns milhões de pedidos</td><td>Quantos pedidos existem hoje? E daqui a dois anos?</td></tr>
    <tr><td>Um cliente chamado “Silva, João” desloca todas as colunas seguintes</td><td>No primeiro nome com vírgula</td><td>O que pode vir dentro de um campo de texto?</td></tr>
    <tr><td>Com cultura pt-BR, <code>1234.56</code> sai como <code>1234,56</code> e o total passa a ocupar duas colunas</td><td>No dia em que o servidor muda</td><td>Em que cultura isso roda?</td></tr>
    <tr><td>Um nome que começa com <code>=</code> vira fórmula quando alguém abre o arquivo na planilha</td><td>Quando alguém descobre</td><td>Quem abre esse arquivo, e com quê?</td></tr>
    <tr><td>Não há paginação, limite de requisições nem teste</td><td>Quando outro sistema passa a depender do endpoint</td><td>Quem vai chamar isso, e com que frequência?</td></tr>
  </tbody>
</table>

Nenhuma dessas seis coisas é exótica, e a IA sabe resolver todas: basta alguém pedir. O construtor B pede porque sabe que as perguntas existem. O A descobre uma de cada vez, em produção.

E repare que a tabela não diz que o código da IA é ruim. Ele responde ao pedido. O pedido é que tinha uma linha.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>O que os números de 2025 e 2026 dizem</h2></div>
</div>

Analogia convence, mas não prova. Estes são os dados mais recentes que encontrei, com as ressalvas de cada um.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">48% confiam, se der para conferir</div>
    <div class="provider-detail">Stack Overflow, 2026: a resposta mais comum sobre a saída de ferramentas de IA foi <strong>“confio quando consigo verificar com facilidade”</strong>. Só <strong>6,6%</strong> confiam nela inclusive para decisões importantes de trabalho.</div>
    <div class="provider-price">14.304 respostas</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">66% esbarram no “quase certo”</div>
    <div class="provider-detail">Stack Overflow, 2025: a maior frustração foram as soluções de IA <strong>“quase certas, mas não exatamente”</strong>; 45% disseram que depurar código gerado por IA toma mais tempo do que esperavam.</div>
    <div class="provider-price">mais de 49 mil respostas</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">IA é amplificador</div>
    <div class="provider-detail">DORA, 2025: o papel principal da IA no desenvolvimento de software é o de <strong>amplificador</strong> — ela aumenta as forças e as fraquezas que a organização já tem.</div>
    <div class="provider-price">State of AI-assisted Software Development</div>
  </div>
</div>

Somados ao teste da Veracode, dizem a mesma coisa por ângulos diferentes: a confiança é condicional, e a condição é conferir. Só que conferir exige saber como é o certo — exatamente o que o construtor B tem e o A não.

<div class="callout callout-warn">
  <div class="callout-label">Cuidado com o número velho</div>
  O estudo mais citado sobre IA e produtividade é o do METR, de julho de 2025: 16 desenvolvedores experientes, 246 tarefas reais em repositórios que eles conheciam bem e uma manchete — com IA, levaram <strong>19% mais tempo</strong>. Em fevereiro de 2026 o próprio METR marcou esse resultado como desatualizado. Com as ferramentas do fim de 2025, a estimativa virou ganho (18% no grupo original, 4% entre os novos participantes, ambos com intervalo de confiança que inclui zero), e os autores avisam que o número provavelmente subestima o efeito real, porque muita gente já não aceita trabalhar sem IA só para participar do estudo. Quem ainda cita “19% mais lento” como fato atual está citando um número que os autores consideram vencido.
</div>

O que não venceu foi a outra metade do achado. Antes do estudo de 2025, os participantes esperavam ficar 24% mais rápidos. Depois, tendo ficado mais lentos, ainda acreditavam ter sido 20% mais rápidos. **Sensação de velocidade não é medida** — e gente experiente errou até o sinal da própria conta.

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Onde o vibe coding está certo</h2></div>
</div>

Nada disso é um texto contra vibe coding. O próprio Karpathy, no tuíte que criou o termo, disse para que ele servia: "projetos descartáveis de fim de semana". Para isso, é ótimo.

Um muro de jardim de um metro não precisa de sondagem, cálculo estrutural nem ART. Se cair, cai na grama, e você levanta outro no sábado seguinte. Protótipo para validar uma ideia, script que roda uma vez, automação pessoal, ferramenta que só você usa: assentar tijolo sem olhar o corte é a decisão certa, e gastar uma semana de engenharia nisso é que seria o erro.

A regra é proporcionalidade — o rigor acompanha a altura:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Muro de jardim</div>
    <div class="provider-detail"><strong>1 metro.</strong> Protótipo, script descartável, automação pessoal. <strong>Se cair:</strong> você refaz em uma tarde.</div>
    <div class="provider-price">Vibe coding, sem culpa</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Parede de casa</div>
    <div class="provider-detail"><strong>3 metros.</strong> Ferramenta interna, MVP com usuário de verdade. <strong>Se cair:</strong> alguém perde trabalho ou dado.</div>
    <div class="provider-price">IA + ler o que foi gerado + testar o caminho crítico</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Prédio</div>
    <div class="provider-detail"><strong>50 metros.</strong> Pagamento, dado pessoal, sistema regulado. <strong>Se cair:</strong> dinheiro, dado e confiança de terceiros.</div>
    <div class="provider-price">Engenharia inteira: a IA acelera, você responde</div>
  </div>
</div>

O problema nunca foi o muro de jardim. É o muro de jardim que ganha um segundo andar sem que ninguém desça para olhar a fundação: o protótipo que vai para produção porque "já está funcionando".

Dois casos públicos mostram o mesmo corte vazio. Em maio de 2025, um pesquisador divulgou a CVE-2025-48757: em 170 projetos gerados pela plataforma Lovable, 303 endpoints estavam sem políticas adequadas de acesso por linha (Row Level Security) no banco, e a chave pública embutida no front-end bastava para ler e alterar dados de usuários sem login. Em fevereiro de 2026 foi a vez do Moltbook, a rede social para agentes de IA cujo criador disse não ter escrito uma linha de código: a empresa de segurança Wiz encontrou o banco de produção aberto pelo mesmo motivo, com 1,5 milhão de tokens de autenticação e dezenas de milhares de e-mails expostos. Nos dois casos o produto funcionava. Era a parede vista de frente.

O que separa uma coisa da outra não é quem digitou. Simon Willison traçou a linha em março de 2025: se a IA escreveu o código e você revisou, testou a fundo e consegue explicar a outra pessoa como ele funciona, isso não é vibe coding — é desenvolvimento de software. A regra dele para código de produção cabe num post-it: não commitar o que você não sabe explicar.

O próprio autor do termo fez a distinção. Um ano depois do tuíte, Karpathy propôs outro nome para o trabalho profissional com agentes — *agentic engineering*: "agentic" porque em 99% do tempo você já não escreve o código diretamente; "engineering" para enfatizar que existe arte, ciência e conhecimento especializado nisso.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>O risco novo: a parede não cai mais aos dois metros</h2></div>
</div>

Antes da IA, a altura da parede era limitada por quem a construía. Quem não sabia o que estava fazendo não ia longe: o muro caía aos dois metros, num trabalho de faculdade ou numa tarefa pequena, e a queda ensinava. Era um erro barato, com professor embutido.

**A IA tirou o limite de altura. Não tirou o risco de queda.** Hoje dá para chegar aos 50 metros sem nunca ter visto um muro cair — e a primeira queda acontece em produção, com dado de cliente dentro.

<img src="{{ site.baseurl }}/assets/img/posts/parede-de-50-metros/matriz-experiencia-ia.svg"
     alt="Matriz de quatro quadros cruzando experiência e uso de IA. Muita experiência sem IA: parede sólida e lenta. Muita experiência com IA: parede sólida e rápida. Pouca experiência sem IA: muro baixo que cai cedo, um erro barato. Pouca experiência com IA: parede alta e sem fundação, o risco novo."
     style="width:100%;max-width:600px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Dos quatro quadros, só um é novidade: o de baixo, à direita. Os outros três sempre existiram.

Há um experimento pequeno, com grupo de controle, sobre o lado do aprendizado. Em janeiro de 2026, pesquisadores da Anthropic colocaram 52 engenheiros, a maioria júnior, para aprender uma biblioteca de Python que nenhum deles conhecia — um grupo com assistente de IA, outro sem. No teste aplicado logo depois, o grupo com IA tirou em média 50%; o grupo sem, 67%. A maior diferença apareceu nas perguntas de depuração, justamente a habilidade de descobrir por que a parede rachou. E o grupo com IA nem chegou a ser mais rápido de forma estatisticamente significativa.

O detalhe que salva: o resultado variou com o jeito de usar. Quem delegou o código inteiro ficou abaixo de 40%. Quem usou a IA para fazer perguntas conceituais e conferir o próprio entendimento ficou em 65% ou mais. São só 52 pessoas, um teste feito na hora e uma associação, não uma prova de causa — os próprios autores tratam o resultado como preliminar. Mas a direção é coerente com o resto: a ferramenta é a mesma, o que muda é quem está segurando.

Para quem já tem experiência, a IA é multiplicador — e multiplicador multiplica o que encontra. Simon Willison resumiu em uma frase: ferramentas de IA amplificam a expertise que já existe. O DORA chegou à mesma conclusão olhando para organizações inteiras. E o mercado já está precificando isso: em [A tesoura do mercado júnior]({{ site.baseurl }}/artigos/a-tesoura-do-mercado-junior/) mostrei que a retomada das vagas de software desde 2025 ficou concentrada em posições sênior.

<div class="section-header">
  <div class="section-num">10</div>
  <div class="section-title-wrap"><h2>A escora que ninguém pediu</h2></div>
</div>

Escora é a parte da obra que some antes da foto. Ninguém pede, ninguém vê, e é ela que decide se um erro vira susto ou desabamento.

<!-- TODO (Guilherme): reescrever este relato na minha voz antes de publicar e confirmar que a empresa continua sem nome. -->
<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — O gateway atrás de uma lista
  </div>
  <p>O caso mais claro de escora que já vivi foi a entrada de um novo gateway de pagamento no meu empregador atual. A parte difícil não era o nosso código: era um ambiente externo, de um terceiro, que não controlávamos e que só dava para exercitar de verdade com usuários e clientes reais. Virar a operação inteira no primeiro dia não era opção.</p>
  <p>A integração subiu atrás de uma feature flag com uma lista de usuários. Para quem estava na lista, o pagamento passava pelo gateway novo; para todo o resto, nada mudava. As primeiras transações reais mostraram erros na configuração da nossa conta do lado do provedor — o tipo de coisa que nenhum sandbox tinha mostrado. Abrimos chamado, o provedor corrigiu e tentamos de novo em produção, sem deploy, com um ou dois clientes afetados em vez da operação inteira.</p>
  <p>A flag não deixou a integração correta. Deixou barato descobrir que ela não estava. Os detalhes técnicos estão em <a href="{{ site.baseurl }}/artigos/feature-flags-vs-ab-testing/">Feature Flags vs. A/B Testing</a> (em inglês).</p>
</div>

Nenhum pedido de uma linha diz "e coloque uma escora". Quem coloca é quem já pensou no que acontece se a parede não aguentar.

<div class="callout callout-tip">
  <div class="callout-label">E este texto?</div>
  Também foi levantado com IA, e isso está nas <a href="{{ site.baseurl }}/notas-editoriais/">notas editoriais</a> do blog. A divisão é a mesma da obra: eu trago a experiência, o contexto, as perguntas e o julgamento; a IA ajuda a estruturar, pesquisar, conectar e expressar. Cada número aqui tem fonte nas referências, e a responsabilidade pelo que está publicado continua sendo minha.
</div>

<div class="section-header">
  <div class="section-num">11</div>
  <div class="section-title-wrap"><h2>Antes do primeiro tijolo</h2></div>
</div>

O que fazer com isso, na prática.

**Se você está começando:**

- **Levante muros baixos à mão, de vez em quando.** Você precisa ver um muro cair enquanto ele ainda é baixo.
- **Use a IA para perguntar "por quê", não só para mandar fazer.** No estudo acima, foi o que separou quem aprendeu de quem só entregou.
- **Peça o corte.** "O que você assumiu?", "o que quebra isso?", "que teste está faltando?" — a IA responde, se alguém perguntar.
- **Não commite o que você não sabe explicar.**

**Se você já tem estrada:**

- **Seu valor mudou de lugar.** Saiu do tijolo e foi para a pergunta, a conferência e a assinatura.
- **Meça, não sinta.** Você pode estar mais lento e jurando que está mais rápido.
- **Escreva a sondagem.** A IA trabalha com o contexto que recebe. O legado, a restrição regulatória, o incidente antigo que explica aquela regra esquisita: nada disso cabe num pedido de uma linha, e é você quem sabe.

**Se você contrata ou lidera:**

- **Demo é foto de frente.** Peça o corte: testes, rollback, quem atende o plantão.
- **A IA amplifica o time que você já tem.** Ela não troca fundação fraca por fundação boa — só faz a parede subir mais rápido em cima da que existe.

<div class="conclusion">
  <h2>Conclusão</h2>
  <p>A IA barateou o tijolo. Assentar tijolo — digitar código — nunca foi a parte cara da obra; era só a parte que aparecia na foto. O que continua custando o mesmo é saber para que serve a parede, o que tem embaixo dela e quem responde se ela cair.</p>
  <p>Com ou sem IA, a parede do construtor B fica de pé pelo motivo de sempre. Com IA, ela só sobe mais rápido. A do construtor A também sobe mais rápido — e esse é o problema: agora dá para errar a 50 metros de altura.</p>
  <p>Antes do próximo prompt, a pergunta é a mesma da obra: 50 metros de quê — e pra quê?</p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>Stack Overflow. <strong>Stack Overflow's 2026 Developer Survey Reveals Positive Sentiment Towards AI — but Trust Remains Conditional</strong> (06/10/2026). <a href="https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional" target="_blank">stackoverflow.co</a></li>
    <li>Simon Willison. <strong>Not all AI-assisted programming is vibe coding (but vibe coding rocks)</strong> (19/03/2025) — reproduz o tuíte original de Andrej Karpathy. <a href="https://simonwillison.net/2025/Mar/19/vibe-coding/" target="_blank">simonwillison.net</a></li>
    <li>Hot Press. <strong>Collins Dictionary announces “vibe coding” as word of the year</strong> (06/11/2025). <a href="https://www.hotpress.com/culture/collins-dictionary-announces-vibe-coding-as-word-of-the-year-23116566" target="_blank">hotpress.com</a></li>
    <li>Parsekian, G. A.; Medeiros, W. A. <strong>Parâmetros de projeto de alvenaria estrutural com blocos de concreto</strong>, 2ª ed., conforme a ABNT NBR 16868:2020 (EdUFSCar, 2021). <a href="https://abcp.org.br/wp-content/uploads/2021/11/Alvenaria_Estrutural_Parametros_Projeto_2ed.pdf" target="_blank">abcp.org.br</a></li>
    <li>Guinness World Records. <strong>Tallest load-bearing brick building</strong> (Monadnock Building). <a href="https://www.guinnessworldrecords.com/world-records/681047-tallest-load-bearing-brick-building" target="_blank">guinnessworldrecords.com</a></li>
    <li>Encyclopaedia Britannica. <strong>Monadnock Building.</strong> <a href="https://www.britannica.com/place/Monadnock-Building" target="_blank">britannica.com</a></li>
    <li>Montana Fish, Wildlife &amp; Parks. <strong>Anaconda Smoke Stack State Park.</strong> <a href="https://fwp.mt.gov/anaconda-smoke-stack" target="_blank">fwp.mt.gov</a></li>
    <li>Veracode. <strong>Spring 2026 GenAI Code Security Update: Despite Claims, AI Models Are Still Failing Security</strong> (24/03/2026). <a href="https://www.veracode.com/blog/spring-2026-genai-code-security/" target="_blank">veracode.com</a></li>
    <li>Confea. <strong>Anotação de Responsabilidade Técnica – ART</strong> (Lei 6.496/1977). <a href="https://www.confea.org.br/servicos-prestados/anotacao-de-responsabilidade-tecnica-art" target="_blank">confea.org.br</a></li>
    <li>Microsoft Learn. <strong>String interpolation in C#</strong> (cultura padrão de strings interpoladas). <a href="https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/strings/interpolation" target="_blank">learn.microsoft.com</a></li>
    <li>Microsoft Learn. <strong>AuthorizationOptions.FallbackPolicy</strong> (nula por padrão). <a href="https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.authorizationoptions.fallbackpolicy" target="_blank">learn.microsoft.com</a></li>
    <li>OWASP. <strong>CSV Injection.</strong> <a href="https://owasp.org/www-community/attacks/CSV_Injection" target="_blank">owasp.org</a></li>
    <li>Stack Overflow. <strong>2026 Developer Survey — Trust in AI tools</strong> (out/2026). <a href="https://survey.stackoverflow.co/2026/ai/data/ai-trust" target="_blank">survey.stackoverflow.co</a></li>
    <li>Stack Overflow Developer Survey 2025, apud VentureBeat. <strong>Stack Overflow data reveals the hidden productivity tax of “almost right” AI code</strong> (29/07/2025). <a href="https://venturebeat.com/ai/stack-overflow-data-reveals-the-hidden-productivity-tax-of-almost-right-ai-code" target="_blank">venturebeat.com</a></li>
    <li>DORA. <strong>State of AI-assisted Software Development 2025.</strong> <a href="https://dora.dev/research/2025/dora-report/" target="_blank">dora.dev</a></li>
    <li>METR. <strong>Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity</strong> (10/07/2025, com aviso de resultado desatualizado). <a href="https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/" target="_blank">metr.org</a></li>
    <li>METR. <strong>We are Changing our Developer Productivity Experiment Design</strong> (24/02/2026). <a href="https://metr.org/blog/2026-02-24-uplift-update/" target="_blank">metr.org</a></li>
    <li>Superblocks. <strong>Lovable Vulnerability Explained: How 170+ Apps Were Exposed</strong> (CVE-2025-48757). <a href="https://superblocks.com/blog/lovable-vulnerabilities" target="_blank">superblocks.com</a></li>
    <li>Infosecurity Magazine. <strong>Vibe-Coded Moltbook Exposes User Data, API Keys and More</strong> (03/02/2026). <a href="https://www.infosecurity-magazine.com/news/moltbook-exposes-user-data-api/" target="_blank">infosecurity-magazine.com</a></li>
    <li>Neowin. <strong>Moltbook had an exposed database with over 20,000 emails, 1.5 million API keys and more.</strong> <a href="https://www.neowin.net/news/moltbook-had-an-exposed-database-with-over-20000-emails-15-million-api-keys-and-more/" target="_blank">neowin.net</a></li>
    <li>The New Stack. <strong>Vibe coding is passé. Karpathy has a new name for the future of software.</strong> (10/02/2026). <a href="https://thenewstack.io/vibe-coding-is-passe/" target="_blank">thenewstack.io</a></li>
    <li>Anthropic. <strong>How AI assistance impacts the formation of coding skills</strong> (29/01/2026). <a href="https://www.anthropic.com/research/AI-assistance-coding-skills" target="_blank">anthropic.com</a></li>
    <li>Simon Willison. <strong>Vibe engineering</strong> (07/10/2025). <a href="https://simonwillison.net/2025/Oct/7/vibe-engineering/" target="_blank">simonwillison.net</a></li>
  </ol>
</div>
