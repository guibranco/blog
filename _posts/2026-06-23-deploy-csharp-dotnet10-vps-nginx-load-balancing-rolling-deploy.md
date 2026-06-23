---
layout: post
lang: pt
render_with_liquid: false
title: "Deploy de aplicação C# .NET 10 em VPS Ubuntu com Nginx, SSL e rolling deploy"
description: "Guia completo para publicar uma aplicação .NET 10 em uma VPS OCI Ubuntu usando GitHub Actions, rsync, duas instâncias com load balancing no Nginx e deploy sem downtime."
date: 2026-06-23
categories: [Infraestrutura]
subcategories:
  - "Infraestrutura/DevOps"
tags: [csharp, dotnet, dotnet10, deploy, vps, ubuntu, nginx, github-actions, ci-cd, certbot, ssl, systemd, oci, healthchecks, load-balancing, kestrel, rsync, rolling-deploy, linux, infraestrutura, zero-downtime]
reading_time: 18
image: /assets/img/posts/csharp-deploy-dotnet10.png
---

<p class="lead">Guia completo para fazer o deploy de uma aplicação C# .NET 10 em uma VPS Ubuntu na OCI — com duas instâncias rodando em paralelo, load balancing no Nginx, rolling deploy sem downtime via GitHub Actions e rsync, e SSL automático pelo Certbot.</p>

> **Baseado em:** deploy de produção com .NET 10 em VPS OCI Ubuntu 24.04.
> **Testado em:** Ubuntu 24.04 LTS, .NET 10, Nginx, Certbot, GitHub Actions.

<div class="divider">· · ·</div>

## Por que duas instâncias?

Rodar duas instâncias da mesma aplicação em portas diferentes traz duas vantagens concretas:

**Load balancing real:** o Nginx distribui as requisições em round-robin entre `:5001` e `:5002`. Se uma instância estiver sob carga, a outra absorve parte do tráfego.

**Rolling deploy sem downtime:** ao atualizar, paramos uma instância por vez. Enquanto a instância 1 está sendo atualizada e reiniciando, a instância 2 continua atendendo 100% do tráfego — e vice-versa. O usuário final não percebe interrupção.

Essa arquitetura é o padrão adotado aqui, não uma opção. Toda a pipeline e a configuração do Nginx são construídas ao redor disso.

<div class="divider">· · ·</div>

## 1. Pré-requisitos

### Na VPS

- Ubuntu 24.04 LTS
- Nginx instalado e rodando
- UFW configurado
- Certbot instalado
- Usuário `deploy` com chave SSH configurada
- Diretório `/opt/webhooksHandler` criado

### No GitHub

Configure os seguintes secrets em **Settings → Secrets and variables → Actions**:

| Secret | Descrição |
|---|---|
| `SSH_HOST` | IP ou hostname da VPS |
| `SSH_PRIVATE_KEY` | Chave privada SSH do usuário `deploy` |
| `APP_DOMAIN` | Domínio da aplicação (ex: `api.straccini.com`) |

Adicione secrets extras para variáveis específicas da aplicação (strings de conexão, API keys, etc.).

<div class="divider">· · ·</div>

## 2. Instalação do .NET 10 Runtime na VPS

O build acontece no GitHub Actions — a VPS só precisa do runtime para executar a aplicação publicada.

```bash
# Adicionar repositório oficial da Microsoft
wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb \
  -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

apt update

# Runtime do ASP.NET Core 10 (inclui o .NET Runtime base)
apt install -y aspnetcore-runtime-10.0
```

Verifique:

```bash
dotnet --version
dotnet --list-runtimes
```

<div class="divider">· · ·</div>

## 3. Usuário da aplicação e estrutura de diretórios

O deploy usa dois usuários distintos com responsabilidades separadas:

- **`deploy`** — usado pelo GitHub Actions para fazer SSH e transferir arquivos
- **`webhooksHandler`** — usuário de sistema sem shell, que executa a aplicação

