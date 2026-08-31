---
layout: post
lang: pt-BR
title: "CLT, PJ ou MEI? Qual devo escolher"
description: "As diferenças entre CLT, PJ e MEI para quem trabalha com tecnologia — com a conta completa refeita com os números de 2026: tabelas de INSS e IRRF, Simples Nacional, Fator R, teto do MEI e o multiplicador real de conversão."
date: 2020-01-23
last_modified_at: 2026-08-19
categories: [Career]
subcategories:
  - "Career/Freelancing"
tags: [clt, pj, mei, carreira, financeiro, impostos, simples-nacional, fator-r, inss, irpf, fgts, pejotizacao, salario, ti, desenvolvedor]
reading_time: 24
cover: /assets/img/posts/clt-pj-mei-2026.svg
image: /assets/img/posts/clt-pj-mei-2026.png
---

<p class="lead">Um dos assuntos que mais gera dúvida entre o pessoal de TI, principalmente desenvolvedores, é quando optar por CLT ou PJ — quais as diferenças, obrigações e benefícios de cada um. Escrevi este artigo em janeiro de 2020. Seis anos depois, praticamente todos os números envelheceram e algumas das regras simplesmente deixaram de existir. Refiz a conta inteira.</p>

<div class="callout callout-warn">
  <div class="callout-label">Revisão de agosto de 2026</div>
  <p>O texto original é de <strong>23/01/2020</strong>. Esta versão foi reescrita em <strong>19/08/2026</strong> com dados verificados na data. O que mudou desde a publicação original:</p>
  <ul>
    <li>A <strong>EIRELI deixou de existir</strong> (Lei 14.195/2021). Quem estava nela virou SLU automaticamente.</li>
    <li>A tabela do <strong>INSS virou progressiva</strong> (7,5% a 14%) — não é mais alíquota única sobre o salário inteiro.</li>
    <li>O <strong>Imposto de Renda mudou de forma histórica</strong>: desde 01/01/2026, quem tem rendimento tributável de até R$ 5.000,00 por mês não paga nada (Lei 15.270/2025).</li>
    <li>Aquele "<strong>6% de imposto com o CNAE certo</strong>" que eu escrevi em 2020 estava incompleto: os 6% dependem do <strong>Fator R</strong>, calculado mês a mês. Sem ele, a alíquota inicial é 15,5%.</li>
    <li>O <strong>teto do MEI continua em R$ 81.000</strong> desde 2018 — e desenvolvedor continua sem poder usá-lo.</li>
    <li>O <strong>STF ainda não decidiu</strong> se a contratação PJ é lícita como regra (Tema 1389). Isso é novo e importa muito.</li>
  </ul>
</div>

Em poucas palavras, e isso não mudou em seis anos: quem se sente ameaçado de perder o emprego e/ou não tem educação financeira deve optar pelo CLT se possível. Quem sabe gerenciar o próprio dinheiro, investe, tem reserva de emergência e se considera com pouca chance de ficar desempregado por longos períodos pode optar pelo PJ sem medo.

Sabendo negociar, o valor PJ pode resultar no mesmo líquido do CLT, com uma diferença: você recebe tudo mensalmente e decide onde gastar ou aplicar o excedente. Por isso a educação financeira é indispensável para quem opta pelo PJ.

O que mudou é que hoje eu consigo colocar número em cima disso. E o número surpreende.

<img
  src="{{ site.baseurl }}/assets/img/posts/clt-pj-multiplicador-2026.svg"
  alt="Gráfico comparando o multiplicador de custo do empregador com o multiplicador de equivalência do trabalhador PJ, para salários CLT de R$ 6.000, R$ 12.000 e R$ 20.000"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap">
    <h2>Os números que você precisa ter na mão</h2>
  </div>
</div>

Toda discussão de CLT × PJ que ignora os parâmetros do ano vira achismo. Estes são os de 2026:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Salário mínimo</div>
    <div class="provider-detail">Base do DAS do MEI, do piso do seguro-desemprego e do INSS mínimo.</div>
    <div class="provider-price">R$ 1.621,00 · Decreto 12.797/2025</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Teto do INSS</div>
    <div class="provider-detail">Acima disso não há contribuição nem benefício. Desconto máximo do empregado: R$ 988,09.</div>
    <div class="provider-price">R$ 8.475,55</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Isenção de IR</div>
    <div class="provider-detail">Rendimento tributável mensal até esse valor: imposto zero. Redução parcial até R$ 7.350,00.</div>
    <div class="provider-price">R$ 5.000,00 · Lei 15.270/2025</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Teto do MEI</div>
    <div class="provider-detail">Inalterado desde 2018. Média de R$ 6.750,00/mês, sem teto mensal fixo.</div>
    <div class="provider-price">R$ 81.000,00/ano</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Teto do Simples Nacional</div>
    <div class="provider-detail">Acima disso, Lucro Presumido ou Lucro Real.</div>
    <div class="provider-price">R$ 4.800.000,00/ano</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Teto do seguro-desemprego</div>
    <div class="provider-detail">De 3 a 5 parcelas. Quem tem média salarial acima de R$ 3.703,99 recebe o teto.</div>
    <div class="provider-price">R$ 2.518,65/parcela</div>
  </div>
</div>

### Tabela do INSS 2026 (empregado CLT)

A mudança mais mal compreendida desde 2020: o desconto é **progressivo**. A alíquota de cada faixa incide só sobre a parcela do salário que cai naquela faixa.

