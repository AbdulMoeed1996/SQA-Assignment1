import unittest
import testcode2


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(testcode2.add(10, 5), 15)
        self.assertEqual(testcode2.add(-1, 1), 0)
        self.assertEqual(testcode2.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(testcode2.subtract(10, 5), 5)
        self.assertEqual(testcode2.subtract(-1, 1), -2)
        self.assertEqual(testcode2.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(testcode2.multiply(10, 5), 50)
        self.assertEqual(testcode2.multiply(-1, 1), -1)
        self.assertEqual(testcode2.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(testcode2.divide(10, 5), 2)
        self.assertEqual(testcode2.divide(-1, 1), -1)
        self.assertEqual(testcode2.divide(-1, -1), 1)
        self.assertEqual(testcode2.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            testcode2.divide(10, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)