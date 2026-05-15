---
layout: post
title: "Should You Use UUIDs as Primary Keys? Performance Myths, Real-World Trade-Offs, and the Ideal Architecture"
description: "A deep dive into UUID vs. numeric primary key performance — B-Tree fragmentation, the numeric PK + UUID public ID pattern used by Stripe and GitHub, UUIDv7, ULID, and practical recommendations."
date: 2025-12-11
categories: [Coding]
tags: [uuid, primary-key, database, sql, performance, b-tree, uuidv7, ulid, arquitetura, backend, csharp, dotnet]
reading_time: 7
image: /assets/img/posts/UUID-primary-key.png
---

<p class="lead">Database schema design is always full of trade-offs, but few debates are as persistent as the one around <strong>UUIDs vs. numeric primary keys</strong>. If you've ever wondered whether a UUID primary key actually slows down your database — and what to do about it — this post is for you.</p>

Let's go methodically through the myths, the technical reality, and the architecture used by big-scale platforms.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Why do UUID primary keys get a bad reputation?</h2></div>
</div>

On paper, UUIDs look great: they're globally unique, safe to expose, and avoid ID collisions across systems. But under the hood, they affect performance in a few very specific ways.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Sequential vs. random inserts</h2></div>
</div>

One of the core reasons UUID primary keys are slower is how they behave inside a **B-Tree index**.

With a numeric auto-incremented primary key, inserts follow a predictable, sequential pattern. New rows always land at the end of the index — keeping it compact and efficient, with minimal page splits.

With **UUIDv4**, inserts are essentially random. New rows land unpredictably across many index pages, causing fragmentation and page splits on every write. The database must constantly reorganize existing pages to accommodate the new values.

<div class="callout callout-warn">
  <div class="callout-label">The biggest penalty</div>
  B-Tree fragmentation from random UUID inserts is the single most significant performance cost of using UUIDv4 as a primary key. Write-heavy workloads feel this the most.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>The best of both worlds: numeric PK + UUID public ID</h2></div>
</div>

A widely-used pattern — employed by **Stripe, Shopify, GitHub**, and many others — is to combine:

- An **internal numeric primary key** (auto-increment or sequence)
- A **public UUID field** for external exposure (URLs, API endpoints, webhooks)

This provides the write speed of sequential keys while retaining the safety and opacity of UUIDs. Internal joins and foreign keys stay fast and compact; external consumers never see the internal integer.

### Why this works so well

<table class="compare-table">
  <thead>
    <tr>
      <th>Concern</th>
      <th>Numeric PK + UUID public ID</th>
      <th>UUID-only PK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Insert performance</td>
      <td><span class="check">✓</span> Sequential, fast</td>
      <td><span class="cross">✗</span> Random, fragmented</td>
    </tr>
    <tr>
      <td>Foreign key size</td>
      <td><span class="check">✓</span> 4–8 bytes</td>
      <td><span class="cross">✗</span> 16 bytes</td>
    </tr>
    <tr>
      <td>External ID safety</td>
      <td><span class="check">✓</span> UUID hides internal structure</td>
      <td><span class="check">✓</span> UUID hides internal structure</td>
    </tr>
    <tr>
      <td>Index memory pressure</td>
      <td><span class="check">✓</span> Small, lean</td>
      <td><span class="cross">✗</span> Larger, more I/O</td>
    </tr>
    <tr>
      <td>UUID lookup speed</td>
      <td><span class="check">✓</span> Fast via dedicated index</td>
      <td><span class="check">✓</span> Fast (it is the PK)</td>
    </tr>
  </tbody>
</table>

This pattern avoids **all** the classic pitfalls of using UUIDs as primary keys.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Index and storage impact</h2></div>
</div>

The size difference is concrete:

- **UUID:** 16 bytes per value
- **Integer (INT):** 4 bytes
- **Big integer (BIGINT):** 8 bytes

That difference compounds when the same field is used as a primary key, a foreign key in many child tables, and the clustered index on disk. Larger keys mean larger indexes, which means more memory pressure and more I/O per query.

