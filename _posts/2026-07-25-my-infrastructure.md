---
layout: post
lang: en
title: "A Map of My Infrastructure: How I Run a Dozen Side Projects on a Budget"
description: "A walkthrough of the small, multi-provider estate that keeps my portfolio, bots, and APIs running — five hosting surfaces, a decoupled webhook pipeline, a VPN-gated database, external data feeds and two monitoring layers."
date: 2026-07-25
categories: [Infrastructure]
subcategories:
  - "Infrastructure/Self-Hosting"
  - "Infrastructure/DevOps"
  - "Infrastructure/Cloud"
tags: [oci, cloudamqp, vercel, github-pages, nginx, wireguard, homelab, self-hosting, infra, cloud, oracle, ssd-nodes, pivpn, rabbitmq, php, csharp, dotnet, github-actions, appveyor, healthchecks, uptimerobot, side-projects, portfolio]
cover: /assets/img/posts/infra-banner.svg
image: /assets/img/posts/infra-og.png
---

<p class="lead">I maintain a growing collection of side projects — a chat-style bot, a handful of small APIs, a couple of dashboards, and the odd legacy site I can't quite bring myself to retire. Over time these have spread across several hosting providers, and I recently sat down to draw the whole thing out. This post is a tour of that map: what runs where, and why.</p>

<figure style="margin:1.75rem auto;max-width:960px;">
  <object
    type="image/svg+xml"
    data="{{ site.baseurl }}/assets/img/posts/infra-map-animated.svg"
    aria-label="An animated diagram of my personal infrastructure across five hosting surfaces"
    style="width:100%;display:block;border-radius:8px;border:1px solid var(--border);box-shadow:0 4px 20px var(--shadow,rgba(26,23,20,.08));">
    <img id="infra-map-raster"
      src="{{ site.baseurl }}/assets/img/posts/infra-map-dark.png"
      data-light="{{ site.baseurl }}/assets/img/posts/infra-map-light.png"
      data-dark="{{ site.baseurl }}/assets/img/posts/infra-map-dark.png"
      alt="A diagram of my personal infrastructure across five hosting surfaces"
      style="width:100%;display:block;border-radius:8px;border:1px solid var(--border);">
  </object>
  <figcaption style="text-align:center;color:var(--ink-muted);font-size:.85rem;margin-top:.6rem;">
    The live map — traffic, queue, VPN and monitoring flows animate, and it follows your light / dark theme. Static image shown if your browser blocks SVG animation.
  </figcaption>
</figure>

<script>
(function () {
  var img = document.getElementById('infra-map-raster');
  if (!img) return;
  function sync() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    var next = dark ? img.getAttribute('data-dark') : img.getAttribute('data-light');
    if (next && img.getAttribute('src') !== next) img.setAttribute('src', next);
  }
  sync();
  new MutationObserver(sync).observe(document.documentElement,
    { attributes: true, attributeFilter: ['data-theme'] });
})();
</script>

The map is organized by **provider**, and within each provider by **server**. On every server the ordering is deliberate: anything that isn't a web service — a background daemon, a scheduled script, a VPN — sits at the top, then the reverse proxy, then the HTTP APIs below it. Once you know that rule, you can read any box top-to-bottom and immediately tell what's exposed to the web and what isn't.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Five places to run things</h2></div>
</div>

The estate spans five hosting surfaces, each chosen for what it's genuinely good at rather than out of loyalty to any one vendor.

