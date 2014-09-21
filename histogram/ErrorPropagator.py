#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                         (C) 2007 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from math import sqrt


class ErrorPropagator:

    def inverse(self, this):
        this._error2 /= this._value ** 4
        this._value = 1./this._value
        return this


    def __neg__(self, this):
        this._value *= -1
        return this
    

    def __iadd__(self, this, other ):
        this._value += other._value
        if other._error2 is None and this._error2 is None: return this
        this._error2 = this._error2 or 0
        if other._error2 is not None: this._error2 += other._error2
        return this


    def __isub__(self, this, other):
        this._value -= other._value
        if other._error2 is None and this._error2 is None: return this
        this._error2 = this._error2 or 0
        if other._error2 is not None: this._error2 += other._error2
        return this


    def __imul__(self, this, other):
        x, dx2 = this._value, this._error2
        
        this._value *= other._value
        if other._error2 is None and this._error2 is None: return this

        if other._error2 is None:
            this._error2 *= other._value ** 2
            return this

        if this._error2 is None:
            this._error2 = other._error2 * this._value ** 2
            return this
        
        y,  dy2 = other._value, other._error2
        dy = sqrt(dy2)
        
        #(xdy+ydx)^2
        dx = sqrt(dx2)

        dx *= y
        dx += dy * x
        dx **= 2
            
        this._error2 = dx
        return this


    def __idiv__(self, this, other):
        y,  dy2 = other._value, other._error2
        this._value /= y

        if dy2 is None and this._error2 is None: return this
        
        if dy2 is None or dy2 == 0 or dy2 == 0.0: #special case
            #ydx/y^2
            this._error2 /= y*y
            return this

        x,  dx2 = this._value, this._error2
        if dx2 is None or dx2 == 0 or dx2 == 0.:
            this._error2 = dy2 * (x/y/y) ** 2
            return this

        dy = sqrt(dy2)
        dx = sqrt(dx2);
        dx *= y
        dx += x * dy
        dx /= y*y
        dx **= 2

        this._error2 = dx
        return this
        
    
    def __add__(self, this, other):
        r = this.copy()
        r += other
        return r
        

    __radd__ = __add__


    def __sub__(self, this, other):
        r = this.copy()
        r -= other
        return r


    def __rsub__(self, this, other):
        r = this.copy()
        r *= (-1,0)
        r += other
        return r


    def __mul__(self, this, other):
        r = this.copy()
        r *= other
        return r


    __rmul__ = __mul__
        
                
    def __div__(self, this, other):
        r = this.copy()
        r /= other
        return r


    def __rdiv__(self, this, other):
        r = this.copy()
        r.inverse()
        r *= other
        return r
            
        
    pass # end of ErrorPropagator

# version
__id__ = "$Id$"

# End of file
