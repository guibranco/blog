---
layout: post
title: "Playing with Docker: NGINX, Apache, RabbitMQ, MailHog, MySQL/MariaDB"
description: "Set up a complete PHP development environment using Docker Compose — with NGINX, PHP-FPM, Apache, MySQL, MariaDB, Redis, MongoDB, RabbitMQ and MailHog, all wired together with healthchecks and ready to use."
date: 2026-06-17
categories: [Coding, Infraestrutura]
subcategories:
  - "Coding/PHP"
  - "Coding/Testing"
  - "Infraestrutura/DevOps"
tags: [docker, docker-compose, nginx, apache, php, php-fpm, mysql, mariadb, redis, mongodb, rabbitmq, mailhog, container, devops, devsecops, environment, dev-environment, developer-environment, infra, linux, windows, queue, smtp, sql, no-sql, nosql, database, web-server, webserver, server, healthcheck, message-broker, cache, local-environment]
reading_time: 15
image: /assets/img/posts/playing-with-docker.png
---

<p class="lead">Running <code>docker compose up</code> and having a fully working PHP development environment — with a web server, database, cache layer, message queue and email testing — in under two minutes. No global installs, no version conflicts, no "works on my machine". This guide walks through every service, explains what each one does and provides a production-grade <code>docker-compose.yml</code> with healthchecks included.</p>

<div class="callout callout-tip">
  <div class="callout-label">Target environment</div>
  This stack is designed for <strong>PHP development</strong>. It covers the most common needs: an HTTP server (NGINX or Apache), a relational database (MySQL or MariaDB), a cache and session store (Redis), a document store (MongoDB), a message queue (RabbitMQ) and a local SMTP trap (MailHog). Pick only what your project needs — every service is independent.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Why Docker for PHP development?</h2></div>
</div>

PHP applications typically depend on several external services: a web server, a database, a cache, maybe a queue. Installing and managing all of these locally — across Windows, macOS and Linux — leads to version drift and environment inconsistencies.

Docker solves this by packaging each service in an isolated container with a fixed version. The entire stack is defined in a single `docker-compose.yml` that every developer on the team runs identically.

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Zero global installs</div>
    <div class="provider-detail">No PHP, MySQL or NGINX installed on the host. Everything runs in containers and disappears with <code>docker compose down -v</code>.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Pinned versions</div>
    <div class="provider-detail">Every service runs on a specific version tag. Upgrading PHP 8.2 → 8.3 is a one-line change, reversible in seconds.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Isolated networks</div>
    <div class="provider-detail">Services communicate over an internal bridge network. Nothing is exposed to the internet unless explicitly mapped with a port.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Healthchecks</div>
    <div class="provider-detail">Docker waits for each service to be genuinely ready before starting dependents — no more race conditions on startup.</div>
  </div>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Stack overview</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Service</th><th>Image</th><th>Purpose</th><th>Port(s)</th></tr>
  </thead>
  <tbody>
    <tr><td>PHP-FPM</td><td><code>php:8.3-fpm</code></td><td>PHP processor (used by NGINX)</td><td>9000 (internal)</td></tr>
    <tr><td>NGINX</td><td><code>nginx:alpine</code></td><td>HTTP server + reverse proxy to PHP-FPM</td><td>8080</td></tr>
    <tr><td>Apache</td><td><code>php:8.3-apache</code></td><td>Alternative HTTP server with PHP built-in</td><td>8081</td></tr>
    <tr><td>MySQL</td><td><code>mysql:8.0</code></td><td>Relational database</td><td>3306</td></tr>
    <tr><td>MariaDB</td><td><code>mariadb:11.4</code></td><td>MySQL-compatible, community fork</td><td>3307</td></tr>
    <tr><td>Redis</td><td><code>redis:7-alpine</code></td><td>Cache, sessions, rate limiting</td><td>6379</td></tr>
    <tr><td>MongoDB</td><td><code>mongo:7</code></td><td>NoSQL document store</td><td>27017</td></tr>
    <tr><td>RabbitMQ</td><td><code>rabbitmq:3.13-management-alpine</code></td><td>Message queue + Management UI</td><td>5672 / 15672</td></tr>
    <tr><td>MailHog</td><td><code>mailhog/mailhog</code></td><td>Local SMTP trap + Web UI</td><td>1025 / 8025</td></tr>
  </tbody>
