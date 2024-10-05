<p align="center">
    <a href="https://github.com/YisusChrist/xdg-ninja-report/issues">
        <img src="https://img.shields.io/github/issues/YisusChrist/xdg-ninja-report?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/xdg-ninja-report/forks">
        <img src="https://img.shields.io/github/forks/YisusChrist/xdg-ninja-report?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/xdg-ninja-report/stargazers">
        <img src="https://img.shields.io/github/stars/YisusChrist/xdg-ninja-report?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/xdg-ninja-report/actions">
        <img alt="Tests Passing" src="https://github.com/YisusChrist/xdg-ninja-report/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/xdg-ninja-report/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/YisusChrist/xdg-ninja-report?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/GPL-3.0">
        <img alt="License" src="https://img.shields.io/github/license/YisusChrist/xdg-ninja-report?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/YisusChrist/xdg-ninja-report/issues/new?assignees=YisusChrist&labels=bug&projects=&template=bug_report.yml">Report Bug</a>
    ·
    <a href="https://github.com/YisusChrist/xdg-ninja-report/issues/new?assignees=YisusChrist&labels=feature&projects=&template=feature_request.yml">Request Feature</a>
    ·
    <a href="https://github.com/YisusChrist/xdg-ninja-report/issues/new?assignees=YisusChrist&labels=question&projects=&template=question.yml">Ask Question</a>
    ·
    <a href="https://github.com/YisusChrist/xdg-ninja-report/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/c112f5dae70d838ec44c2f28807f54075afb16f4.svg "Repobeats analytics image")

<br>

`xdg-ninja-report` is a Python library that allows you to easily find the dotfiles that are not `XDG Base Directory Specification` compliant and are not recognized by [xdg-ninja](https://github.com/b3nj5m1n/xdg-ninja). This library is designed to be used in the terminal and is compatible with all operating systems that support Python. The aim of this tool is to help users submit new custom configurations to the [xdg-ninja](https://github.com/b3nj5m1n/xdg-ninja) project database.

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [Manual installation](#manual-installation)
  - [Uninstall](#uninstall)
- [Usage](#usage)
  - [Example of execution](#example-of-execution)
- [Contributors](#contributors)
  - [How do I contribute to xdg-ninja-report?](#how-do-i-contribute-to-xdg-ninja-report)
- [License](#license)

</details>

# Requirements

Here's a breakdown of the packages needed and their versions:

- [poetry](https://pypi.org/project/poetry) >= 1.7.1 (_only for manual installation_)
- [core-helpers](https://github.com/YisusChrist/core_helpers)
- [rich](https://pypi.org/project/rich) >= 13.7.1
- [string-grab](https://pypi.org/project/string-grab) >= 1.3.0

> [!NOTE]
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

# Installation

## From PyPI

`xdg-ninja-report` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install xdg-ninja-report
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `xdg-ninja-report` would be:
>
> ```bash
> pipx install xdg-ninja-report
> ```

## Manual installation

If you prefer to install the program manually, follow these steps:

> [!WARNING]
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [xdg-ninja-report](https://github.com/YisusChrist/xdg-ninja-report) from this repository:

   ```sh
   git clone https://github.com/YisusChrist/xdg-ninja-report
   cd xdg-ninja-report
   ```

2. Install the package:

   ```sh
   poetry install --only main
   ```

## Uninstall

If you installed it from PyPI, you can use the following command:

```bash
pipx uninstall xdg-ninja-report
```

# Usage

> [!TIP]
> For more information about the usage of the program, run `xdg_ninja_report --help` or `xdg_ninja_report -h`.

![options](https://github.com/user-attachments/assets/af5cf138-f450-41fa-8189-f6b328facfb9)

## Example of execution

<img width="563" alt="Screenshot 2024-09-08 010616" src="https://github.com/user-attachments/assets/f57b13c5-e479-4f98-b58d-40ffa88c9ec2">

# Contributors

<a href="https://github.com/YisusChrist/xdg-ninja-report/graphs/contributors"><img src="https://contrib.rocks/image?repo=YisusChrist/xdg-ninja-report" /></a>

## How do I contribute to xdg-ninja-report?

Before you participate in our delightful community, please read the [code of conduct](https://github.com/YisusChrist/.github/blob/main/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/YisusChrist/xdg-ninja-report/issues) and help where you can.

See [Contributing Guidelines](https://github.com/YisusChrist/.github/blob/main/CONTRIBUTING.md) for more details.

# License

`xdg-ninja-report` is released under the [GPL-3.0 License](https://opensource.org/license/GPL-3.0).
