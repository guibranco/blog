---
layout: post
title: "Envio de SMS pela Internet: Da API ao Smartphone como Gateway"
description: "Quatro abordagens para enviar SMS programaticamente — do serviço em nuvem ao modem físico atrás da sua mesa."
date: 2026-03-20
categories: [Infraestrutura, Telecomunicações]
tags: [sms, api, gsm, android, twilio, gateway, simbox, php, iot, automação]
reading_time: 12
image: /assets/img/posts/envio-sms-internet.png
---

<p class="lead">Seja para notificações de sistemas, alertas de monitoramento, autenticação em dois fatores ou automações criativas durante uma viagem, enviar um SMS pela internet é uma necessidade que aparece cedo ou tarde na vida de qualquer desenvolvedor. As opções vão do pragmático ao surpreendentemente artesanal.</p>

O SMS — apesar de ter quase cinco décadas — continua sendo o canal mais universalmente alcançável do mundo. Não precisa de app instalado, não depende de internet no destinatário, não cai em spam silencioso. É por isso que sistemas críticos ainda o usam e por isso que desenvolvedores continuam precisando enviá-lo programaticamente.

Neste artigo, exploramos quatro abordagens distintas para integrar o envio de SMS em sistemas e automações: APIs em nuvem, modems GSM com comandos AT, smartphones como gateways e as chamadas *chipeiras* ou SIM boxes. Cada uma tem seu lugar dependendo do volume, custo, conectividade e grau de controle que você precisa.

<div class="divider">· · ·</div>

<!-- ═══════════════════════════════════════
     SEÇÃO 1 — APIs
════════════════════════════════════════ -->

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap">
    <h2>APIs de SMS em nuvem</h2>
    <span class="badge badge-paid">Pago</span>
  </div>
</div>

A forma mais simples e escalável de enviar SMS de qualquer lugar do mundo é através de uma API de terceiros. Você faz uma requisição HTTP com suas credenciais, especifica o número de destino e o conteúdo da mensagem, e o provedor cuida de todo o resto — roteamento internacional, fallbacks de operadora, relatórios de entrega e conformidade regulatória.

O modelo de precificação é quase sempre baseado em consumo: você paga por mensagem enviada, com valores que variam por país de destino. Para baixo volume, o custo é irrisório. Para alto volume, a negociação direta com o provedor pode fazer diferença significativa.

### Principais provedores

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Twilio</div>
    <div class="provider-detail">O mais popular. SDK para qualquer linguagem, documentação exemplar, dashboard completo.</div>
    <div class="provider-price">~$0.0079/SMS (EUA)</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Amazon SNS</div>
    <div class="provider-detail">Ideal para quem já usa AWS. Integra nativamente com Lambda, SQS, CloudWatch.</div>
    <div class="provider-price">~$0.00645/SMS (EUA)</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Vonage / Nexmo</div>
    <div class="provider-detail">Boa cobertura internacional. APIs bem documentadas. Créditos de teste generosos.</div>
    <div class="provider-price">~€0.0052/SMS (EU)</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Infobip</div>
    <div class="provider-detail">Forte no mercado europeu e LATAM. Robusto para uso empresarial e alto volume.</div>
    <div class="provider-price">Cotação por volume</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">MessageBird</div>
    <div class="provider-detail">Interface limpa, APIs modernas, bom para startups e produtos SaaS.</div>
    <div class="provider-price">~€0.007/SMS (EU)</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Zenvia / Sinch</div>
    <div class="provider-detail">Focados no mercado brasileiro. Suporte localizado e conformidade com Anatel.</div>
    <div class="provider-price">Cotação nacional</div>
  </div>
</div>

### Exemplo prático com Twilio

A implementação é quase trivial. Com credenciais em mãos (`Account SID` e `Auth Token`), basta uma chamada à API REST:

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">PHP 8.2+</div>
  </div>
  <pre><span class="cm">// Instalação: composer require twilio/sdk</span>
<span class="kw">use</span> <span class="va">Twilio\Rest\Client</span>;

<span class="va">$sid</span>   = <span class="st">'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'</span>;
<span class="va">$token</span> = <span class="st">'seu_auth_token'</span>;

<span class="va">$twilio</span> = <span class="kw">new</span> <span class="fn">Client</span>(<span class="va">$sid</span>, <span class="va">$token</span>);