</table>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Project structure</h2></div>
</div>

```
project/
├── docker-compose.yml
├── .env
├── src/
│   └── index.php          ← your PHP application lives here
└── docker/
    ├── nginx/
    │   └── default.conf   ← NGINX virtual host
    ├── apache/
    │   └── vhost.conf     ← Apache virtual host
    └── php/
        └── php.ini        ← custom PHP settings
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>The <code>.env</code> file</h2></div>
</div>

Keep credentials out of `docker-compose.yml` by using a `.env` file. Docker Compose loads it automatically.

```ini
# .env — never commit to version control
COMPOSE_PROJECT_NAME=phpdev

# MySQL / MariaDB
DB_ROOT_PASSWORD=rootpass
DB_NAME=dev_db
DB_USER=dev_user
DB_PASSWORD=dev_pass

# MongoDB
MONGO_ROOT_USER=root
MONGO_ROOT_PASSWORD=rootpass

# RabbitMQ
RABBITMQ_USER=dev_user
RABBITMQ_PASS=dev_pass
RABBITMQ_VHOST=dev_vhost
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>docker-compose.yml — full stack with healthchecks</h2></div>
</div>

```yaml
# docker-compose.yml
# PHP development stack: NGINX + PHP-FPM, Apache, MySQL, MariaDB,
# Redis, MongoDB, RabbitMQ, MailHog
# Run: docker compose up -d

services:

  # ── PHP-FPM ────────────────────────────────────────────────────
  php:
    image: php:8.3-fpm
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_php
    restart: unless-stopped
    volumes:
      - ./src:/var/www/html
      - ./docker/php/php.ini:/usr/local/etc/php/conf.d/custom.ini
    networks:
      - dev_network
    depends_on:
      mysql:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD-SHELL", "php-fpm -t 2>&1 | grep -q 'successful'"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # ── NGINX ──────────────────────────────────────────────────────
  nginx:
    image: nginx:alpine
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_nginx
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./src:/var/www/html
      - ./docker/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
    networks:
      - dev_network
    depends_on:
      php:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "nginx", "-t"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 5s

  # ── Apache (alternative to NGINX — disable one or the other) ──
  apache:
    image: php:8.3-apache
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_apache
    restart: unless-stopped
    ports:
      - "8081:80"
    volumes:
      - ./src:/var/www/html
      - ./docker/apache/vhost.conf:/etc/apache2/sites-enabled/000-default.conf:ro
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "apache2ctl", "-t"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # ── MySQL ──────────────────────────────────────────────────────
  mysql:
    image: mysql:8.0
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_mysql
    restart: unless-stopped
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "127.0.0.1",
             "-u", "root", "-p${DB_ROOT_PASSWORD}"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

  # ── MariaDB (MySQL-compatible alternative) ─────────────────────
  mariadb:
    image: mariadb:11.4
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_mariadb
    restart: unless-stopped
    ports:
      - "3307:3306"
    environment:
      MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MARIADB_DATABASE: ${DB_NAME}
      MARIADB_USER: ${DB_USER}
      MARIADB_PASSWORD: ${DB_PASSWORD}
    volumes:
      - mariadb_data:/var/lib/mysql
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

  # ── Redis ──────────────────────────────────────────────────────
  redis:
    image: redis:7-alpine
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_redis
    restart: unless-stopped
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 15s
      timeout: 5s
      retries: 3
      start_period: 5s

  # ── MongoDB ────────────────────────────────────────────────────
  mongodb:
    image: mongo:7
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_mongodb
    restart: unless-stopped
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_ROOT_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_ROOT_PASSWORD}
      MONGO_INITDB_DATABASE: ${DB_NAME}
    volumes:
      - mongodb_data:/data/db
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "mongosh", "--quiet", "--eval",
             "db.adminCommand('ping').ok"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 15s

  # ── RabbitMQ ───────────────────────────────────────────────────
  rabbitmq:
    image: rabbitmq:3.13-management-alpine
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_rabbitmq
    restart: unless-stopped
    ports:
      - "5672:5672"    # AMQP protocol
      - "15672:15672"  # Management UI
    environment:
      RABBITMQ_DEFAULT_USER: ${RABBITMQ_USER}
      RABBITMQ_DEFAULT_PASS: ${RABBITMQ_PASS}
      RABBITMQ_DEFAULT_VHOST: ${RABBITMQ_VHOST}
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "ping"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s

  # ── MailHog ────────────────────────────────────────────────────
  mailhog:
    image: mailhog/mailhog:latest
    container_name: ${COMPOSE_PROJECT_NAME:-phpdev}_mailhog
    restart: unless-stopped
    ports:
      - "1025:1025"   # SMTP
      - "8025:8025"   # Web UI
    networks:
      - dev_network
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1",
             "--spider", "http://localhost:8025"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 5s

# ── Shared network ─────────────────────────────────────────────
networks:
  dev_network:
    driver: bridge

# ── Persistent volumes ─────────────────────────────────────────
volumes:
  mysql_data:
  mariadb_data:
  redis_data:
  mongodb_data:
  rabbitmq_data:
```

