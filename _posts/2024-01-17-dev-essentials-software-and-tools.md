---
layout: post
title: "Dev Essentials - Part I - Software and Tools"
description: "A curated list of the essential software and tools I use daily as a software engineer — from API clients and database managers to .NET tools, Git clients and productivity utilities."
date: 2024-01-17
categories: [Coding]
tags: [dotnet, setup, software, tools, visual-studio, visual-studio-code, produtividade, devtools, docker, git, postman, insomnia, nodejs, php, python, rust]
reading_time: 3
image: /assets/img/posts/setup-scaled.jpg
series: dev-essentials
series_title: "Dev Essentials"
series_part: 1
---

<p class="lead">In this first part of the <strong>Dev Essentials</strong> series, I will present some software and tools I use in my day-to-day as a software engineer.</p>

As a software engineer, having the right software and tools at your disposal is crucial for optimizing productivity, streamlining development processes, and ensuring the delivery of high-quality code. With the ever-evolving landscape of software engineering, it's essential to stay up-to-date with the latest technologies and tools that can enhance your efficiency and effectiveness.

<div class="divider">· · ·</div>

<div class="providers-grid">

  <div class="provider-card">
    <div class="provider-name"><a href="https://jmeter.apache.org/" target="_blank">Apache JMeter</a></div>
    <div class="provider-detail">Load and performance testing tool. Simulate heavy traffic and measure response times across APIs and web applications.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.scootersoftware.com/" target="_blank">Beyond Compare</a></div>
    <div class="provider-detail">File and folder diff/merge tool. Compare text, code, binary files and entire directory trees side by side.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://catlight.io/" target="_blank">Catlight</a></div>
    <div class="provider-detail">Build and issue status notifier for GitHub, Azure DevOps, Jira and more. Keeps you aware of CI status without leaving the editor.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.charlesproxy.com/" target="_blank">Charles Proxy</a></div>
    <div class="provider-detail">HTTP proxy and monitor for debugging network traffic. Inspect, throttle and rewrite requests between your machine and the internet.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://chocolatey.org/" target="_blank">Chocolatey</a></div>
    <div class="provider-detail">Package manager for Windows. Install, update and manage hundreds of developer tools from the command line.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://getcomposer.org/" target="_blank">Composer</a></div>
    <div class="provider-detail">Dependency manager for PHP. Declares, resolves and installs project libraries with version constraints.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://dbeaver.io/" target="_blank">DBeaver</a></div>
    <div class="provider-detail">Universal database client supporting MySQL, PostgreSQL, SQL Server, SQLite and many more. Free and open source.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://apps.microsoft.com/detail/9pgcv4v3bk4w?hl=en-us&gl=US" target="_blank">DevToys</a></div>
    <div class="provider-detail">Swiss army knife for developers: JSON formatter, encoder/decoder, diff, UUID generator, regex tester and more — offline.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/RicoSuter/DNT" target="_blank">DNT (DotNetTools)</a></div>
    <div class="provider-detail">CLI tool for managing .NET solutions: update packages, switch between project references and packages, run scripts across projects.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker Desktop</a></div>
    <div class="provider-detail">Container runtime for local development. Build, run and manage containers and Kubernetes clusters from a desktop GUI.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://dotnet.microsoft.com/en-us/download/visual-studio-sdks" target="_blank">.NET SDK</a></div>
    <div class="provider-detail">Official .NET SDK for building and publishing .NET applications across Windows, Linux and macOS.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/Webreaper/CentralisedPackageConverter" target="_blank">.NET tool — CentralisedPackageConverter</a></div>
    <div class="provider-detail">Migrates .NET projects to centralized NuGet package management (Directory.Packages.props) automatically.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://csharpier.com/" target="_blank">.NET tool — CSharpier</a></div>
    <div class="provider-detail">Opinionated C# code formatter. Runs on save and in CI, keeping code style consistent with zero configuration.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://alirezanet.github.io/Husky.Net/" target="_blank">.NET tool — Husky.NET</a></div>
    <div class="provider-detail">Git hooks manager for .NET projects. Run linters, formatters and tests automatically on commit or push.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.jetbrains.com/help/dotcover/Coverage-Analysis-with-Command-Line-Tool.html" target="_blank">.NET tool — JetBrains.ReSharper.GlobalTools</a></div>
    <div class="provider-detail">Command-line tools for code coverage analysis and inspection — integrates with CI pipelines without the full IDE.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.nx-dotnet.com/" target="_blank">.NET tool — Nx-DotNet</a></div>
    <div class="provider-detail">Nx monorepo support for .NET projects. Brings affected commands, dependency graph and task scheduling to .NET solutions.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://docs.sonarsource.com/sonarqube/9.7/analyzing-source-code/scanners/sonarscanner-for-dotnet/" target="_blank">.NET tool — SonarScanner</a></div>
    <div class="provider-detail">SonarQube scanner for .NET. Collects code quality and security metrics and sends them to a SonarQube or SonarCloud instance.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://stryker-mutator.io/" target="_blank">.NET tool — Stryker</a></div>
    <div class="provider-detail">Mutation testing framework for .NET. Verifies test suite effectiveness by injecting bugs and checking if tests catch them.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.telerik.com/download/fiddler" target="_blank">Fiddler4</a></div>
    <div class="provider-detail">Web debugging proxy for HTTP/HTTPS traffic inspection, modification and replay. Essential for diagnosing API issues.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://git-fork.com/" target="_blank">Fork</a></div>
    <div class="provider-detail">Fast and friendly Git client for Mac and Windows. Visual diff, interactive rebase, conflict resolution and repository management.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://git-scm.com/download/win" target="_blank">GIT for Windows</a></div>
    <div class="provider-detail">Official Git distribution for Windows, including Git Bash and Git GUI.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.google.com/intl/en/chrome/" target="_blank">Google Chrome</a></div>
    <div class="provider-detail">Web browser with powerful DevTools for debugging JavaScript, inspecting network requests and profiling performance.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.grammarly.com/" target="_blank">Grammarly</a></div>
    <div class="provider-detail">AI writing assistant for grammar, style and clarity. Integrates with browsers, Word and desktop apps.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://insomnia.rest/" target="_blank">Insomnia</a></div>
    <div class="provider-detail">API design and testing tool. Supports REST, GraphQL and gRPC with environment variables, collections and test scripts.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.jetbrains.com/resharper/" target="_blank">JetBrains ReSharper</a></div>
    <div class="provider-detail">Productivity extension for Visual Studio with refactoring, code analysis, navigation and code generation for C# and .NET.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.jetbrains.com/rider/" target="_blank">JetBrains Rider</a></div>
    <div class="provider-detail">Cross-platform .NET IDE by JetBrains. Fast, feature-rich alternative to Visual Studio that runs on Windows, macOS and Linux.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://app.prntscr.com/en/index.html" target="_blank">Lightshot</a></div>
    <div class="provider-detail">Lightweight screenshot tool with annotation support, instant sharing and searchable screenshot history.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://azure.microsoft.com/en-us/products/data-explorer" target="_blank">Microsoft Azure Data Explorer</a></div>
    <div class="provider-detail">Fast and scalable data exploration service for log and telemetry data. Supports KQL for querying large datasets in real time.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16" target="_blank">SSMS</a></div>
    <div class="provider-detail">SQL Server Management Studio — the go-to tool for SQL Server administration, query writing and database management.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://nodejs.org/en" target="_blank">Node.js</a></div>
    <div class="provider-detail">JavaScript runtime built on Chrome's V8 engine. Required for most frontend toolchains and JS-based backend services.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/glideapps/quicktype" target="_blank">NPM QuickType</a></div>
    <div class="provider-detail">Generates strongly-typed code from JSON, JSON Schema and GraphQL in C#, TypeScript, Go, Rust and many more languages.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://github.com/nvm-sh/nvm" target="_blank">NVM (Node Version Manager)</a></div>
    <div class="provider-detail">Switch between Node.js versions easily. Essential when working across projects that require different Node versions.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://notepad-plus-plus.org/downloads/" target="_blank">Notepad++</a></div>
    <div class="provider-detail">Free and lightweight source code editor for Windows. Fast to open, supports syntax highlighting for dozens of languages.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://apps.microsoft.com/detail/9wzdncrdmdm3?hl=en-us&gl=US" target="_blank">NuGet Package Explorer</a></div>
    <div class="provider-detail">Inspect the contents of NuGet packages, view metadata, and create or edit packages without the command line.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://windows.php.net/download" target="_blank">PHP</a></div>
    <div class="provider-detail">PHP runtime for Windows. Required for local PHP development and running Composer-based projects.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.pgadmin.org/" target="_blank">pgAdmin 4</a></div>
    <div class="provider-detail">Administration and management tool for PostgreSQL. Query editor, schema browser, backup and restore in a web-based UI.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.postman.com/" target="_blank">Postman</a></div>
    <div class="provider-detail">API development and testing platform with collections, environments, automated tests and team collaboration.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://learn.microsoft.com/en-us/shows/it-ops-talk/how-to-install-powershell-7" target="_blank">PowerShell 7</a></div>
    <div class="provider-detail">Cross-platform PowerShell. Replaces the built-in Windows PowerShell with modern features and Linux/macOS support.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.python.org/" target="_blank">Python</a></div>
    <div class="provider-detail">Python runtime and interpreter. Used for scripting, automation, data analysis and ML tooling.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://www.rust-lang.org/" target="_blank">Rust</a></div>
    <div class="provider-detail">Systems programming language focused on safety, speed and concurrency. Toolchain includes rustup, cargo and rustfmt.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://developer.hashicorp.com/terraform/install" target="_blank">Terraform CLI</a></div>
    <div class="provider-detail">Infrastructure as code CLI by HashiCorp. Provision and manage cloud infrastructure across AWS, Azure, OCI and more.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://visualstudio.microsoft.com/" target="_blank">Visual Studio</a></div>
    <div class="provider-detail">Microsoft's full-featured IDE for .NET and C++ development. The primary IDE for C# projects and enterprise .NET solutions.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a></div>
    <div class="provider-detail">Lightweight, extensible code editor by Microsoft. The daily driver for PHP, JavaScript, TypeScript, Python and everything else.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://ubuntu.com/desktop/wsl" target="_blank">WSL — Ubuntu</a></div>
    <div class="provider-detail">Windows Subsystem for Linux running Ubuntu. Full Linux environment inside Windows for shell scripting, Docker and CLI tools.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://wakatime.com/plugins" target="_blank">WakaTime plugins</a></div>
    <div class="provider-detail">Automatic time tracking for VS, VS Code, Excel, Word, PowerPoint and more. Generates detailed coding activity reports.</div>
  </div>

  <div class="provider-card">
    <div class="provider-name"><a href="https://yarnpkg.com/" target="_blank">YARN</a></div>
    <div class="provider-detail">Fast, reliable JavaScript package manager. Deterministic installs with workspaces support for monorepos.</div>
  </div>

</div>
