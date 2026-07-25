---
layout: post
title: "A Map of My Infrastructure: How I Run a Dozen Side Projects on a Budget"
description: "A walkthrough of the small, multi-provider estate that keeps my portfolio, bots, and APIs running — five hosting surfaces, a decoupled webhook pipeline, a VPN-gated database and two monitoring layers."
date: 2026-07-25
categories: [Infraestrutura, DevOps]
subcategories:
  - "Infraestrutura/Self-Hosting"
  - "DevOps/Cloud"
tags: [oci, cloudamqp, vercel, github-pages, nginx, wireguard, homelab, self-hosting, infra, cloud, oracle, ssd-nodes, pivpn, rabbitmq, php, csharp, dotnet, github-actions, appveyor, healthchecks, uptimerobot, side-projects, portfolio]
reading_time: 8
image: /assets/img/posts/infra-map.png
---

<p class="lead">I maintain a growing collection of side projects — a chat-style bot, a handful of small APIs, a couple of dashboards, and the odd legacy site I can't quite bring myself to retire. Over time these have spread across several hosting providers, and I recently sat down to draw the whole thing out. This post is a tour of that map: what runs where, and why.</p>

![A diagram of my personal infrastructure across five hosting surfaces](/assets/img/posts/infra-map.png)

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
    <div class="provider-detail">Four single-core always-free instances doing the heavy lifting for anything needing a real Linux box. Each is a focused, single-purpose worker: VPN gateway, webhook ingestion, queue consumer, scheduled trigger and newer APIs. Every VM runs its own NGINX as the front door.</div>
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

When something happens on GitHub, the delivery lands on a C# ingestion service on one of the VMs. That service does almost nothing except validate the payload and drop it onto a message queue hosted on **CloudAMQP** (their free tier runs a LavinMQ broker — I actually have several instances spread across regions). A separate processor on a *different* VM consumes from the queue and writes the result to the database.

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
  <div class="section-title-wrap"><h2>A private tunnel to the database</h2></div>
</div>

The database never accepts connections from the open internet. Instead, a **WireGuard VPN** (via [PiVPN](/blog/artigos/criando-uma-vpn-gratis-com-oci-oracle-cloud-infrastructure/)) runs on one of the OCI VMs, and anything that needs database access — including **GitHub Actions** CI pipelines — joins the tunnel and reaches the database through an encrypted connection. Ephemeral CI runners spin up, connect to the VPN, do their work, and vanish. The database's attack surface stays effectively zero.

<div class="callout callout-tip">
  <div class="callout-label">One tunnel, two jobs</div>
  That same VPN pulls double duty as an <strong>exit node</strong> — so I (and a few friends) can browse with a Brazilian IP address when we need one. One tunnel, two completely different jobs.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>CI/CD from two directions</h2></div>
</div>

Continuous integration runs through both **GitHub Actions** and **AppVeyor** — the latter as a complementary pipeline that still notifies one of my legacy webhook handlers when builds complete. Belt and braces.

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
  <div class="section-num">06</div>
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
  <p>Two reasons. First, drawing it forced me to notice things I'd lost track of — a legacy endpoint still receiving traffic, a service quietly depending on a broker on another continent, a box carrying more than its share of RAM. Second, the map now doubles as a launchpad: every provider, control panel and monitoring dashboard is one click away from the same diagram.</p>
  <p>The estate keeps growing, and the map grows with it. If there's interest, I'll write a follow-up on the specific tooling that keeps it maintainable — the config-driven diagram itself, the healthcheck patterns, and how I keep a dozen deployments from becoming a dozen headaches.</p>
</div>