<div class="callout callout-warn">
  <div class="callout-label">MySQL and MariaDB are alternatives</div>
  Running both simultaneously is only useful if you need to compare behaviour. In a real project, pick one and comment out (or remove) the other. The PHP connection string is identical for both — just change the host name and port.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>Configuration files</h2></div>
</div>

### NGINX virtual host — `docker/nginx/default.conf`

NGINX does not run PHP natively. It delegates `.php` requests to PHP-FPM over FastCGI.

```nginx
server {
    listen 80;
    server_name localhost;

    root  /var/www/html;
    index index.php index.html;

    # Pretty URLs (Laravel, Symfony, etc.)
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    # PHP-FPM proxy
    location ~ \.php$ {
        fastcgi_pass   php:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include        fastcgi_params;
        fastcgi_read_timeout 120;
    }

    # Deny .htaccess access
    location ~ /\.ht {
        deny all;
    }
}
```

### Apache virtual host — `docker/apache/vhost.conf`

Apache with the `php:8.3-apache` image runs PHP directly via `mod_php` — no separate FPM service needed.

```apache
<VirtualHost *:80>
    ServerName localhost
    DocumentRoot /var/www/html

    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog  ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

### PHP settings — `docker/php/php.ini`

```ini
; docker/php/php.ini
display_errors       = On
display_startup_errors = On
error_reporting      = E_ALL
max_execution_time   = 120
memory_limit         = 256M
upload_max_filesize  = 64M
post_max_size        = 64M

; MailHog SMTP
[mail function]
sendmail_path = /usr/sbin/sendmail -S mailhog:1025
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">07</div>
  <div class="section-title-wrap"><h2>Service breakdown</h2></div>
</div>

### NGINX + PHP-FPM

NGINX is the recommended web server for PHP in modern stacks. It handles static files itself (CSS, JS, images) and forwards PHP requests to the `php` container over FastCGI on port `9000`. The two containers share the `./src` volume so they both see the same files.

