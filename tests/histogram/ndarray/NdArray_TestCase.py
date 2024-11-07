#!/usr/bin/env python

# NdArray has a fixed interface
# this test test the subclasses of NdArray and see if all methods
# defined in the interface are satisfied.
# In the NdArray module, we have a unittest TestCase base class to test
# all those methods.
# Here we just need to override the setUp method of the TestCase
# base class so that different subclass can be tested.


# from histogram.ndarray.AbstractNdArray import NdArray_TestCase
# from histogram.ndarray.AbstractNdArray import NdArray
import tempfile
import os

# test of interface
import unittest
from unittest import TestCase


class NdArray_TestCase(TestCase):
    def setUp(self):
        from histogram.ndarray.NumpyNdArray import NdArray as NumpyNA
        # overload this to test a special subclass of NdArray
        self.NdArray = NumpyNA
        return

    def testCtor(self):
        """NdArray: ctor"""
        v = self.NdArray("double", [1, 2, 3])
        self.assertEqual(v.asNumarray()[0], 1)
        self.assertEqual(v.asNumarray()[1], 2)
        self.assertEqual(v.datatype(), 6)

        v = self.NdArray("float", 3, 2)
        self.assertEqual(v.asNumarray()[0], 2)
        self.assertEqual(v.size(), 3)
        self.assertEqual(v.datatype(), 5)

        v = self.NdArray("int", 3, 2)
        self.assertEqual(v.asNumarray()[0], 2)
        self.assertEqual(v.size(), 3)
        self.assertEqual(v.datatype(), 24)

        v = self.NdArray("uint", 3, 2)
        self.assertEqual(v.asNumarray()[0], 2)
        self.assertEqual(v.size(), 3)
        self.assertEqual(v.datatype(), 25)

        return

    def test__neg__(self):
        "NdArray: operator '-a'"
        v = self.NdArray("double", [1, 2, 3])
        v2 = -v
        self.assertTrue(v2.compare(self.NdArray("double", [-1, -2, -3])))
        return

    def test__add__(self):
        "NdArray: operator 'a+b'"
        v = self.NdArray("double", [1, 2, 3])
        v2 = v + 1
        self.assertTrue(v2.compare(self.NdArray("double", [2, 3, 4])))

        v2 = 1 + v
        self.assertTrue(v2.compare(self.NdArray("double", [2, 3, 4])))

        v3 = v + self.NdArray("double", [2, 3, 4])
        self.assertTrue(v3.compare(self.NdArray("double", [3, 5, 7])))

        self.assertRaises(NotImplementedError, v.__add__, "a")
        return

    def test__mul__(self):
        "NdArray: operator 'a*b'"
        v = self.NdArray("double", [1, 2, 3])
        v2 = v * 2
        self.assertTrue(v2.compare(self.NdArray("double", [2, 4, 6])))

        v2 = 2 * v
        self.assertTrue(v2.compare(self.NdArray("double", [2, 4, 6])))

        v2 = v * v
        self.assertTrue(v2.compare(self.NdArray("double", [1, 4, 9])))

        return

    def test__sub__(self):
        "NdArray: operator 'a-b'"
        v = self.NdArray("double", [1, 2, 3])
        v2 = v - 2
        self.assertTrue(v2.compare(self.NdArray("double", [-1, 0, 1])))

        v2 = v - v
        self.assertTrue(v2.compare(self.NdArray("double", [0, 0, 0])))
        return

    def test__div__(self):
        "NdArray: operator 'a/b'"
        v = self.NdArray("double", [1, 2, 3])

        v2 = v.copy()
        v2 /= 2
        self.assertTrue(v2.compare(self.NdArray("double", [0.5, 1, 1.5])))

        v2 = v.copy()
        v2 = 1 / v2
        self.assertTrue(v2.compare(self.NdArray("double", [1, 0.5, 1.0 / 3])))

        v2 = v.copy()
        v2 /= v2
        self.assertTrue(v2.compare(self.NdArray("double", [1, 1, 1])))
        
        v = self.NdArray("double", list(range(1,13)))
        v.setShape((3, 4))
 
        v2 = v.copy()
        v2 /=v2
        v2.setShape((12,))
        self.assertTrue(v2.compare(self.NdArray("double", [1] * 12)))

        return

    def test__iadd__(self):
        "NdArray: operator 'a+=b'"
        v = self.NdArray("double", [1, 2, 3])
        v += 1
        self.assertTrue(v.compare(self.NdArray("double", [2, 3, 4])))

        v += self.NdArray("double", [2, 3, 4])
        self.assertTrue(v.compare(self.NdArray("double", [4, 6, 8])))

        print("__iadd__ big array")
        v = self.NdArray("double", 1024000, 2)
        v += self.NdArray("double", 1024000, 1)
        self.assertTrue(v.compare(self.NdArray("double", 1024000, 3)))

        self.assertRaises(NotImplementedError, v.__iadd__, "a")
        return

    def test__isub__(self):
        "NdArray: operator 'a-=b'"
        v = self.NdArray("double", [1, 2, 3])
        v -= 1
        self.assertTrue(v.compare(self.NdArray("double", [0, 1, 2])))

        v -= self.NdArray("double", [2, 3, 4])
        self.assertTrue(v.compare(self.NdArray("double", [-2, -2, -2])))

        self.assertRaises(NotImplementedError, v.__isub__, "a")
        return

    def test__imul__(self):
        "NdArray: operator 'a*=b'"
        v = self.NdArray("double", [1, 2, 3])
        v *= 2
        self.assertTrue(v.compare(self.NdArray("double", [2, 4, 6])))

        v *= self.NdArray("double", [2, 3, 4])
        self.assertTrue(v.compare(self.NdArray("double", [4, 12, 24])))

        self.assertRaises(NotImplementedError, v.__imul__, "a")
        return

    def test__idiv__(self):
        "NdArray: operator 'a/=b'"
        v = self.NdArray("double", [1, 2, 3])
        v /= 2
        self.assertTrue(v.compare(self.NdArray("double", [0.5, 1, 1.5])))

        v /= self.NdArray("double", [0.5, 1, 1.5])
        self.assertTrue(v.compare(self.NdArray("double", [1, 1, 1])))

        self.assertRaises(NotImplementedError, v.__idiv__, "a")
        return

    def testReverse(self):
        "NdArray: array  -> 1./array"
        v = self.NdArray("double", [1, 2, 3])
        v.reverse()
        self.assertTrue(v.compare(self.NdArray("double", [1, 1.0 / 2, 1.0 / 3])))
        return

    def testTranspose(self):
        "NdArray: transpose"
        v = self.NdArray("double", list(range(6)))
        v.setShape((2, 3))
        vt = v.transpose()
        self.assertEqual(vt.shape(), (3, 2))
        self.assertEqual(vt[0, 0], 0)
        self.assertEqual(vt[0, 1], 3)
        self.assertEqual(vt[1, 0], 1)
        self.assertEqual(vt[1, 1], 4)
        self.assertEqual(vt[2, 0], 2)
        self.assertEqual(vt[2, 1], 5)
        return

    def test__getitem__(self):
        "NdArray: operator 'a[3:5], a[3]'"
        v = self.NdArray("double", list(range(12)))
        self.assertTrue(v[3:5].compare(self.NdArray("double", [3, 4])))
        self.assertAlmostEqual(v[3], 3)

        v.setShape((3, 4))
        subarr = v[1:2, 1:2]
        expected = self.NdArray("double", [5])
        expected.setShape((1, 1))
        self.assertTrue(subarr.compare(expected))
        return

    def test__setitem__(self):
        "NdArray: operator 'a[3]=4'"
        v = self.NdArray("double", list(range(12)))
        v[3:5] = [1, 2]
        self.assertTrue(v[3:5].compare(self.NdArray("double", [1, 2])))

        v[10] = 11
        self.assertAlmostEqual(v[10], 11)

        v[3:5] = 0
        self.assertTrue(v[3:5].compare(self.NdArray("double", [0, 0])))
        return

    def testCopy(self):
        "NdArray: method 'copy'"
        v = self.NdArray("double", list(range(12)))
        self.assertTrue(v.compare(v.copy()))
        return

    def testCastCopy(self):
        "NdArray: method 'castCopy'"
        v = self.NdArray("double", list(range(12)))
        v2 = self.NdArray("int", list(range(12)))
        self.assertTrue(v2.compare(v.castCopy("int")))
        return

    def testIntegrate(self):
        "NdArray: integrate"
        v = self.NdArray("double", list(range(3)))
        r = v.integrate(0, 2, 0.1)
        self.assertAlmostEqual(r, 0.1)
        return

    def testSquare(self):
        "NdArray: square"
        v = self.NdArray("double", list(range(3)))
        r = v.square()
        self.assertTrue(v.compare(self.NdArray("double", [0, 1, 4])))
        return

    def testSqrt(self):
        "NdArray: sqrt"
        v = self.NdArray("double", [1, 4, 9])
        v.sqrt()
        self.assertTrue(v.compare(self.NdArray("double", [1, 2, 3])))
        return

    def testSum(self):
        "NdArray: sum"
        v = self.NdArray("double", list(range(3)))
        r = v.sum()
        self.assertAlmostEqual(r, 3)

        v = self.NdArray("double", list(range(9)))
        v.setShape((3, 3))
        r = v.sum()
        self.assertAlmostEqual(r, 36)
        r1 = v.sum(axis=0)
        expected_r1 = self.NdArray("double", [9, 12, 15])
        self.assertTrue(r1.compare(expected_r1))
        return

    def testAssign(self):
        "NdArray: assign"
        v = self.NdArray("double", list(range(3)))
        v.assign(5, 1.0)
        self.assertTrue(v.compare(self.NdArray("double", [1, 1, 1, 1, 1])))
        return

    def testAsList(self):
        "NdArray: asList"
        v = self.NdArray("double", list(range(3)))
        l = v.asList()
        self.assertTrue(v.compare(self.NdArray("double", l)))
        return

    def testAsNumarray(self):
        "NdArray: asNumarray"
        v = self.NdArray("double", list(range(3)))
        na = v.asNumarray()
        import numpy

        self.assertTrue(isinstance(na, numpy.ndarray))
        self.assertTrue(v.compare(self.NdArray("double", list(na))))

        v = self.NdArray("double", list(range(12)))
        v.setShape((3, 4))
        na = v.asNumarray()
        shape = na.shape
        self.assertEqual(shape[0], 3)
        self.assertEqual(shape[1], 4)
        return

    def test_dump(self):
        "NdArray: pickle.dump"
        import pickle

        v = self.NdArray("double", [1, 2, 3, 4])
        v.setShape((2, 2))
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "tmp.pkl"), "wb") as f:
                            pickle.dump(v, f)
        return

    def test_load(self):
        "NdArray: pickle.load"
        import pickle

        v = self.NdArray("double", [1, 2, 3, 4])
        v.setShape((2, 2))
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "tmp.pkl"), "wb") as f:
                pickle.dump(v, f)
            with open(os.path.join(temp_dir, "tmp.pkl"), "rb") as f:    
                v1 = pickle.load(f)
                print(v1.asNumarray())
                assert v1.compare(v)
        return

    def test_setShape(self):
        "NdArray: setShape"
        v = self.NdArray("double", list(range(12)))
        v.setShape((3, 4))

        self.assertRaises(ValueError, v.setShape, (4, 4))
        return

    pass  # end of NdArray_TestCase


# from . import converters
def pysuite():
    suite1 = unittest.makeSuite(NdArray_TestCase)
    return unittest.TestSuite((suite1,))


if __name__ == "__main__":
    unittest.main()





# def createTestCase(klass):
#     class TC(NdArray_TestCase):
#         def setUp(self):
#             self.NdArray = klass
#             return

#         pass  # end of TC

#     return TC


# def pysuite():
#     from histogram.ndarray.NumpyNdArray import NdArray as NumpyNA

#     klasses = [NumpyNA]
#     testcases = [createTestCase(klass) for klass in klasses]
#     suites = [unittest.makeSuite(tc) for tc in testcases]
#     return unittest.TestSuite(suites)


# def main():
#     pytests = pysuite()
#     alltests = unittest.TestSuite((pytests,))
#     unittest.TextTestRunner(verbosity=2).run(alltests)
#     return

# if __name__ == "__main__":
#     main()
