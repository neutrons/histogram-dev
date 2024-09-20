# Histogram
histogram data object

## Installation

### Package Build and Installation Instructions

1. Python wheel

  .. code-block:: shell

    $ python -m build --wheel --no-isolation
    $ check-wheel-contents dist/histogram_*.whl

2. Conda package

  .. code-block:: shell

    # create a conda package
    $ cd conda.recipe
    $ echo "versioningit $(versioningit ../)"
    $ CHANNELS="--channel mcvine --channel conda-forge"
    $ VERSION=$(versioningit ../) conda mambabuild $CHANNELS --output-folder . .
    $ conda verify noarch/histogram-*.tar.bz2
    # install a local conda package
    $ conda install noarch/<histogram.tar.bz2 file>

### Installation Instructions for editable mode

  .. code-block:: shell

    $ pip install -e . --no-deps

* Tests

  In root directory of histogram-dev,type

  .. code-block:: shell

    `pytest`

* [Documentation](http://danse-inelastic.github.io/histogram)

---

[![CI](https://github.com/neutrons/histogram-dev/actions/workflows/actions.yml/badge.svg?branch=next)](https://github.com/neutrons/histogram-dev/actions/workflows/actions.yml)
[![codecov](https://codecov.io/gh/neutrons/histogram-dev/graph/badge.svg?token=Z0Y3B6XEWP)](https://codecov.io/gh/neutrons/histogram-dev)
