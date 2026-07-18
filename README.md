<div align="center">

# ✈️🛠️ Tecnologia & Viagens

**Blog sobre tecnologia, infraestrutura e automação para quem viaja e constrói.**

Publicado via [Jekyll](https://jekyllrb.com/) · Hospedado via [GitHub Pages](https://pages.github.com/) · Zero custo de servidor

[![Deploy](https://github.com/guibranco/blog/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/guibranco/blog/actions)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red?logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

[🌐 Ver o blog](https://guilherme.stracini.com.br/blog) · [📡 RSS](https://guilherme.stracini.com.br/blog/feed.xml) · [🗺️ Sitemap](https://guilherme.stracini.com.br/blog/sitemap.xml)

</div>

---

## 📋 Sobre

Blog pessoal construído com Jekyll e publicado gratuitamente via GitHub Pages. Cada artigo é um arquivo Markdown em `_posts/` — um `git push` para a branch `main` dispara o build e publica automaticamente em ~1 minuto.

O design é totalmente customizado — sem temas de terceiros — com tipografia editorial (Playfair Display + Source Serif 4 + JetBrains Mono), sidebar fixa com avatar, ícones sociais e navegação por categorias e tópicos.

---

## 🗂️ Estrutura do projeto

```
blog/                                # nome do repositório
│
├── _posts/                          # Artigos em Markdown (30+ posts)
│   └── AAAA-MM-DD-slug.md
│
├── _layouts/
│   ├── post.html                    # Template de artigo
│   ├── page.html                    # Template de página estática
│   ├── category.html                # Template de página de categoria
│   └── tag.html                     # Template de página de tópico/tag
│
├── _includes/                       # Partials reutilizáveis
│   ├── sidebar.html
│   ├── sidebar-script.html
│   ├── footer.html
│   ├── post-card.html
│   ├── pagination.html
│   ├── breadcrumb.html
│   ├── series.html
│   └── analytics.html
│
├── _data/
│   └── quotes.yml                   # Lista de quotes da sidebar
│
├── categorias/                      # Uma página .md por categoria
│   ├── career.md
│   ├── coding.md
│   ├── devops.md
│   ├── hobbies.md
│   ├── infraestrutura.md
│   ├── investments.md
│   ├── telecomunicacoes.md
│   ├── testing.md
│   └── travel-places.md
│
├── topicos/                         # Uma página .md por tag (geradas automaticamente)
│   └── <slug>.md                    # Centenas de páginas de tópicos
│
├── feed/                            # Feeds RSS por categoria
│   ├── career.xml
│   ├── coding.xml
│   ├── devops.xml
│   ├── hobbies.xml
│   ├── infraestrutura.xml
│   ├── investments.xml
│   ├── telecomunicacoes.xml
│   ├── testing.xml
│   └── travel-places.xml
│
├── assets/
│   ├── css/
│   │   └── main.css                 # Estilos compartilhados (tokens CSS em :root)
│   └── img/
│       ├── cover.jpg                # Imagem de fundo da sidebar
│       └── avatar.png               # Foto de perfil circular
│
├── index.html                       # Página inicial (paginada)
├── busca.html                       # Página de busca
├── viagens.html                     # Página de viagens
├── search.json                      # Índice de busca client-side
├── 404.html                         # Página de erro 404
├── _config.yml                      # Configurações do Jekyll
├── Gemfile                          # Dependências Ruby
└── README.md
```

---

## 🗃️ Gerenciando categorias

O Jekyll não gera páginas de categoria automaticamente. Para cada nova categoria usada nos posts, é preciso criar um arquivo `.md` correspondente em `categorias/`.

**Criando uma nova categoria:**

```bash
cat > categorias/devops.md << 'FRONTMATTER'
---
layout: category
category: DevOps
permalink: /categorias/devops/
---
FRONTMATTER
```

A categoria declarada no campo `category:` deve ser idêntica à usada no front matter dos posts (incluindo acentos e capitalização). O `permalink` usa a versão slugificada, sem acentos.

**Categorias existentes:**

| Categoria | Arquivo | URL |
|---|---|---|
| Career | `categorias/career.md` | `/categorias/career/` |
| Coding | `categorias/coding.md` | `/categorias/coding/` |
| DevOps | `categorias/devops.md` | `/categorias/devops/` |
| Hobbies | `categorias/hobbies.md` | `/categorias/hobbies/` |
| Infraestrutura | `categorias/infraestrutura.md` | `/categorias/infraestrutura/` |
| Investments | `categorias/investments.md` | `/categorias/investments/` |
| Telecomunicações | `categorias/telecomunicacoes.md` | `/categorias/telecomunicacoes/` |
| Testing | `categorias/testing.md` | `/categorias/testing/` |
| Travel Places | `categorias/travel-places.md` | `/categorias/travel-places/` |

> Ao publicar um post com uma categoria nova, lembre-se sempre de criar o arquivo correspondente em `categorias/` e o feed correspondente em `feed/` — caso contrário os links retornarão 404.

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
title: "Título do artigo"
description: "Resumo em uma linha para SEO e cards."
date: 2026-04-10
categories: [Infraestrutura]
tags: [docker, linux, automação]
reading_time: 8
cover: /assets/img/posts/meu-artigo-cover.svg    # opcional — imagem usada no site (hero do post e card na listagem)
image: /assets/img/posts/meu-artigo-cover.png    # opcional — imagem estática usada no Open Graph/Twitter card e no schema.org (via jekyll-seo-tag)
---
```

Se apenas `image` for definido, ele é usado tanto no site quanto no Open Graph (comportamento antigo, ainda suportado). `cover` serve para permitir uma imagem animada (SVG) na página sem quebrar o preview em redes sociais, que exigem um raster estático.

**3.** Escreva o conteúdo em Markdown. Componentes visuais customizados como callouts, blocos de código com syntax highlighting e cards podem ser usados diretamente com HTML inline.

**4.** Publique:

```bash
git add .
git commit -m "feat: novo artigo sobre X"
git push origin main
```

O GitHub Pages detecta o push, roda o build do Jekyll e publica em ~60 segundos.

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
| `title` | string | ✅ | Título do artigo |
| `date` | date | ✅ | Data de publicação (`AAAA-MM-DD`) |
| `description` | string | — | Subtítulo e meta description para SEO |
| `categories` | list | — | Categorias (aparecem como pills e na nav) |
| `tags` | list | — | Tags (aparecem no rodapé do artigo e geram páginas em `topicos/`) |
| `reading_time` | number | — | Tempo estimado de leitura em minutos |
| `image` | path | — | Caminho da imagem de capa do artigo |

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

### Plugins utilizados

| Plugin | Função |
|---|---|
| `jekyll-feed` | Gera `/feed.xml` automaticamente |
| `jekyll-seo-tag` | Meta tags Open Graph e Twitter Card |
| `jekyll-sitemap` | Gera `/sitemap.xml` automaticamente |
| `jekyll-paginate-v2` | Paginação avançada da página inicial |
| `jekyll-redirect-from` | Redirecionamentos via front matter |

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

## 📄 Licença

MIT © [Guilherme Branco Stracini](https://github.com/guibranco)
