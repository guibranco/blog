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
│   ├── schema.html                   # JSON-LD (schema.org)
│   └── analytics.html
│
├── _plugins/                         # Generators e filtros Ruby customizados (ver "Scripts e automação")
│   ├── category_pages_generator.rb   # Gera /categorias/{cat}/ e /categorias/{cat}/{sub}/
│   ├── tag_pages_generator.rb        # Gera /topicos/{slug}/
│   ├── feed_generator.rb             # Gera /feed/{cat}.xml e /feed/{cat}-{sub}.xml
│   ├── git_last_modified.rb          # Calcula a data real de "última atualização" via histórico do git
│   └── localized_date.rb             # Filtro Liquid `localized_date` — nomes de mês em pt-BR/en
│
├── _data/
│   ├── categories.yml                # Categorias/subcategorias (nome, slug, ícone, redirect_from)
│   ├── tags.yml                      # Tags (nome, slug, redirect_from) — uma página por entrada
│   ├── countries.yml                 # Países visitados em posts de viagem (nome, slug) — lista curada
│   ├── i18n.yml                      # Strings de UI em pt-BR e en
│   └── quotes.yml                    # Lista de quotes da sidebar
│
├── assets/
│   ├── css/
│   │   └── main.css                  # Estilos compartilhados (tokens CSS em :root)
│   ├── js/
│   │   └── lang-switcher.js          # Troca o idioma da UI no cliente + detecta idioma do navegador
│   └── img/
│       ├── cover.jpg                 # Imagem de fundo da sidebar
│       ├── avatar.png                # Foto de perfil circular
│       └── posts/                    # Imagens/covers dos artigos
│
├── docs/
│   ├── adr/                          # Architecture Decision Records
│   └── agents/                       # Documentação voltada a agentes de IA (issue tracker, domínio)
│
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml                # Build + deploy no GitHub Pages (push em main)
│   │   ├── blog-audit.yml            # Roda audit_blog.py em push/PR que tocam posts ou dados
│   │   └── sync-category-tag-data.yml # Registra categorias/tags novas automaticamente em PRs
│   └── scripts/
│       ├── audit_blog.py             # Audita a estrutura do blog
│       └── create_missing_pages.py   # Sincroniza _data/categories.yml e _data/tags.yml
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
reading_time: 8
cover: /assets/img/posts/meu-artigo-cover.svg    # opcional — imagem usada no site (hero do post e card na listagem)
image: /assets/img/posts/meu-artigo-cover.png    # opcional — imagem estática usada no Open Graph/Twitter card e no schema.org (via jekyll-seo-tag)
---
```

Se apenas `image` for definido, ele é usado tanto no site quanto no Open Graph (comportamento antigo, ainda suportado). `cover` serve para permitir uma imagem animada (SVG) na página sem quebrar o preview em redes sociais, que exigem um raster estático.

Ver [Front matter — referência completa](#-front-matter--referência-completa) para todos os campos disponíveis, incluindo `series*` e `location`/`locations`/`countries` para posts de viagem.

**3.** Escreva o conteúdo em Markdown. Componentes visuais customizados como callouts, blocos de código com syntax highlighting e cards podem ser usados diretamente com HTML inline.

**4.** Publique via branch + pull request — **não dê push direto em `main`**:

```bash
git checkout -b feat/novo-artigo-sobre-x
git add .
git commit -m "feat: novo artigo sobre X"
git push origin feat/novo-artigo-sobre-x
```

Abra o PR no GitHub. Ao abrir/atualizar o PR:

- `sync-category-tag-data.yml` registra categorias/subcategorias/tags novas em `_data/` automaticamente (só roda em eventos de `pull_request` — um push direto em `main` pula essa etapa silenciosamente).
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
| Imagem externa referenciada no corpo do post retornando erro HTTP | ⚠️ aviso (⚠️ apenas o `image:` de capa é bloqueante) |
| `description`/`reading_time`/`image` ausentes | ⚠️ aviso |
| `cover:` num formato inesperado | ⚠️ aviso |

Rodar localmente:

```bash
python3 .github/scripts/audit_blog.py
# lê audit-report.md ao final, ou o output impresso no terminal
```

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

### Workflows (`.github/workflows/`)

| Workflow | Dispara em | O que faz |
|---|---|---|
| `deploy.yml` | push em `main` (ou manual) | `jekyll build` + deploy no GitHub Pages |
| `blog-audit.yml` | push/PR tocando posts ou `_data/{tags,categories,countries}.yml` | Roda `audit_blog.py` |
| `sync-category-tag-data.yml` | abertura/atualização de PR | Roda `create_missing_pages.py` e comita/comenta o resultado |

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
| `reading_time` | number | — | Tempo estimado de leitura em minutos |
| `image` | path | — | Imagem de capa (og:image/Twitter card) — precisa ser raster (png/jpg/jpeg/gif) |
| `cover` | path | — | Hero visual da página do post (SVG, PNG, JPG, GIF ou WebP) |
| `gallery` | boolean | — | Ativa o lightbox (GLightbox) para imagens `.glightbox` no corpo do post |
| `featured` | boolean | — | Fixa o post na seção de destaques da home |
| `series` | string | — | Slug da série (agrupa posts na navegação de série e em `/series/`) |
| `series_title` | string | — | Título de exibição da série |
| `series_part` | number | — | Número da parte dentro da série |
| `location` | object | — | Post de viagem com **um** ponto: `{ lat, lng, label }` — aparece no mapa de `/viagens/` |
| `locations` | list | — | Post de viagem com **múltiplos** pontos: `[{ lat, lng, label }, ...]` |
| `countries` | list | — | País(es) visitados no post (ex.: `[Malta]`, `[Albânia, Grécia]`) — devem existir em `_data/countries.yml`; usado na tabela "Artigos por país" de `/viagens/` |

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

### Plugins utilizados

**Gems (`Gemfile`, comportamento pronto):**

| Plugin | Função |
|---|---|
| `jekyll-feed` | Gera `/feed.xml` automaticamente |
| `jekyll-seo-tag` | Meta tags Open Graph e Twitter Card |
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
- **[docs/adr/](docs/adr/)** — Architecture Decision Records explicando por que categoria/tag/feed viraram páginas geradas em vez de arquivos físicos, e como o workflow de posts escritos com apoio de IA funciona.
- **[docs/agents/](docs/agents/)** — documentação voltada a agentes de IA (onde ficam as issues, como o domínio é modelado).
- **[CLAUDE.md](CLAUDE.md)** — instruções para agentes de IA (Claude Code) que trabalham neste repositório.

---

## 📄 Licença

MIT © [Guilherme Branco Stracini](https://github.com/guibranco)
