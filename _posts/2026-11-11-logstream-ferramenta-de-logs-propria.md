---
layout: post
lang: pt-BR
title: "LogStream: por que construí minha própria ferramenta de logs (sabendo que não deveria)"
description: "Do echo no PHP procedural ao error_log no cPanel, passando pela Inovação, pelo CrispyWaffle e por quatro anos de Seq: por que criei o LogStream, um servidor de logs em PHP/ReactPHP com UI em React, para rodar numa VM de 1 GB — e o que eu troquei por isso."
date: 2026-11-11
categories: [Coding, Infrastructure]
subcategories:
  - "Coding/PHP"
  - "Coding/Architecture"
  - "Infrastructure/Self-Hosting"
tags: [logs, observabilidade, php, reactphp, react, websocket, mariadb, self-hosting, open-source, side-projects]
cover: /assets/img/posts/logstream/cover.svg
image_alt: "Capa do post: o título LogStream, logs do meu jeito, ao lado de um terminal com o live tail de logs e uma linha do tempo de error_log até LogStream"
card_style: dark
medium_tags: [logs, php, react, observabilidade, open-source]
---

<!-- TODO: atualizar `date:` (e o nome do arquivo) para o dia da publicação — o post só sai junto com a demo pública. -->

<p class="lead">Eu sei que, para quase todo mundo, a resposta certa para "preciso de uma ferramenta de logs" é usar uma pronta. Eu digo isso para os outros. E mesmo assim passei os últimos meses construindo a minha: o <strong>LogStream</strong>, um servidor de ingestão de logs em PHP com uma UI em React. Este texto conta por que, de onde vieram as ideias, como ele funciona por dentro e — principalmente — o que eu abri mão para ter uma ferramenta feita sob medida para a minha infraestrutura.</p>