<span class="va">$mensagem</span> = <span class="va">$twilio</span>->messages-><span class="fn">create</span>(
    <span class="st">'+5511999998888'</span>,  <span class="cm">// destinatário</span>
    [
        <span class="st">'from'</span> => <span class="st">'+15017122661'</span>,  <span class="cm">// número Twilio</span>
        <span class="st">'body'</span> => <span class="st">'Olá! Sua reserva foi confirmada. ✈️'</span>,
    ]
);

<span class="kw">echo</span> <span class="va">$mensagem</span>->sid;  <span class="cm">// SM1234567890abcdef...</span></pre>
</div>

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">cURL (puro HTTP — sem SDK)</div>
  </div>
  <pre><span class="kw">curl</span> -X POST <span class="st">"https://api.twilio.com/2010-04-01/Accounts/ACXXX/Messages.json"</span> \
  -u <span class="st">"ACXXX:auth_token"</span> \
  --data-urlencode <span class="st">"To=+5511999998888"</span> \
  --data-urlencode <span class="st">"From=+15017122661"</span> \
  --data-urlencode <span class="st">"Body=Sua entrega chegou!"</span></pre>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Dica de viagem</div>
  APIs em nuvem são ideais quando você está em movimento. Funcionam de qualquer rede com acesso à internet, sem hardware adicional. Para sistemas de notificação de viagens, rastreamento de bagagem ou alertas de check-in, são a solução mais prática.
</div>

O principal cuidado é com a regulamentação local de cada país: muitas operadoras bloqueiam SMS enviados por números internacionais ou exigem registro do remetente (*Sender ID*). Provedores como Twilio e Infobip cuidam disso automaticamente nas regiões onde têm acordos estabelecidos.

<div class="divider">· · ·</div>

<!-- ═══════════════════════════════════════
     SEÇÃO 2 — MODEM GSM
════════════════════════════════════════ -->

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap">
    <h2>Modem GSM e comandos AT+</h2>
    <span class="badge badge-hybrid">Pago / Gratuito</span>
  </div>
</div>

Antes das APIs em nuvem dominarem o cenário, a forma mais comum de enviar SMS programaticamente era através de um modem GSM conectado ao servidor via USB ou porta serial. O modem é essencialmente um chipset de celular em formato compacto — você insere um SIM card, conecta ao computador e se comunica com ele usando o protocolo **AT+**, um conjunto de comandos padronizado pela ITU desde os anos 1980.

Modems GSM populares como o **Huawei E1750**, **SIM800L**, **SIM900** e **Quectel EC21** podem ser encontrados por preços que vão de R$50 a R$300. Depois disso, o custo de envio é simplesmente o plano do SIM card inserido — que pode ser um pré-pago convencional ou um chip M2M de operadora empresarial.

### Comandos AT+ essenciais para SMS

<table class="at-table">
  <thead>
    <tr>
      <th>Comando</th>
      <th>Função</th>
      <th>Resposta esperada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AT</td>
      <td>Verificar conexão com o modem</td>
      <td><code>OK</code></td>
    </tr>
    <tr>
      <td>AT+CMGF=1</td>
      <td>Definir modo texto (em vez de PDU)</td>
      <td><code>OK</code></td>
    </tr>
    <tr>
      <td>AT+CSCS="UTF-8"</td>
      <td>Definir charset para suporte a acentos</td>
      <td><code>OK</code></td>
    </tr>
    <tr>
      <td>AT+CMGS="+5511999998888"</td>
      <td>Iniciar envio para o número especificado</td>
      <td><code>&gt;</code> (aguarda texto)</td>
    </tr>
    <tr>
      <td><em>[texto]</em> + Ctrl+Z</td>
      <td>Finalizar e enviar a mensagem</td>
      <td><code>+CMGS: 42</code> + <code>OK</code></td>
    </tr>
    <tr>
      <td>AT+CSQ</td>
      <td>Verificar força do sinal (0–31)</td>
      <td><code>+CSQ: 18,0</code></td>
    </tr>
    <tr>
      <td>AT+CPIN?</td>
      <td>Verificar status do SIM card</td>
      <td><code>+CPIN: READY</code></td>
    </tr>
    <tr>
      <td>AT+CMGL="ALL"</td>
      <td>Listar mensagens armazenadas na memória</td>
      <td>Lista de mensagens</td>
    </tr>
  </tbody>