| Faixa de salário de contribuição | Alíquota |
|---|---|
| Até R$ 1.621,00 | 7,5% |
| De R$ 1.621,01 a R$ 2.902,84 | 9% |
| De R$ 2.902,85 a R$ 4.354,27 | 12% |
| De R$ 4.354,28 a R$ 8.475,55 | 14% |

Quem ganha R$ 12.000,00 não paga 14% de INSS. Paga R$ 988,09 — o teto —, o que dá 8,2% efetivos.

### Imposto de Renda 2026

A tabela progressiva mensal continua a mesma de 2023 (isenção formal em R$ 2.428,80, desconto simplificado de R$ 607,20, dedução de R$ 189,59 por dependente). O que a Lei 15.270/2025 criou foi um **redutor aplicado depois** do cálculo normal:

<table class="compare-table">
  <thead>
    <tr><th>Rendimento tributável mensal</th><th>Redutor</th></tr>
  </thead>
  <tbody>
    <tr><td>Até R$ 5.000,00</td><td>Zera o imposto <span class="check">✓</span></td></tr>
    <tr><td>De R$ 5.000,01 a R$ 7.350,00</td><td>R$ 978,62 − (0,133145 × rendimento) <span class="partial">~</span></td></tr>
    <tr><td>Acima de R$ 7.350,00</td><td>Nenhum <span class="cross">✗</span></td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Por que isso muda a conta do PJ</div>
  O pró-labore de um PJ costuma ficar entre R$ 3.000,00 e R$ 5.500,00. Até 2025, esse valor pagava IR. Em 2026, quase sempre não paga. Sozinha, essa mudança melhorou o lado PJ da equação em algumas centenas de reais por mês — e barateou a estratégia do Fator R, que você vai ver na seção 05.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap">
    <h2>Definições — o que mudou desde 2020</h2>
  </div>
</div>

### CLT

CLT, ou Consolidação das Leis do Trabalho, é a lei de 1943 que regula o direito trabalhista. É sinônimo de "carteira assinada": o empregador registra a contratação na CTPS, hoje digital.

O que o regime garante, com os valores de 2026:

- **Férias remuneradas** — 30 dias corridos após 12 meses trabalhados, pagos com adicional de 1/3.
- **13º salário** — proporcional ao tempo trabalhado, em duas parcelas entre novembro e dezembro.
- **FGTS** — depósito de 8% do salário pela empresa, todo mês, mais 8% sobre o 13º.
- **Multa de 40% do FGTS** — em demissão sem justa causa, sobre todo o saldo depositado.
- **Seguro-desemprego** — de 3 a 5 parcelas, de R$ 1.621,00 a R$ 2.518,65 cada.
- **Aviso prévio** — 30 dias, mais 3 dias por ano trabalhado, limitado a 90.
- **INSS** — desconto progressivo de até R$ 988,09 do empregado; a empresa paga a parte patronal por fora.
- **Estabilidades e licenças** — acidente de trabalho, gestante, licença-maternidade e paternidade.

### PJ

PJ, ou Pessoa Jurídica, é a formalização de uma empresa — uma pessoa física constitui um CNPJ além do CPF. Trabalhar sem emitir nota fiscal e sem CNPJ configura trabalho informal e, na maioria dos casos, é ilegal.

**Tipo societário** — e aqui está a primeira correção grande em relação ao texto de 2020:

| Tipo | Situação em 2026 |
|---|---|
| EI | Empresa Individual. Existe, mas o patrimônio do empresário e da empresa se misturam. |
| EIRELI | **Extinta pela Lei 14.195/2021.** Todas foram convertidas automaticamente em SLU. |
| SLU | Sociedade Limitada Unipessoal. Sucessora da EIRELI, **sem capital social mínimo** e sem sócio. É hoje a escolha padrão do PJ solo. |
| LTDA | Sociedade Limitada com dois ou mais sócios, responsabilidade limitada ao capital social. |
| S.A. | Sociedade Anônima, capital dividido em ações. Faz sentido para quem troca de sócio com frequência. |

<div class="callout callout-warn">
  <div class="callout-label">Se você abriu empresa antes de 2021</div>
  Sua EIRELI já é uma SLU por força do art. 41 da Lei 14.195/2021 — a conversão foi automática nas Juntas Comerciais, sem necessidade de qualquer ato seu. Vale, ainda assim, fazer uma alteração contratual para tirar a sigla "EIRELI" do nome e dos documentos, porque cadastros antigos ainda geram atrito com bancos e clientes.
</div>

**Enquadramento de porte**

| Porte | Faturamento anual |
|---|---|
| MEI | Até R$ 81.000 |
| ME | Até R$ 360.000 |
| EPP | De R$ 360.000 até R$ 4,8 milhões |
| Médio/Grande | Acima de R$ 4,8 milhões |

**Enquadramento tributário**

| Regime | Para quem |
|---|---|
| SIMEI | Exclusivo para MEI |
| Simples Nacional | ME e EPP |
| Lucro Presumido | Qualquer porte até o limite legal — costuma compensar acima de ~R$ 30 mil/mês com folha baixa |
| Lucro Real | Obrigatório acima de R$ 78 milhões/ano e em alguns setores |

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap">
    <h2>Quanto um CLT custa de verdade para a empresa</h2>
  </div>
</div>

Em 2020 eu escrevi que a empresa gasta cerca de 1,7× o salário registrado. A regra continua boa, mas a faixa real é mais larga: de **1,73× a 1,97×**, e ela cai conforme o salário sobe — porque os benefícios de valor fixo (vale-refeição, plano de saúde) pesam proporcionalmente menos.