<div class="providers-grid">

  <div class="provider-card">
    <div class="provider-name">Nuvem Hospedagem — Shared cPanel</div>
    <div class="provider-detail">The oldest tenant. Hosts my first portfolio (<a href="https://zerocool.com.br" target="_blank">zerocool.com.br</a>), email, a shared database and the original GStraccini-Bot site. Also home to the <em>API BR</em> family (<a href="https://apibr.com" target="_blank">apibr.com</a>) — jobs aggregator, sports agenda, banks reference, currency and account-balance endpoints. Read-heavy PHP with a mail server: cheap, and it just works.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name">Oracle Cloud (OCI) — 4 Always-Free VMs</div>
    <div class="provider-detail">Four single-core always-free instances doing the heavy lifting for anything needing a real Linux box. Each is a focused, single-purpose worker: VPN gateway, webhook ingestion, queue consumer, scheduled trigger and newer APIs — including a job-vacancy labeler bot and an economic-indicators mirror. Every VM runs its own NGINX as the front door — the full breakdown of what runs where is in [18 serviços em 4 VMs de 1 GB](/blog/artigos/18-servicos-4-vms-1gb-free-tier/).</div>
  </div>

  <div class="provider-card">
    <div class="provider-name">SSD Nodes VPS — 8 cores / 32 GB</div>
    <div class="provider-detail">Still on the drawing board — planned for workloads the tiny OCI instances can't comfortably host: a self-hosted message broker, PostgreSQL, Redis, Elasticsearch, a finance organiser and a trading bot. The goal is provider diversity and real headroom.</div>
    <div class="provider-price">Planned · not yet live</div>
  </div>

  <div class="provider-card">
    <div class="provider-name">Vercel</div>
    <div class="provider-detail">Three deploy-and-forget projects: a progress-bar widget and a couple of GitHub readme-stats tools. The right home for static or serverless work that benefits from a global edge without thinking about it.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name">GitHub Pages</div>
    <div class="provider-detail">All public front-ends and documentation: portfolio, this blog, and the browser UIs for nearly every API I run — bookmarks, exchange rates, pull-request tooling, a log viewer and more. Each UI is a static SPA talking to its corresponding API on one of the VMs. Free, versioned, backed by the same git repos as the code.</div>
  </div>

</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Webhook processing, decoupled</h2></div>
</div>

When something happens on GitHub, the delivery lands on a C# ingestion service on one of the VMs. That service does almost nothing except validate the payload and drop it onto a message queue hosted on [**CloudAMQP**](/blog/artigos/rabbitmq-gratuito-cloudamqp/) (their free tier runs a LavinMQ broker — I actually have several instances spread across regions). A separate processor on a *different* VM consumes from the queue and writes the result to the database.

The bot family leans on this pattern more than once. The GStraccini-Bot queues sit behind a small **load-balanced pool** — because each free-tier LavinMQ instance is capped at two million messages a month, spreading the bot's traffic across three instances buys real headroom before I hit any limit. The job-vacancy labeler bot runs the same shape end to end: GitHub webhook → its own ingress → a dedicated Vagas queue → a worker that applies the labels.

<div class="callout callout-tip">
  <div class="callout-label">Why the split?</div>
  Resilience. If the processor is down or slow, messages pile up in the queue while the ingestion service keeps happily acknowledging GitHub's deliveries — nothing is lost and GitHub never sees a failed webhook. Coupling ingestion and processing into one service (how the old PHP version worked) meant an outage in one took down the other.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Email as an ingestion channel</h2></div>
</div>

A neat trick I lean on: some services are fed *by email*. A message arrives at the shared host's mail server, a small PHP script picks it up and forwards it over HTTP to the relevant API on a VM. It lets the shared host do what it's uniquely good at — receiving mail — while the real application logic lives in a proper API I control.

Two of my newer services ingest their data exactly this way. The shared host becomes a lightweight gateway; the VM does the actual work.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Standing on other people's data</h2></div>
</div>

Several of my services are only as good as an upstream I don't control. That's a real dependency — different in kind from the infrastructure I rent — so on the map it gets its own class: **external data providers**, the sources of record my APIs mirror or aggregate.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Jobs — the vacancy aggregator</div>
    <div class="provider-detail">Pulls openings from <strong>ProgramaThor</strong>, <strong>LinkedIn</strong> and <strong>GitHub</strong> issue boards. A scrape-shaped dependency: when a site changes its markup, the aggregator notices before I do.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Sports — the agenda</div>
    <div class="provider-detail">Fixtures and results from <strong>ESPN</strong> and <strong>O Gol</strong>. Two sources so one going quiet doesn't blank the schedule.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Markets — stocks &amp; funds</div>
    <div class="provider-detail">Listed-fund data from <strong>B3</strong> (the Brazilian exchange) and <strong>FIIs.com.br</strong>, feeding the stocks and REIT endpoints.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Economy — indicators</div>
    <div class="provider-detail">The <strong>Central Bank of Brazil</strong> time-series API (BCB SGS) backs an <em>indicators</em> service — a small mirror of figures like the minimum wage and reference rates.</div>
  </div>
