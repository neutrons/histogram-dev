#!/usr/bin/env python


skip = True

import unittest

from histogram.ndarray.converters import *


class converters_TestCase(unittest.TestCase):
    @unittest.expectedFailure
    def testStdVectorNdArray2NumpyNdArray(self):
        "histogram.ndarray.converters: StdVectorNdArray2NumpyNdArray"
        from histogram.ndarray.StdVectorNdArray import NdArray

        v = [1, 2, 3]
        a = NdArray("int", v)
        n = a.as_("NumpyNdArray")
        self.assertEqual(n.size(), 3)
        l = n.asList()
        for a, b in zip(l, v):
            self.assertEqual(a, b)
            continue
        self.assertEqual(n.__module__, "histogram.ndarray.NumpyNdArray")

        v = list(range(12))
        a = NdArray("int", v)
        a.setShape((3, 4))
        n = a.as_("NumpyNdArray")
        self.assertEqual(n.size(), 12)
        self.assertEqual(n.shape(), (3, 4))

        l = n.asNumarray().copy()
        l.shape = (-1,)
        for a, b in zip(l, v):
            self.assertEqual(a, b)
            continue
        self.assertEqual(n.__module__, "histogram.ndarray.NumpyNdArray")

        return
    @unittest.expectedFailure
    def testNumpyNdArray2StdVectorNdArray(self):
        "histogram.ndarray.converters: NumpyNdArray2StdVectorNdArray"
        from histogram.ndarray.NumpyNdArray import NdArray

        v = [1, 2, 3]
        a = NdArray("int", v)
        n = a.as_("StdVectorNdArray")
        self.assertEqual(n.size(), 3)
        l = n.asList()
        for a, b in zip(l, v):
            self.assertEqual(a, b)
            continue
        self.assertEqual(n.__module__, "histogram.ndarray.StdVectorNdArray")

        v = list(range(12))
        a = NdArray("int", v)
        a.setShape((3, 4))
        n = a.as_("StdVectorNdArray")
        self.assertEqual(n.size(), 12)
        self.assertEqual(n.shape(), (3, 4))

        l = n.asNumarray().copy()
        l.shape = (-1,)
        for a, b in zip(l, v):
            self.assertEqual(a, b)
            continue
        self.assertEqual(n.__module__, "histogram.ndarray.StdVectorNdArray")

        return

    pass  # end of converters_TestCase


def pysuite():
    suite = unittest.makeSuite(converters_TestCase)
    return unittest.TestSuite([suite])


def main():
    tests = pysuite()
    unittest.TextTestRunner(verbosity=2).run(tests)
    return


if __name__ == "__main__":
    main()