Os dois repositórios são públicos: o [logstream-server](https://github.com/guibranco/logstream-server) (PHP 8.3 + ReactPHP + Ratchet) e o [logstream-ui](https://github.com/guibranco/logstream-ui) (React + Vite + TypeScript). A instância que eu uso no dia a dia roda só na rede interna, e uma versão de demonstração pública está a caminho.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Vinte anos procurando erro</h2></div>
</div>

Comecei a programar bem antes do primeiro emprego formal, em 2011. Na época de estudo e dos freelas, era PHP procedural — e depois um PHP orientado a objetos ainda engatinhando. Debug era `echo`, `print_r` e `var_dump` espalhados no código até a coisa funcionar. Sem Xdebug, sem ferramenta de log, sem teste unitário, sem teste de integração. Quando o código amadurecia o suficiente para ir para produção, os erros que escapavam iam parar num lugar só: o `error_log`.

Esse hábito sobreviveu mais do que deveria. Boa parte dos meus projetos pessoais roda numa hospedagem compartilhada com cPanel, e por anos o fluxo para descobrir um problema foi este: entrar no cPanel, abrir o gerenciador de arquivos, achar o `error_log` da pasta certa, ler, corrigir, apagar o arquivo e torcer.

O primeiro remendo foi dentro do [Projects Monitor](/blog/artigos/my-infrastructure/), o serviço que acompanha toda a minha infraestrutura: um scanner que varre os `error_log` da hospedagem e uma tabela `messages` para onde algumas aplicações mandavam mensagens específicas. Resolveu metade do problema. A outra metade ficou exposta:

- **Erro transacional não aparece no `error_log`.** Uma cobrança que falhou, um webhook que chegou fora de ordem, uma API externa que respondeu 502 — nada disso é um erro do PHP. Precisa nascer estruturado, com contexto, no momento em que acontece.
- **Nem tudo roda no cPanel.** Os serviços nas VMs da Oracle Cloud — em .NET, em shell, em PHP fora da hospedagem — não têm o mesmo `error_log` padrão. Cada um logava de um jeito, em um lugar.

A tabela `messages` do Projects Monitor nunca foi pensada para ser uma ferramenta de log geral. Não tinha busca decente, não tinha retenção, não tinha live tail. Era uma caixa onde as coisas caíam.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>De onde vem o LogStream</h2></div>
</div>

O LogStream não saiu do nada. Ele é a quarta ou quinta encarnação de uma ideia que me acompanha desde o primeiro emprego.

<img src="{{ site.baseurl }}/assets/img/posts/logstream/linhagem.svg"
     alt="Linha do tempo das ferramentas de log: echo e error_log nos freelas; Inovação de 2011 a 2018 com Redis, RabbitMQ, Elasticsearch e UI em React; CrispyWaffle open source desde 2019; Serilog e Seq de 2020 a 2026 na Farfetch, Talabat e OUTsurance; Projects Monitor com o scanner de error_log; e o LogStream em 2026. Abaixo, o que cada etapa deixou."
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

### Inovação (2011–2018): Redis, RabbitMQ e Elasticsearch — ao mesmo tempo

Passei quase sete anos na Editora Inovação (Inovação Media Brasil), boa parte deles como o principal — às vezes o único — desenvolvedor. O maior produtor de mensagens era o serviço de integração, mas todos os projetos internos e externos, hospedados na Locaweb ou em servidores dentro da própria empresa, mandavam mensagens estruturadas para três destinos: **Redis** (pub/sub), **RabbitMQ** e **Elasticsearch**. Uma UI em React consumia o Redis e o RabbitMQ para mostrar as mensagens em tempo real, e o Elasticsearch alimentava relatórios e gráficos.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — overengineering assumido
  </div>
  <p>Vou ser honesto: eu joguei log nas três ferramentas ao mesmo tempo porque queria aprender cada uma delas — e porque queria colocá-las no currículo como "usei em produção". Foi overengineering puro. No fim, acabei tirando proveito de cada uma: pub/sub para o tempo real, fila para não perder mensagem, Elasticsearch para relatório. Mas a lição mais importante veio do que <em>não</em> funcionou: quando dava problema de verdade, quase sempre eu acabava abrindo os arquivos de log em texto no servidor. A mensagem estruturada atendia a mim e um pouco à equipe; a busca boa, que faria a gente largar o arquivo de texto, nunca chegou.</p>
</div>
<!-- TODO: revisar o personal-story acima na sua voz antes de publicar -->

O código daquela UI (o repositório *Notifications*) continua privado — por um motivo nada nobre: ele guarda segredos no próprio código, de uma época em que eu ainda não usava variáveis de ambiente, muito menos um cofre de segredos.

### CrispyWaffle (2019 →): o produtor não sabe para onde o log vai

A parte de log daquele ecossistema virou o módulo de logs do [CrispyWaffle](https://github.com/guibranco/CrispyWaffle), meu toolkit .NET open source. A ideia central é a separação entre quem produz a mensagem e para onde ela vai: o código chama o log, e uma lista de **providers** decide o destino — console, arquivo de texto com rotação, Redis pub/sub, RabbitMQ, Elasticsearch, Event Log do Windows, Log4Net. O formato da mensagem (`LogMessage`) já carregava aplicação, categoria, nível, host, IP, processo, thread e uma "operação" para agrupar mensagens relacionadas.

### Serilog e Seq (2020–2026): message templates mudam o jogo

Na Farfetch, na Talabat e, principalmente, nos quase quatro anos de OUTsurance, aqui em Dublin, o padrão foi Serilog — e, na OUTsurance, Seq como destino. O conceito que mais mudou a minha forma de investigar problema foi o de [message templates](https://messagetemplates.org/): você escreve `"Charge failed for invoice {InvoiceId}"`, e a ferramenta guarda tanto a frase renderizada quanto o template e cada propriedade separadamente. Dá para achar todas as ocorrências daquela linha de código, independentemente dos valores, e filtrar por qualquer propriedade.

O LogStream se baseia bastante no Seq — não copiando, mas usando como referência alguns filtros e formas de exibir os logs, adaptados ao que eu preciso e corrigindo coisas do Seq que, pessoalmente, não me agradam.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Por que não usar o Seq (ou ELK, ou Loki)?</h2></div>
</div>

Essa é a pergunta certa, e a resposta tem uma parte técnica e uma parte que é só minha.

**A parte técnica é hardware.** O LogStream roda numa VM *micro* da Oracle Cloud: 1 vCPU e 1 GB de RAM, dividida com outros serviços. A documentação do próprio Seq pede, para cargas leves — poucos eventos por segundo, retidos por 30 dias —, no mínimo **2 núcleos e 3,5 GB de RAM**, e recomenda rodá-lo numa máquina dedicada, porque ele tenta usar toda a memória e CPU disponíveis. Elasticsearch é ainda mais faminto. Não cabe.

**A parte que é só minha** pesou tanto quanto:

- **Escolher cada peça da stack.** PHP, que eu domino há duas décadas; o MariaDB que eu já tenho na hospedagem; nada de JVM, nada de container obrigatório.
- **Não depender de terceiros para evoluir.** Se eu quero um filtro novo, eu escrevo. Não abro uma issue e espero um pull request ser aceito.
- **Aprender fazendo.** Eu sempre tive esse perfil: construir do zero para entender como funciona por dentro. O LogStream me obrigou a pensar em ingestão, indexação, retenção e streaming de um jeito que usar o Seq nunca obrigaria.
- **Diversão.** Criar uma ferramenta própria, depois de tantos anos usando as dos outros, é motivação suficiente para um projeto pessoal.

<div class="callout callout-warn">
  <div class="callout-label">O preço</div>
  Ferramenta caseira tem custo: eu perco a maturidade, a performance de busca e o ecossistema de uma ferramenta consolidada, e todo bug é meu. Para uma empresa, quase nunca vale a pena. Para a infraestrutura pessoal de uma pessoa só, rodando em hardware gratuito, a conta fecha — e a seção 08 mostra a porta de saída que eu deixei aberta.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Como ele funciona</h2></div>
</div>

<img src="{{ site.baseurl }}/assets/img/posts/logstream/arquitetura.svg"
     alt="Arquitetura do LogStream: clientes em PHP (Pancake), .NET e shell enviam POST /api/logs com chave e token por aplicação para o logstream-server, um processo PHP 8.3 com ReactPHP e Ratchet que tem servidor HTTP, storage em MariaDB ou JSONL, um executor de retenção e um servidor WebSocket; a logstream-ui recebe cada entrada por WebSocket e faz buscas por GET /api/logs; o Projects Monitor segue como fallback."
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

O servidor é **um único processo PHP** rodando em loop de eventos com [ReactPHP](https://reactphp.org/): um servidor HTTP para ingestão e busca e um servidor WebSocket ([Ratchet](http://socketo.me/)) para o live tail, no mesmo processo. Cada entrada salva é transmitida na hora para todas as UIs conectadas.

**Ingestão por HTTP.** Escolhi HTTP porque era o mais simples e rápido de implementar, seguindo os padrões que eu já conhecia — o mesmo modelo do logger do Projects Monitor. Um `POST /api/logs` aceita uma entrada ou um lote:

```json
{
  "app_key":  "billing-api",
  "app_id":   "production",
  "batch_id": "550e8400-e29b-41d4-a716-446655440000",
  "logs": [
    {
      "level":    "error",
      "category": "payments",
      "message":  "Charge failed for invoice {invoice.id}",
      "context":  { "invoice": { "id": 1234 }, "code": "card_declined" },
      "trace_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
    }
  ]
}
```

**Eventos no estilo Serilog.** A `message` pode ser um template: os placeholders apontam para chaves do `context` (inclusive aninhadas, com ponto), o servidor renderiza a frase e guarda o template original em `message_template`. Placeholder que não resolve fica como está — mensagens que têm chaves por outro motivo não são estragadas. Cada entrada ganha um ID [ULID](https://github.com/ulid/spec), ordenável por tempo, e o IP de quem enviou, capturado pelo servidor (com suporte a proxies confiáveis).

**Dois modos de storage.** O primeiro foi o *file mode*: um arquivo JSONL por dia, o mais fácil de colocar de pé numa máquina de testes e na VM onde ele ficou no início. Logo depois veio o **MariaDB** — o mesmo que eu já tenho na hospedagem —, que trouxe o que faltava para virar um sistema de verdade:

- **uma chave e um token por aplicação** (`X-Api-Key` + `X-Api-Token`), em vez de um segredo compartilhado;
- **filtros apoiados em índice**, incluindo busca de texto no `context` com índice FULLTEXT e filtros `context[order.id]=42` por propriedade;
- **políticas de retenção** por nível, aplicação, ambiente, idade, regex ou glob — aplicadas tanto à mensagem renderizada quanto ao template.

Hoje o file mode serve para a demo e para ambientes restritos que não precisam de banco.

```json
{
  "name": "remove-debug-7d",
  "level": "debug",
  "older_than_days": 7
}
```

**Leitura e escrita separadas.** Quem envia log usa a chave de escrita; a UI usa só uma chave de leitura. Uma UI comprometida não consegue injetar log, e um serviço comprometido não consegue ler o log dos outros.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>A interface</h2></div>
</div>

A [logstream-ui](https://github.com/guibranco/logstream-ui) é um app React + Vite + TypeScript hospedado no GitHub Pages, sem nenhuma configuração em tempo de build: a URL da API, a do WebSocket e a chave de leitura são informadas numa tela de configuração e ficam no navegador. As capturas abaixo usam dados fictícios.

<img src="{{ site.baseurl }}/assets/img/posts/logstream/ui-dashboard.png"
     alt="Dashboard da logstream-ui no tema verde escuro: barra de busca, filtros por aplicação, nível, período, trace ID e batch ID, e uma tabela de eventos com horário, nível, aplicação, categoria e mensagem"
     loading="lazy"
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

O que eu mais uso no dia a dia:

- **Live tail com pausa.** Novas entradas entram em tempo real; ao expandir uma, o fluxo pausa para a tela não andar debaixo do mouse.
- **Propriedades do contexto como filtros.** Cada valor do `context` tem *Find* e *Exclude* — o atalho que eu mais sentia falta de ter num clique só.
- **Navegação por lote e por trace.** Um clique mostra todas as entradas do mesmo `batch_id` ou do mesmo `trace_id`.
- **Filtros avançados** por texto no contexto, por `chave = valor` e por message template.
- **Desempenho e conforto.** Virtualização de linhas para listas grandes e 16 temas, cada um com variante clara e escura.

<img src="{{ site.baseurl }}/assets/img/posts/logstream/ui-evento-expandido.png"
     alt="Um evento de erro expandido na logstream-ui: mensagem completa, categoria, user agent, IP de origem, batch ID, botões para ver o lote e o trace, e as propriedades do contexto com ações de buscar, excluir e copiar"
     loading="lazy"
     style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Os clientes</h2></div>
</div>

Hoje, três jeitos de mandar log para o LogStream convivem na minha infraestrutura.

**PHP, pelo [Pancake](https://github.com/guibranco/pancake).** Meu toolkit PHP ganhou uma classe `LogStream`, usada pelo GStraccini-bot, pelas APIs do API BR e pelo próprio Projects Monitor:

```php
use GuiBranco\Pancake\LogStream;

$logs = new LogStream(
    baseUrl:  'https://logs.example.com',
    appKey:   'billing-api',
    appId:    'production',
    authMode: LogStream::AUTH_API_KEY,
    apiKey:   'billing-api',
    apiToken: getenv('LOGSTREAM_TOKEN'),
);

$logs->error('Charge failed for invoice {invoice.id}', [
    'invoice' => ['id' => 1234],
    'code'    => 'card_declined',
], 'payments');
```

**.NET, direto no WebhooksHandler.** Por enquanto é um cliente simples dentro do serviço que processa os webhooks do GitHub. O destino natural é virar um *sink* do Serilog — ou um provider do CrispyWaffle, ou um pacote NuGet próprio. Ainda não decidi.

**Shell, com cURL.** Os jobs que rodam como serviço do systemd mandam log com uma linha:

```bash
curl -sS -X POST "$LOGSTREAM_URL/api/logs" \
  -H "X-Api-Key: trigger-jobs" -H "X-Api-Token: $LOGSTREAM_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"app_key":"trigger-jobs","app_id":"production","level":"info","message":"tick"}'
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Quando deu errado</h2></div>
</div>

O LogStream ficou **parado de agosto até o último domingo, 08/11/2026**. O motivo foi o file mode: a VM micro, que já era dividida com outros serviços, não aguentou a carga de escrita em disco. O sistema travava sem responder e, algumas vezes, o processo foi morto pelo *OOM killer* do Linux.

Também não descarto que parte da carga tenha vindo de tráfego que não deveria estar lá, numa época em que eu testava muita coisa em paralelo. Isso pesou diretamente em duas decisões: o modelo de **chave e token por aplicação** e o **rate limit por cliente**, que está no backlog.

No domingo, ele voltou rodando sobre o MariaDB. Desde então já passou de **1 milhão de mensagens** — e não por acaso: domingo e segunda são os dias de maior volume na minha infraestrutura, porque é quando o Dependabot abre a maior parte dos pull requests de atualização, e cada um deles gera uma cascata de webhooks, processamento e automação no GStraccini-bot. O servidor segurou bem esse primeiro pico. Ainda estou medindo a carga normal e o consumo de CPU e memória para ter números honestos.

<!-- TODO: preencher com números reais antes de publicar — mensagens/dia em dia normal vs. domingo/segunda, RAM e CPU do processo, tamanho da tabela -->

Enquanto isso, a tabela `messages` do Projects Monitor continua viva como **fallback**. Ela só sai quando o LogStream cobrir tudo o que ela faz — migração gradual, sem big bang.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>O que eu perdi, o que eu ganhei</h2></div>
</div>

<table class="compare-table">
  <thead><tr><th>Critério</th><th>LogStream</th><th>Seq</th><th>ELK</th></tr></thead>
  <tbody>
    <tr><td>Roda em 1 vCPU / 1 GB</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Message templates e propriedades</td><td><span class="check">✓</span></td><td><span class="check">✓</span></td><td><span class="partial">~</span></td></tr>
    <tr><td>Live tail</td><td><span class="check">✓</span></td><td><span class="check">✓</span></td><td><span class="partial">~</span></td></tr>
    <tr><td>Busca rápida em volume grande</td><td><span class="partial">~</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Dashboards e alertas</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Maturidade e comunidade</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Evolui no meu ritmo, na minha stack</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td><td><span class="cross">✗</span></td></tr>
  </tbody>
</table>

Sinceramente, até agora não sinto falta de nada no dia a dia. Parte disso é que eu uso o Claude Code para tirar da frente o trabalho repetitivo, o que me dá liberdade para fazer o que eu quiser na velocidade que eu quiser. A outra parte é que o que falta já está desenhado: entre server e UI, são algo entre 10 e 20 funcionalidades planejadas, abertas como issues.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Próximos passos</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-bolt"></i> Ingestão</div>
    <div class="provider-detail">Listener UDP para quem não quer esperar resposta, compressão gzip nas respostas HTTP e amostragem configurável para descartar uma fração dos logs mais verbosos. Mais adiante, socket, gRPC ou SignalR.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-shield-alt"></i> Segurança</div>
    <div class="provider-detail">Rate limit de ingestão por cliente e chaves de leitura com escopo por aplicação — uma UI que só enxerga os logs de um serviço.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-heartbeat"></i> Operação</div>
    <div class="provider-detail">Saúde de cada cliente com "visto pela última vez", endpoint de métricas e estatísticas, alertas por limiar via webhook e uma tela de visão geral.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-share-square"></i> Integração</div>
    <div class="provider-detail">Encaminhar logs para Loki, Seq ou um webhook qualquer, exportar e arquivar. É a porta de saída: se um dia o LogStream não fizer mais sentido, os logs saem pela porta da frente.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-search"></i> UX</div>
    <div class="provider-detail">Buscas salvas, telas para configurar alertas, amostragem e rate limit, e o status dos encaminhamentos.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-database"></i> Storage</div>
    <div class="provider-detail">Substituir o file mode por um banco feito para logs. O candidato mais natural é o VictoriaLogs: schemaless, guarda cada campo em blocos separados e foi pensado para gastar pouca RAM.</div>
  </div>
</div>

Várias dessas issues estão marcadas como `good first issue` e `help wanted` nos dois repositórios. Se quiser contribuir, é por lá.

<div class="conclusion">
  <h2>Ferramenta pronta é quase sempre melhor. Quase.</h2>
  <p>O LogStream não compete com o Seq, nem quer competir. Ele existe porque eu tinha uma restrição real de hardware, um problema específico — erro transacional e serviços espalhados fora da hospedagem — e vinte anos de vontade de entender como as coisas funcionam por dentro. Cada etapa deixou uma ideia: a Inovação me ensinou que mensagem estruturada vale mais que texto solto, o CrispyWaffle que o produtor não deve saber para onde o log vai, e o Seq que message templates mudam a forma de investigar.</p>
  <p>Se você está pensando em fazer o mesmo, a minha recomendação continua sendo usar uma ferramenta pronta. Mas, se a conta fechar para você — pelo hardware, pelo aprendizado ou pela diversão —, os dois repositórios estão abertos. <!-- TODO: link da demo pública quando estiver no ar --></p>
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>guibranco. <strong>logstream-server.</strong> <a href="https://github.com/guibranco/logstream-server" target="_blank">github.com</a></li>
    <li>guibranco. <strong>logstream-ui.</strong> <a href="https://github.com/guibranco/logstream-ui" target="_blank">github.com</a></li>
    <li>guibranco. <strong>CrispyWaffle — módulo de logs.</strong> <a href="https://github.com/guibranco/CrispyWaffle" target="_blank">github.com</a></li>
    <li>guibranco. <strong>Pancake — LogStream.</strong> <a href="https://guibranco.github.io/pancake/user-guide/logstream/" target="_blank">guibranco.github.io</a></li>
    <li>Datalust. <strong>Seq — System Requirements.</strong> <a href="https://datalust.co/docs/system-requirements" target="_blank">datalust.co</a></li>
    <li><strong>Message Templates.</strong> <a href="https://messagetemplates.org/" target="_blank">messagetemplates.org</a></li>
    <li>VictoriaMetrics. <strong>VictoriaLogs — FAQ.</strong> <a href="https://docs.victoriametrics.com/victorialogs/faq/" target="_blank">docs.victoriametrics.com</a></li>
    <li><strong>ReactPHP.</strong> <a href="https://reactphp.org/" target="_blank">reactphp.org</a> · <strong>Ratchet.</strong> <a href="http://socketo.me/" target="_blank">socketo.me</a></li>
  </ol>
</div>
