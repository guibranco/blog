<div align="center">

# ✈️🛠️ Tecnologia & Viagens

**Blog sobre tecnologia, infraestrutura e automação para quem viaja e constrói.**

Publicado via [Jekyll](https://jekyllrb.com/) · Hospedado no [GitHub Pages](https://pages.github.com/) · Zero custo de servidor

[![Deploy](https://github.com/guibranco/blog-tech-viagens/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/guibranco/blog-tech-viagens/actions)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red?logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

[🌐 Ver o blog](https://guibranco.github.io/blog-tech-viagens) · [📡 RSS](https://guibranco.github.io/blog-tech-viagens/feed.xml) · [🗺️ Sitemap](https://guibranco.github.io/blog-tech-viagens/sitemap.xml)

</div>

---

## 📋 Sobre

Blog pessoal construído com Jekyll e publicado gratuitamente via GitHub Pages. Cada artigo é um arquivo Markdown em `_posts/` — um `git push` para a branch `main` dispara o build e publica automaticamente em ~1 minuto.

O design é totalmente customizado — sem temas de terceiros — com tipografia editorial (Playfair Display + Source Serif 4 + JetBrains Mono), sidebar fixa com avatar, ícones sociais e navegação por categorias.

---

## 🗂️ Estrutura do projeto

```
blog-tech-viagens/
│
├── _posts/                          # Artigos em Markdown
│   └── 2026-03-20-envio-sms-internet.md
│
├── _layouts/
│   └── post.html                    # Template de artigo
│
├── assets/
│   └── css/
│       └── main.css                 # Estilos compartilhados
│   └── img/
│       ├── cover.jpg                # Imagem de fundo da sidebar
│       └── avatar.jpg               # Foto de perfil circular
│
├── index.html                       # Página inicial
├── _config.yml                      # Configurações do Jekyll
├── Gemfile                          # Dependências Ruby
└── README.md
```

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
image: /assets/img/posts/meu-artigo-cover.jpg   # opcional
---
```

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
author_bio: "Software engineer. PHP, C#, JS, Rust. Integrações, APIs, seguros & logística."
author_avatar: /assets/img/avatar.jpg    # foto circular na sidebar
author_cover: /assets/img/cover.jpg     # imagem de fundo da sidebar

# URLs
url: "https://guibranco.github.io"
baseurl: "/blog-tech-viagens"

# Quote do dia (exibida na sidebar)
quote:
  text: "Never, never, never give up."
  author: "Winston Churchill"

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
  website:       http://guilherme.stracini.com
```

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
| `tags` | list | — | Tags (aparecem no rodapé do artigo e na nuvem da home) |
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

# Acesse em: http://localhost:4000
```

### Plugins utilizados

| Plugin | Função |
|---|---|
| `jekyll-feed` | Gera `/feed.xml` automaticamente |
| `jekyll-seo-tag` | Meta tags Open Graph e Twitter Card |
| `jekyll-sitemap` | Gera `/sitemap.xml` automaticamente |

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
