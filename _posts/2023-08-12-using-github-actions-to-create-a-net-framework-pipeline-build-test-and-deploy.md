---
layout: post
title: "Using GitHub Actions to create a .NET Framework pipeline: Build, test, and deploy"
description: "A step-by-step guide to setting up a CI/CD pipeline for a .NET Framework project using GitHub Actions — build, test with VSTest, restore NuGet packages, and run the application automatically."
date: 2023-08-12
categories: [Coding, DevOps, Testing]
tags: [dotnet, dotnet-framework, net-framework, github-actions, ci-cd, build, deploy, pipeline, yaml, msbuild, nuget, vstest, coverage, csharp, automacao, workflows, teste, testes, tests, testing]
reading_time: 6
image: /assets/img/posts/GitHubActionsLogo.webp
---

<p class="lead">In this article we cover the CI/CD process of a .NET Framework project using GitHub Actions to build, test, and run — from the first workflow file to a complete automated pipeline.</p>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">01</div>
  <div class="section-title-wrap"><h2>What are GitHub Actions?</h2></div>
</div>

GitHub Actions provides a flexible way to automate various tasks directly from your GitHub repositories — building, testing, and deploying applications. These actions are defined in YAML files as **workflows** and can be customized to suit your project's specific requirements.

For reference, I set up a repository on GitHub with a PoC (Proof of Concept) based on this tutorial. That repository has many more features than what I cover here:

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">POC-GHActions-CI-NetFramework</div>
    <div class="provider-detail">A working proof of concept on GitHub showing GitHub Actions CI for a .NET Framework solution — with build, test, and coverage steps already configured.</div>
    <div class="provider-price">
      <a href="https://github.com/GuilhermeStracini/POC-GHActions-CI-NetFramework" target="_blank">github.com/GuilhermeStracini/POC-GHActions-CI-NetFramework</a>
    </div>
  </div>
</div>

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">02</div>
  <div class="section-title-wrap"><h2>Creating the pipeline — step by step</h2></div>
</div>

**Step 1 — Open the Actions tab**

Open your repository on GitHub and click on the **Actions** tab.

**Step 2 — Set up a workflow yourself**

GitHub provides numerous workflow templates for different languages and frameworks. To write your own from scratch, click **Set up a workflow yourself** above the *Choose a workflow* section.

**Step 3 — Name the workflow and define triggers**

In the GitHub Actions editor, name the workflow and define the events that will fire it:

```yaml
name: Build .NET Framework

on:
  push:
  workflow_dispatch:
```

- `push` fires the workflow on every push to the repository.
- `workflow_dispatch` allows running the workflow manually from the Actions page.

A complete reference of all trigger events is in the [official GitHub Actions documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows){:target="_blank"}.

**Step 4 — Define the build job on a Windows runner**

.NET Framework requires a Windows environment. Create a job and target `windows-latest`:

```yaml
jobs:
  build:
    name: Build
    runs-on: windows-latest
```

The `runs-on` value is job-scoped — different jobs in the same workflow can target different operating systems.

**Step 5 — Configure the job steps**

The job needs the following steps in order:

1. Checkout the source code
2. Set up MSBuild
3. Set up VSTest
4. Set up NuGet
5. Restore NuGet packages
6. Build the solution in Release mode
7. Run the tests
8. *(Optional)* Run the compiled executable

```yaml
steps:
  - name: Checkout Code
    uses: actions/checkout@v3
    with:
      fetch-depth: 0

  - name: Setup MSBuild Path
    uses: microsoft/setup-msbuild@v1.3
    env:
      ACTIONS_ALLOW_UNSECURE_COMMANDS: true

  - name: Setup VSTest
    uses: darenm/Setup-VSTest@v1.2

  - name: Setup NuGet
    uses: NuGet/setup-nuget@v1.2
    env:
      ACTIONS_ALLOW_UNSECURE_COMMANDS: true

  - name: Restore NuGet Packages
    run: nuget restore your-solution-name.sln

  - name: Build Release
    run: msbuild your-solution-name.sln /p:Configuration=Release

  - name: Test
    run: vstest.console.exe path-to-test-binary.dll

  - name: Run
    run: path-to-application-binary.exe
```