Access: **[http://localhost:8080](http://localhost:8080)**

### Apache

`php:8.3-apache` bundles Apache and PHP in a single image with `mod_php` enabled. Simpler to configure than NGINX+FPM, and `.htaccess` files work out of the box — useful if you're maintaining a legacy codebase that relies on them.

Access: **[http://localhost:8081](http://localhost:8081)**

### MySQL 8.0

The most widely deployed open-source relational database. MySQL 8.0 brings significant performance improvements, native JSON support and `utf8mb4` as the default charset. The `mysql_data` volume persists data between container restarts.

Connection string: `mysql://dev_user:dev_pass@mysql:3306/dev_db`

### MariaDB 11.4

A fully MySQL-compatible community fork with additional storage engines, better performance on write-heavy workloads and a more open governance model. Runs on port `3307` to avoid conflicting with the MySQL container when both are active. The PHP PDO connection string is identical — just swap `mysql` for `mariadb` and `3306` for `3307`.

Connection string: `mysql://dev_user:dev_pass@mariadb:3306/dev_db`

### Redis

An in-memory key-value store most commonly used in PHP applications for:

- **Session storage** — faster than file or database sessions
- **Application cache** — full-page cache, query cache, object cache
- **Rate limiting** — sliding window counters
- **Pub/Sub** — lightweight messaging between processes

The `--appendonly yes` flag enables persistence so data survives container restarts. The `--maxmemory-policy allkeys-lru` evicts the least-recently-used keys when memory is full — ideal for a cache.

Connection: `redis://redis:6379`

### MongoDB

A document-oriented NoSQL database. In a PHP stack it complements MySQL/MariaDB when your data is:

- **Hierarchical or nested** — product catalogs, CMS content
- **Schema-less** — event logs, user activity streams
- **Rapidly evolving** — prototypes where the shape of data changes frequently

Connection string: `mongodb://root:rootpass@mongodb:27017/dev_db?authSource=admin`

### RabbitMQ

A message broker that decouples PHP processes from slow or asynchronous operations. Common use cases:

- **Email dispatch** — publish a job, consume it in a worker
- **Image processing** — upload triggers a resize queue
- **Third-party API calls** — don't block the HTTP response
- **Webhooks** — retry logic for outbound events

The `management` plugin (included in the `management-alpine` image tag) provides a browser-based UI for monitoring queues, bindings and message rates.

Access: **[http://localhost:15672](http://localhost:15672)** → `dev_user / dev_pass`
AMQP: `amqp://dev_user:dev_pass@rabbitmq:5672/dev_vhost`

### MailHog

A local SMTP server that **catches all outgoing email** and displays it in a web inbox — without actually delivering anything to a real recipient. Essential for development: you can test registration emails, password resets and notifications safely.

Configure PHP's `sendmail_path` in `php.ini` to point to MailHog on port `1025` (done in the config above). All mail sent via PHP's `mail()` function, PHPMailer or Symfony Mailer will appear in the UI instantly.

SMTP: `mailhog:1025`
Access: **[http://localhost:8025](http://localhost:8025)**

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">08</div>
  <div class="section-title-wrap"><h2>Web interfaces at a glance</h2></div>
</div>

<table class="compare-table">
  <thead>
    <tr><th>Service</th><th>URL</th><th>Credentials</th></tr>
  </thead>
  <tbody>
    <tr><td>PHP app (NGINX)</td><td><a href="http://localhost:8080" target="_blank">localhost:8080</a></td><td>—</td></tr>
    <tr><td>PHP app (Apache)</td><td><a href="http://localhost:8081" target="_blank">localhost:8081</a></td><td>—</td></tr>
    <tr><td>RabbitMQ UI</td><td><a href="http://localhost:15672" target="_blank">localhost:15672</a></td><td>dev_user / dev_pass</td></tr>
    <tr><td>MailHog inbox</td><td><a href="http://localhost:8025" target="_blank">localhost:8025</a></td><td>—</td></tr>
  </tbody>
</table>

<div class="callout callout-tip">
  <div class="callout-label">Database GUIs</div>
  No web UI is included for MySQL/MariaDB or MongoDB by design — they add container weight. Use a desktop client instead: <strong>TablePlus</strong>, <strong>DBeaver</strong> or <strong>MySQL Workbench</strong> for relational databases, and <strong>MongoDB Compass</strong> or <strong>Studio 3T</strong> for MongoDB. All connect to <code>localhost</code> on the mapped port.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">09</div>
  <div class="section-title-wrap"><h2>Using the services in PHP</h2></div>
</div>

### MySQL / MariaDB with PDO

```php
<?php
$pdo = new PDO(
    dsn: 'mysql:host=mysql;port=3306;dbname=dev_db;charset=utf8mb4',
    username: 'dev_user',
    password: 'dev_pass',
    options: [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ]
);
// For MariaDB: host=mariadb;port=3306 (same DSN format)
```

### Redis with Predis

```bash
composer require predis/predis
```

```php
<?php
use Predis\Client;

$redis = new Client([
    'scheme' => 'tcp',
    'host'   => 'redis',
    'port'   => 6379,
]);

// Cache
$redis->setex('my_key', 3600, json_encode($data));
$cached = $redis->get('my_key');

// Session (set in php.ini instead)
// session.save_handler = redis
// session.save_path    = "tcp://redis:6379"
```

### MongoDB with the official driver

```bash
composer require mongodb/mongodb
```

```php
<?php
use MongoDB\Client;

$mongo  = new Client('mongodb://root:rootpass@mongodb:27017/?authSource=admin');
$db     = $mongo->dev_db;
$coll   = $db->events;

$coll->insertOne(['type' => 'page_view', 'url' => '/home', 'at' => new \DateTime()]);
$recent = $coll->find(['type' => 'page_view'], ['limit' => 10]);
```

### RabbitMQ with php-amqplib

```bash
composer require php-amqplib/php-amqplib
```

```php
<?php
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

// Publisher
$connection = new AMQPStreamConnection('rabbitmq', 5672, 'dev_user', 'dev_pass', 'dev_vhost');
$channel    = $connection->channel();
$channel->queue_declare('emails', false, true, false, false);

$msg = new AMQPMessage(
    json_encode(['to' => 'user@example.com', 'subject' => 'Welcome']),
    ['delivery_mode' => AMQPMessage::DELIVERY_MODE_PERSISTENT]
);
$channel->basic_publish($msg, '', 'emails');

$channel->close();
$connection->close();
```

```php
<?php
// Consumer (run as a separate worker process)
$channel->basic_consume('emails', '', false, false, false, false,
    function (AMQPMessage $msg) {
        $data = json_decode($msg->body, true);
        // send the email...
        $msg->ack();
    }
);
while ($channel->is_consuming()) {
    $channel->wait();
}
```

### Sending mail through MailHog

If `sendmail_path` is configured in `php.ini` (as shown above), `mail()` works automatically. For PHPMailer:

```bash
composer require phpmailer/phpmailer
```

```php
<?php
use PHPMailer\PHPMailer\PHPMailer;

$mail = new PHPMailer();
$mail->isSMTP();
$mail->Host       = 'mailhog';
$mail->Port       = 1025;
$mail->SMTPAuth   = false;

$mail->setFrom('app@dev.local', 'My App');
$mail->addAddress('user@example.com');
$mail->Subject = 'Test email';
$mail->Body    = '<h1>Hello from Docker!</h1>';
$mail->isHTML(true);

$mail->send(); // visible at http://localhost:8025
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">10</div>
  <div class="section-title-wrap"><h2>Useful commands</h2></div>
</div>

```bash
# Start the stack
docker compose up -d

# Follow logs for all services
docker compose logs -f

# Follow logs for a single service
docker compose logs -f rabbitmq

# Check healthcheck status
docker compose ps

# Open a shell inside the PHP container
docker compose exec php bash

# Run a one-off PHP command
docker compose exec php php artisan migrate

# Stop and remove containers (keeps volumes)
docker compose down

# Stop and remove everything including volumes (wipes database data)
docker compose down -v

# Rebuild images after changing Dockerfile
docker compose up -d --build
```

<div class="divider">· · ·</div>

<div class="conclusion">
  <h2>A complete PHP dev environment in one file</h2>
  <p>The stack above covers the full surface area of a modern PHP application: HTTP serving, SQL persistence, caching, document storage, asynchronous messaging and email testing. Every service is containerised, versioned, healthchecked and isolated — with no side effects on the host machine.</p>
  <p>Start with what your project actually needs. A typical Laravel app needs NGINX + PHP-FPM + MySQL + Redis. Add RabbitMQ when you introduce queued jobs, MongoDB if you need a document store, and MailHog from day one so email never silently fails in development. Scale up or down by commenting services in and out of <code>docker-compose.yml</code>.</p>
  <p>The <code>.env</code> file keeps credentials out of version control, the healthchecks ensure correct startup order, and persistent volumes mean your data survives container restarts. <code>docker compose up -d</code> — and you're ready to build.</p>
</div>