In a table with millions of rows and dozens of related tables, the cumulative storage and memory difference between a UUID PK and a BIGINT PK can be significant — especially when the database's buffer pool is the bottleneck.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Want UUIDs only? Use UUIDv7 or ULID</h2></div>
</div>

If you genuinely need UUIDs as primary keys — for instance in a distributed system where nodes generate IDs independently — there are safer and faster alternatives to UUIDv4:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">UUIDv7</div>
    <div class="provider-detail">Time-ordered UUID. Encodes a Unix timestamp in the most significant bits, making values monotonically increasing. Insert patterns are nearly as sequential as auto-increment integers, eliminating most B-Tree fragmentation.</div>
    <div class="provider-price">RFC 9562 · 2024 standard</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">ULID</div>
    <div class="provider-detail">Universally Unique Lexicographically Sortable Identifier. 128-bit, URL-safe, millisecond precision. Sorts correctly as a string, making it index-friendly and human-readable in logs.</div>
    <div class="provider-price">ulid.github.io</div>
  </div>
</div>

Both maintain index locality — new values always land near the end of the B-Tree, keeping inserts efficient even at scale.

<div class="callout callout-tip">
  <div class="callout-label">UUIDv7 in .NET</div>
  Starting with .NET 9, <code>Guid.CreateVersion7()</code> is built into the BCL — no third-party package needed. For earlier versions, libraries like <strong>UUIDNext</strong> or <strong>Medo.Uuid7</strong> provide the same functionality.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Query flow with UUID public IDs</h2></div>
</div>

Even though the internal primary key is numeric, your APIs can fully expose UUIDs without architectural penalty. The typical request flow:

1. Client sends a request containing a UUID (e.g. `GET /orders/01932f3a-...`)
2. API queries the database using a **dedicated index** on the UUID column
3. Database resolves the numeric PK from that index in a single lookup
4. All internal JOINs and foreign key relationships use the efficient numeric key
5. Response returns to the client using the UUID — the internal integer is never exposed

The UUID index lookup adds one extra index read compared to querying by numeric PK directly, but in practice this is negligible. The wins in write performance, index size, and external security far outweigh this tiny overhead.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Practical recommendations</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Best practice — most applications</div>
    <div class="provider-detail">Use a numeric primary key (INT or BIGINT auto-increment) paired with a UUID <code>public_id</code> column. Index the UUID column. Expose only the UUID externally. You get fast writes, small indexes, secure URLs, and lightweight foreign keys.</div>
    <div class="provider-price">✓ Recommended default</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">UUID-only — when it makes sense</div>
    <div class="provider-detail">Use UUIDv7 or ULID when designing a distributed system that requires global uniqueness across nodes, you won't rely heavily on relational foreign-key joins, and you accept the larger storage footprint.</div>
    <div class="provider-price">⚠ Specific use cases</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Avoid — UUIDv4 as PK</div>
    <div class="provider-detail">UUIDv4 as a primary key is almost never the right choice. Random inserts cause B-Tree fragmentation, page splits, larger indexes, and higher memory pressure — all without any benefit over UUIDv7 or the numeric+UUID pattern.</div>
    <div class="provider-price">✗ Avoid in write-heavy tables</div>
  </div>
</div>

<div class="conclusion">
  <h2>Pick the right tool for the right problem</h2>
  <p>The debate around UUID primary keys often stems from misunderstandings about what UUIDs actually cost and where that cost comes from.</p>
  <p><strong>UUIDv4 as a primary key?</strong> Works, but harms write performance through B-Tree fragmentation. Avoid it in write-heavy tables.</p>
  <p><strong>Numeric PK + UUID public ID?</strong> The most robust and scalable design for everyday relational applications. Used in production by Stripe, Shopify, GitHub and many others.</p>
  <p><strong>UUIDv7 or ULID?</strong> A great alternative when you truly need distributed, globally unique, sortable identifiers — with a much smaller performance penalty than UUIDv4.</p>
  <p>With the full engineering picture in mind, you can choose the right structure for your system with confidence.</p>
</div>
