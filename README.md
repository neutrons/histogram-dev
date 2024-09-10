# Histogram
histogram data object

## Installation

### Package Build and Installation Instructions

1. Python wheel

  .. code-block:: shell

    $ python -m build --wheel --no-isolation
    $ check-wheel-contents dist/drtsans-*.whl

2. Conda package

  .. code-block:: shell

    # create a conda package
    $ cd conda.recipe
    $ echo "versioningit $(versioningit ../)"
    $ CHANNELS="--channel mantid/label/main --channel conda-forge"
    $ VERSION=$(versioningit ../) conda mambabuild $CHANNELS --output-folder . .
    $ conda verify noarch/drtsans-*.tar.bz2
    # install a local conda package
    $ conda install noarch/<drtsans .tar.bz2 file>

### Installation Instructions for editable mode

  .. code-block:: shell

    $ pip install -e . --no-deps

* Tests

  In root directory of histogram-dev,type

  .. code-block:: shell
  
    `pytest`


* [Documentation](http://danse-inelastic.github.io/histogram)
