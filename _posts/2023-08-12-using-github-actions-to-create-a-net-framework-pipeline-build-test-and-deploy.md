---
layout: post
title: "Using GitHub Actions to create a .NET Framework pipeline. Build, test, and deploy!"
description: "In this article, we gonna cover the CI/CD process of a .NET Framework project using GitHub Actions to build, test, and run. What are GitHub Actions? GitHub Actions provides a flexible way to automate..."
date: 2023-08-12
categories: [Coding, DevOps, Testing]
tags: [net, net-framework, actions, build, cd, ci, code, coverage, deploy, gh, gh-actions, github, pipeline, test, workflows, yaml, yml]
reading_time: 5
---

In this article, we gonna cover the CI/CD process of a .NET Framework project using GitHub Actions to build, test, and run.

What are GitHub Actions?  
GitHub Actions provides a flexible way to automate various tasks directly from your GitHub repositories, such as building, testing, and deploying applications. These actions are defined in YAML files as workflows and can be customized to suit your project's specific requirements.

For reference, I have set up a repository in GitHub with a PoC (Proof of Concept) based on this tutorial. This repository has many more features than the simple ones I will guide you through this tutorial.

[![POC GH Actions CI .NET Framework](https://github-readme-stats-guibranco.vercel.app/api/pin/?username=GuilhermeStracini&repo=POC-GHActions-CI-NetFramework&show_owner=false&show_forks=true&show_issues=true)](https://github.com/GuilhermeStracini/POC-GHActions-CI-NetFramework)

---

Creating a GitHub Actions Pipeline for .NET Framework Projects:

1. Open your repository on GitHub and click on the "Actions" tab.

2. GitHub provides numerous workflow templates for different programming languages and frameworks. To set up a workflow yourself, click on the **Set up a workflow yourself** link above the **Choose a workflow**section.

3. In the GitHub Actions editor, let's name this workflow and set up the triggers that will fire this workflow run.

```yaml
name: Build .NET Framework

on:
  push:
  workflow_dispatch:
```

In the first line, we defined the workflow name to: **Build .NET Framework**

In the next lines, the workflow triggers, push events, and workflow\_dispatch were defined.  
The **push** event will trigger this workflow whenever a new push is done to this repository.  
The **workflow\_dispatch**allows us to run the workflow manually from the **Actions**page.  
You can find a complete reference of all events that trigger a workflow run here: [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows "Events that trigger workflows").

4. Now, we need to define our job to build the solution. But for it, we need some steps like:

- Inform GitHub Actions runner to run this workflow in a Windows-based environment.
- Checkout the code.
- Setup MSBuild as the build tool.
- Setup NuGet tool to restore packages.
- Setup VSTest as the test tool.
- Restore the NuGet packages.
- Build the solution.
- Run the test project.
- (Optionally) Run the fresh build executable (assuming that it is a **.exe** project).

So let's do that, let's first create a job and set up a Windows-based environment:

```yaml
jobs:
  build:
    name: Build
    runs-on: windows-latest
```

In these four lines, we did:

- Informed GH Actiosn that we will start out the **jobs** section
- Create our first job named **build**(it could be anything)
- Give a name to the job (for logging purposes)
- Selected which environment we want to run this job (environments are job-based, so different jobs can run in different environments)

Now we need to configure the job`s steps as we mentioned before

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

  - name: Setup Nuget
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

In the code below, we have 8 steps that will do all the required actions to set up the environment, restore NuGet packages, build, test, and finally run the application.

- In both steps (**restore NuGet Packages** and **build release**), replace **your-solution-name.sln** with the path/name of your solution.
- In the Test step, replace **path-to-test-binary.dll** with the path where the tests project dll is present after a successfully built release run. Usually, this is inside the bin/Release/ directory with the tests project directory.
- In the **path-to-application-binary.exe,** replace the /bin/Release/ directory with the file name of your solution's leading project.

5. Save and Trigger the Workflow: Once you've customized the workflow according to your project's requirements, save the changes and trigger the workflow manually or automatically on specific events, such as pushes to the repository or pull requests.

6. Monitor the Pipeline: GitHub Actions provides a comprehensive view of the pipeline's execution. You can track progress, view logs, and debug potential issues directly from the Actions tab in your repository.

Here we have the full workflow file to build, test and run a .NET Framework solution within GitHub Actions:

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

    - name: Setup Nuget
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

---

Benefits of GitHub Actions for your projects:  
By leveraging GitHub Actions to create a pipeline for your projects, developers can enjoy several benefits, including:

1. Automated Builds: GitHub Actions enables automatic build execution whenever changes are pushed to the repository, ensuring consistent and up-to-date builds.

2. Testing Automation: Integrate automated testing into your pipeline using tools like xUnit or NUnit. This ensures that code changes are thoroughly tested before deployment, reducing the risk of introducing bugs into production.

3. Submit coverage reports to Sonar Cloud, Code Climate, Codefactor, Codecov, etc

4. Deployment Flexibility: GitHub Actions provides a range of deployment options, allowing you to seamlessly deploy your .NET Framework projects to various hosting environments, such as Azure, AWS, or on-premises servers.

5. Collaboration and Transparency: With GitHub Actions, all pipeline workflows are visible to the development team, promoting collaboration and transparency. Team members can review, provide feedback, and contribute to the pipeline configuration.

References:

- [Official GitHub Actions documentation](https://docs.github.com/en/actions)
- [GH Action: actions/checkout](https://github.com/actions/checkout)
- [GH Action: Microsoft/setup-msbuild](https://github.com/microsoft/setup-msbuild)
- [GH Action: darenm/Setup-VSTest](https://github.com/darenm/Setup-VSTest)
- [GH Action: NuGet/setup-nuget](https://github.com/NuGet/setup-nuget)