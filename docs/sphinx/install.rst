.. _install:

Installation
============

The histogram package can be installed with 2 ways:

* from the source code:

    1. Install `Pixi <https://pixi.sh/>`_ for managing environments, dependencies, packaging, and task execution. (if it is not already installed).

        Pixi installation e.g. for Linux:

        .. code:: shell

            $ curl -fsSL https://pixi.sh/install.sh | sh


        Also install git, if it is missing.

        .. code:: shell

            $ sudo apt update # for updating the package list
            $ sudo apt install git


    2. Go to a location where you would like to install the program, run:

        .. code:: shell

            $ git clone https://github.com/neutrons/histogram-dev.git

    3. Setup and enter the environment

        .. code:: shell

            $ pixi shell

* as a conda package: `Histogram Package Installation Instructions <https://anaconda.org/neutrons/histogram>`_


 To test, in the root directory type:

 pytest

:ref:`Additional details <install-details>`
