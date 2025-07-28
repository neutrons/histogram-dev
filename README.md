# Histogram
histogram data object

## Installation

1. Install [Pixi](https://pixi.sh/) for managing environments, dependencies, packaging, and task execution. (if it is not already installed).

   Pixi installation e.g. for Linux:

   ```bash

   curl -fsSL https://pixi.sh/install.sh | sh

   ```
   Also install git, if it is missing.

2. Go to a location where you would like to install histogram, run:

   ```bash
   git clone https://github.com/neutrons/histogram-dev.git

   ```

3. Setup-activate and enter the environment

    ```bash
    pixi shell
    ```

The histogram environment is activated and the application is ready to use.


## For Contributors


* Pixi additional Information

  Any change to pyproject.toml, e.g. new dependencies, requires updating the pixi.lock file and including it in the commit.

  ```bash

  pixi.lock

  ```

  to install/update the enrivornment

    ```bash
    pixi install

    ```

* Tests

  In root directory of histogram-dev,type

    ```bash
    pytest

    ```
* [Documentation](https://histogram-dev.readthedocs.io/en/latest/)

---

[![CI](https://github.com/neutrons/histogram-dev/actions/workflows/test_and_deploy.yml/badge.svg?branch=next)](https://github.com/neutrons/histogram-dev/actions/workflows/test_and_deploy.yml)
[![codecov](https://codecov.io/gh/neutrons/histogram-dev/graph/badge.svg?token=Z0Y3B6XEWP)](https://codecov.io/gh/neutrons/histogram-dev)
