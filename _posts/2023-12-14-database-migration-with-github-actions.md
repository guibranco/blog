---
layout: post
lang: en
title: "Database migration with GitHub Actions"
description: "How I built a GitHub Action to manage versioned SQL database migrations across MySQL, MariaDB, PostgreSQL and MSSQL — with dry-run, integrity checks, SHA-256 checksums and Docker-based testing, all from a CI/CD pipeline."
date: 2023-12-14
categories: [Coding, Infraestrutura]
subcategories:
  - "Coding/Database"
  - "Infraestrutura/DevOps"
tags: [database, github, github-actions, migration, sql, pipeline, testing, ci-cd, devops, mysql, mariadb, postgresql, mssql, schema, versioning, docker, shell-script, continuous-integration, infrastructure-as-code, gitops, db-migration, query-builder, orm, checksum, integrity]
reading_time: 10
image: /assets/img/posts/database-migration.jpg
---

<p class="lead">Database schema changes are one of the riskiest parts of any deployment. A migration applied twice, out of order, or missing entirely can corrupt data or take an application offline. In this post I walk through a GitHub Action I built to manage versioned SQL migrations across multiple database drivers — with dry-run preview, SHA-256 checksums and integrity checks, all without an ORM or a migration framework dependency.</p>

The action is open source and available at **[guibranco/github-database-migration-action](https://github.com/guibranco/github-database-migration-action){:target="_blank"}**.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>The problem with manual SQL scripts</h2></div>
</div>

Most teams start with a `changes.sql` file or a shared folder of scripts. It works until it doesn't:

- Someone applies `v3` before `v2` on the staging server
- A script gets applied twice because nobody tracked it
- Production is one migration behind and nobody knows which one
- A rollback is needed but there's no record of what changed

Frameworks like Laravel (Artisan), Doctrine, Flyway and Liquibase solve this elegantly — but they require a specific language runtime, an ORM or a Java dependency. If your stack is polyglot, or if you simply want the migrations to live and run in the CI/CD pipeline without installing additional tools, a GitHub Action is a natural fit.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>How the action works</h2></div>
</div>

The action is a Docker-based GitHub Action written in POSIX shell (`sh`). It connects directly to the database using the native client for each driver and manages a `schema_version` table that tracks every applied migration file.

### The `schema_version` table

On first run, the action creates this table automatically — one definition per supported driver:

```sql
-- MySQL / MariaDB
CREATE TABLE IF NOT EXISTS `schema_version` (
  `Sequence` INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  `Filename` VARCHAR(255)     NOT NULL,
  `Checksum` CHAR(64)         NOT NULL,
  `Date`     TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Sequence`),
  UNIQUE (`Filename`),
  UNIQUE (`Checksum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

```sql
-- PostgreSQL
CREATE TABLE IF NOT EXISTS schema_version (
  sequence SERIAL       PRIMARY KEY,
  filename VARCHAR(255) NOT NULL UNIQUE,
  checksum CHAR(64)     NOT NULL UNIQUE,
  date     TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

```sql
-- SQL Server (MSSQL)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='schema_version')
  CREATE TABLE schema_version (
    Sequence INT IDENTITY(1,1) PRIMARY KEY,
    Filename NVARCHAR(255) NOT NULL,
    Checksum CHAR(64)      NOT NULL,
    Date     DATETIME      NOT NULL DEFAULT GETDATE(),
    CONSTRAINT UQ_sv_Filename UNIQUE (Filename),
    CONSTRAINT UQ_sv_Checksum UNIQUE (Checksum)
  );
```

Each row records the **filename**, a **SHA-256 checksum** of the file's content, and the **timestamp** of when it was applied. The `UNIQUE` constraint on `Filename` prevents double-application, and the `UNIQUE` on `Checksum` prevents applying a different file that happens to share a name.

### Migration file naming

All `.sql` files inside a `migrations/` directory at the repository root are processed in **alphabetical order**. The recommended convention is to prefix files with a zero-padded sequence number:

```
migrations/
├── 0001_create_users_table.sql
├── 0002_add_email_index.sql
├── 0003_create_orders_table.sql
└── 0004_add_foreign_keys.sql
```

<div class="callout callout-warn">
  <div class="callout-label">Filename restrictions</div>
  Only alphanumeric characters, dots, hyphens and underscores are allowed in migration filenames. Any other character causes the action to fail with an error. This is intentional — it prevents SQL injection through filename manipulation in the <code>INSERT</code> statement that records the migration.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>The four operations</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">check</div>
    <div class="provider-detail">Lists all migration files and their status — <code>[APPLIED]</code> or <code>[PENDING]</code>. Does not modify the database. Useful as a PR status check.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">dry-run</div>
    <div class="provider-detail">Lists only the <code>[PENDING]</code> migrations — the ones that would be applied. Does not execute any SQL. Safe to run on production.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">migrate</div>
    <div class="provider-detail">Applies all pending migrations in order, skipping already-applied ones. Records each filename and its SHA-256 checksum in <code>schema_version</code>.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">integrity</div>
    <div class="provider-detail">Runs a list of SQL queries from a file and verifies that each returns at least one row. Fails the pipeline if any check returns empty — useful for post-deployment validation.</div>
  </div>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Supported databases</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Driver</th><th>Value</th><th>Client used</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td>MySQL</td><td><code>mysql</code></td><td><code>mysql</code> CLI</td><td>Full support</td></tr>
    <tr><td>MariaDB</td><td><code>mariadb</code></td><td><code>mysql</code> CLI</td><td>Full support (compatible with MySQL client)</td></tr>
    <tr><td>PostgreSQL</td><td><code>postgresql</code></td><td><code>psql</code></td><td>Full support</td></tr>
    <tr><td>SQL Server</td><td><code>mssql</code></td><td><code>tsql</code> (FreeTDS)</td><td>Full support</td></tr>
    <tr><td>Oracle 11g</td><td><code>oracle11g</code></td><td>n/a</td><td>Not bundled — requires custom Docker image with Oracle Instant Client</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Oracle 11g</div>
  Oracle Instant Client cannot be bundled in the public Docker image due to licensing restrictions. To use Oracle, build a custom image <code>FROM guibranco/github-database-migration-action</code> and add Oracle Instant Client and <code>sqlplus</code> manually.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>Configuration and inputs</h2></div>
</div>

```yaml
- uses: guibranco/github-database-migration-action@latest
  env:
    DATABASE_PWD: ${{ secrets.DATABASE_PWD }}
  with:
    operation: migrate         # dry-run | migrate | check | integrity
    driver:    mysql           # mysql | mariadb | postgresql | mssql
    host:      127.0.0.1
    user:      app_user
    database:  my_database
    integrity_commands_file: integrity-checks.sql  # only for integrity operation
```

<div class="callout callout-warn">
  <div class="callout-label">Never put the password in <code>with:</code></div>
  The database password is passed as an <strong>environment variable</strong> (<code>DATABASE_PWD</code>), not as an input. GitHub Actions masks environment variables set from secrets, so the password never appears in logs. Passing it as an input would expose it in the workflow run summary.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Full workflow examples</h2></div>
</div>

### Check on every pull request

Show migration status without touching the database — great as a PR reviewer aid:

```yaml
name: Migration status

on:
  pull_request:

jobs:
  status:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: mydb
          MYSQL_USER: app
          MYSQL_PASSWORD: secret
        ports: ["3306:3306"]
        options: >-
          --health-cmd="mysqladmin ping -h 127.0.0.1 -uroot -proot"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=5

    steps:
      - uses: actions/checkout@v4

      - name: Check migration status
        uses: guibranco/github-database-migration-action@latest
        env:
          DATABASE_PWD: secret
        with:
          operation: check
          driver:    mysql
          host:      127.0.0.1
          user:      app
          database:  mydb
```

### Migrate on merge to main

Apply pending migrations automatically when code reaches the main branch:

```yaml
name: Deploy migrations

on:
  push:
    branches: [main]
    paths:
      - 'migrations/**.sql'

jobs:
  migrate:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Dry-run first
        uses: guibranco/github-database-migration-action@latest
        env:
          DATABASE_PWD: ${{ secrets.PROD_DB_PASSWORD }}
        with:
          operation: dry-run
          driver:    postgresql
          host:      ${{ secrets.PROD_DB_HOST }}
          user:      ${{ secrets.PROD_DB_USER }}
          database:  ${{ secrets.PROD_DB_NAME }}

      - name: Apply migrations
        uses: guibranco/github-database-migration-action@latest
        env:
          DATABASE_PWD: ${{ secrets.PROD_DB_PASSWORD }}
        with:
          operation: migrate
          driver:    postgresql
          host:      ${{ secrets.PROD_DB_HOST }}
          user:      ${{ secrets.PROD_DB_USER }}
          database:  ${{ secrets.PROD_DB_NAME }}

      - name: Verify integrity
        uses: guibranco/github-database-migration-action@latest
        env:
          DATABASE_PWD: ${{ secrets.PROD_DB_PASSWORD }}
        with:
          operation:               integrity
          driver:                  postgresql
          host:                    ${{ secrets.PROD_DB_HOST }}
          user:                    ${{ secrets.PROD_DB_USER }}
          database:                ${{ secrets.PROD_DB_NAME }}
          integrity_commands_file: integrity-checks.sql
```

### Testing with a Docker service (multi-driver matrix)

Run the full migration suite against multiple databases in parallel:

```yaml
name: CI — Migration tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - driver: mysql
            image:  mysql:8.0
            env:    {MYSQL_ROOT_PASSWORD: root, MYSQL_DATABASE: test, MYSQL_USER: test, MYSQL_PASSWORD: test}
            port:   "3306:3306"
            health: "mysqladmin ping -h 127.0.0.1 -uroot -proot"
          - driver: mariadb
            image:  mariadb:11.4
            env:    {MARIADB_ROOT_PASSWORD: root, MARIADB_DATABASE: test, MARIADB_USER: test, MARIADB_PASSWORD: test}
            port:   "3306:3306"
            health: "healthcheck.sh --connect --innodb_initialized"
          - driver: postgresql
            image:  postgres:16
            env:    {POSTGRES_DB: test, POSTGRES_USER: test, POSTGRES_PASSWORD: test}
            port:   "5432:5432"
            health: "pg_isready -U test"

    services:
      db:
        image: ${{ matrix.image }}
        env:   ${{ matrix.env }}
        ports: [${{ matrix.port }}]
        options: --health-cmd="${{ matrix.health }}" --health-interval=10s --health-retries=5

    steps:
      - uses: actions/checkout@v4

      - name: Run migrations (${{ matrix.driver }})
        uses: guibranco/github-database-migration-action@latest
        env:
          DATABASE_PWD: test
        with:
          operation: migrate
          driver:    ${{ matrix.driver }}
          host:      127.0.0.1
          user:      test
          database:  test
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Integrity checks</h2></div>
</div>

The `integrity` operation runs a file of SQL queries (one per line) and verifies that each one returns at least one row. If any query returns empty, the step fails and the pipeline stops.

**`integrity-checks.sql`:**
```sql
-- Verify the users table exists and has at least one row
SELECT 1 FROM users LIMIT 1

-- Verify a required index exists (MySQL example)
SELECT 1 FROM information_schema.statistics
  WHERE table_name = 'users' AND index_name = 'idx_users_email'

-- Verify a foreign key constraint exists
SELECT 1 FROM information_schema.key_column_usage
  WHERE constraint_name = 'fk_orders_user_id'

-- Verify a required seed record exists
SELECT 1 FROM roles WHERE name = 'admin'

# Lines starting with # are comments and are skipped
```

<div class="callout callout-tip">
  <div class="callout-label">When to use integrity checks</div>
  Run <code>integrity</code> immediately after <code>migrate</code> in the same deployment workflow. It acts as a smoke test confirming that the expected schema objects and seed data are in place before the application starts routing production traffic.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Implementation highlights</h2></div>
</div>

A few design decisions in the shell script are worth calling out:

**`MIG:` prefix for reliable result parsing.** Each driver client adds different noise to its output (column headers, row counts, locale messages). To reliably extract filenames from the `schema_version` query, every `SELECT` wraps the value in a `MIG:` prefix, then `grep '^MIG:'` filters out everything else regardless of the driver.

```sh
exec_sql_mysql "SELECT CONCAT('MIG:', Filename) FROM schema_version ORDER BY Sequence;"
# output contains: MIG:0001_create_users_table.sql
```

**SHA-256 checksums.** Every migration file is hashed with `sha256sum` before and after application. The hash is stored in `schema_version`. If the same filename is re-submitted with different content, the `UNIQUE` constraint on `Checksum` will reject it — preventing silent content drift in migration files.

**File-level cache.** Applied migrations are loaded once into a temporary file (`/tmp/applied_migrations.txt`) at startup, and `grep -qFx` checks against that cache rather than querying the database for every file. This keeps the action fast even with hundreds of migration files.

**POSIX `sh` — no Bash.** The script uses `#!/bin/sh` (not `#!/bin/bash`) for maximum portability across Alpine Linux (used in the Docker image) and any other base image.

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>Versioned, auditable, CI-native database migrations</h2>
  <p>The <code>schema_version</code> table gives you a permanent audit trail of every migration ever applied to a database — who (the CI system), when and what checksum. The four operations cover the full lifecycle: preview changes on PRs (<code>check</code>), confirm what will run (<code>dry-run</code>), apply (<code>migrate</code>) and verify (<code>integrity</code>). No ORM, no migration framework, no extra runtime required.</p>
  <p>The action works with any workflow trigger and any environment — local Docker services for testing, staging databases via secrets, or production behind a VPN. Drop a <code>migrations/</code> folder in your repository, wire up the secrets and let the pipeline manage the rest.</p>
  <p><strong>Repository:</strong> <a href="https://github.com/guibranco/github-database-migration-action" target="_blank">github.com/guibranco/github-database-migration-action</a></p>
</div>