</table>

### Automação via PHP com porta serial

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">PHP — comunicação serial com modem GSM</div>
  </div>
  <pre><span class="cm">// Abre a porta serial onde o modem está conectado</span>
<span class="va">$porta</span> = <span class="fn">fopen</span>(<span class="st">'/dev/ttyUSB0'</span>, <span class="st">'r+b'</span>);

<span class="kw">if</span> (!<span class="va">$porta</span>) {
    <span class="kw">throw new</span> <span class="fn">RuntimeException</span>(<span class="st">'Não foi possível abrir a porta serial.'</span>);
}

<span class="cm">// Configura velocidade da serial (Linux)</span>
<span class="fn">exec</span>(<span class="st">'stty -F /dev/ttyUSB0 115200 cs8 -cstopb -parenb'</span>);

<span class="va">$enviar</span> = <span class="kw">function</span>(<span class="va">string</span> <span class="va">$cmd</span>) <span class="kw">use</span> (<span class="va">$porta</span>): <span class="va">string</span> {
    <span class="fn">fwrite</span>(<span class="va">$porta</span>, <span class="va">$cmd</span> . <span class="st">"\r\n"</span>);
    <span class="fn">usleep</span>(<span class="nu">500000</span>);
    <span class="kw">return</span> <span class="fn">fread</span>(<span class="va">$porta</span>, <span class="nu">1024</span>);
};

<span class="va">$enviar</span>(<span class="st">'AT'</span>);
<span class="va">$enviar</span>(<span class="st">'AT+CMGF=1'</span>);
<span class="va">$enviar</span>(<span class="st">'AT+CSCS="UTF-8"'</span>);
<span class="va">$enviar</span>(<span class="st">'AT+CMGS="+5511999998888"'</span>);
<span class="va">$resposta</span> = <span class="va">$enviar</span>(<span class="st">"Sua encomenda chegou!\x1A"</span>); <span class="cm">// \x1A = Ctrl+Z</span>

<span class="fn">fclose</span>(<span class="va">$porta</span>);

<span class="kw">if</span> (<span class="fn">str_contains</span>(<span class="va">$resposta</span>, <span class="st">'+CMGS'</span>)) {
    <span class="kw">echo</span> <span class="st">"SMS enviado com sucesso!\n"</span>;
}</pre>
</div>

<div class="callout callout-warn">
  <div class="callout-label">Atenção</div>
  Em sistemas Windows, a porta será algo como <code>COM3</code> ou <code>COM4</code>. No Linux, tipicamente <code>/dev/ttyUSB0</code> ou <code>/dev/ttyACM0</code>. Use o comando <code>dmesg | grep tty</code> após conectar o modem USB para identificar o dispositivo correto.
</div>

Bibliotecas como **Gammu** (Python/C) e **Kannel** (gateway SMS completo) abstraem toda essa comunicação serial e adicionam filas, logs, suporte a múltiplos modems e relatórios de entrega. Para produção, dificilmente faz sentido escrever a comunicação serial na mão.

A grande vantagem desta abordagem é a **independência de terceiros**: você usa o plano do seu SIM card, sem depender de API externa, sem expor dados a provedores. A desvantagem é a escala — um único modem consegue enviar entre 6 e 10 SMS por minuto, limitado pelo próprio protocolo GSM.

<div class="divider">· · ·</div>

<!-- ═══════════════════════════════════════
     SEÇÃO 3 — SMARTPHONE GATEWAY
════════════════════════════════════════ -->

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap">
    <h2>Smartphone como gateway SMS via HTTP</h2>
    <span class="badge badge-free">Baixo custo / Gratuito</span>
  </div>
</div>

Aqui entra uma das abordagens mais criativas e práticas para quem já tem um smartphone Android disponível: transformá-lo em um gateway SMS que expõe uma API HTTP local. O celular fica conectado à rede Wi-Fi da casa ou escritório, rodando um app que escuta requisições HTTP e usa a interface de SMS nativa do Android para disparar as mensagens.

É o equilíbrio perfeito entre custo e praticidade. Você usa o plano de dados/SMS do celular, não precisa de hardware adicional e tem acesso à rede GSM real sem modem externo. O app faz a ponte entre o mundo HTTP e o mundo GSM.