</div>

<div class="callout callout-warn">
  <div class="callout-label">Liveness isn't freshness</div>
  A mirror has a failure mode a plain API doesn't: it can be perfectly <em>alive</em> — fast, returning 200, every probe green — while quietly serving <em>stale</em> data because the upstream sync stopped days ago. So the indicators service carries two checks, not one: a liveness ping from its <code>/health</code> endpoint, and a separate freshness ping that only fires on a successful sync. On the map that's a tri-state: green when both pass, amber when it's alive but stale, red when it's down. A green dot that means "responding" would be lying about the one thing that matters for a data mirror.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>A private tunnel to the database</h2></div>
</div>

The database never accepts connections from the open internet. Instead, a **WireGuard VPN** (via [PiVPN](/blog/artigos/criando-uma-vpn-gratis-com-oci-oracle-cloud-infrastructure/)) runs on one of the OCI VMs, and anything that needs database access — including **GitHub Actions** CI pipelines — joins the tunnel and reaches the database through an encrypted connection. Ephemeral CI runners spin up, connect to the VPN, do their work, and vanish. The database's attack surface stays effectively zero.

<div class="callout callout-tip">
  <div class="callout-label">One tunnel, two jobs</div>
  That same VPN pulls double duty as an <strong>exit node</strong> — so I (and a few friends) can browse with a Brazilian IP address when we need one. One tunnel, two completely different jobs.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>CI/CD from two directions</h2></div>
</div>

Continuous integration runs through both **GitHub Actions** and [**AppVeyor**](/blog/artigos/appveyor-vs-github-actions/) — the latter as a complementary pipeline that still notifies one of my legacy webhook handlers when builds complete. Belt and braces.

<table class="compare-table">
  <thead>
    <tr><th>Pipeline</th><th>Role</th><th>Triggers</th></tr>
  </thead>
  <tbody>
    <tr><td>GitHub Actions</td><td>Primary CI/CD, database migrations, deployment</td><td>Push, PR, schedule, workflow_dispatch</td></tr>
    <tr><td>AppVeyor</td><td>Complementary build validation (legacy .NET Framework)</td><td>Push — notifies webhook handler on build complete</td></tr>
  </tbody>
</table>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Keeping an eye on all of it</h2></div>
</div>

With this many moving parts across this many providers, monitoring isn't optional. Two external services watch the estate from opposite directions:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">healthchecks.io — dead-man's switch</div>
    <div class="provider-detail">Services and scheduled scripts ping it when they succeed. It alerts when a ping <em>doesn't</em> arrive. Perfect for catching the silent failures — a cron job that simply stops firing, for example.</div>
    <div class="provider-price">Inbound pings · silence = alert</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">UptimeRobot — outbound polling</div>
    <div class="provider-detail">Polls public endpoints from the outside to confirm they're reachable. Complementary to healthchecks — one watches internal heartbeats, the other watches the public face.</div>
    <div class="provider-price">External polling · public endpoints</div>
  </div>
</div>

On top of that, a home-grown **Projects Monitor** service watches everything internally — it has a connection to every other service on the map, which is why, in the diagram, it's the box with threads running to absolutely everything.

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>Why bother mapping it?</h2>
  <p>Two reasons. First, drawing it forced me to notice things I'd lost track of — a legacy endpoint still receiving traffic, a service quietly depending on a broker on another continent, a box carrying more than its share of RAM, and a whole class of upstream data sources I'd never modelled as dependencies at all. Second, the map now doubles as a launchpad: every provider, control panel and monitoring dashboard is one click away from the same diagram.</p>
  <p>The estate keeps growing, and the map grows with it. If there's interest, I'll write a follow-up on the specific tooling that keeps it maintainable — the config-driven diagram itself, the healthcheck patterns, and how I keep a dozen deployments from becoming a dozen headaches.</p>
</div>
