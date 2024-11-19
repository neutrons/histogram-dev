import logging

logger = logging.getLogger("Histogram")


def compareFPLists(a, b, tol):
    if len(a) != len(b):
        logger.info("array size is different: {0!s} != {1!s}".format(len(a), len(b)))
        return False

    ret = True

    for a1, b1 in zip(a, b):
        if abs(a1 - b1) > tol:
            logger.info("{0!s}!={1!s}".format(a1, b1))
            ret = False
        continue

    return ret
