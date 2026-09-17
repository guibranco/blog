<div align="center">

# ✈️🛠️ Tecnologia & Viagens

**Blog sobre tecnologia, infraestrutura e automação para quem viaja e constrói.**

Publicado via [Jekyll](https://jekyllrb.com/) · Hospedado via [GitHub Pages](https://pages.github.com/) · Zero custo de servidor

[![Deploy](https://github.com/guibranco/blog/actions/workflows/deploy.yml/badge.svg)](https://github.com/guibranco/blog/actions/workflows/deploy.yml)
[![Blog Structure Audit](https://github.com/guibranco/blog/actions/workflows/blog-audit.yml/badge.svg)](https://github.com/guibranco/blog/actions/workflows/blog-audit.yml)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red?logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

[🌐 Ver o blog](https://guilherme.stracini.com.br/blog) · [📡 RSS](https://guilherme.stracini.com.br/blog/feed.xml) · [🗺️ Sitemap XML](https://guilherme.stracini.com.br/blog/sitemap.xml) · [🗺️ Mapa do site](https://guilherme.stracini.com.br/blog/mapa-do-site/)

</div>

---

## 📋 Sobre

Blog pessoal construído com Jekyll e publicado gratuitamente via GitHub Pages. Cada artigo é um arquivo Markdown em `_posts/` — um `git push` para a branch `main` dispara o build e publica automaticamente em ~1 minuto.

O design é totalmente customizado — sem temas de terceiros — com tipografia editorial (Playfair Display + Source Serif 4 + JetBrains Mono), sidebar fixa com avatar, ícones sociais e navegação por categorias e tópicos.

O conteúdo é bilíngue (pt-BR/en) por artigo — ver [Idiomas (i18n)](#-idiomas-i18n) — e a estrutura do blog (categorias, tags, RSS, mapa do site) é validada automaticamente em cada push via GitHub Actions — ver [Scripts e automação](#-scripts-e-automação).

---

## 🗂️ Estrutura do projeto

```
blog/                                 # nome do repositório
│
├── _posts/                           # Artigos em Markdown (52 posts)
│   └── AAAA-MM-DD-slug.md
│
├── _layouts/
│   ├── post.html                     # Template de artigo
│   ├── page.html                     # Template de página estática simples (usado por 404.html)
│   ├── category.html                 # Template de página de categoria/subcategoria
│   └── tag.html                      # Template de página de tópico/tag
│
├── _includes/                        # Partials reutilizáveis
│   ├── sidebar.html                  # Sidebar fixa: avatar, nav, categorias, busca, seletor de idioma
│   ├── sidebar-script.html           # JS do menu mobile/toggle da sidebar
│   ├── footer.html
│   ├── post-card.html                # Card de artigo usado nas listagens (home, categoria, tag)
│   ├── post-dates.html               # "Publicado em X" + "· Atualizado em Y" (só quando os dias diferem)
│   ├── pagination.html
│   ├── breadcrumb.html               # Categoria › Subcategoria › Artigo
│   ├── series.html                   # Navegação de série dentro do artigo
│   ├── resolve-lang.html             # Resolve `_lang`/`_t` (idioma + tabela de traduções) de uma página
│   ├── photo.html                    # Foto de galeria responsiva: <picture> AVIF/WebP + width/height + GLightbox
│   ├── schema.html                   # JSON-LD (schema.org) do post: Article, BreadcrumbList, ItemList (série), FAQPage
│   ├── schema-series.html            # Nó ItemList de uma série — usado por schema.html e por series.html (/series/)
│   └── analytics.html
│
├── _plugins/                         # Generators e filtros Ruby customizados (ver "Scripts e automação")
│   ├── category_pages_generator.rb   # Gera /categorias/{cat}/ e /categorias/{cat}/{sub}/
│   ├── tag_pages_generator.rb        # Gera /topicos/{slug}/
│   ├── feed_generator.rb             # Gera /feed/{cat}.xml e /feed/{cat}-{sub}.xml
│   ├── git_last_modified.rb          # Calcula a data real de "última atualização" via histórico do git
│   ├── localized_date.rb             # Filtro Liquid `localized_date` — nomes de mês em pt-BR/en
│   ├── reading_time.rb               # Calcula `reading_time` a partir do texto quando o front matter não define
│   ├── schema_filters.rb             # Filtros Liquid `faq_items` e `json_ld_string` usados pelo schema.html
│   └── seo_tag_json_ld_opt_out.rb    # Adiciona `json_ld=false` ao `{% seo %}` — o layout de post emite o próprio JSON-LD
│
├── _data/
│   ├── categories.yml                # Categorias/subcategorias (nome, slug, ícone, redirect_from)
│   ├── tags.yml                      # Tags (nome, slug, redirect_from) — uma página por entrada
│   ├── countries.yml                 # Países visitados em posts de viagem (nome em inglês, slug, name_pt) — lista curada
│   ├── i18n.yml                      # Strings de UI em pt-BR e en
│   ├── quotes.yml                    # Lista de quotes da sidebar
│   └── images.json                   # GERADO por build_images.py (gitignored): dimensões + derivados das fotos
│
├── assets/
│   ├── css/
│   │   └── main.css                  # Estilos compartilhados (tokens CSS em :root)
│   ├── js/
│   │   └── lang-switcher.js          # Troca o idioma da UI no cliente + detecta idioma do navegador
│   └── img/
│       ├── cover.jpg                 # Imagem de fundo da sidebar
│       ├── avatar.png                # Foto de perfil circular
│       ├── posts/                    # Imagens/covers dos artigos
│       │   └── <post-slug>/          # Fotos de galeria do post (originais sanitizados — sem EXIF/GPS)
│       └── derived/                  # GERADO por build_images.py (gitignored): AVIF/WebP em 480/960/1600px
│
├── docs/
│   ├── adr/                          # Architecture Decision Records
│   └── agents/                       # Documentação voltada a agentes de IA (issue tracker, domínio)
│
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml                # build_images.py + jekyll build + deploy no GitHub Pages (push em main)
│   │   ├── blog-audit.yml            # Roda audit_blog.py em push/PR que tocam posts, dados ou fotos
│   │   ├── sync-category-tag-data.yml # Registra categorias/tags novas automaticamente em PRs
│   │   └── og-cards.yml              # Gera o og:image (PNG 1200×630) dos posts sem imagem e comita no PR
│   ├── scripts/
│   │   ├── audit_blog.py             # Audita a estrutura do blog
│   │   ├── build_images.py           # Sanitiza fotos de galeria e gera os derivados AVIF/WebP + images.json
│   │   ├── build_og_cards.py         # Renderiza o card Open Graph a partir do front matter (ou rasteriza o cover SVG)
│   │   └── create_missing_pages.py   # Sincroniza _data/categories.yml e _data/tags.yml
│   └── fonts/                        # GERADO por build_og_cards.py --download-fonts (gitignored): TTFs da marca
│
├── index.html                        # Página inicial (paginada)
├── search.html                       # Página de busca (/busca/)
├── search.json                       # Índice de busca client-side (lunr.js)
├── travels.html                      # Página de viagens (/viagens/) — mapa + tabela por país
├── series.html                       # Índice de séries (/series/)
├── tags.html                         # Todos os tópicos (/topicos/)
├── sitemap.html                      # Mapa do site navegável para humanos (/mapa-do-site/)
├── 404.html                          # Página de erro 404
├── CONTEXT.md                        # Glossário de domínio (Post, Category, Tag, Series, Trip…)
├── CLAUDE.md                         # Instruções para agentes de IA que trabalham neste repo
├── _config.yml                       # Configurações do Jekyll
├── Gemfile                           # Dependências Ruby
└── README.md
```

> Cada arquivo de página no root (`travels.html`, `tags.html`, `series.html`, `search.html`, `sitemap.html`…) tem nome de arquivo em inglês, mas `permalink:` em português (`/viagens/`, `/topicos/`, `/mapa-do-site/`…) — essa é a URL pública do blog, que é em pt-BR.

Categoria, subcategoria, tag e feed RSS **não são arquivos individuais** — são gerados no build a partir de `_data/categories.yml` e `_data/tags.yml`. Ver [ADR-0001](docs/adr/0001-stub-files-for-category-tag-feed-pages.md), [ADR-0003](docs/adr/0003-tag-pages-generated-from-data-file.md), [ADR-0004](docs/adr/0004-category-pages-generated-from-data-file.md) e [ADR-0005](docs/adr/0005-feed-pages-generated-from-data-file.md).

---

## 🌐 Idiomas (i18n)

Todo artigo é escrito em **um** idioma — `en` ou `pt-BR` — declarado no front matter. As strings de UI (botões, labels, datas) do resto do site (sidebar, cards, navegação) existem nas duas línguas em `_data/i18n.yml` e são trocadas no cliente por `assets/js/lang-switcher.js`, sem duplicar página nenhuma.

**Como funciona:**

- `_data/i18n.yml` tem duas chaves de topo (`pt-BR:` e `en:`) com o mesmo conjunto de strings traduzidas.
- `_includes/resolve-lang.html` resolve `_lang` (`page.lang`, com fallback fixo `"pt-BR"`) e `_t` (a tabela de traduções correspondente) para uso em Liquid durante o build.
- Elementos HTML marcados com `data-i18n="chave"` (texto), `data-i18n-title`, `data-i18n-aria` ou `data-i18n-placeholder` são retraduzidos **no navegador** por `lang-switcher.js` quando o visitante troca o idioma pelos botões da sidebar — sem reload de página.
- `lang-switcher.js` detecta o idioma do navegador (`navigator.languages`) na primeira visita e lembra a preferência em `localStorage`.
- Cada artigo exibe uma badge (`PT-BR`/`EN`) com o idioma em que **aquele post específico** foi escrito — independente do idioma selecionado na UI.

**`lang:` é obrigatório em todo post** — `.github/scripts/audit_blog.py` falha o build se um post não tiver `lang: en` ou `lang: pt-BR` (ver [Scripts e automação](#-scripts-e-automação)).

---

## 🗃️ Gerenciando categorias e tópicos

Categorias, subcategorias e tags **não são arquivos** — são entradas em `_data/categories.yml` e `_data/tags.yml`, e suas páginas são geradas no build pelo Jekyll:

- Categorias: `/categorias/{slug}/` (`_plugins/category_pages_generator.rb`)
- Subcategorias: `/categorias/{cat_slug}/{sub_slug}/` (mesmo generator)
- Tags: `/topicos/{slug}/` (`_plugins/tag_pages_generator.rb`)

Feeds RSS (`_plugins/feed_generator.rb`) existem **apenas para categorias e subcategorias** — tags não têm feed:

- Categorias: `/feed/{slug}.xml`
- Subcategorias: `/feed/{cat_slug}-{sub_slug}.xml`

**Isso é automático:** ao abrir um PR com um post usando uma categoria/subcategoria/tag nova, o workflow `sync-category-tag-data.yml` roda `.github/scripts/create_missing_pages.py`, que adiciona a entrada faltante em `_data/categories.yml` (categoria nova entra com ícone placeholder `fas fa-folder` — revise antes de mergear) ou `_data/tags.yml`, e comita a mudança direto na branch do PR. A página e o feed correspondentes aparecem sozinhos no próximo build — nada precisa ser criado manualmente.

**Categorias existentes** (ver `_data/categories.yml` para a lista completa com subcategorias):

| Categoria | Slug | URL |
|---|---|---|
| Career | `career` | `/categorias/career/` |
| Coding | `coding` | `/categorias/coding/` |
| Hobbies | `hobbies` | `/categorias/hobbies/` |
| Infrastructure | `infrastructure` | `/categorias/infrastructure/` |
| Investments | `investments` | `/categorias/investments/` |

---

## ✍️ Publicando um novo artigo

**1.** Crie o arquivo em `_posts/` seguindo o padrão `AAAA-MM-DD-slug.md`:

```bash
touch _posts/2026-04-10-meu-novo-artigo.md
```

**2.** Adicione o front matter no topo do arquivo:

```yaml
---
layout: post
lang: pt-BR                                      # obrigatório — "en" ou "pt-BR"
title: "Título do artigo"
description: "Resumo em uma linha para SEO e cards."
date: 2026-04-10
categories: [Infrastructure]
subcategories:
  - "Infrastructure/DevOps"                       # opcional — "Categoria/Subcategoria"
tags: [docker, linux, automação]
cover: /assets/img/posts/meu-artigo-cover.svg    # opcional — imagem usada no site (hero do post e card na listagem)
image: /assets/img/posts/meu-artigo-cover.png    # opcional — imagem estática usada no Open Graph/Twitter card e no schema.org (via _includes/schema.html)
card_style: dark                                 # opcional — força o estilo do card gerado (dark ou cream)
---
```

Se apenas `image` for definido, ele é usado tanto no site quanto no Open Graph (comportamento antigo, ainda suportado). `cover` serve para permitir uma imagem animada (SVG) na página sem quebrar o preview em redes sociais, que exigem um raster estático.

**Não informe `reading_time`.** O plugin `_plugins/reading_time.rb` calcula o tempo de leitura no build a partir do próprio texto — prosa a 200 palavras/min, blocos de código a 150, mais 10 s por imagem — e o valor aparece na página do post, nos cards, na home e na busca como se estivesse no front matter. Um `reading_time:` escrito à mão continua valendo como override, mas o `audit_blog.py` avisa quando ele destoa do valor calculado. Ver [ADR-0013](docs/adr/0013-reading-time-computed-from-body.md).

**Post sem foto não precisa de imagem nenhuma.** Ao abrir o PR, o workflow `og-cards.yml` renderiza o card Open Graph (PNG 1200×630) a partir do próprio front matter — título, descrição, categoria, série, data, tags — no estilo *cream editorial* (padrão) ou *dark tech* (Coding e Infrastructure), grava-o em `assets/img/posts/<slug-do-post>.png`, preenche `image:` e comita na branch. Se o post já tiver um `cover:` SVG desenhado à mão, é esse SVG que vira o PNG. Posts de viagem (`location`/`locations`/`countries`) e posts que já declaram um `image:` raster não são tocados. Ver `build_og_cards.py` em [Scripts e automação](#-scripts-e-automação) e [ADR-0012](docs/adr/0012-og-cards-generated-in-ci-from-front-matter.md).

Ver [Front matter — referência completa](#-front-matter--referência-completa) para todos os campos disponíveis, incluindo `series*` e `location`/`locations`/`countries` para posts de viagem.

**3.** Escreva o conteúdo em Markdown. Componentes visuais customizados como callouts, blocos de código com syntax highlighting e cards podem ser usados diretamente com HTML inline. Fotos de galeria entram pelo include `photo.html` — ver [Galeria de fotos](#galeria-de-fotos).

**4.** Publique via branch + pull request — **não dê push direto em `main`**:

```bash
git checkout -b feat/novo-artigo-sobre-x
git add .
git commit -m "feat: novo artigo sobre X"
git push origin feat/novo-artigo-sobre-x
```

Abra o PR no GitHub. Ao abrir/atualizar o PR:

- `sync-category-tag-data.yml` registra categorias/subcategorias/tags novas em `_data/` automaticamente (só roda em eventos de `pull_request` — um push direto em `main` pula essa etapa silenciosamente).
- `og-cards.yml` renderiza e comita o card Open Graph dos posts alterados que ainda não têm `image:` (idem — só em `pull_request`).
- `blog-audit.yml` audita o post (front matter obrigatório, `lang:` válido, categorias/tags registradas, imagens locais e externas) e comenta os problemas encontrados — ver [Scripts e automação](#-scripts-e-automação).

Depois de mergear, o GitHub Pages detecta o push em `main`, roda o build do Jekyll (`deploy.yml`) e publica em ~60 segundos.

---

## 🤖 Scripts e automação

### `.github/scripts/audit_blog.py`

Audita a estrutura inteira do blog e escreve um relatório em `audit-report.md` (e no `$GITHUB_STEP_SUMMARY` do Actions). Roda em todo push/PR que toca `_posts/**`, `_data/tags.yml`, `_data/categories.yml` ou `_data/countries.yml` (workflow `blog-audit.yml`), e falha o build (`exit 1`) se houver algum problema **bloqueante**:

| Checagem | Bloqueante? |
|---|---|
| `lang:` ausente ou diferente de `en`/`pt-BR` | ✅ erro |
| Categoria/subcategoria usada no post mas não registrada em `_data/categories.yml` | ✅ erro |
| `countries:` usado no post mas não registrado em `_data/countries.yml` | ✅ erro |
| Tag usada mas não registrada em `_data/tags.yml` | ✅ erro |
| `image:`/`cover:` apontando para um arquivo local inexistente | ✅ erro |
| `image:` (og:image) num formato não-raster (deve ser png/jpg/jpeg/gif) | ✅ erro |
| Foto de galeria (`assets/img/posts/<slug>/`) com GPS no EXIF ou orientação EXIF não aplicada nos pixels | ✅ erro |
| Imagem externa referenciada no corpo do post retornando erro HTTP | ⚠️ aviso (⚠️ apenas o `image:` de capa é bloqueante) |
| `description`/`image` ausentes | ⚠️ aviso |
| `reading_time:` manual destoando do valor calculado (mais de 10% e mais de 1 min) ou que não é um inteiro positivo | ⚠️ aviso |
| `cover:` num formato inesperado | ⚠️ aviso |
| Foto de galeria com outros metadados EXIF/XMP remanescentes | ⚠️ aviso |

Rodar localmente:

```bash
python3 .github/scripts/audit_blog.py
# lê audit-report.md ao final, ou o output impresso no terminal
```

A checagem de fotos precisa do Pillow (`pip install Pillow`); sem ele, ela é pulada com um aviso e o resto da auditoria roda normalmente.

### `.github/scripts/build_images.py`

Pipeline de fotos de galeria ([ADR-0011](docs/adr/0011-gallery-derivatives-at-build-time-sanitized-sources.md)). Para cada `.jpg`/`.jpeg`/`.png` dentro de uma pasta por post (`assets/img/posts/<post-slug>/`):

1. **Sanitiza o original no lugar** se ele ainda tiver metadados: aplica a orientação EXIF nos pixels e remove EXIF/XMP (GPS, modelo do celular, data…), mantendo o perfil ICC. O JPEG é reencodado com as próprias tabelas de quantização, então a perda é desprezível. Idempotente — arquivo já limpo não é tocado. **Esse arquivo sanitizado é o que deve ser commitado**: é o `href` que o GLightbox abre em resolução cheia e o fallback do `<img>`.
2. **Gera derivados AVIF e WebP** em 480/960/1600 px (nunca amplia; fonte mais estreita que 1600 px ganha também um degrau na largura nativa) em `assets/img/derived/<post-slug>/`, com um hash curto da fonte no nome.
3. **Escreve `_data/images.json`** com largura/altura intrínsecas e os conjuntos de derivados — é o que `_includes/photo.html` lê para montar o `<picture>`.

Derivados e manifesto são **saída de build** (gitignored): o `deploy.yml` roda o script antes do `jekyll build`, com `assets/img/derived/` em cache entre execuções. Localmente:

```bash
python3 -m pip install "Pillow>=11.2"
python3 .github/scripts/build_images.py            # sanitiza + gera só o que falta
python3 .github/scripts/build_images.py --force    # regenera tudo
python3 .github/scripts/build_images.py --no-sanitize
```

Fotos em HEIC não são suportadas — converta para JPEG antes de colocar na pasta.

### `.github/scripts/build_og_cards.py`

Gera o card Open Graph ([ADR-0012](docs/adr/0012-og-cards-generated-in-ci-from-front-matter.md)) dos posts que não são de viagem e ainda não têm um `image:` raster. Chamado pelo workflow `og-cards.yml` com os posts alterados no PR; para cada um:

- **sem `cover:` nem `image:`** → renderiza um card a partir do front matter (título dividido em manchete + complemento nos primeiros dois-pontos, descrição, categoria › subcategoria, série/parte, data, tempo de leitura e, no estilo dark, as tags como chips). O estilo vem da primeira categoria — *dark tech* para Coding e Infrastructure, *cream editorial* para o resto — ou de `card_style: dark|cream` no front matter;
- **com `cover:` SVG e sem `image:`** → rasteriza o próprio SVG desenhado à mão (escala uniforme, fundo na cor do SVG);
- grava `assets/img/posts/<slug-do-post>.png` e escreve `image:` no post. O PNG leva um marcador (`Software: guibranco/blog build_og_cards.py`) — um card gerado é re-renderizado sempre que o post muda no PR; um PNG feito à mão com o mesmo nome nunca é sobrescrito.

A tipografia é a mesma do site (Playfair Display, Source Serif 4, JetBrains Mono), baixada do `google/fonts` num commit fixo para `.github/fonts/` (gitignored) e exposta ao CairoSVG via um `fonts.conf` privado; se alguma família não resolver, o script falha em vez de renderizar com fonte substituta. Localmente (Linux/macOS com libcairo):

```bash
python3 -m pip install cairosvg "Pillow>=11.2" pyyaml
python3 .github/scripts/build_og_cards.py --download-fonts        # uma vez
python3 .github/scripts/build_og_cards.py --dry-run               # o que seria renderizado
python3 .github/scripts/build_og_cards.py _posts/2026-04-10-meu-novo-artigo.md
python3 .github/scripts/build_og_cards.py --svg-only --out-dir /tmp/cards --no-front-matter   # só o SVG (funciona no Windows, sem cairo)
```

Para pré-visualizar um card sem comitar nada, rode `og-cards.yml` manualmente (Actions → *Open Graph cards* → *Run workflow*) sem marcar *commit*: o PNG e o SVG sobem como artifact.

### `.github/scripts/create_missing_pages.py`

Chamado pelo workflow `sync-category-tag-data.yml` com a lista de posts alterados no PR. Não cria páginas — categoria/subcategoria/tag "existe" a partir do momento em que está registrada em `_data/categories.yml`/`_data/tags.yml`, e as páginas nascem sozinhas no build seguinte (ver [ADR-0001](docs/adr/0001-stub-files-for-category-tag-feed-pages.md)). O script só garante que as entradas estejam lá:

```bash
python3 .github/scripts/create_missing_pages.py _posts/2026-04-10-meu-novo-artigo.md
```

Categoria nova entra com ícone placeholder (`fas fa-folder`) — revise e ajuste manualmente em `_data/categories.yml` depois.

### Plugins Ruby customizados (`_plugins/`)

Além dos generators de categoria/tag/feed (ver [seção acima](#-gerenciando-categorias-e-tópicos)):

- **`git_last_modified.rb`** — para cada post/página, percorre o histórico do git e compara o **corpo** (conteúdo após o front matter) entre revisões consecutivas, achando o commit mais recente que de fato mudou o texto — um commit que só mexeu em front matter (tags, `reading_time`, `lang`…) é ignorado. O resultado vira `page.last_modified_at`, usado por `_includes/post-dates.html` (mostra "Atualizado em" só quando o dia é diferente do de publicação) e lido automaticamente pelo `jekyll-sitemap` para o `<lastmod>` do `sitemap.xml`. **Requer histórico completo do git** — o checkout do `deploy.yml` usa `fetch-depth: 0` de propósito; um clone raso faz todo post parecer "atualizado hoje".
- **`localized_date.rb`** — filtro Liquid `localized_date: date, format, lang`. `%B` do `strftime` do Ruby usa o locale da própria máquina de build (normalmente inglês, mesmo com `%d de %B de %Y`), então esse filtro troca `%B` pelo nome do mês certo (pt-BR ou en) antes de formatar, sem depender do locale do runner.
- **`reading_time.rb`** — preenche `page.reading_time` (minutos inteiros) em todo post que não define o campo no front matter, contando as palavras do corpo: prosa a 200 palavras/min, blocos de código (``` ou `<pre>`) a 150, mais 10 s por imagem; tags HTML, Liquid, comentários e URLs de links não contam. Um `reading_time:` manual sempre vence. As taxas podem ser ajustadas num bloco `reading_time:` do `_config.yml` (`words_per_minute`, `code_words_per_minute`, `seconds_per_image`). `.github/scripts/reading_time.py` é a mesma conta em Python, usada pelo `audit_blog.py` (aviso de drift) e pelo `build_og_cards.py` (tempo de leitura no card) — mudou um, mude o outro. Ver [ADR-0013](docs/adr/0013-reading-time-computed-from-body.md).
- **`schema_filters.rb`** — dois filtros Liquid usados por `_includes/schema.html`. `faq_items` extrai pares pergunta/resposta do HTML renderizado do post (títulos `h2`–`h4` terminados em `?` e o texto até o próximo título do mesmo nível, sem código, tabelas e figuras) para o nó `FAQPage`, ativado por `faq: true` no front matter. `json_ld_string` serializa texto livre como string JSON com `</` escapado, para que título, descrição ou resposta nunca fechem o `<script>` — use-o em vez de `escape`, que geraria `&amp;` literal dentro do JSON.
- **`seo_tag_json_ld_opt_out.rb`** — adiciona a flag `json_ld=false` ao `{% seo %}` do `jekyll-seo-tag`, nos moldes de `title=false`. O layout de post usa `{% seo json_ld=false %}`: as meta tags continuam vindo da gem, mas o JSON-LD vem inteiro do `schema.html` (um `@graph` com `Article`, `BreadcrumbList`, `ItemList` da série e `FAQPage`) — sem a flag, a gem emitiria um `BlogPosting` descrevendo o mesmo artigo uma segunda vez. As demais páginas continuam com o JSON-LD da gem. Ver [ADR-0014](docs/adr/0014-post-json-ld-graph-replaces-seo-tag-node.md).

### Workflows (`.github/workflows/`)

| Workflow | Dispara em | O que faz |
|---|---|---|
| `deploy.yml` | push em `main` (ou manual) | `build_images.py` (derivados em cache) + `jekyll build` + deploy no GitHub Pages |
| `blog-audit.yml` | push/PR tocando posts, `_data/{tags,categories,countries}.yml` ou `assets/img/posts/**` | Roda `audit_blog.py` |
| `sync-category-tag-data.yml` | abertura/atualização de PR | Roda `create_missing_pages.py` e comita/comenta o resultado |
| `og-cards.yml` | abertura/atualização de PR tocando `_posts/**` (ou manual) | Roda `build_og_cards.py` nos posts alterados e comita o PNG + `image:`; manual sem *commit* só sobe um artifact de preview |

---

## ⚙️ Configuração (`_config.yml`)

```yaml
# Identidade
title: "Tecnologia & Viagens"
description: "Blog sobre tecnologia, infraestrutura e automação para quem viaja e constrói."
author: "Guilherme Branco Stracini"
author_bio: "Software engineer. PHP, C#, JS, Rust. Integrations, APIs, insurance & logistics. Lego collector."
author_avatar: /assets/img/avatar.png    # foto circular na sidebar
author_cover: /assets/img/cover.jpg     # imagem de fundo da sidebar

google_analytics: G-E6MXHTTEDH

# URLs
url: "https://guilherme.stracini.com.br"
baseurl: "/blog"

# Permalinks
permalink: /artigos/:slug/

# Redes sociais (todos opcionais)
social:
  github:        https://github.com/guibranco
  linkedin:      https://www.linkedin.com/in/guilhermestracini/
  instagram:     https://instagram.com/gui.stracini
  facebook:      https://www.facebook.com/guilherme.stracini/
  youtube:       https://www.youtube.com/@GuilhermeBrancoStracini
  stackoverflow: https://stackoverflow.com/users/1890220/guilherme-branco-stracini
  pinterest:     https://www.pinterest.com/guibranco/
  whatsapp:      https://api.whatsapp.com/send/?phone=353871471762
  website:       https://guilherme.stracini.com.br
  strava:        https://www.strava.com/athletes/171612487
  spotify:       https://open.spotify.com/user/22x2qmq6hbuqyjy2emg6k4xiq
  soundcloud:    https://soundcloud.com/guilherme-stracini
  reddit:        https://www.reddit.com/user/SilverSport8845/
  medium:        https://medium.com/@guilhermebrancostracini
```

> Não há mais um `lang:` de topo no `_config.yml` — cada post declara o próprio idioma (`lang: en`/`lang: pt-BR`), e páginas fixas do site (home, busca, tópicos…) assumem `pt-BR` diretamente. O idioma padrão da UI para um visitante novo vem da detecção de navegador em `lang-switcher.js`, não de uma config fixa.

---

## 💬 Quotes da sidebar

As quotes são selecionadas dinamicamente a cada build a partir do arquivo `_data/quotes.yml`. O Jekyll usa os segundos do horário do build como seed — então cada `git push` exibe uma quote diferente.

**Formato do arquivo:**

```yaml
- text: "The best way to predict the future is to invent it."
  author: "Alan Kay"

- text: "Not all those who wander are lost."
  author: "J.R.R. Tolkien"
```

Para adicionar uma nova quote, basta incluir um novo item no final do arquivo. Não há limite de quantidade — quanto mais quotes, mais variação entre builds.

---

## 🖼️ Imagens da sidebar

A sidebar suporta dois campos distintos:

| Campo | Uso | Fallback |
|---|---|---|
| `author_cover` | Imagem de fundo (square/landscape) com `object-fit: cover` e opacidade reduzida | Padrão geométrico diagonal |
| `author_avatar` | Foto circular em primeiro plano | Inicial do nome do autor |

---

## 🏷️ Front matter — referência completa

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `layout` | string | ✅ | Sempre `post` |
| `lang` | string | ✅ | Idioma do artigo — `en` ou `pt-BR`. Validado por `audit_blog.py` |
| `title` | string | ✅ | Título do artigo |
| `date` | date | ✅ | Data de publicação (`AAAA-MM-DD`) |
| `description` | string | — | Subtítulo e meta description para SEO |
| `categories` | list | — | Categorias (aparecem como pills e na nav) — devem existir em `_data/categories.yml` |
| `subcategories` | list | — | `"Categoria/Subcategoria"` — cada item precisa existir em `_data/categories.yml` |
| `tags` | list | — | Tags (aparecem no rodapé do artigo); cada uma vira uma entrada em `_data/tags.yml` e uma página `/topicos/{slug}/` |
| `reading_time` | number | — | Override manual do tempo de leitura, em minutos inteiros. Se ausente, `_plugins/reading_time.rb` calcula a partir do texto no build ([ADR-0013](docs/adr/0013-reading-time-computed-from-body.md)); se presente e muito diferente do calculado, `audit_blog.py` avisa |
| `image` | path | — | Imagem de capa (og:image/Twitter card) — precisa ser raster (png/jpg/jpeg/gif). Se ausente num post que não é de viagem, `og-cards.yml` gera e preenche |
| `cover` | path | — | Hero visual da página do post (SVG, PNG, JPG, GIF ou WebP). Um `cover` SVG sem `image` é rasterizado pelo `og-cards.yml` |
| `card_style` | string | — | `dark` ou `cream` — força o estilo do card gerado (padrão: dark para Coding/Infrastructure, cream para o resto) |
| `gallery` | boolean | — | Ativa o lightbox (GLightbox) para imagens `.glightbox` no corpo do post |
| `featured` | boolean | — | Fixa o post na seção de destaques da home |
| `faq` | boolean | — | Emite um nó `FAQPage` no JSON-LD do post: todo título `h2`–`h4` cujo texto termina em `?` vira uma `Question`, e o texto até o próximo título do mesmo nível (sem código, tabelas e figuras) vira a `Answer`. Só marque posts que de fato têm uma seção de perguntas e respostas visível |
| `series` | string | — | Slug da série (agrupa posts na navegação de série e em `/series/`) |
| `series_title` | string | — | Título de exibição da série |
| `series_part` | number | — | Número da parte dentro da série |
| `location` | object | — | Post de viagem com **um** ponto: `{ lat, lng, label }` — aparece no mapa de `/viagens/` |
| `locations` | list | — | Post de viagem com **múltiplos** pontos: `[{ lat, lng, label }, ...]` |
| `countries` | list | — | País(es) visitados no post, **em inglês** (ex.: `[Malta]`, `[Albania, Greece]`) — cada valor deve ser igual ao `name` de uma entrada em `_data/countries.yml`; a tradução em pt-BR (`name_pt`) é exibida quando a UI está em pt-BR. Usado na tabela "Artigos por país" de `/viagens/` |

---

## 🧩 Componentes disponíveis nos artigos

Os componentes abaixo são usados como HTML inline dentro do Markdown.

### Callout

```html
<div class="callout callout-tip">
  <div class="callout-label">Dica</div>
  Texto do callout aqui.
</div>

<div class="callout callout-warn">
  <div class="callout-label">Atenção</div>
  Texto de aviso aqui.
</div>
```

### Bloco de código customizado

```html
<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">PHP 8.2+</div>
  </div>
  <pre>// seu código aqui</pre>
</div>
```

### Parágrafo de destaque (lead)

```html
<p class="lead">Texto de abertura em destaque, levemente maior e em itálico.</p>
```

### Divisor de seção

```html
<div class="divider">· · ·</div>
```

### Galeria de fotos

Requer `gallery: true` no front matter (carrega o GLightbox). As fotos ficam na pasta do post, `assets/img/posts/<post-slug>/`, e cada uma entra pelo include `photo.html` — nunca por `<img>` escrito à mão:

```liquid
<div class="photo-gallery">
  {% include photo.html src="/assets/img/posts/meu-artigo/01-canal-entardecer.jpg"
     alt="Canal do centro histórico ao fim da tarde, com casas de canal e um barco"
     title="Centro histórico, no fim da tarde da chegada — 25/04"
     gallery="amsterda" %}
  {% include photo.html src="/assets/img/posts/meu-artigo/02-oosterdok.jpg"
     alt="Pôr do sol no Oosterdok visto da ponte"
     title="Pôr do sol no Oosterdok — 25/04"
     gallery="amsterda" %}
</div>
```

O include gera `<a class="glightbox" href="<original>" data-gallery data-title>` envolvendo um `<picture>` com `srcset` AVIF/WebP em 480/960/1600 px, `sizes` ajustado à grade da galeria, `width`/`height` intrínsecos (zero layout shift), `loading="lazy"` e `decoding="async"`. O GLightbox continua abrindo o original em resolução cheia. As regras editoriais de `alt` e `title` (→ `data-title`) são as mesmas de antes: `alt` descreve o que aparece na foto; `title` é a legenda do lightbox.

Parâmetros opcionais: `sizes` (sobrescreve o `sizes`), `loading="eager"` (foto acima da dobra), `class` e `lightbox=false` (foto avulsa no corpo do texto, sem lightbox, em largura total).

Os derivados vêm de `.github/scripts/build_images.py` ([Scripts e automação](#-scripts-e-automação)); sem eles — clone novo, ou foto fora de uma pasta por post — o include cai no `<img>` simples de antes.

---

## 💻 Desenvolvimento local

```bash
# Pré-requisitos: Ruby 3.x + Bundler
gem install bundler

# Instalar dependências
bundle install

# Iniciar servidor local com live reload
bundle exec jekyll serve

# Acesse em: http://localhost:4000/blog
```

`git_last_modified.rb` lê o histórico do git a partir do clone local — rode os comandos acima dentro de um clone normal (não raso) para ver as datas de "atualizado em" corretas em desenvolvimento.

Para rodar a auditoria de estrutura localmente antes de abrir um PR:

```bash
python3 .github/scripts/audit_blog.py
```

Fotos de galeria: sem os derivados, `jekyll serve` mostra o `<img>` simples. Para ver o `<picture>` responsivo como em produção (e para sanitizar fotos novas antes de commitar):

```bash
python3 -m pip install "Pillow>=11.2"
python3 .github/scripts/build_images.py
```

### Plugins utilizados

**Gems (`Gemfile`, comportamento pronto):**

| Plugin | Função |
|---|---|
| `jekyll-feed` | Gera `/feed.xml` automaticamente |
| `jekyll-seo-tag` | Meta tags Open Graph e Twitter Card; JSON-LD só nas páginas que não são posts — no post, `_includes/schema.html` assume (ver `seo_tag_json_ld_opt_out.rb`) |
| `jekyll-sitemap` | Gera `/sitemap.xml` automaticamente (lê `last_modified_at` quando presente) |
| `jekyll-paginate-v2` | Paginação avançada da página inicial |
| `jekyll-redirect-from` | Redirecionamentos via front matter |

**Plugins customizados (`_plugins/`, código deste repositório):** ver [Scripts e automação](#-scripts-e-automação).

---

## 🎨 Design system

| Elemento | Valor |
|---|---|
| Fonte de display | Playfair Display (700 / italic) |
| Fonte de corpo | Source Serif 4 (300 / 400 / 600) |
| Fonte mono | JetBrains Mono (400 / 500) |
| Cor principal | `#1a1714` (ink) |
| Cor de acento | `#2d6a4f` (verde) |
| Cor de acento quente | `#b85c00` (âmbar) |
| Destaque verde | `#93c97a` |
| Superfície | `#faf9f6` |

Todos os tokens estão em `assets/css/main.css` como variáveis CSS em `:root`.

---

## 📚 Documentação adicional

- **[CONTEXT.md](CONTEXT.md)** — glossário de domínio: o que é um Post, Category, Subcategory, Tag, Series e Trip, e como se relacionam.
- **[docs/adr/](docs/adr/)** — Architecture Decision Records explicando por que categoria/tag/feed viraram páginas geradas em vez de arquivos físicos, como o workflow de posts escritos com apoio de IA funciona, por que as fotos de galeria são sanitizadas no repositório e servidas via derivados gerados no build, e por que o card Open Graph é renderizado no CI e comitado no PR.
- **[docs/agents/](docs/agents/)** — documentação voltada a agentes de IA (onde ficam as issues, como o domínio é modelado).
- **[CLAUDE.md](CLAUDE.md)** — instruções para agentes de IA (Claude Code) que trabalham neste repositório.

---

## 📄 Licença

MIT © [Guilherme Branco Stracini](https://github.com/guibranco)