<div class="gateway-diagram">
  <div class="gw-flow">
    <div class="gw-node">Servidor / Script<small>faz requisição HTTP</small></div>
    <div class="gw-arrow">→</div>
    <div class="gw-node">Rede local Wi-Fi<small>192.168.x.x</small></div>
    <div class="gw-arrow">→</div>
    <div class="gw-node accent">Smartphone Android<small>app gateway rodando</small></div>
    <div class="gw-arrow">→</div>
    <div class="gw-node">Rede GSM<small>operadora do SIM</small></div>
    <div class="gw-arrow">→</div>
    <div class="gw-node">Destinatário<small>qualquer número</small></div>
  </div>
  <p class="gw-caption">Fluxo completo: requisição HTTP interna → gateway Android → SMS real via operadora</p>
</div>

### Aplicativos populares para esta função

<ul class="app-list">
  <li>
    <div class="app-icon">SMS+</div>
    <div class="app-info">
      <strong>SMS Gateway — Android</strong>
      <span>Expõe endpoint REST local. Suporta autenticação por token. Configurável por porta. Opção mais simples e direta.</span>
    </div>
  </li>
  <li>
    <div class="app-icon">GW</div>
    <div class="app-info">
      <strong>Android SMS Gateway (Play Store)</strong>
      <span>Permite configurar porta HTTP personalizada, autenticação básica e suporta múltiplos SIM cards em dispositivos dual-SIM.</span>
    </div>
  </li>
  <li>
    <div class="app-icon">AIO</div>
    <div class="app-info">
      <strong>AIO SMS Gateway</strong>
      <span>Além de HTTP local, suporta webhooks e integração com serviços externos. Interface de gerenciamento pelo browser.</span>
    </div>
  </li>
  <li>
    <div class="app-icon">TSK</div>
    <div class="app-info">
      <strong>Tasker + AutoShare</strong>
      <span>Para entusiastas de automação: o Tasker pode criar fluxos que recebem intents HTTP e disparam SMS, com lógica customizável.</span>
    </div>
  </li>
</ul>

### Como fazer a requisição do servidor

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">PHP — requisição para o gateway Android na rede local</div>
  </div>
  <pre><span class="cm">// O smartphone está em 192.168.1.42 na porta 8080</span>
<span class="va">$gatewayUrl</span> = <span class="st">'http://192.168.1.42:8080/send'</span>;

<span class="va">$payload</span> = [
    <span class="st">'phone'</span>   => <span class="st">'+5511999998888'</span>,
    <span class="st">'message'</span> => <span class="st">'Alerta: servidor respondendo lentamente!'</span>,
    <span class="st">'sim'</span>     => <span class="nu">1</span>,
];

<span class="va">$ch</span> = <span class="fn">curl_init</span>(<span class="va">$gatewayUrl</span>);
<span class="fn">curl_setopt_array</span>(<span class="va">$ch</span>, [
    <span class="va">CURLOPT_POST</span>           => <span class="kw">true</span>,
    <span class="va">CURLOPT_POSTFIELDS</span>     => <span class="fn">json_encode</span>(<span class="va">$payload</span>),
    <span class="va">CURLOPT_HTTPHEADER</span>     => [
        <span class="st">'Content-Type: application/json'</span>,
        <span class="st">'Authorization: Bearer seu_token_aqui'</span>,
    ],
    <span class="va">CURLOPT_RETURNTRANSFER</span> => <span class="kw">true</span>,
    <span class="va">CURLOPT_TIMEOUT</span>        => <span class="nu">10</span>,
]);

<span class="va">$resposta</span> = <span class="fn">curl_exec</span>(<span class="va">$ch</span>);
<span class="va">$status</span>   = <span class="fn">curl_getinfo</span>(<span class="va">$ch</span>, <span class="va">CURLINFO_HTTP_CODE</span>);
<span class="fn">curl_close</span>(<span class="va">$ch</span>);

<span class="kw">if</span> (<span class="va">$status</span> === <span class="nu">200</span>) {
    <span class="kw">echo</span> <span class="st">"SMS enviado via gateway Android!\n"</span>;
}</pre>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Caso de uso viajante</div>
  Deixe um Android antigo com chip pré-pago conectado em casa rodando o gateway. Durante uma viagem internacional, você pode disparar SMS para números brasileiros sem pagar tarifas de roaming — seu script acessa o gateway via VPN ou túnel e o celular em casa faz o envio local.