```bash
APP=webhooksHandler

# Usuário da aplicação — sem shell, sem home
useradd --system --no-create-home --shell /usr/sbin/nologin $APP

# Diretório principal da aplicação
mkdir -p /opt/$APP
chown $APP:$APP /opt/$APP
chmod 750 /opt/$APP

# Diretório de staging (usado durante o deploy para swap atômico)
mkdir -p /opt/${APP}-staging
chown deploy:deploy /opt/${APP}-staging
chmod 750 /opt/${APP}-staging
```

<div class="divider">· · ·</div>

## 4. Chave SSH e sudoers

### Chave SSH para o GitHub Actions

Na sua máquina local:

```bash
ssh-keygen -t ed25519 -C "github-actions-deploy" -f ~/.ssh/deploy_webhookshandler -N ""
```

Copie a chave pública para o servidor. Em ambientes OCI o `ssh-copy-id` pode falhar antes do usuário `deploy` estar configurado — use o método manual:

```bash
# No servidor, logado como ubuntu:
sudo mkdir -p /home/deploy/.ssh
echo "COLE_A_CHAVE_PUBLICA_AQUI" | sudo tee -a /home/deploy/.ssh/authorized_keys
sudo chmod 700 /home/deploy/.ssh
sudo chmod 600 /home/deploy/.ssh/authorized_keys
sudo chown -R deploy:deploy /home/deploy/.ssh
```

Adicione o conteúdo da **chave privada** como secret `SSH_PRIVATE_KEY` no GitHub.

### Sudoers — permissões cirúrgicas para o deploy

O usuário `deploy` precisa de `sudo` apenas para parar/iniciar os serviços e ajustar permissões. Nada além disso:

```bash
APP=webhooksHandler

cat > /etc/sudoers.d/${APP}-deploy << EOF
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl start ${APP}-1
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl start ${APP}-2
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl stop ${APP}-1
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl stop ${APP}-2
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status ${APP}-1
deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl status ${APP}-2
deploy ALL=(ALL) NOPASSWD: /usr/bin/rsync
deploy ALL=(ALL) NOPASSWD: /usr/bin/chown -R ${APP}\:${APP} /opt/${APP}
deploy ALL=(ALL) NOPASSWD: /usr/bin/chmod -R 750 /opt/${APP}
deploy ALL=(ALL) NOPASSWD: /usr/bin/mkdir -p /opt/${APP}-staging
deploy ALL=(ALL) NOPASSWD: /usr/bin/rm -rf /opt/${APP}-staging
EOF

chmod 440 /etc/sudoers.d/${APP}-deploy
visudo -c -f /etc/sudoers.d/${APP}-deploy
```

<div class="divider">· · ·</div>

## 5. Arquivo de ambiente

Crie o arquivo de variáveis de ambiente que o systemd vai carregar em cada instância. As instâncias diferem apenas na porta:

```bash
APP=webhooksHandler

# Instância 1 — porta 5001
cat > /opt/$APP/environment-1 << EOF
ASPNETCORE_ENVIRONMENT=Production
ASPNETCORE_URLS=http://127.0.0.1:5001
DOTNET_PRINT_TELEMETRY_MESSAGE=false

# Exemplo de variáveis da aplicação
ConnectionStrings__DefaultConnection=Server=127.0.0.1;Database=mydb;User=myapp;Password=change-me;
AppSettings__ApiKey=change-me
EOF

# Instância 2 — porta 5002
cp /opt/$APP/environment-1 /opt/$APP/environment-2
sed -i 's/5001/5002/' /opt/$APP/environment-2

# Permissões restritas — só o usuário da app lê
chown $APP:$APP /opt/$APP/environment-1 /opt/$APP/environment-2
chmod 640 /opt/$APP/environment-1 /opt/$APP/environment-2
```

<div class="callout callout-info">
<p class="callout-label">💡 Variáveis de ambiente vs appsettings</p>
O .NET mapeia variáveis de ambiente com <code>__</code> (duplo underscore) para a hierarquia do <code>appsettings.json</code>. <code>ConnectionStrings__DefaultConnection</code> equivale a <code>ConnectionStrings:DefaultConnection</code>.
</div>

<div class="divider">· · ·</div>

## 6. Serviços systemd — duas instâncias

