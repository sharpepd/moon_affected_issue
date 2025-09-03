# Introduction

This project is for researching Conan2 concepts.

# Getting Started

Just install moon and get going!

# Research branches

- **ptci_deps**: Look into using a Conan generator to set-up a workspace with integrity source content.


# Dev Notes:

In this commit we have updated to use the conan toolchain.

Running `moon r app1:conanBuild` fails:

```
▪▪▪▪ app1:conanInstall
python -m dpedo_armstrong.conan jsonw ./build/task-data/conanInstall.conan.json -- install ./conanfile.py --output-folder ./. '-pr:h' ./conan.profile '-pr:b' ./conan.profile '--build=missing' '--conf tools.env.virtualenv:powershell=powershell' (in .\packages\app1)
app1:conanInstall | ERROR: Error reading './conan.profile' profile: Profile not found: windows
▪▪▪▪ app1:conanInstall (2s 775ms)
Error: task_runner::run_failed
```

The .conan folder exists but does not contain the conan config we specified in the toolchain.yml