</div>

O ponto fraco desta solução é a confiabilidade: o celular pode reiniciar, o app pode ser morto pelo sistema operacional para economizar bateria (*doze mode*), ou a bateria pode descarregar. Para uso crítico, é necessário fixar o app na memória nas configurações do Android, manter o celular plugado e monitorar o uptime do gateway.

<div class="divider">· · ·</div>

<!-- ═══════════════════════════════════════
     SEÇÃO 4 — SIM BOX
════════════════════════════════════════ -->

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap">
    <h2>SIM Box — a chipeira industrial</h2>
    <span class="badge badge-paid">Pago</span>
  </div>
</div>

Menos conhecida fora de ambientes de telecom, a **SIM Box** — popularmente chamada de *chipeira* no Brasil — é essencialmente a evolução do modem GSM em formato rack. Trata-se de um hardware dedicado que acomoda múltiplos SIM cards simultaneamente (tipicamente 4, 8, 16, 32 ou até 128 slots) e expõe todos eles como uma interface de telefonia unificada.

O dispositivo se conecta à rede IP e implementa protocolos VoIP/SIP e interfaces de SMS, funcionando como uma ponte entre o mundo digital e a rede celular — mas com capacidade de envio paralelo muito superior ao modem único. É o hardware preferido em call centers, empresas de marketing SMS e operações de comunicação de alto volume.

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">SIM<br>BOX</div>
    <div class="simbox-header-text">
      <h4>GoIP-16 / Dinstar / OpenVox — SIM Box típica</h4>
      <span>Hardware de gateway GSM multi-canal</span>
    </div>
  </div>
  <div class="simbox-body">
    <div class="simbox-specs">
      <div class="spec-item"><div class="spec-label">Canais</div><div class="spec-value">4–128 SIMs</div></div>
      <div class="spec-item"><div class="spec-label">Throughput</div><div class="spec-value">~6 SMS/min/SIM</div></div>
      <div class="spec-item"><div class="spec-label">Protocolos</div><div class="spec-value">SIP / HTTP / SMPP</div></div>
      <div class="spec-item"><div class="spec-label">Conectividade</div><div class="spec-value">Ethernet / Wi-Fi</div></div>
      <div class="spec-item"><div class="spec-label">Preço (16 ch.)</div><div class="spec-value">US$300–600</div></div>
      <div class="spec-item"><div class="spec-label">Gestão</div><div class="spec-value">Web UI / API</div></div>
    </div>
    <p>A maioria dos modelos expõe uma API HTTP REST ou suporte ao protocolo SMPP (Short Message Peer-to-Peer), permitindo integração direta com plataformas de envio como o <strong>Kannel</strong> ou soluções proprietárias. A interface de administração web facilita monitoramento de sinal, balanceamento de carga entre SIM cards e logs de entrega.</p>
  </div>
</div>

### Como funciona na prática

Cada slot da SIM box opera como um modem GSM independente. O firmware do dispositivo orquestra a distribuição de mensagens entre os chips, garantindo que nenhum SIM exceda os limites da operadora. A integração mais comum é via protocolo **SMPP** (Short Message Peer-to-Peer), o protocolo nativo de telecomunicações para troca de SMS em alta velocidade.

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">Integração SMPP com PHP — biblioteca php-smpp</div>
  </div>
  <pre><span class="cm">// composer require onlinecity/php-smpp</span>
<span class="kw">use</span> <span class="va">smpp\SMPP</span>;
<span class="kw">use</span> <span class="va">smpp\transport\TcpIpTransport</span>;
<span class="kw">use</span> <span class="va">smpp\SmppClient</span>;
<span class="kw">use</span> <span class="va">smpp\Address</span>;

<span class="va">$transport</span> = <span class="kw">new</span> <span class="fn">TcpIpTransport</span>(<span class="st">'192.168.1.100'</span>, <span class="nu">2775</span>);
<span class="va">$transport</span>-><span class="fn">setRecvTimeout</span>(<span class="nu">10000</span>);

<span class="va">$smpp</span> = <span class="kw">new</span> <span class="fn">SmppClient</span>(<span class="va">$transport</span>);
<span class="va">$smpp</span>-><span class="fn">bindTransmitter</span>(<span class="st">'usuario'</span>, <span class="st">'senha'</span>);