Veja o detalhamento para um desenvolvedor pleno/sênior com salário CLT de **R$ 12.000,00**:

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">CLT</div>
    <div class="simbox-header-text">
      <h4>Custo mensal para a empresa — salário de R$ 12.000,00</h4>
      <span>Empresa fora do Simples · encargos de 26,8% (INSS patronal 20% + RAT 1% + terceiros 5,8%)</span>
    </div>
  </div>
  <div class="simbox-body">
    <div class="simbox-specs">
      <div class="spec-item"><div class="spec-label">Salário bruto</div><div class="spec-value">R$ 12.000,00</div></div>
      <div class="spec-item"><div class="spec-label">Provisão 13º</div><div class="spec-value">R$ 1.000,00</div></div>
      <div class="spec-item"><div class="spec-label">Provisão férias + 1/3</div><div class="spec-value">R$ 1.333,33</div></div>
      <div class="spec-item"><div class="spec-label">Encargos s/ salário</div><div class="spec-value">R$ 4.176,00</div></div>
      <div class="spec-item"><div class="spec-label">Encargos s/ provisões</div><div class="spec-value">R$ 812,00</div></div>
      <div class="spec-item"><div class="spec-label">Provisão multa FGTS</div><div class="spec-value">R$ 458,67</div></div>
      <div class="spec-item"><div class="spec-label">Vale refeição</div><div class="spec-value">R$ 1.100,00</div></div>
      <div class="spec-item"><div class="spec-label">Plano de saúde</div><div class="spec-value">R$ 600,00</div></div>
    </div>
    <p style="font-size:14px;color:#5a534a;line-height:1.65;">Custo total mensal para a empresa: <strong>R$ 21.480,00</strong> — ou <strong>1,79×</strong> o salário registrado. Em doze meses: <strong>R$ 257.760,00</strong>.</p>
  </div>
</div>

O mesmo cálculo em três níveis salariais:

<table class="compare-table">
  <thead>
    <tr><th>Salário CLT</th><th>Custo mensal p/ a empresa</th><th>Multiplicador</th></tr>
  </thead>
  <tbody>
    <tr><td>R$ 6.000,00</td><td>R$ 11.590,00</td><td>1,93×</td></tr>
    <tr><td>R$ 12.000,00</td><td>R$ 21.480,00</td><td>1,79×</td></tr>
    <tr><td>R$ 20.000,00</td><td>R$ 34.666,67</td><td>1,73×</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Detalhe que quase ninguém considera</div>
  Se a contratante é <strong>optante pelo Simples Nacional</strong> nos Anexos III ou V, a contribuição patronal (CPP) já está embutida no DAS dela. Nesse caso o multiplicador cai para algo perto de <strong>1,45× a 1,55×</strong>, e a margem que ela tem para te pagar como PJ é bem menor. Vale perguntar o regime tributário da empresa antes de negociar.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap">
    <h2>Quanto o CLT recebe de verdade</h2>
  </div>
</div>

O erro clássico é comparar o líquido mensal do CLT com o faturamento bruto do PJ. São grandezas diferentes. O CLT recebe treze salários e meio por ano, mais benefícios, mais FGTS.

Ainda no salário de R$ 12.000,00:

| Componente | Valor |
|---|---|
| Salário líquido mensal (após INSS de R$ 988,09 e IRRF de R$ 2.119,55) | R$ 8.892,36 |
| Salário líquido × 12 | R$ 106.708,32 |
| 13º líquido | R$ 8.892,36 |
| Férias + 1/3, líquidas | R$ 11.792,36 |
| Vale-refeição e plano de saúde (12 meses) | R$ 20.400,00 |
| **Subtotal em caixa no ano** | **R$ 147.793,04** |
| FGTS depositado (8% sobre 13 salários) | R$ 12.480,00 |
| **Pacote anual total** | **R$ 160.273,04** |

A carga tributária pessoal do CLT nesse patamar é de **25,9% sobre o bruto**. Guarde esse número.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap">
    <h2>O lado PJ — e o Fator R, que eu errei em 2020</h2>
  </div>
</div>

Em 2020 eu escrevi que, com o CNAE 6209-1/00, você pagaria "apenas 6% de tributos" pelo Simples Nacional. Isso está errado, ou pelo menos incompleto, e vale a correção pública: **os 6% dependem do Fator R**.

Todos os CNAEs de tecnologia relevantes — 6201-5/01 (desenvolvimento sob encomenda), 6202-3/00, 6203-1/00, 6204-0/00 (consultoria) e 6209-1/00 (suporte e manutenção) — são atividades de natureza intelectual e caem por padrão no **Anexo V**, cuja alíquota inicial é **15,5%**. Só migram para o **Anexo III**, com alíquota inicial de 6%, se o Fator R for igual ou superior a 28%.

```
Fator R = Folha de Pagamento (12 meses) ÷ Receita Bruta (12 meses)

Onde "folha" inclui: salários, pró-labore dos sócios,
13º, férias, INSS patronal e FGTS.
Não inclui: aluguéis e distribuição de lucros.

Fator R ≥ 0,28  →  Anexo III  (6% a 33%)
Fator R <  0,28  →  Anexo V   (15,5% a 30,5%)
```

O cálculo é **refeito todo mês**. Na prática, para o PJ solo, isso significa fixar o pró-labore em pelo menos 28% do faturamento.