Crie um arquivo de serviço para cada instância. A diferença entre eles é a porta via `EnvironmentFile` e o `SyslogIdentifier`.

### Instância 1

```bash
APP=webhooksHandler

cat > /etc/systemd/system/${APP}-1.service << EOF
[Unit]
Description=${APP} .NET 10 API (instância 1)
After=network.target
Wants=network-online.target

[Service]
Type=notify
User=${APP}
Group=${APP}
WorkingDirectory=/opt/${APP}

ExecStart=/usr/bin/dotnet /opt/${APP}/${APP}.dll

EnvironmentFile=/opt/${APP}/environment-1

StandardOutput=journal
StandardError=journal
SyslogIdentifier=${APP}-1

Restart=on-failure
RestartSec=5s
KillSignal=SIGINT
TimeoutStopSec=30

NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF
```

### Instância 2

```bash
cat > /etc/systemd/system/${APP}-2.service << EOF
[Unit]
Description=${APP} .NET 10 API (instância 2)
After=network.target
Wants=network-online.target

[Service]
Type=notify
User=${APP}
Group=${APP}
WorkingDirectory=/opt/${APP}

ExecStart=/usr/bin/dotnet /opt/${APP}/${APP}.dll

EnvironmentFile=/opt/${APP}/environment-2

StandardOutput=journal
StandardError=journal
SyslogIdentifier=${APP}-2

Restart=on-failure
RestartSec=5s
KillSignal=SIGINT
TimeoutStopSec=30

NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF
```

Ative e inicie os dois serviços:

```bash
systemctl daemon-reload
systemctl enable ${APP}-1 ${APP}-2
systemctl start ${APP}-1 ${APP}-2
systemctl status ${APP}-1 ${APP}-2
```

<div class="callout callout-info">
<p class="callout-label">💡 Type=notify vs Type=simple</p>
<code>Type=notify</code> instrui o systemd a aguardar o sinal de "pronto" do Kestrel antes de considerar o serviço iniciado. Isso evita que o health check dispare antes da aplicação estar de fato aceitando conexões. Requer o pacote <code>libsystemd-dev</code> no host.
</div>

<div class="divider">· · ·</div>

## 7. Nginx — load balancing com upstream

Com duas instâncias em `:5001` e `:5002`, o Nginx atua como proxy reverso e distribui as requisições em round-robin.

```bash
APP=webhooksHandler

cat > /etc/nginx/sites-available/$APP << 'NGINXEOF'
upstream webhookshandler_backend {
    # Round-robin automático entre as duas instâncias
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;

    # Reutiliza conexões HTTP/1.1 com o upstream
    keepalive 32;
}

# HTTP → HTTPS redirect
server {
    listen 80;
    listen [::]:80;
    server_name seu-dominio.com;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# HTTPS — proxy reverso com load balancing
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name seu-dominio.com;

    # Certbot preenche automaticamente
    ssl_certificate     /etc/letsencrypt/live/seu-dominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/seu-dominio.com/privkey.pem;
    include             /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam         /etc/letsencrypt/ssl-dhparams.pem;

    # Headers de segurança
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
    add_header X-Content-Type-Options    "nosniff"                             always;
    add_header X-Frame-Options           "SAMEORIGIN"                          always;
    add_header Referrer-Policy           "strict-origin-when-cross-origin"     always;

    # API — todas as rotas
    location / {
        proxy_pass         http://webhookshandler_backend;
        proxy_http_version 1.1;
        proxy_set_header   Connection        "";
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
        proxy_connect_timeout 10s;
        proxy_send_timeout 60s;
    }

    # Health check — sem poluir os logs
    location /health {
        proxy_pass         http://webhookshandler_backend;
        proxy_http_version 1.1;
        proxy_set_header   Connection        "";
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        access_log off;
    }
}
NGINXEOF

ln -s /etc/nginx/sites-available/$APP /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
```

<div class="divider">· · ·</div>

## 8. SSL com Certbot

O DNS precisa estar apontando para o IP da VPS antes deste passo.

```bash
certbot --nginx -d seu-dominio.com
```

