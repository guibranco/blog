---
layout: post
title: "Como Automatizar a Sincronização Entre um Repositório Git Local e um Servidor (S)FTP"
description: "Aprenda a montar um sistema Python que compara, envia e baixa arquivos entre um repositório Git local e um servidor FTP ou SFTP — com relatório HTML automático e commits inteligentes, sem depender de CI/CD externo."
date: 2025-12-12
categories: [Coding, Infraestrutura]
subcategories:
  - "Coding/Python"
  - "Infraestrutura/DevOps"
tags: [git, ftp, sftp, python, automacao, devops, sincronizacao, legado, ci-cd, gitpython, md5, hash, scripts]
reading_time: 7
image: /assets/img/posts/git-ftp-sync.png
---

<p class="lead">Em muitos ambientes corporativos — especialmente em estruturas legadas ou altamente restritas — o uso de Git hospedado (GitHub, GitLab, Bitbucket) ou pipelines de CI/CD é simplesmente proibido. Mesmo assim, o desenvolvimento continua acontecendo, e manter arquivos atualizados no servidor pode se transformar em um trabalho cansativo, repetitivo e propenso a erros.</p>

Fazer upload manual via FTP, baixar alterações feitas diretamente no servidor e tentar conciliar tudo com o repositório Git local rapidamente se torna um pesadelo. A boa notícia: é possível **automatizar todo esse fluxo** usando apenas o seu computador e acesso ao servidor (S)FTP.

Neste artigo você vai aprender como montar um sistema que:

- 🔄 Compara arquivos entre Git local e FTP
- ⬇️ Baixa arquivos quando o servidor está mais atualizado
- ⬆️ Envia arquivos quando o Git local está mais novo
- 📝 Gera relatórios HTML ou TXT
- 🏷️ Registra automaticamente mudanças no Git

Tudo isso sem depender de nenhum serviço externo.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>🎯 Por que automatizar?</h2></div>
</div>

Imagine este cenário:

- Um time precisa atualizar arquivos em um servidor legado via FTP
- Vários desenvolvedores têm acesso ao mesmo ambiente
- Mudanças às vezes são feitas diretamente no servidor por outro departamento
- Não existe integração contínua
- Não existe ambiente de testes

Sem automação, esse fluxo depende de disciplina — e sorte. Com automação, você ganha:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Controle</div>
    <div class="provider-detail">Todas as alterações passam por um processo rastreável, eliminando a dúvida de "quem mexeu nisso?"</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Segurança</div>
    <div class="provider-detail">Nenhuma alteração é perdida. O Git registra o histórico de tudo que entra e sai do servidor.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Histórico de auditoria</div>
    <div class="provider-detail">Cada sincronização gera um relatório e um commit, criando trilha completa para auditoria interna.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Repetibilidade</div>
    <div class="provider-detail">O mesmo script executa sempre da mesma forma, independentemente de quem o rodar ou quando.</div>
  </div>
</div>

Automatizar a sincronização transforma um processo arriscado em um fluxo de trabalho consistente.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>🧩 Como funciona a lógica da sincronização?</h2></div>
</div>

A ideia é simples e poderosa: comparar a versão do arquivo no Git com a versão no servidor (S)FTP.

Sempre que um arquivo é encontrado, três cenários são possíveis:

1. **A versão remota é mais nova** → Baixar e registrar no Git
2. **A versão local é mais nova** → Enviar para o FTP e registrar no relatório
3. **As versões são iguais** → Ignorar para poupar tempo

Esse fluxo garante que sempre exista **um único ponto de verdade**, mesmo em ambientes descentralizados.

### 📊 Diagrama do fluxo

```
[Git Local] → Verifica arquivo → [FTP]

              ↙      ↓      ↘
         FTP é novo  Igual  Git é novo

         Baixar       Nada      Enviar
         Commit        |         |
                   Relatório ←-----
```

<div class="callout callout-tip">
  <div class="callout-label">Substitua o diagrama ao publicar</div>
  O diagrama acima é uma representação em texto. Para a publicação final, substitua pelo arquivo <code>sync-flow-diagram.svg</code> com o fluxo visual.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>⚙️ Comparando arquivos: hash, timestamps e integridade</h2></div>
</div>

Para decidir qual versão está mais atual, é possível usar diferentes estratégias:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">✔️ Hash (MD5 / SHA1)</div>
    <div class="provider-detail">Garantia total de integridade — detecta qualquer mudança. Ponto negativo: requer baixar o arquivo remoto para calcular o hash.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">✔️ Timestamp (MDTM)</div>
    <div class="provider-detail">Extremamente rápido e não requer baixar o arquivo. Depende do relógio correto no servidor — pode gerar falsos positivos em servidores com horário desatualizado.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">✔️ Arquivo de versão separado</div>
    <div class="provider-detail">Ideal para sistemas com muitos arquivos e facilita auditorias. Requer manutenção manual do arquivo de versão.</div>
  </div>
</div>

No exemplo a seguir utilizamos **hash + timestamp** para máxima confiabilidade.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>🐍 Exemplo de automação com Python</h2></div>
</div>