<table class="compare-table">
  <thead>
    <tr><th>Faturamento em 12 meses (RBT12)</th><th>Anexo III</th><th>Anexo V</th></tr>
  </thead>
  <tbody>
    <tr><td>Até R$ 180.000,00</td><td>6,00%</td><td>15,50%</td></tr>
    <tr><td>De R$ 180.000,01 a R$ 360.000,00</td><td>11,20% − R$ 9.360,00</td><td>18,00% − R$ 4.500,00</td></tr>
    <tr><td>De R$ 360.000,01 a R$ 720.000,00</td><td>13,50% − R$ 17.640,00</td><td>19,50% − R$ 9.900,00</td></tr>
    <tr><td>De R$ 720.000,01 a R$ 1.800.000,00</td><td>16,00% − R$ 35.640,00</td><td>20,50% − R$ 17.100,00</td></tr>
    <tr><td>De R$ 1.800.000,01 a R$ 3.600.000,00</td><td>21,00% − R$ 125.640,00</td><td>23,00% − R$ 62.100,00</td></tr>
    <tr><td>De R$ 3.600.000,01 a R$ 4.800.000,00</td><td>33,00% − R$ 648.000,00</td><td>30,50% − R$ 540.000,00</td></tr>
  </tbody>
</table>

A alíquota da tabela é a **nominal**; a efetiva sai de `(RBT12 × alíquota − parcela a deduzir) ÷ RBT12`. Na primeira faixa, efetiva e nominal coincidem.

<div class="callout callout-warn">
  <div class="callout-label">O preço de errar o Fator R</div>
  Faturando R$ 15.000,00 por mês, o DAS no Anexo III é de <strong>R$ 900,00</strong>. No Anexo V, <strong>R$ 2.325,00</strong>. A diferença é de <strong>R$ 17.100,00 por ano</strong> — mais de um mês de faturamento, perdido por não acompanhar um cálculo que o contador deveria fazer todo mês.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap">
    <h2>MEI — as regras, os números e por que dev fica de fora</h2>
  </div>
</div>

Essa seção não existia no texto original, e é a dúvida que mais recebo. Vamos por partes.

### O limite

O teto do MEI é de **R$ 81.000,00 por ano**, valor congelado desde 1º de janeiro de 2018. Dividido por doze, dá uma média de **R$ 6.750,00 por mês** — mas é importante entender que **não existe teto mensal**. Você pode faturar R$ 12.000,00 em um mês e R$ 2.000,00 no outro; o que a Receita olha é a soma de janeiro a dezembro.

- **Abertura no meio do ano:** o limite é proporcional aos meses restantes. Abrindo em junho, são 7 meses → R$ 47.250,00.
- **Estouro de até 20%** (até R$ 97.200,00): você continua MEI até dezembro, paga um DAS complementar e é desenquadrado em janeiro seguinte.
- **Estouro acima de 20%:** o desenquadramento **retroage a janeiro do ano corrente**, com recálculo de tributos como ME, multa e juros Selic.

Isso não é teórico: só em 2024, a Receita Federal desenquadrou mais de **570 mil MEIs** por excesso de faturamento, cruzando notas fiscais, maquininhas, e-Financeira e marketplaces.

### O custo — e o que ele cobre

O MEI paga um valor **fixo**, independente do quanto fatura. Em 2026, com o salário mínimo em R$ 1.621,00:

<table class="compare-table">
  <thead>
    <tr><th>Atividade</th><th>Composição</th><th>DAS mensal</th></tr>
  </thead>
  <tbody>
    <tr><td>Comércio e indústria</td><td>R$ 81,05 (INSS) + R$ 1,00 (ICMS)</td><td>R$ 82,05</td></tr>
    <tr><td>Prestação de serviços</td><td>R$ 81,05 (INSS) + R$ 5,00 (ISS)</td><td>R$ 86,05</td></tr>
    <tr><td>Comércio e serviços</td><td>R$ 81,05 + R$ 1,00 + R$ 5,00</td><td>R$ 87,05</td></tr>
    <tr><td>MEI caminhoneiro</td><td>R$ 194,52 (INSS, 12% do mínimo) + ICMS e/ou ISS</td><td>R$ 195,52 a R$ 200,52</td></tr>
  </tbody>
</table>

A parcela do INSS é 5% do salário mínimo e se reajusta sozinha todo ano. ICMS e ISS estão congelados em R$ 1,00 e R$ 5,00 desde 2006. Vencimento no dia 20 de cada mês.

**O que esses R$ 86,05 cobrem** — seis benefícios previdenciários, respeitadas as carências:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-check-circle"></i> Coberto pelo DAS</div>
    <div class="provider-detail">Aposentadoria por idade · Aposentadoria por invalidez · Auxílio-doença · Salário-maternidade · Pensão por morte e auxílio-reclusão (aos dependentes).</div>
    <div class="provider-price">Benefício limitado a 1 salário mínimo</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-times-circle"></i> Não coberto</div>
    <div class="provider-detail">Aposentadoria por tempo de contribuição, valor de benefício acima do mínimo, FGTS, 13º, férias, seguro-desemprego.</div>
    <div class="provider-price">Precisa de complementação ou reserva própria</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Complementação do INSS do MEI</div>
  Os 5% do DAS só dão direito à aposentadoria por idade no piso. Para que o período conte como tempo de contribuição e para poder ter benefício acima do mínimo, é preciso recolher os <strong>15% restantes</strong> em GPS separada (código 1910) — R$ 243,15 por mês em 2026, chegando aos 20% totais. Muita gente descobre isso perto de se aposentar, quando já não dá para corrigir.
</div>

### A conta do MEI no teto

