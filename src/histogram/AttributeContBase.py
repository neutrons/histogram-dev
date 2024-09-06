#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved

msg = "{0!s} must override {1!s}"


class AttributeContBase(object):
    """attribute container interface"""

    def getAttribute(self, name):
        """getAttribute( name) -> value"""
        raise NotImplementedError(msg.format(self.__class__.__name__, "getAttribute"))

    def listAttributes(self):
        """listAttributes() -> [names of attributes]"""
        raise NotImplementedError(msg.format(self.__class__.__name__, "listAttributes"))

    def setAttribute(self, name, value):
        """setAttribute( name, value) -> None"""
        raise NotImplementedError(msg.format(self.__class__.__name__, "setAttribute"))


# version
__id__ = "$Id$"

# End of file
