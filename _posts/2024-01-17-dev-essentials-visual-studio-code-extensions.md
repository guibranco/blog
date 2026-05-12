---
layout: post
title: "Dev Essentials - Visual Studio Code Extensions"
description: "The VS Code extensions I rely on for PHP, C#, Python, Rust, Go, JavaScript, Docker, Kubernetes, Git and more — a curated list built from years of daily use."
date: 2024-01-17
categories: [Coding]
tags: [visual-studio-code, extensions, produtividade, setup, php, csharp, python, rust, javascript, devtools]
series: dev-essentials
series_title: "Dev Essentials"
series_part: 3
reading_time: 2
image: /assets/img/posts/logo-vsc.png
---

<p class="lead">In this third part of the <strong>Dev Essentials</strong> series, I present the extensions I use in <strong>Visual Studio Code</strong> — covering every language and tool in my stack.</p>

**Series index:**

- [Part I — Software and Tools](/blog/artigos/dev-essentials-software-and-tools/)
- [Part II — Visual Studio (IDE) Extensions](/blog/artigos/dev-essentials-visual-studio-ide-extensions/)
- **Part III — Visual Studio Code Extensions** ← you are here
- [Part IV — JetBrains ReSharper Extensions](/blog/artigos/dev-essentials-jetbrains-resharper-extensions/)

<div class="divider">· · ·</div>

<div class="providers-grid">
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=4ops.terraform" target="_blank">Terraform</a></div><div class="provider-detail">Terraform language support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap" target="_blank">Codesnap</a></div><div class="provider-detail">Take beautiful screenshots of your code.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=csharpier.csharpier-vscode" target="_blank">Csharpier Vscode</a></div><div class="provider-detail">CSharpier formatter for C# files.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=DEVSENSE.phptools-vscode" target="_blank">Phptools Vscode</a></div><div class="provider-detail">Complete PHP language support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=dotJoshJohnson.xml" target="_blank">Xml</a></div><div class="provider-detail">XML tools — formatting, XPath, XQuery.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets" target="_blank">Es7 React Js Snippets</a></div><div class="provider-detail">ES7+ React/Redux snippets.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank">Gitlens</a></div><div class="provider-detail">Supercharged Git integration — blame, history, lens.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode" target="_blank">Prettier Vscode</a></div><div class="provider-detail">Opinionated code formatter.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=fernandoescolar.vscode-solution-explorer" target="_blank">Vscode Solution Explorer</a></div><div class="provider-detail">Manage .NET solutions like Visual Studio.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner" target="_blank">Code Runner</a></div><div class="provider-detail">Run code snippets directly in the editor.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=GitHub.copilot" target="_blank">Copilot</a></div><div class="provider-detail">AI pair programmer by GitHub.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=golang.go" target="_blank">Go</a></div><div class="provider-detail">Official Go language support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree" target="_blank">Todo Tree</a></div><div class="provider-detail">Highlights TODO, FIXME and similar comments in a tree view.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=hashicorp.terraform" target="_blank">Terraform</a></div><div class="provider-detail">Official Terraform extension by HashiCorp.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=humao.rest-client" target="_blank">Rest Client</a></div><div class="provider-detail">HTTP client directly in the editor — send requests from .http files.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=jmrog.vscode-nuget-package-manager" target="_blank">Vscode Nuget Package Manager</a></div><div class="provider-detail">Add and update NuGet packages from VS Code.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock" target="_blank">Vscode Peacock</a></div><div class="provider-detail">Color the editor window per project/workspace.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=mathiasfrohlich.Kotlin" target="_blank">Kotlin</a></div><div class="provider-detail">Kotlin language support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker" target="_blank">Vscode Docker</a></div><div class="provider-detail">Docker integration — build, run, manage containers.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp" target="_blank">Csharp</a></div><div class="provider-detail">Official C# extension by Microsoft.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools" target="_blank">Vscode Kubernetes Tools</a></div><div class="provider-detail">Kubernetes cluster management and YAML support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank">Python</a></div><div class="provider-detail">Official Python extension.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter" target="_blank">Jupyter</a></div><div class="provider-detail">Jupyter notebook support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers" target="_blank">Remote Containers</a></div><div class="provider-detail">Develop inside Docker containers.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl" target="_blank">Remote Wsl</a></div><div class="provider-detail">Develop in WSL from Windows.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode.powershell" target="_blank">Powershell</a></div><div class="provider-detail">PowerShell language support and debugger.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight" target="_blank">Color Highlight</a></div><div class="provider-detail">Highlights web colors inline in the editor.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest" target="_blank">Vscode Jest</a></div><div class="provider-detail">Jest test runner integration.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml" target="_blank">Vscode Yaml</a></div><div class="provider-detail">YAML language support with JSON schema validation.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer" target="_blank">Rust Analyzer</a></div><div class="provider-detail">Official Rust language server.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=snyk-security.snyk-vulnerability-scanner" target="_blank">Snyk Vulnerability Scanner</a></div><div class="provider-detail">Snyk security scanning for code and dependencies.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode" target="_blank">Sonarlint Vscode</a></div><div class="provider-detail">SonarLint static code analysis.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker" target="_blank">Code Spell Checker</a></div><div class="provider-detail">Spell checker for source code.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-portuguese-brazilian" target="_blank">Code Spell Checker Portuguese Brazilian</a></div><div class="provider-detail">Brazilian Portuguese dictionary for Code Spell Checker.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons" target="_blank">Vscode Icons</a></div><div class="provider-detail">File icons for the Explorer panel.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=Vue.volar" target="_blank">Volar</a></div><div class="provider-detail">Official Vue 3 language support.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=WakaTime.vscode-wakatime" target="_blank">Vscode Wakatime</a></div><div class="provider-detail">Automatic time tracking for coding.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost" target="_blank">Vscode Import Cost</a></div><div class="provider-detail">Shows the size of imported packages inline.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug" target="_blank">Php Debug</a></div><div class="provider-detail">PHP debugger with XDebug support.</div></div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">Sync across machines</div>
  Enable <strong>Settings Sync</strong> in VS Code (built-in since 1.48) to keep your extensions, keybindings and settings in sync across all your machines via GitHub or Microsoft account.
</div>