<table class="compare-table">
  <thead>
    <tr><th>Item</th><th>Ano</th><th>Mês (média)</th></tr>
  </thead>
  <tbody>
    <tr><td>Faturamento máximo</td><td>R$ 81.000,00</td><td>R$ 6.750,00</td></tr>
    <tr><td>DAS (serviços)</td><td>R$ 1.032,60</td><td>R$ 86,05</td></tr>
    <tr><td>Contador</td><td>R$ 0,00</td><td>R$ 0,00</td></tr>
    <tr><td><strong>Líquido</strong></td><td><strong>R$ 79.967,40</strong></td><td><strong>R$ 6.663,95</strong></td></tr>
    <tr><td>Carga tributária efetiva</td><td colspan="2"><strong>1,27%</strong></td></tr>
  </tbody>
</table>

É a menor carga tributária legal disponível para pessoa física trabalhando no Brasil. Por isso o regime é tão disputado — e tão fiscalizado.

<img
  src="{{ site.baseurl }}/assets/img/posts/mei-vs-me-teto-2026.svg"
  alt="Comparação entre MEI no teto de R$ 81.000 por ano e uma Microempresa no Anexo III com o mesmo faturamento, mostrando diferença de R$ 9.682,20 anuais"
  style="width:100%;max-width:860px;display:block;margin:1.75rem auto;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px rgba(26,23,20,.08);">

Com o **mesmo faturamento** de R$ 6.750,00/mês, uma ME no Anexo III pagaria R$ 405,00 de DAS, R$ 250,00 de contador, R$ 30,00 de taxas e R$ 207,90 de INSS sobre o pró-labore — sobrando **R$ 5.857,10 por mês**, ou R$ 70.285,20 no ano. O MEI leva **R$ 9.682,20 a mais por ano** pelo mesmo trabalho.

### Quanto o teto do MEI vale em CLT

Aqui está o número que costuma decidir a conversa:

<div class="callout callout-warn">
  <div class="callout-label">A régua do MEI</div>
  Faturando o teto — R$ 6.750,00 por mês, todos os meses, sem falhar — o MEI fica com <strong>R$ 79.967,40 por ano</strong>. Considerando um pacote CLT com vale-refeição de R$ 1.100,00 e plano de saúde de R$ 600,00, isso equivale a um salário registrado de aproximadamente <strong>R$ 4.270,00</strong> (contando FGTS) ou <strong>R$ 4.644,00</strong> (ignorando o FGTS).
</div>

Ou seja: **o teto do MEI é o teto de um CLT júnior**. Para desenvolvedor pleno em diante, o regime já não caberia mesmo que fosse permitido.

### E ele não é permitido

O MEI **não admite atividades de natureza intelectual**. Nenhum dos CNAEs de desenvolvimento, licenciamento, consultoria ou suporte em TI está na lista de ocupações permitidas — 6201-5/01, 6202-3/00, 6203-1/00, 6204-0/00 e 6209-1/00 estão todos fora. Quem escreve código precisa abrir ME (ou EPP) desde o primeiro dia.

Sobre as tentativas de mudar isso:

- O **PLP 59/2017**, que eu citei no texto original, nunca saiu do lugar.
- O **PLP 108/2021** chegou a prever teto de R$ 130.000 (versão do Senado) e R$ 144.900 (versão da Câmara). Nenhum dos dois foi aprovado.
- O **PLP 186/2026**, enviado pelo governo em junho de 2026, propõe elevação progressiva para R$ 110.000 em 2027 e R$ 140.000 em 2028. Ainda depende de Câmara e Senado.

Nenhuma dessas propostas resolve a vedação às atividades intelectuais. Até agosto de 2026, **o teto vigente é R$ 81.000 e desenvolvedor não pode ser MEI**.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap">
    <h2>A conta da equivalência</h2>
  </div>
</div>

Agora a pergunta que interessa: **quanto preciso faturar como PJ para ficar igual a um CLT de R$ 12.000,00?**

O pacote CLT anual, calculado na seção 04, é de **R$ 160.273,04**. Vamos ao lado PJ, faturando **R$ 15.000,00 por mês**:

<div class="simbox-card">
  <div class="simbox-header">
    <div class="simbox-icon">PJ</div>
    <div class="simbox-header-text">
      <h4>PJ faturando R$ 15.000,00/mês — Simples Nacional, Anexo III</h4>
      <span>RBT12 de R$ 180.000,00 · 1ª faixa · pró-labore de 28% para garantir o Fator R</span>
    </div>
  </div>
  <div class="simbox-body">
    <div class="simbox-specs">
      <div class="spec-item"><div class="spec-label">NFS-e emitida</div><div class="spec-value">R$ 15.000,00</div></div>
      <div class="spec-item"><div class="spec-label">DAS (6%)</div><div class="spec-value">− R$ 900,00</div></div>
      <div class="spec-item"><div class="spec-label">Pró-labore</div><div class="spec-value">R$ 4.200,00</div></div>
      <div class="spec-item"><div class="spec-label">INSS s/ pró-labore (11%)</div><div class="spec-value">− R$ 462,00</div></div>
      <div class="spec-item"><div class="spec-label">IRRF s/ pró-labore</div><div class="spec-value">− R$ 0,00</div></div>
      <div class="spec-item"><div class="spec-label">Contador</div><div class="spec-value">− R$ 250,00</div></div>
      <div class="spec-item"><div class="spec-label">Certificado, taxas, banco</div><div class="spec-value">− R$ 30,00</div></div>
      <div class="spec-item"><div class="spec-label">Disponível no mês</div><div class="spec-value">R$ 13.358,00</div></div>
    </div>
    <p style="font-size:14px;color:#5a534a;line-height:1.65;">Carga total sobre o faturamento: <strong>9,1%</strong> — contra os 25,9% que o CLT paga sobre o bruto. O IRRF é zero porque o pró-labore de R$ 4.200,00 está abaixo da nova faixa de isenção de R$ 5.000,00.</p>
  </div>