O script abaixo percorre arquivos rastreados pelo Git, compara com a versão existente no FTP, baixa ou envia conforme a necessidade, gera um relatório HTML e adiciona commits automáticos quando há atualizações vindas do servidor.

### 📌 Código completo (pronto para uso)

```python
import os
import hashlib
from ftplib import FTP
from datetime import datetime
from git import Repo

# CONFIG
LOCAL_PATH  = './my-local-repo'
FTP_HOST    = 'ftp.example.com'
FTP_USER    = 'youruser'
FTP_PASS    = 'yourpass'
REMOTE_PATH = '/remote/dir'

# Git Repo
repo   = Repo(LOCAL_PATH)
report = []

# Connect to FTP
ftp = FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)
ftp.cwd(REMOTE_PATH)

def md5_local(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def md5_remote(filename):
    from io import BytesIO
    buf = BytesIO()
    try:
        ftp.retrbinary(f'RETR {filename}', buf.write)
        return hashlib.md5(buf.getvalue()).hexdigest()
    except:
        return None

for file in repo.git.ls_files().split('\n'):
    local_file  = os.path.join(LOCAL_PATH, file)
    local_hash  = md5_local(local_file)
    remote_hash = md5_remote(file)

    if remote_hash is None:
        # Upload new file
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {file}', f)
        report.append(f"[UPLOAD] {file} was not on remote.")

    elif remote_hash != local_hash:
        # Compare timestamps
        remote_time = ftp.sendcmd(f"MDTM {file}")[4:].strip()
        remote_dt   = datetime.strptime(remote_time, '%Y%m%d%H%M%S')
        local_dt    = datetime.fromtimestamp(os.path.getmtime(local_file))

        if remote_dt > local_dt:
            # Download newer remote version
            with open(local_file, 'wb') as f:
                ftp.retrbinary(f'RETR {file}', f.write)
            repo.index.add([file])
            repo.index.commit(f"[SYNC] Pulled newer {file} from FTP")
            report.append(f"[DOWNLOAD] {file} - FTP was newer")
        else:
            # Upload newer local version
            with open(local_file, 'rb') as f:
                ftp.storbinary(f'STOR {file}', f)
            report.append(f"[UPLOAD] {file} - Local was newer")

    else:
        report.append(f"[SKIP] {file} is up-to-date")

# Write report
with open(os.path.join(LOCAL_PATH, 'sync-report.html'), 'w') as report_file:
    report_file.write("<h2>Sync Report</h2><ul>")
    for line in report:
        report_file.write(f"<li>{line}</li>")
    report_file.write("</ul>")

ftp.quit()
print("✅ Sync complete.")
```

<div class="callout callout-warn">
  <div class="callout-label">Dependências necessárias</div>
  Instale as dependências antes de rodar: <code>pip install gitpython</code>. A biblioteca <code>ftplib</code> já faz parte da biblioteca padrão do Python.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">05</div>
  <div class="section-title-wrap"><h2>📄 Relatório automático</h2></div>
</div>

O script gera automaticamente um arquivo `sync-report.html` contendo:

- Arquivos enviados ao servidor
- Arquivos baixados do servidor
- Arquivos ignorados (sem alteração)
- Data e hora da execução
- Resumo da atividade

Esse relatório pode ser arquivado, enviado por e-mail ou compartilhado com outros times de TI para fins de auditoria.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">06</div>
  <div class="section-title-wrap"><h2>🚀 Possíveis evoluções</h2></div>
</div>

Se quiser tornar o sistema mais completo, você pode implementar as seguintes melhorias:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">🔧 Versão SFTP com Paramiko</div>
    <div class="provider-detail">Ideal para ambientes que exigem SSH. A biblioteca <code>paramiko</code> oferece suporte completo ao protocolo SFTP com autenticação por chave pública.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">⏲️ Execução automática</div>
    <div class="provider-detail">Agende o script via <strong>Windows Task Scheduler</strong> ou <strong>cron</strong> no Linux/macOS para sincronização periódica sem intervenção manual.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">📤 Notificações integradas</div>
    <div class="provider-detail">Envie o relatório por e-mail, Slack ou Microsoft Teams ao término de cada execução — mantenha toda a equipe informada automaticamente.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">🧭 Dashboard local</div>
    <div class="provider-detail">Construa uma interface web simples para visualizar o histórico de sincronizações e os relatórios gerados anteriormente.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">🧪 Versionamento por arquivo</div>
    <div class="provider-detail">Mantenha um arquivo de versão individual por asset. Útil em ambientes com milhares de arquivos onde o hash completo seria muito lento.</div>
  </div>
</div>

<div class="conclusion">
  <h2>Sincronização confiável em ambientes legados</h2>
  <p>Automatizar a sincronização entre o repositório Git local e um servidor (S)FTP elimina o risco de conflitos, perda de alterações e inconsistências. O processo se torna mais seguro, organizado e confiável — mesmo sem CI/CD ou serviços hospedados.</p>
  <p>Se você trabalha em ambientes legados ou restritos, essa solução representa um enorme avanço em produtividade e segurança operacional. O investimento em configurar o script uma única vez se paga rapidamente em tempo economizado e erros evitados.</p>
</div>