<span class="va">$from</span> = <span class="kw">new</span> <span class="fn">Address</span>(<span class="st">'SistemaCRM'</span>, <span class="va">SMPP::TON_ALPHANUMERIC</span>);
<span class="va">$to</span>   = <span class="kw">new</span> <span class="fn">Address</span>(<span class="st">'+5511999998888'</span>, <span class="va">SMPP::TON_INTERNATIONAL</span>);

<span class="va">$smpp</span>-><span class="fn">sendSMS</span>(<span class="va">$from</span>, <span class="va">$to</span>, <span class="st">'Cobrança disponível no portal.'</span>);
<span class="va">$smpp</span>-><span class="fn">close</span>();</pre>
</div>

<div class="callout callout-warn">
  <div class="callout-label">Importante — Questão Legal</div>
  SIM boxes são ferramentas legítimas para uso interno corporativo. Porém, seu uso para bypass de tráfego internacional (fazer chamadas/SMS internacionais parecerem locais para burlar tarifas de roaming) é ilegal em muitos países e viola os termos de uso das operadoras. O uso legítimo é em LANs privadas para sistemas internos, com chips regularmente cadastrados.
</div>

Fabricantes como **GoIP**, **Dinstar**, **OpenVox** e **Synway** dominam o mercado de SIM boxes. Muitos modelos também suportam chamadas de voz via VoIP (protocolo SIP), o que os torna versáteis para centrais telefônicas internas que também precisam de SMS.

<div class="divider">· · ·</div>

<!-- ═══════════════════════════════════════
     COMPARATIVO
════════════════════════════════════════ -->

<div class="section-header">
  <div class="section-num">—</div>
  <div class="section-title-wrap">
    <h2>Comparativo das abordagens</h2>
  </div>
</div>

<table class="compare-table">
  <thead>
    <tr>
      <th>Abordagem</th>
      <th>Custo</th>
      <th>Escala</th>
      <th>Int'l</th>
      <th>Hardware</th>
      <th>Offline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>API em nuvem</td>
      <td>Por mensagem</td>
      <td><span class="check">✓</span> Alta</td>
      <td><span class="check">✓</span></td>
      <td>Nenhum</td>
      <td><span class="cross">✗</span></td>
    </tr>
    <tr>
      <td>Modem GSM + AT+</td>
      <td>Plano SIM</td>
      <td><span class="partial">◑</span> Baixa</td>
      <td><span class="partial">◑</span></td>
      <td>Modem USB</td>
      <td><span class="check">✓</span></td>
    </tr>
    <tr>
      <td>Smartphone gateway</td>
      <td>Plano SIM</td>
      <td><span class="partial">◑</span> Média</td>
      <td><span class="partial">◑</span></td>
      <td>Android</td>
      <td><span class="check">✓</span></td>
    </tr>
    <tr>
      <td>SIM Box</td>
      <td>Hardware + SIMs</td>
      <td><span class="check">✓</span> Alta</td>
      <td><span class="partial">◑</span></td>
      <td>SIM Box</td>
      <td><span class="check">✓</span></td>
    </tr>
  </tbody>
</table>

<!-- ═══════════════════════════════════════
     CONCLUSÃO
════════════════════════════════════════ -->

<div class="conclusion">
  <h2>Qual escolher?</h2>
  <p>Para a maioria dos projetos — sistemas web, automações, notificações de apps — uma <strong>API em nuvem como Twilio ou Vonage</strong> é a escolha óbvia. Setup em minutos, escalável, sem hardware, com relatórios de entrega e suporte para dezenas de países.</p>
  <p>Se você precisa de <strong>independência de terceiros</strong> e opera em rede local, o <strong>smartphone como gateway</strong> é surpreendentemente eficaz para volume baixo a médio. Um Android velho com chip pré-pago pode ser tudo que você precisa.</p>
  <p>Para <strong>embarcados, IoT ou cenários sem internet</strong>, o <strong>modem GSM com comandos AT+</strong> continua sendo a solução mais robusta e direta, especialmente com chips M2M que têm cobertura em regiões remotas.</p>
  <p>E para operações de <strong>alto volume com controle total da infraestrutura</strong>, a <strong>SIM Box</strong> entrega paralelismo real com múltiplos SIM cards — desde que usada dentro dos limites legais e dos termos das operadoras.</p>
</div>