</div>

Só que esses R$ 13.358,00 **não são seu salário**. São o valor bruto de onde saem todas as reservas que a CLT fazia por você:

| Reserva mensal | Valor | Equivale a |
|---|---|---|
| 13º | R$ 741,03 | R$ 8.892,36 em dezembro |
| Férias + 1/3 | R$ 982,70 | R$ 11.792,36 por ano |
| Alimentação | R$ 1.100,00 | Vale-refeição |
| Plano de saúde | R$ 600,00 | Plano equivalente |
| Reserva tipo FGTS | R$ 1.040,00 | R$ 12.480,00 por ano |
| **Total reservado** | **R$ 4.463,73** | |
| **Sobra livre** | **R$ 8.894,27** | |

<div class="callout callout-tip">
  <div class="callout-label">O resultado</div>
  R$ 8.894,27 livres como PJ contra <strong>R$ 8.892,36</strong> de líquido mensal como CLT. Diferença de <strong>R$ 1,91</strong>. Um CLT de R$ 12.000,00 e um PJ de R$ 15.000,00 são, em 2026, matematicamente a mesma coisa — desde que o PJ realmente faça as reservas.
</div>

### O multiplicador real

Refazendo essa conta em três níveis salariais:

<table class="compare-table">
  <thead>
    <tr><th>Salário CLT</th><th>PJ equivalente (12 meses faturados)</th><th>Multiplicador</th><th>Com 1 mês de férias real</th></tr>
  </thead>
  <tbody>
    <tr><td>R$ 6.000,00</td><td>R$ 9.229,24</td><td>1,54×</td><td>R$ 10.068,26 (1,68×)</td></tr>
    <tr><td>R$ 12.000,00</td><td>R$ 14.997,90</td><td>1,25×</td><td>R$ 16.361,34 (1,36×)</td></tr>
    <tr><td>R$ 20.000,00</td><td>R$ 24.740,63</td><td>1,24×</td><td>R$ 27.172,37 (1,36×)</td></tr>
  </tbody>
</table>

Três leituras importantes dessa tabela:

**Primeira:** o multiplicador de equivalência **cai conforme o salário sobe**. Isso acontece porque o INSS do CLT trava no teto enquanto o IRRF continua subindo até 27,5%, enquanto o PJ paga 6% a 8% sobre tudo. Quanto maior o salário, mais o Simples Nacional compensa.

**Segunda:** a coluna da direita é a honesta. As outras assumem que você fatura doze meses por ano — ou seja, **não tira férias**. Se você quer efetivamente parar trinta dias, precisa faturar em onze meses o que faturaria em doze. Aí o multiplicador volta para perto de **1,36×**, e aquele "1,7×" de 2020 deixa de parecer exagero.

**Terceira, e a mais útil numa negociação:** a empresa economiza mais do que você ganha. No exemplo de R$ 12.000,00, ela gastava R$ 21.480,00 e passa a gastar R$ 15.000,00 — **R$ 6.480,00 a menos por mês, 30% de redução**. Entre o 1,79× que ela pagava e o 1,25× que te deixa igual, existem 54 pontos percentuais de margem. Essa margem é o espaço da negociação, e você só sabe que ela existe se fizer a conta.

<div class="personal-story">
  <div class="personal-story-label">
    <i class="fas fa-user-circle"></i> Minha experiência — PJ em 2020
  </div>
  <p>Escrevi a primeira versão deste artigo em janeiro de 2020, mais ou menos quando comecei a atuar como PJ contratado por um banco em São Paulo. A conta que eu tinha na cabeça na época era a do multiplicador de custo do empregador — o tal 1,7× —, e não a da equivalência real do trabalhador. Só fui entender a diferença depois de alguns meses, quando percebi que o dinheiro que entrava todo mês não era meu: uma parte era férias que eu ainda ia tirar, outra era o 13º que ninguém ia depositar, outra era o plano de saúde que passou a sair do meu bolso.</p>
  <p>Quem organiza as reservas no primeiro mês transforma o PJ em uma escolha ótima. Quem trata o valor cheio como salário descobre o problema em dezembro.</p>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap">
    <h2>O que a conta não captura</h2>
  </div>
</div>

A matemática acima empata os dois regimes. Estes itens não entram na planilha e podem desempatar:

<table class="compare-table">
  <thead>
    <tr><th>Item</th><th>CLT</th><th>PJ</th></tr>
  </thead>
  <tbody>
    <tr><td>Seguro-desemprego</td><td><span class="check">✓</span> até R$ 2.518,65 × 5</td><td><span class="cross">✗</span></td></tr>
    <tr><td>Multa de 40% do FGTS na demissão</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Aviso prévio</td><td><span class="check">✓</span> 30 a 90 dias</td><td><span class="partial">~</span> conforme contrato</td></tr>
    <tr><td>Estabilidade em acidente e gestação</td><td><span class="check">✓</span></td><td><span class="cross">✗</span></td></tr>
    <tr><td>Auxílio-doença no valor do salário</td><td><span class="check">✓</span> até o teto</td><td><span class="partial">~</span> limitado ao pró-labore</td></tr>
    <tr><td>Base de aposentadoria</td><td><span class="check">✓</span> salário integral até o teto</td><td><span class="partial">~</span> só o pró-labore</td></tr>
    <tr><td>Crédito imobiliário e locação</td><td><span class="check">✓</span> comprovação simples</td><td><span class="partial">~</span> exige DECORE, IR e histórico</td></tr>
    <tr><td>Controle sobre o próprio dinheiro</td><td><span class="partial">~</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Múltiplos clientes e contratos no exterior</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
    <tr><td>Dedução de despesas do negócio</td><td><span class="cross">✗</span></td><td><span class="check">✓</span></td></tr>
  </tbody>
