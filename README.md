# Introduction

This project is for researching Conan2 concepts.

# Getting Started

Just install moon and get going!

# Research branches

- **ptci_deps**: Look into using a Conan generator to set-up a workspace with integrity source content.


# Dev Notes:

In this commit I noted that the toolchain.yml was still also installing conan. So this is removed.

`moon r app1:conanBuild` still fails due to lack of conan profiles