Teste a renovação automática:

```bash
certbot renew --dry-run
```

O Certbot instala um timer systemd que renova os certificados automaticamente antes do vencimento.

<div class="divider">· · ·</div>

## 9. Configuração do Kestrel — ForwardedHeaders

Como o Kestrel roda atrás do Nginx, ele precisa confiar nos headers encaminhados para identificar corretamente o IP real do cliente e o protocolo:

```csharp
// Program.cs — adicione antes de app.UseRouting()
app.UseForwardedHeaders(new ForwardedHeadersOptions
{
    ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
});
```

Sem isso, `HttpContext.Connection.RemoteIpAddress` sempre retorna `127.0.0.1` (o Nginx) e redirects HTTPS podem entrar em loop.

### HealthChecks

```csharp
builder.Services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy())
    .AddCheck("ready", () => HealthCheckResult.Healthy(), tags: ["ready"]);

// ...

app.MapHealthChecks("/health");
app.MapHealthChecks("/health/live", new HealthCheckOptions
{
    Predicate = _ => false   // liveness — retorna 200 se o processo está vivo
});
app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
    Predicate = hc => hc.Tags.Contains("ready")
});
```

<div class="divider">· · ·</div>

## 10. GitHub Actions — CI e rolling deploy

O workflow é dividido em dois arquivos: `ci.yml` para validação em pull requests, e `deploy.yml` para o deploy em produção ao fazer push na `main`.

### `ci.yml` — build e testes em pull requests

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
  workflow_dispatch:

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup .NET 10
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'

      - name: Restore
        run: dotnet restore

      - name: Build
        run: dotnet build --no-restore --configuration Release

      - name: Test
        run: |
          dotnet test --no-build --configuration Release --verbosity normal \
            /p:CollectCoverage=true /p:CoverletOutputFormat=opencover
```

### `deploy.yml` — rolling deploy sem downtime

O deploy segue esta sequência:

1. Build e publish no runner do GitHub Actions
2. rsync dos artefatos para `/opt/webhooksHandler-staging/` (instâncias ainda servindo tráfego)
3. Rolling deploy da instância 1: stop → swap de arquivos → start → health check em `:5001`
4. Se a instância 1 passou, rolling deploy da instância 2: stop → start → health check em `:5002`
5. Health check final via Nginx (HTTPS público)
6. Limpeza do diretório de staging

```yaml
# .github/workflows/deploy.yml
name: Build & Deploy

on:
  push:
    branches:
      - main
  workflow_dispatch:

env:
  DOTNET_VERSION: '10.0.x'
  PROJECT_PATH: 'src/WebhooksHandler/WebhooksHandler.csproj'
  PUBLISH_DIR: './publish'
  REMOTE_DIR: '/opt/webhooksHandler'
  SSH_USER: deploy
  SSH_HOST: ${{ secrets.SSH_HOST }}
  SERVICE_1: webhooksHandler-1
  SERVICE_2: webhooksHandler-2

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      # ── 1. Checkout ──────────────────────────────────────────────────────────
      - name: Checkout repository
        uses: actions/checkout@v4

      # ── 2. Setup .NET 10 ─────────────────────────────────────────────────────
      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: ${{ env.DOTNET_VERSION }}

      # ── 3. Restore & Publish ─────────────────────────────────────────────────
      - name: Restore dependencies
        run: dotnet restore ${{ env.PROJECT_PATH }}

      - name: Publish
        run: |
          dotnet publish ${{ env.PROJECT_PATH }} \
            --configuration Release \
            --output ${{ env.PUBLISH_DIR }} \
            --no-restore \
            --self-contained false

      # ── 4. Setup SSH ─────────────────────────────────────────────────────────
      - name: Setup SSH key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan -H ${{ env.SSH_HOST }} >> ~/.ssh/known_hosts

      # ── 5. rsync para o diretório de staging ─────────────────────────────────
      # As duas instâncias continuam servindo tráfego normalmente durante esta etapa
      - name: Upload release to staging
        run: |
          ssh ${{ env.SSH_USER }}@${{ env.SSH_HOST }} \
            "sudo mkdir -p /opt/webhooksHandler-staging && \
             sudo chown deploy:deploy /opt/webhooksHandler-staging"

          rsync -avz --delete \
            -e "ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no" \
            ${{ env.PUBLISH_DIR }}/ \
            ${{ env.SSH_USER }}@${{ env.SSH_HOST }}:/opt/webhooksHandler-staging/

      # ── 6. Rolling deploy — instância 1 ──────────────────────────────────────
      - name: Rolling deploy — instance 1
        run: |
          ssh ${{ env.SSH_USER }}@${{ env.SSH_HOST }} << 'ENDSSH'
            set -e

            echo "==> Parando instância 1..."
            sudo systemctl stop webhooksHandler-1

            echo "==> Sincronizando arquivos do staging..."
            sudo rsync -a --delete /opt/webhooksHandler-staging/ /opt/webhooksHandler/
            sudo chown -R webhooksHandler:webhooksHandler /opt/webhooksHandler
            sudo chmod -R 750 /opt/webhooksHandler

            echo "==> Iniciando instância 1..."
            sudo systemctl start webhooksHandler-1

            echo "==> Aguardando instância 1 em :5001..."
            for i in $(seq 1 12); do
              if curl -sf http://127.0.0.1:5001/health > /dev/null 2>&1; then
                echo "✅ Instância 1 saudável (tentativa $i)"
                exit 0
              fi
              echo "Tentativa $i — aguardando..."
              sleep 5
            done

            echo "❌ Instância 1 não respondeu — abortando"
            exit 1
          ENDSSH

      # ── 7. Rolling deploy — instância 2 ──────────────────────────────────────
      # Só executa se a instância 1 passou no health check
      - name: Rolling deploy — instance 2
        run: |
          ssh ${{ env.SSH_USER }}@${{ env.SSH_HOST }} << 'ENDSSH'
            set -e

            echo "==> Parando instância 2..."
            sudo systemctl stop webhooksHandler-2

            echo "==> Iniciando instância 2 (arquivos já no lugar)..."
            sudo systemctl start webhooksHandler-2

            echo "==> Aguardando instância 2 em :5002..."
            for i in $(seq 1 12); do
              if curl -sf http://127.0.0.1:5002/health > /dev/null 2>&1; then
                echo "✅ Instância 2 saudável (tentativa $i)"
                exit 0
              fi
              echo "Tentativa $i — aguardando..."
              sleep 5
            done

            echo "❌ Instância 2 não respondeu — abortando"
            exit 1
          ENDSSH

      # ── 8. Cleanup do staging ─────────────────────────────────────────────────
      - name: Cleanup staging
        if: always()
        run: |
          ssh ${{ env.SSH_USER }}@${{ env.SSH_HOST }} \
            "sudo rm -rf /opt/webhooksHandler-staging" || true

      # ── 9. Health check final via Nginx ───────────────────────────────────────
      - name: Final health check
        run: |
          HEALTH_URL="https://${{ secrets.APP_DOMAIN }}/health"
          echo "Verificando $HEALTH_URL ..."
          for i in {1..10}; do
            STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$HEALTH_URL" || echo "000")
            echo "Tentativa $i — HTTP $STATUS"
            if [ "$STATUS" = "200" ]; then
              echo "✅ Deploy concluído — ambas as instâncias saudáveis"
              exit 0
            fi
            sleep 5
          done
          echo "❌ Health check final falhou"
          exit 1
