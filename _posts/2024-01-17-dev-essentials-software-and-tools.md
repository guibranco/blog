---
layout: post
title: "Dev Essentials - Software and Tools"
description: "The software and tools I use every day as a software engineer — from API testing to database management, code formatting, Git clients and productivity utilities."
date: 2024-01-17
categories: [Coding]
tags: [dotnet, setup, software, tools, visual-studio, visual-studio-code, produtividade, devtools]
reading_time: 2
---

<p class="lead">In this first part of the <strong>Dev Essentials</strong> series, I present the software and tools I use in my day-to-day as a software engineer — curated after years of trial and error.</p>

**Series index:**

- **Part I — Software and Tools** ← you are here
- [Part II — Visual Studio (IDE) Extensions](/blog/artigos/dev-essentials-visual-studio-ide-extensions/)
- [Part III — Visual Studio Code Extensions](/blog/artigos/dev-essentials-visual-studio-code-extensions/)
- [Part IV — JetBrains ReSharper Extensions](/blog/artigos/dev-essentials-jetbrains-resharper-extensions/)

<div class="divider">· · ·</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><a href="https://jmeter.apache.org/" target="_blank">Apache JMeter</a></div>
    <div class="provider-detail">Load and performance testing tool.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.scootersoftware.com/" target="_blank">Beyond Compare</a></div>
    <div class="provider-detail">File and folder diff/merge tool.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://catlight.io/" target="_blank">Catlight</a></div>
    <div class="provider-detail">Build and issue status notifier for GitHub, Azure DevOps and more.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.charlesproxy.com/" target="_blank">Charles Proxy</a></div>
    <div class="provider-detail">HTTP proxy and monitor for debugging network traffic.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://chocolatey.org/" target="_blank">Chocolatey</a></div>
    <div class="provider-detail">Package manager for Windows.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://getcomposer.org/" target="_blank">Composer</a></div>
    <div class="provider-detail">Dependency manager for PHP.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://dbeaver.io/" target="_blank">DBeaver</a></div>
    <div class="provider-detail">Universal database client supporting MySQL, PostgreSQL, SQL Server and more.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://apps.microsoft.com/detail/9pgcv4v3bk4w" target="_blank">DevToys</a></div>
    <div class="provider-detail">Swiss army knife for developers — JSON formatter, encoder, diff, and more.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/RicoSuter/DNT" target="_blank">DNT (DotNetTools)</a></div>
    <div class="provider-detail">CLI tool for managing .NET solutions.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker Desktop</a></div>
    <div class="provider-detail">Container runtime for local development.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://dotnet.microsoft.com/en-us/download/visual-studio-sdks" target="_blank">.NET SDK</a></div>
    <div class="provider-detail">Official .NET SDK downloads.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://csharpier.com/" target="_blank">CSharpier</a></div>
    <div class="provider-detail">Opinionated C# code formatter.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://alirezanet.github.io/Husky.Net/" target="_blank">Husky.NET</a></div>
    <div class="provider-detail">Git hooks manager for .NET projects.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://stryker-mutator.io/" target="_blank">Stryker</a></div>
    <div class="provider-detail">Mutation testing framework for .NET.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.telerik.com/download/fiddler" target="_blank">Fiddler</a></div>
    <div class="provider-detail">Web debugging proxy for HTTP/HTTPS traffic inspection.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://git-fork.com/" target="_blank">Fork</a></div>
    <div class="provider-detail">Fast and friendly Git client for Mac and Windows.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://git-scm.com/download/win" target="_blank">GIT for Windows</a></div>
    <div class="provider-detail">Official Git distribution for Windows.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.grammarly.com/" target="_blank">Grammarly</a></div>
    <div class="provider-detail">AI writing assistant for grammar and style.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://insomnia.rest/" target="_blank">Insomnia</a></div>
    <div class="provider-detail">API design and testing tool.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.jetbrains.com/resharper/" target="_blank">JetBrains ReSharper</a></div>
    <div class="provider-detail">Productivity extension for Visual Studio with refactoring and code analysis.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.jetbrains.com/rider/" target="_blank">JetBrains Rider</a></div>
    <div class="provider-detail">Cross-platform .NET IDE by JetBrains.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms" target="_blank">SSMS</a></div>
    <div class="provider-detail">SQL Server Management Studio.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://nodejs.org/en" target="_blank">Node.js</a></div>
    <div class="provider-detail">JavaScript runtime built on Chrome's V8 engine.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/nvm-sh/nvm" target="_blank">NVM</a></div>
    <div class="provider-detail">Node Version Manager — switch between Node versions easily.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://notepad-plus-plus.org/downloads/" target="_blank">Notepad++</a></div>
    <div class="provider-detail">Free source code editor for Windows.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.pgadmin.org/" target="_blank">PgAdmin4</a></div>
    <div class="provider-detail">Administration and management tool for PostgreSQL.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://www.postman.com/" target="_blank">Postman</a></div>
    <div class="provider-detail">API development and testing platform.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://learn.microsoft.com/en-us/shows/it-ops-talk/how-to-install-powershell-7" target="_blank">PowerShell 7</a></div>
    <div class="provider-detail">Cross-platform PowerShell.</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Tip</div>
  Most of these tools are free or have a free tier. Start with the ones that match your current stack and add others as your workflow evolves. You don't need everything at once.
</div>