<div class="callout callout-warn">
  <div class="callout-label">Placeholders to replace</div>
  Replace <code>your-solution-name.sln</code> with the actual path to your solution file in both the <em>Restore</em> and <em>Build</em> steps. Replace <code>path-to-test-binary.dll</code> with the DLL path of the test project after a Release build — usually inside <code>bin/Release/</code>. Replace <code>path-to-application-binary.exe</code> with the path to the compiled executable of your main project.
</div>

**Steps 6 and 7 — Save, trigger, and monitor**

Save the workflow file — it lives at `.github/workflows/build.yml` in your repository. GitHub Actions triggers it automatically on the next push, or you can run it manually from the Actions tab. Each run shows a full view of progress, logs, and error details.

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">03</div>
  <div class="section-title-wrap"><h2>Complete workflow file</h2></div>
</div>

Here is the full workflow to build, test, and run a .NET Framework solution:

```yaml
name: Build .NET Framework

on:
  push:
  workflow_dispatch:

jobs:
  build:
    name: Build
    runs-on: windows-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup MSBuild Path
        uses: microsoft/setup-msbuild@v1.3
        env:
          ACTIONS_ALLOW_UNSECURE_COMMANDS: true

      - name: Setup VSTest
        uses: darenm/Setup-VSTest@v1.2

      - name: Setup NuGet
        uses: NuGet/setup-nuget@v1.2
        env:
          ACTIONS_ALLOW_UNSECURE_COMMANDS: true

      - name: Restore NuGet Packages
        run: nuget restore your-solution-name.sln

      - name: Build Release
        run: msbuild your-solution-name.sln /p:Configuration=Release

      - name: Test
        run: vstest.console.exe path-to-test-binary.dll

      - name: Run
        run: path-to-application-binary.exe
```

<div class="divider">· · ·</div>

<div class="section-header">
  <div class="section-num">04</div>
  <div class="section-title-wrap"><h2>Benefits of GitHub Actions for your projects</h2></div>
</div>

<div class="providers-grid">
  <div class="provider-card">
    <div class="provider-name">Automated builds</div>
    <div class="provider-detail">Builds fire automatically whenever changes are pushed, ensuring consistent and up-to-date compiled outputs without manual intervention.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Testing automation</div>
    <div class="provider-detail">Integrate xUnit, NUnit or MSTest via VSTest. Code changes are tested before they can be merged or deployed, reducing the risk of shipping bugs to production.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Coverage reporting</div>
    <div class="provider-detail">Submit coverage reports to SonarCloud, Code Climate, Codefactor, Codecov and others — directly from the pipeline, no manual uploads needed.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Deployment flexibility</div>
    <div class="provider-detail">Deploy to Azure, AWS, on-premises or any target using community actions. The same workflow that builds and tests can also ship to production.</div>
  </div>
  <div class="provider-card">
    <div class="provider-name">Collaboration and transparency</div>
    <div class="provider-detail">Workflow files live alongside the code. Team members can review, comment on, and contribute to the pipeline configuration the same way they do with code.</div>
  </div>
</div>

<div class="divider">· · ·</div>

<div class="references">
  <p class="references-title">References</p>
  <ol class="references-list">
    <li>
      GitHub. <strong>Official GitHub Actions documentation.</strong>
      <a href="https://docs.github.com/en/actions" target="_blank">docs.github.com/en/actions</a>
    </li>
    <li>
      actions/checkout. <strong>GH Action: actions/checkout.</strong>
      <a href="https://github.com/actions/checkout" target="_blank">github.com/actions/checkout</a>
    </li>
    <li>
      Microsoft. <strong>GH Action: microsoft/setup-msbuild.</strong>
      <a href="https://github.com/microsoft/setup-msbuild" target="_blank">github.com/microsoft/setup-msbuild</a>
    </li>
    <li>
      darenm. <strong>GH Action: darenm/Setup-VSTest.</strong>
      <a href="https://github.com/darenm/Setup-VSTest" target="_blank">github.com/darenm/Setup-VSTest</a>
    </li>
    <li>
      NuGet. <strong>GH Action: NuGet/setup-nuget.</strong>
      <a href="https://github.com/NuGet/setup-nuget" target="_blank">github.com/NuGet/setup-nuget</a>
    </li>
  </ol>
</div>