```

<div class="divider">· · ·</div>

## 11. Por que rsync em vez de scp ou tar?

O artigo anterior usava `scp` com um arquivo `.tar.gz`. A abordagem com `rsync` tem vantagens práticas em um cenário com staging:

| | scp + tar | rsync |
|---|---|---|
| Transferência | Sempre o pacote inteiro | Só os arquivos modificados |
| Swap atômico | Precisa extrair e mover | `rsync --delete` direto no staging |
| Visibilidade | Nenhuma durante a transferência | Progresso arquivo a arquivo |
| Retomada | Não | Sim (`--partial`) |
| Rollback manual | Requer manter o `.tar.gz` anterior | Staging permanece intacto até o cleanup |

Com dois serviços lendo do mesmo `/opt/webhooksHandler/`, o fluxo via staging garante que a cópia dos arquivos acontece de forma completa antes de qualquer instância ser reiniciada.

<div class="divider">· · ·</div>

## 12. Firewall — UFW e OCI Security List

```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
ufw status verbose
```

As portas `5001` e `5002` do Kestrel **não** são abertas externamente — todo o tráfego passa pelo Nginx na porta 443. Mantenha-as fechadas.

Em instâncias OCI com Security List (padrão OCI), espelhe as regras na console:

| Tipo | Protocolo | Porta | Descrição |
|---|---|---|---|
| Ingress | TCP | 22 | SSH |
| Ingress | TCP | 80 | HTTP (redirect) |
| Ingress | TCP | 443 | HTTPS |

<div class="divider">· · ·</div>

## 13. Checklist pós-deploy

- [ ] DNS A record aponta para o IP correto da VPS
- [ ] `systemctl status webhooksHandler-1` mostra `active (running)`
- [ ] `systemctl status webhooksHandler-2` mostra `active (running)`
- [ ] `curl -s https://seu-dominio.com/health` retorna HTTP 200
- [ ] `curl -s http://127.0.0.1:5001/health` retorna 200 direto no Kestrel
- [ ] `curl -s http://127.0.0.1:5002/health` retorna 200 direto no Kestrel
- [ ] `certbot renew --dry-run` bem-sucedido
- [ ] `nginx -t` sem warnings
- [ ] UFW permite apenas portas 22, 80, 443
- [ ] `/opt/webhooksHandler/environment-1` e `environment-2` com `chmod 640`
- [ ] `ForwardedHeaders` configurado no `Program.cs`
- [ ] Rolling restart testado manualmente: parar instância 1, verificar que instância 2 atende
- [ ] GitHub Actions com badge verde na `main`

<div class="divider">· · ·</div>

## 14. Comandos úteis do dia a dia

```bash
# Logs em tempo real
journalctl -u webhooksHandler-1 -f
journalctl -u webhooksHandler-2 -f

# Status dos serviços
sudo systemctl status webhooksHandler-1 webhooksHandler-2

# Restart manual de uma instância
sudo systemctl restart webhooksHandler-1
sudo systemctl restart webhooksHandler-2

# Reload do Nginx (zero downtime — só recarrega config)
sudo systemctl reload nginx

# Verificar qual processo está escutando em uma porta
ss -tlnp | grep 5001
ss -tlnp | grep 5002

# Testar health check direto em cada instância
curl -s http://127.0.0.1:5001/health
curl -s http://127.0.0.1:5002/health

# Testar config do Nginx antes de recarregar
nginx -t

# Log de erros do Nginx
tail -f /var/log/nginx/error.log

# Verificar vencimento do certificado SSL
echo | openssl s_client -connect seu-dominio.com:443 2>/dev/null \
  | openssl x509 -noout -dates

# Forçar renovação do certificado
certbot renew --force-renewal --nginx -d seu-dominio.com

# Publish manual da aplicação (no runner ou localmente)
dotnet publish src/WebhooksHandler/WebhooksHandler.csproj \
  --configuration Release \
  --self-contained false \
  --output ./publish
```

<div class="divider">· · ·</div>

## Referência de variáveis

Substitua os placeholders pelos valores reais do seu projeto:

| Placeholder | Exemplo | Significado |
|---|---|---|
| `webhooksHandler` | `pancake-api` | Nome do app — usado para usuário, diretório e serviços |
| `seu-dominio.com` | `api.straccini.com` | Domínio apontando para a VPS |
| `your-server-ip` | `152.67.xx.xx` | IP público da VPS |
| `WebhooksHandler.csproj` | `Pancake.Api.csproj` | Arquivo de projeto para o publish |
| `WebhooksHandler.dll` | `Pancake.Api.dll` | DLL de entrada compilada |
| `5001` | `5001` | Porta interna da instância 1 |
| `5002` | `5002` | Porta interna da instância 2 |