</table>

<div class="callout callout-warn">
  <div class="callout-label">A aposentadoria é o furo mais silencioso</div>
  No exemplo da seção 07, o CLT contribui sobre R$ 12.000,00 (travado no teto de R$ 8.475,55) enquanto o PJ contribui sobre um pró-labore de R$ 4.200,00. Se você não elevar o pró-labore ou não montar previdência privada por fora, a diferença aparece daqui a vinte anos — e é grande. Trate isso como parte do custo do regime PJ, não como economia.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap">
    <h2>Dois riscos que não existiam em 2020</h2>
  </div>
</div>

### O STF e a pejotização

O Supremo Tribunal Federal está julgando o **Tema 1389** (ARE 1.532.603), que vai definir com efeito vinculante se — e em que condições — é lícito contratar um trabalhador como pessoa jurídica no lugar da CLT.

A cronologia até agora:

- **Abril de 2025** — o relator, ministro Gilmar Mendes, suspende nacionalmente os processos sobre o tema. Cerca de 50 mil ações trabalhistas param.
- **Outubro de 2025** — audiência pública no STF. O Ministério do Trabalho apresenta estimativa de R$ 61,42 bilhões de evasão contributiva entre 2022 e 2024 atribuída à pejotização.
- **Dezembro de 2025** — o julgamento do mérito começa e é suspenso por pedido de vista da ministra Cármen Lúcia.
- **Fevereiro de 2026** — a PGR apresenta parecer favorável à constitucionalidade da contratação PJ.
- **Junho de 2026** — o relator revoga parcialmente a suspensão; os processos voltam a tramitar nas instâncias ordinárias, mas ficam parados após os TRTs até a tese ser fixada.

Até **agosto de 2026, não há tese fixada**. Na prática, nada mudou ainda: um contrato PJ que esconde uma relação de emprego — com subordinação, pessoalidade, habitualidade e onerosidade — continua podendo ser desconstituído na Justiça do Trabalho. O que muda é o tamanho da aposta: a decisão vai valer para todo mundo, nos dois sentidos possíveis.

Se você é PJ com um único cliente, horário fixo, chefe direto e crachá, essa é a sua situação jurídica. Não é motivo para pânico — é motivo para ler o contrato antes de assinar e para não financiar sua vida inteira contando com um vínculo que juridicamente não existe.

### A reforma tributária

A EC 132/2023, regulamentada pela LC 214/2025, substitui PIS, COFINS, IPI, ICMS e ISS por CBS e IBS. **2026 é ano de teste**: CBS de 0,9% e IBS de 0,1%, com foco em adaptação de notas fiscais. As tabelas e faixas do Simples Nacional **não mudaram** em 2026, e o regime segue preservado. Para optantes do Simples, o destaque de IBS e CBS nos documentos fiscais passa a valer a partir de 2027.

Vale acompanhar, porque a alíquota geral estimada do IVA dual está entre 26,5% e 28,6%, e em algum momento a decisão "ficar no Simples ou sair" vai voltar a ser interessante para PJ de TI com faturamento alto e poucas despesas dedutíveis.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">10</div>
  <div class="section-title-wrap">
    <h2>Checklist para quem vai abrir o CNPJ</h2>
  </div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-building"></i> Tipo societário</div>
    <div class="provider-detail">SLU na maioria dos casos: responsabilidade limitada, sem sócio e sem capital mínimo. EI só se você aceitar misturar patrimônios.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-barcode"></i> CNAE</div>
    <div class="provider-detail">6201-5/01 como principal para desenvolvimento sob encomenda, 6209-1/00 como secundário para suporte. Confirme com o contratante quais ele aceita em nota.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-percent"></i> Fator R</div>
    <div class="provider-detail">Pró-labore em pelo menos 28% do faturamento, todo mês. Peça ao contador o acompanhamento mensal por escrito.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-calculator"></i> Contador</div>
    <div class="provider-detail">De R$ 100,00 a R$ 300,00/mês em contabilidade online; de R$ 500,00 a R$ 1.500,00 em escritório tradicional. Para PJ solo de TI, o online resolve.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-piggy-bank"></i> Contas separadas</div>
    <div class="provider-detail">Conta PJ para receber, conta PF para viver. Uma terceira conta ou aplicação só para as reservas de 13º, férias e "FGTS".</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><i class="fas fa-shield-halved"></i> Previdência</div>
    <div class="provider-detail">O INSS sobre o pró-labore não substitui a contribuição de um CLT no teto. Some previdência privada ou renda fixa de longo prazo à conta.</div>
  </div>
</div>

