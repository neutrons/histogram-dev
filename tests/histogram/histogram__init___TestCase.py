#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from histogram import *

import unittest

from unittestX import TestCase


class Histogram_TestCase(TestCase):
    def test_axis(self):
        "Histogram.__init__: axis"
        q = axis("q", arange(0.0, 13.0, 0.1), "angstrom**(-1)")
        detID = axis("detID", list(range(10)))
        detID = axis("detID", [0])
        return

    def test_paxis(self):
        "Histogram.__init__: paxis"
        q = axis("q", arange(0.0, 13.0, 0.1), "angstrom**(-1)")
        q = axis("q", [1.0, 2.0, 4.0, 6.0], "angstrom**(-1)")
        self.assertEqual(q.cellIndexFromValue(1.1), 0)
        self.assertEqual(q.cellIndexFromValue(1.9), 1)
        self.assertEqual(q.cellIndexFromValue(2.1), 1)
        self.assertEqual(q.cellIndexFromValue(3.9), 2)
        self.assertEqual(q.cellIndexFromValue(4.1), 2)
        self.assertEqual(q.cellIndexFromValue(5.9), 3)
        self.assertEqual(q.cellIndexFromValue(6.1), 3)
        return

    def test_histogram1(self):
        """Histogram.__init__: histogram factory method, axes are specified using
        instances of Axis"""
        detIDaxis = axis("detID", list(range(10)))
        pixIDaxis = axis("pixID", list(range(8)))
        axes = [detIDaxis, pixIDaxis]

        from numpy import fromfunction

        def f(i, j):
            return i + j

        data = fromfunction(f, (detIDaxis.size(), pixIDaxis.size()))
        errs = data**2

        h = histogram("h", axes, data, errs)
        detID, pixID = 3, 5
        self.assertVectorAlmostEqual(
            h[detID, pixID], (f(detID, pixID), f(detID, pixID) ** 2)
        )
        return

    def test_histogram1a(self):
        """Histogram.__init__: histogram factory method, keyword 'fromfunction'"""

        def f(x):
            return x * x

        h = histogram("h", [("x", list(range(10)))], fromfunction=f)

        def g(x):
            return x

        h = histogram("h", [("x", list(range(10)))], fromfunction=(f, g))
        return

    def test_histogram1b(self):
        """Histogram.__init__: histogram factory method, keyword 'fromfunction'. 3D"""
        h = histogram(
            "h",
            [
                ("x", list(range(2))),
                ("y", list(range(2, 4))),
                ("z", list(range(4, 6))),
            ],
            fromfunction=lambda x, y, z: x + y + z,
        )

        return

    def test_histogram1c(self):
        """Histogram.__init__: histogram factory method, keyword 'fromfunction'. math.sin"""
        import math

        h = histogram(
            "h",
            [
                ("x", arange(0, 3.0, 0.1)),
            ],
            fromfunction=math.sin,
        )

        h = histogram(
            "h",
            [
                ("x", arange(0, 3.0, 0.1)),
                ("y", arange(0, 3.0, 0.1)),
            ],
            fromfunction=lambda x, y: math.sin(x + y),
        )
        return

    def test_histogram2(self):
        """Histogram.__init__: datasetFromFunction"""
        qaxis = axis("q", arange(0, 13, 0.1), "angstrom**(-1)")
        eaxis = axis("e", arange(-50, 50, 1.0), "meV")
        axes = (qaxis, eaxis)

        def f1(q, e):
            return q**2 + e**2

        data = datasetFromFunction(f1, (qaxis, eaxis))
        errs = data**2
        h = histogram("h", axes, data, errs)

        q = 6.0
        e = 10.0
        self.assertVectorAlmostEqual(h[q, e], (f1(q, e), f1(q, e) ** 2))
        return

    def _test_histogram3a(self):
        """Histogram.__init__: histogram of non-float datatype"""
        detaxis = axis("detectorID", list(range(10)))
        pixaxis = axis("pixelID", list(range(10)))
        mask = histogram("mask", (detaxis, pixaxis), data_type="char")

        from numpy import ones

        data = createDataset(
            "data", shape=(10, 10), data=ones((10, 10), int), data_type="int"
        )
        counts = histogram("counts", (detaxis, pixaxis), data=data, errors=None)

        counts1 = histogram(
            "counts",
            (detaxis, pixaxis),
            data=ones((10, 10), int),
            errors=ones((10, 10), int),
            data_type="double",
        )
        self.assertEqual(counts1.errors().name(), "errors")
        return

    def test_histogram3(self):
        """Histogram.__init__: histogram factory method, axes are specified
        using a list of (name, values)"""
        detIDaxis = "detID", list(range(100))
        tofAxis = "tof", arange(1000, 5000, 1.0), "microsecond"

        shape = len(detIDaxis[1]), len(tofAxis[1])

        from numpy import zeros

        h = histogram("h", (detIDaxis, tofAxis), zeros(shape, "d"), zeros(shape, "d"))

        self.assertVectorAlmostEqual(h[30, 3000.0], (0, 0))
        return

    def test_histogram4(self):
        """Histogram.__init__: histogram factory method, axes are specified
        using a list of (name, values). data and errors are unspecified"""
        detIDaxis = "detID", list(range(100))
        tofAxis = "tof", arange(1000, 5000, 1.0), "microsecond"

        shape = len(detIDaxis[1]), len(tofAxis[1])

        h = histogram("h", (detIDaxis, tofAxis))

        self.assertVectorAlmostEqual(h[30, 3000.0], (0, 0))
        return

    def test_histogram5(self):
        """Histogram.__init__: unit"""
        h = histogram(
            "h",
            [
                ("x", [1, 2, 3]),
            ],
            unit="meter",
        )
        return

    def test_histogram6(self):
        """Histogram.__init__: errors = None"""
        h = histogram(
            "h",
            [
                ("x", [1, 2, 3]),
            ],
            unit="meter",
            data=[1, 2, 3],
        )
        self.assertVectorAlmostEqual(h.errors().storage().asNumarray(), [0, 0, 0])
        return

    def test_getSliceCopyFromHistogram(self):
        """Histogram.__init__: getSliceCopyFromHistogram"""
        h = histogram(
            "h",
            [
                ("x", [1, 2, 3]),
                ("y", [0.1, 0.2, 0.3]),
                ("z", list(range(0, 1000, 100))),
            ],
            unit="meter",
        )
        xaxis = axis("x", [1, 2])
        yaxis = axis("y", [0.2, 0.3])
        s = getSliceCopyFromHistogram("s", [xaxis, yaxis], h)
        self.assertVectorEqual(s.shape(), (2, 2, 10))
        return

    def test_meshgrid(self):
        """Histogram.__init__: meshgrid"""
        x, y, z = [1, 2], [3, 4, 5], [6, 7, 8, 9]
        m = meshgrid(x, y, z)
        self.assertTrue(isinstance(m, list))
        X, Y, Z = m

        from numpy import array

        X1 = array(x * len(y) * len(z))
        X1.shape = len(y), len(z), len(x)
        X1 = X1.transpose(2, 1, 0)
        X1 = X1.flatten()
        X1.shape = len(x), len(y), len(z)
        self.assertTrue((X == X1).all())

        X = meshgrid([x])
        self.assertTrue(isinstance(X, list))
        x = X[0]
        self.assertTrue("numpy" in x.__class__.__module__)
        return

    def test_boundariesFromCenters(self):
        "histogram.__init__: boundariesFromCenters"
        c = [1.0, 2.0, 3.0, 4.0]
        bb = boundariesFromCenters(c)
        self.assertVectorAlmostEqual(bb, [0.5, 1.5, 2.5, 3.5, 4.5])

        c = [1, 2, 4, 5]
        bb = boundariesFromCenters(c)
        self.assertVectorAlmostEqual(bb, [0.5, 1.5, 3, 4.5, 5.5])

        c = [1, 1, 2, 4]
        self.assertRaises(BinsOverlapped, boundariesFromCenters, c)
        return

    def test_calcBinBoundaries(self):
        "histogram.__init__:  calcBinBoundaries"
        bb = calcBinBoundaries(1.0, 1.0, 10)
        self.assertVectorAlmostEqual(bb, [0.5 + 1.0 * i for i in range(11)])
        return

    def test_createContiuousAxis(self):
        "histogram.__init__:  createContinuousAxis"
        name = "energy"
        unit = "meV"
        min, delta, nBins = 10.0, 1.0, 70
        max = min + nBins * delta
        axis = createContinuousAxis(name, unit, arange(min, max, delta))

        self.assertTrue(axis.name() == name)
        self.assertTrue(axis.unit() == unitFromString(unit))

        bb = axis.binBoundaries().asList()
        self.assertVectorAlmostEqual(
            bb, [min - delta / 2.0 + i * delta for i in range(nBins + 1)]
        )
        return

    def test_createDiscreteAxis(self):
        "histogram.__init__:  createDiscreteAxis"
        name = "detectorID"
        items = [1, 3, 8, 10]
        axis = createDiscreteAxis(name, items, "int")

        self.assertTrue(axis.name() == name)

        bb = axis.binBoundaries().asList()
        bc = axis.binCenters()
        self.assertVectorEqual(bc, items)
        self.assertEqual(len(bb), len(items) + 1)
        return

    def test_createDataset(self):
        "histogram.__init__:  createDataset"
        name = "intensity"
        unit = "1"
        shape = [100, 200]
        types = ["double", "float", "int", "unsigned"]
        for datatype in types:
            try:
                ds = createDataset(name, unit, shape=shape, data_type=datatype)
            except:
                raise RuntimeError(datatype)
            self.assertEqual(name, ds.name())
            self.assertEqual(1, ds.unit())
            self.assertVectorEqual(shape, ds.shape())
            self.assertEqual(ds.typecodeAsC(), datatype)
            continue

        from histogram.ndarray.NumpyNdArray import NdArray

        storage = NdArray("float", 20000, 0)
        storage.setShape(shape)
        ds2 = createDataset(name, unit, storage=storage)
        self.assertEqual(name, ds2.name())
        self.assertEqual(1, ds2.unit())
        self.assertVectorEqual(shape, ds2.shape())
        self.assertEqual(ds2.typecodeAsC(), "float")
        return

    def test_makeHistogram(self):
        "histogram.__init__:  makeHistogram"
        name = "I(det,tof)"
        det = ("det", list(range(10)))
        from numpy import arange, ones

        tof = ("tof", arange(1000.0, 1020.0, 1.0))
        axes = [det, tof]
        data = ones((10, 20))
        errs = ones((10, 20))
        hist = makeHistogram(name, axes, data, errs)
        self.assertEqual(name, hist.name())
        return

    def test_plot(self):
        h = histogram(
            "h",
            [
                ("x", [1, 2, 3]),
            ],
            unit="meter",
            data=[1, 2, 3],
        )
        plot(h, output="Ix.png")
        return

    pass  # end of Histogram_TestCase


def pysuite():
    suite1 = unittest.makeSuite(Histogram_TestCase)
    return unittest.TestSuite((suite1,))


def main():
    pytests = pysuite()
    alltests = unittest.TestSuite((pytests,))
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == "__main__":
    main()


# version
__id__ = "$Id: Histogram_TestCase.py 1124 2006-09-05 23:08:19Z linjiao $"

# End of file
