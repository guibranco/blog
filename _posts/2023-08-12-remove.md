---
layout: post
title: "Using GitHub Actions to create a .NET Framework pipeline. Build, test, and deploy!"
description: "Step-by-step guide to set up a CI/CD pipeline for a .NET Framework project using GitHub Actions — covering build, test, and deploy with MSBuild, NuGet, and VSTest."
date: 2023-08-12
categories: [Coding, DevOps, Testing]
tags: [net-framework, github-actions, ci, cd, build, test, deploy, msbuild, nuget, vstest, yaml, pipeline]
reading_time: 5
---

<p class="lead">In this article we'll cover the CI/CD process of a .NET Framework project using GitHub Actions to build, test, and run — from creating the workflow file to monitoring the pipeline execution.</p>

For reference, here's the PoC repository used as the basis for this tutorial:

[![POC GH Actions CI .NET Framework](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=GuilhermeStracini&repo=POC-GHActions-CI-NetFramework&show_owner=false&show_forks=true&show_issues=true)](https://github.com/GuilhermeStracini/POC-GHActions-CI-NetFramework){:target="_blank"}

<div class="callout callout-tip">
  <div class="callout-label">What are GitHub Actions?</div>
  GitHub Actions provides a flexible way to automate tasks directly from your GitHub repositories — building, testing, and deploying applications. Workflows are defined in YAML files and can be customized to your project's requirements.
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>Creating the workflow</h2></div>
</div>

**Step 1:** Open your repository on GitHub and click on the **Actions** tab.

**Step 2:** Click **Set up a workflow yourself** to create a blank workflow file.

**Step 3:** Name the workflow and define the triggers:

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">YAML — triggers</div>
  </div>
  <pre><span class="va">name</span>: <span class="st">Build .NET Framework</span>

<span class="va">on</span>:
  <span class="va">push</span>:
  <span class="va">workflow_dispatch</span>:</pre>
</div>

The `push` event triggers the workflow on every push. `workflow_dispatch` allows manual execution from the Actions tab. Full reference: [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows){:target="_blank"}.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Defining the build job</h2></div>
</div>

**Step 4:** Create the job with a Windows runner (required for .NET Framework):

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">YAML — job definition</div>
  </div>
  <pre><span class="va">jobs</span>:
  <span class="va">build</span>:
    <span class="va">name</span>: <span class="st">Build</span>
    <span class="va">runs-on</span>: <span class="st">windows-latest</span></pre>
</div>

**Step 5:** Add the steps — setup tools, restore packages, build, test, and run:

<div class="code-block">
  <div class="code-header">
    <div class="code-dots"><span></span><span></span><span></span></div>
    <div class="code-lang">YAML — complete steps</div>
  </div>
  <pre><span class="va">steps</span>:
  - <span class="va">name</span>: <span class="st">Checkout Code</span>
    <span class="va">uses</span>: <span class="st">actions/checkout@v3</span>
    <span class="va">with</span>:
      <span class="va">fetch-depth</span>: <span class="nu">0</span>

  - <span class="va">name</span>: <span class="st">Setup MSBuild Path</span>
    <span class="va">uses</span>: <span class="st">microsoft/setup-msbuild@v1.3</span>
    <span class="va">env</span>:
      <span class="va">ACTIONS_ALLOW_UNSECURE_COMMANDS</span>: <span class="st">true</span>

  - <span class="va">name</span>: <span class="st">Setup VSTest</span>
    <span class="va">uses</span>: <span class="st">darenm/Setup-VSTest@v1.2</span>

  - <span class="va">name</span>: <span class="st">Setup Nuget</span>
    <span class="va">uses</span>: <span class="st">NuGet/setup-nuget@v1.2</span>

  - <span class="va">name</span>: <span class="st">Restore NuGet Packages</span>
    <span class="va">run</span>: <span class="st">nuget restore your-solution-name.sln</span>

  - <span class="va">name</span>: <span class="st">Build Release</span>
    <span class="va">run</span>: <span class="st">msbuild your-solution-name.sln /p:Configuration=Release</span>

  - <span class="va">name</span>: <span class="st">Test</span>
    <span class="va">run</span>: <span class="st">vstest.console.exe path-to-test-binary.dll</span>

  - <span class="va">name</span>: <span class="st">Run</span>
    <span class="va">run</span>: <span class="st">path-to-application-binary.exe</span></pre>
</div>

**Replace in your workflow:**
- `your-solution-name.sln` — path/name of your solution file
- `path-to-test-binary.dll` — path to the tests DLL inside `bin/Release/`
- `path-to-application-binary.exe` — path to the main executable

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Monitoring and next steps</h2></div>
</div>

**Step 6:** Save and trigger the workflow — either manually from the Actions tab or automatically on the next push.

**Step 7:** Monitor the pipeline directly from the **Actions** tab. You can track progress, view logs, and debug issues for each step in real time.

<div class="callout callout-tip">
  <div class="callout-label">Going further</div>
  The PoC repository includes additional features beyond this tutorial: code coverage reporting, artifact publishing, and deployment steps. Check it out for a more complete example of a production-ready CI/CD pipeline for .NET Framework.
</div>