<div class="conclusion">
  <h2>CLT, PJ ou MEI?</h2>
  <p>Não existe resposta certa para todos, e isso não mudou desde 2020. A escolha depende do seu perfil financeiro, da sua estabilidade profissional e dos seus objetivos de longo prazo.</p>
  <p>O <strong>MEI</strong> está fora da conversa para quem escreve código: é vedado para atividades intelectuais e, mesmo que não fosse, o teto de R$ 81.000 por ano equivale a um CLT de cerca de R$ 4.270 com benefícios. É um excelente regime para outras profissões — não para esta.</p>
  <p>O <strong>CLT</strong> oferece segurança, previsibilidade e um conjunto de proteções que nenhuma planilha reproduz: seguro-desemprego, multa de 40% do FGTS, estabilidades, auxílio-doença no valor do salário e uma base de aposentadoria muito melhor. É a escolha certa para quem está começando, para quem ainda não construiu reserva e para quem não quer administrar nada disso.</p>
  <p>O <strong>PJ</strong> oferece carga tributária de 9% contra 26%, controle total sobre o próprio dinheiro e liberdade para ter vários clientes — mas exige disciplina, gestão ativa, tolerância a períodos sem contrato e consciência de que o STF ainda não disse se o arranjo é lícito como regra.</p>
  <p>O número que importa continua não sendo o salário bruto nem o valor da nota fiscal. É o que sobra no fim do mês depois de guardar tudo o que a CLT guardaria por você — e o que você faz com esse excedente. Em 2026, esse ponto de equilíbrio fica entre <strong>1,25× e 1,36×</strong> o salário CLT, enquanto a empresa economiza <strong>1,73× a 1,93×</strong>. A diferença entre esses dois números é a sua margem de negociação. Use.</p>
</div>

<div class="callout callout-warn">
  <div class="callout-label">Aviso</div>
  Este artigo é material educativo, não consultoria contábil ou jurídica. Os cálculos usam premissas explícitas (encargos de 26,8%, vale-refeição de R$ 1.100,00, plano de saúde de R$ 600,00, contador a R$ 250,00/mês) que podem não corresponder ao seu caso. Alíquotas de ISS variam por município, o RAT varia por atividade e FAP, e o Fator R muda todo mês. Simule com o seu contador antes de decidir.
</div>

<div class="references">
  <p class="references-title">Referências</p>
  <ol class="references-list">
    <li>
      Receita Federal. <strong>Exemplos de aplicação da Lei 15.270/2025.</strong>
      <a href="https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/exemplos-de-aplicacao-da-lei-15-270-2025" target="_blank">gov.br/receitafederal</a>
    </li>
    <li>
      Receita Federal. <strong>Receita orienta fontes pagadoras e contribuintes a calcular a redução do imposto de renda a partir de 1º de janeiro de 2026.</strong>
      <a href="https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/dezembro/receita-federal-orienta-fontes-pagadoras-e-contribuintes-a-calcular-a-reducao-do-imposto-de-renda-a-partir-de-1o-de-janeiro-de-2026" target="_blank">gov.br/receitafederal</a>
    </li>
    <li>
      Receita Federal / Simples Nacional. <strong>Atualização de valores devidos pelo MEI em 2026.</strong>
      <a href="https://www8.receita.fazenda.gov.br/simplesnacional/Noticias/NoticiaCompleta.aspx?id=c3b2044c-ff97-432a-b33c-ecf2a3df6dc3" target="_blank">receita.fazenda.gov.br</a>
    </li>
    <li>
      Receita Federal. <strong>Anexo III da Lei Complementar 123/2006 — alíquotas e partilha do Simples Nacional.</strong>
      <a href="https://normas.receita.fazenda.gov.br/sijut2consulta/anexoOutros.action?idArquivoBinario=48432" target="_blank">normas.receita.fazenda.gov.br</a>
    </li>
    <li>
      Agência Brasil. <strong>Salário mínimo de R$ 1.621 começa a ser pago.</strong>
      <a href="https://agenciabrasil.ebc.com.br/economia/noticia/2026-02/salario-minimo-de-r-1621-comeca-ser-pago-nesta-segunda" target="_blank">agenciabrasil.ebc.com.br</a>
    </li>
    <li>
      Agência Gov / MTE. <strong>Novos valores do benefício Seguro-Desemprego para 2026.</strong>
      <a href="https://agenciagov.ebc.com.br/noticias/202601/mte-reajusta-valores-do-beneficio-seguro-desemprego" target="_blank">agenciagov.ebc.com.br</a>
    </li>
    <li>
      Presidência da República. <strong>Lei nº 14.195/2021 — extinção da EIRELI e transformação automática em SLU.</strong>
      <a href="https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/L14195.htm" target="_blank">planalto.gov.br</a>
    </li>
    <li>
      TRT-18. <strong>STF afasta aplicação do Tema 1389 em ação que discute vínculo empregatício.</strong>
      <a href="https://www.trt18.jus.br/portal/stf-afasta-aplicacao-do-tema-1389-em-acao-em-tramite-em-aguas-lindas-de-goias-que-discute-vinculo-empregaticio-decisao-e-vinculante/" target="_blank">trt18.jus.br</a>
    </li>
    <li>
      Felsberg Advogados. <strong>Pejotização: STF autoriza retomada de processos sobre contratação de PJs e autônomos (Tema 1389).</strong>
      <a href="https://www.felsberg.com.br/tema-1389-pejotizacao-retomada-processos-stf/" target="_blank">felsberg.com.br</a>
    </li>
    <li>
      Contabilizei. <strong>Limite de faturamento do MEI em 2026 e propostas de aumento.</strong>
      <a href="https://www.contabilizei.com.br/contabilidade-online/faturamento-mei-2026/" target="_blank">contabilizei.com.br</a>
    </li>
    <li>
      Contajá. <strong>Anexo III ou Anexo V? Fator R, diferenças e alíquotas 2026.</strong>
      <a href="https://contaja.com.br/blog/diferenca-anexo-iii-e-v-simples-nacional/" target="_blank">contaja.com.br</a>
    </li>
    <li>
      Agilize. <strong>CNAE 6209-1/00 e CNAE 6203-1/00: enquadramento, Fator R e vedação ao MEI.</strong>
      <a href="https://agilize.com.br/artigos/cnae-6209-1-00/" target="_blank">agilize.com.br</a>
    </li>
  </ol>
</div>
