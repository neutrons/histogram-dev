"""pytest config"""

import pytest

import logging

# Create and configure logger
logging.basicConfig(
    format="%(levelname)s Histogram %(pathname)s:%(lineno)d %(message)s"
)

# Create a logger
logger = logging.getLogger("Histogram")

# Set the logging level
logging_level = logging.DEBUG
logger.setLevel(logging.DEBUG)

print("\n --------------------------------------------")
print(f"      ------ Logger set to {logging.getLevelName(logging_level)} ------")
print(" --------------------------------------------\n")
