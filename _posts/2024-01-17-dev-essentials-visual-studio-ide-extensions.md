---
layout: post
title: "Dev Essentials - Visual Studio (IDE) Extensions"
description: "The Visual Studio extensions I use daily to boost productivity, enforce code quality, automate documentation, and streamline the .NET development workflow."
date: 2024-01-17
categories: [Coding]
tags: [dotnet, visual-studio, extensions, produtividade, csharp, setup, devtools]
series: dev-essentials
series_title: "Dev Essentials"
series_part: 2
reading_time: 2
image: /assets/img/posts/logo-vs-v2.jpg
---

<p class="lead">In this second part of the <strong>Dev Essentials</strong> series, I present the extensions I use in <strong>Visual Studio (IDE)</strong> — the ones that survived years of use and actually make a difference.</p>

**Series index:**

- [Part I — Software and Tools](/blog/artigos/dev-essentials-software-and-tools/)
- **Part II — Visual Studio (IDE) Extensions** ← you are here
- [Part III — Visual Studio Code Extensions](/blog/artigos/dev-essentials-visual-studio-code-extensions/)
- [Part IV — JetBrains ReSharper Extensions](/blog/artigos/dev-essentials-jetbrains-resharper-extensions/)

<div class="divider">· · ·</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.upgradeassistant" target="_blank">.NET Upgrade Assistant</a></div>
    <div class="provider-detail">Helps migrate .NET Framework projects to modern .NET.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022" target="_blank">AWS Toolkit for VS 2022</a></div>
    <div class="provider-detail">AWS integration directly inside Visual Studio.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=cpmcgrath.Codealignment" target="_blank">Code Alignment</a></div>
    <div class="provider-detail">Align code assignments and declarations by a chosen character.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=SteveCadwallader.CodeMaidVS2022" target="_blank">CodeMaid VS2022</a></div>
    <div class="provider-detail">Cleans, digs, and simplifies C# code automatically.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=csharpier.CSharpier" target="_blank">CSharpier</a></div>
    <div class="provider-detail">Opinionated C# formatter — runs on save.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=ErikEJ.EFCorePowerTools" target="_blank">EF Core Power Tools</a></div>
    <div class="provider-detail">Reverse engineering, migrations and diagram visualization for EF Core.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=sergeb.GhostDoc" target="_blank">GhostDoc Pro</a></div>
    <div class="provider-detail">Generates XML documentation comments automatically.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=SharpDevelopTeam.ILSpy2022" target="_blank">ILSpy</a></div>
    <div class="provider-detail">Decompiler — inspect any .NET assembly.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=JetBrains.ReSharper" target="_blank">JetBrains ReSharper</a></div>
    <div class="provider-detail">The most powerful productivity extension for Visual Studio.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=NikolayBalakin.Outputenhancer" target="_blank">Output Enhancer</a></div>
    <div class="provider-detail">Colorizes the Output window for easier log reading.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=MadsKristensen.RainbowBraces" target="_blank">Rainbow Braces</a></div>
    <div class="provider-detail">Colorizes matching brackets for better readability.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=TomEnglert.ResXManager" target="_blank">ResXManager</a></div>
    <div class="provider-detail">Manage all resource files (.resx) in one place.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=Suchiman.SerilogAnalyzer" target="_blank">Serilog Analyzer</a></div>
    <div class="provider-detail">Roslyn analyzer for correct Serilog usage.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=snyk-security.snyk-vulnerability-scanner-vs-2022" target="_blank">Snyk Security</a></div>
    <div class="provider-detail">Scans for vulnerabilities in dependencies and code.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2022" target="_blank">SonarLint</a></div>
    <div class="provider-detail">Static code analysis for bugs, code smells and security issues.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=TechTalkSpecFlowTeam.SpecFlowForVisualStudio2022" target="_blank">SpecFlow for VS 2022</a></div>
    <div class="provider-detail">BDD framework for .NET with Gherkin syntax support.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=RandomEngy.UnitTestBoilerplateGenerator" target="_blank">Unit Test Boilerplate Generator</a></div>
    <div class="provider-detail">Generates unit test boilerplate from a class in one click.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=TomasRestrepo.Viasfora" target="_blank">Viasfora</a></div>
    <div class="provider-detail">Colorizes keywords, string escapes, and rainbow braces.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=WakaTime.WakaTime" target="_blank">WakaTime</a></div>
    <div class="provider-detail">Automatic time tracking for your coding activity.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name"><a href="https://marketplace.visualstudio.com/items?itemName=jsakamoto.xUnitTestProjectTemplate" target="_blank">xUnit Test Project Template</a></div>
    <div class="provider-detail">Adds xUnit project templates to the New Project dialog.</div>
  </div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">How to install</div>
  Go to <strong>Extensions → Manage Extensions</strong> inside Visual Studio and search by name. Most extensions restart VS on install. For bulk installation, consider using a <code>.vsconfig</code> file to share your extension set across machines.
</div>
