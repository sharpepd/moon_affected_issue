# Introduction

This project is for researching Conan2 concepts.

# Getting Started

Just install moon and get going!

# Research branches

- **ptci_deps**: Look into using a Conan generator to set-up a workspace with integrity source content.


# Dev Notes:

# Dev Notes:

In this commit we update the conan tasks to have the conan toolchain specified
This fails the command moon r `app1:conanBuild`

We see the .conan folder now populated with the profiles, but an error occurs 

app1:conanInstall | C:\Users\sharpep\.proto\tools\python\3.11.10\python.exe: Error while finding module specification for 'dpedo_armstrong.conan' (ModuleNotFoundError: No module named 'dpedo_armstrong')
▪▪▪▪ app1:conanInstall (881ms)
▪▪▪▪ app1:conanBuild (skipped)
Error: task_runner::run_failed

  × Task app1:conanInstall failed to run.
  ╰─▶ Process python failed: exit code 1

  The system python has been run without any dependencies. This is presumably because of the wrapper we have on conan to capture the json files.