---
layout: post
title: "Dev Essentials - JetBrains ReSharper Extensions"
description: "The JetBrains ReSharper extensions I use to enforce code quality, measure complexity, improve unit testing workflow and boost overall .NET productivity."
date: 2024-01-17
categories: [Coding]
tags: [dotnet, resharper, jetbrains, extensions, csharp, produtividade, code-quality, testing, setup]
series: dev-essentials
series_title: "Dev Essentials"
series_part: 4
reading_time: 2
image: /assets/img/posts/logo_resharper.png

---

<p class="lead">In this fourth and final part of the <strong>Dev Essentials</strong> series, I present the extensions I use on <strong>JetBrains ReSharper</strong> — plugins that take an already powerful tool even further.</p>

**Series index:**

- [Part I — Software and Tools](/blog/artigos/dev-essentials-software-and-tools/)
- [Part II — Visual Studio (IDE) Extensions](/blog/artigos/dev-essentials-visual-studio-ide-extensions/)
- [Part III — Visual Studio Code Extensions](/blog/artigos/dev-essentials-visual-studio-code-extensions/)
- **Part IV — JetBrains ReSharper Extensions** ← you are here

<div class="divider">· · ·</div>

<div class="providers-grid">
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/19783-attribute-localization-for-resharper" target="_blank">Attribute Localization for ReSharper</a></div><div class="provider-detail">Automates localization of attribute arguments.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11677-cleancode" target="_blank">Clean Code</a></div><div class="provider-detail">Highlights code smells based on clean code principles.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/12391-cognitivecomplexity" target="_blank">Cognitive Complexity</a></div><div class="provider-detail">Measures cognitive complexity of methods inline.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11662-configuration-sense" target="_blank">Configuration Sense</a></div><div class="provider-detail">Autocomplete for appsettings.json and other config files.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11625-cyclomaticcomplexity" target="_blank">Cyclomatic Complexity</a></div><div class="provider-detail">Shows cyclomatic complexity metrics inside the editor.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11621-enhanced-tooltip" target="_blank">Enhanced Tooltip</a></div><div class="provider-detail">Richer tooltips with more context on hover.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/16367-fluentassertions" target="_blank">Fluent Assertions</a></div><div class="provider-detail">Quick-fixes and helpers for Fluent Assertions.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/15946-fluentvalidation" target="_blank">FluentValidation</a></div><div class="provider-detail">Inspections and helpers for FluentValidation rules.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11643-internalsvisibleto-helper" target="_blank">InternalsVisibleTo Helper</a></div><div class="provider-detail">Automates assembly access declarations.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11853-moqcomplete" target="_blank">MOQ Complete</a></div><div class="provider-detail">Autocomplete for Moq mock setups.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11665-resharper-helpers" target="_blank">ReSharper Helpers</a></div><div class="provider-detail">Additional navigation and productivity actions.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11620-respeller-free" target="_blank">ReSpeller Free</a></div><div class="provider-detail">Spell checker integration inside ReSharper.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11619-stylecop-by-jetbrains" target="_blank">StyleCop by JetBrains</a></div><div class="provider-detail">Enforces StyleCop rules with ReSharper inspections.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11648-xml-doc-inspections" target="_blank">XML doc inspections</a></div><div class="provider-detail">Validates XML documentation comments.</div></div>
  <div class="provider-card"><div class="provider-name"><a href="https://plugins.jetbrains.com/plugin/11669-xunit-net-live-templates" target="_blank">xUnit.NET Live Templates</a></div><div class="provider-detail">Live templates for xUnit test patterns.</div></div>
</div>

<div class="callout callout-tip">
  <div class="callout-label">How to install</div>
  In Visual Studio, go to <strong>ReSharper → Extension Manager</strong>, search by name and click Install. You can also browse the full gallery at <a href="https://plugins.jetbrains.com/resharper" target="_blank">plugins.jetbrains.com/resharper</a>.
</div>
