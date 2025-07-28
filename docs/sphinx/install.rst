.. _install:

Installation
============

The histogram package can be installed:

    1. from the source code:

        1. Install [Pixi](https://pixi.sh/) for managing environments, dependencies, packaging, and task execution. (if it is not already installed).

        Pixi installation e.g. for Linux:

        ```bash

        curl -fsSL https://pixi.sh/install.sh | sh

        ```
        Also install git, if it is missing.

        2. Go to a location where you would like to install the program (e.g., $HOME/software), run:


            `git clone https://github.com/neutrons/histogram-dev.git`

        3. Setup/Update the environment

        ```bash
        pixi install
        ```

        or to enter the environment

        ```bash
        pixi shell

        ```
    2. as a conda package: https://anaconda.org/neutrons/histogram


 To test, in the root directory type:

 pytest

:ref:`More details <install-details>`
