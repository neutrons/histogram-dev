#!/usr/bin/env python
# Jiao Lin Copyright (c) 2005 All rights reserved


class AxisMapper:
    """
    map a value in an Axis to a index
    """

    def __call__(self, value):
        """
        @return: index of the given value in the axis
        @rtype: int
        """
        raise NotImplementedError(
            "{0!s} must override __call__".format(self.__class__.__name__)
        )

    def identify(self, visitor):
        raise NotImplementedError(
            "{0!s} must override identify".format(self.__class__.__name__)
        )

    pass  # end of AxisMapper
