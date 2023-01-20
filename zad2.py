#zadanie 2 
import math as m
import unittest

class TestMathMethods(unittest.TestCase):

    def test_log10(self):
        self.assertEqual(m.log10(100), 2)
        with self.assertRaises(ValueError):
            m.log10(-5)

    def test_sqrt(self):
        self.assertEqual(m.sqrt(4), 2)
        self.assertGreaterEqual(m.sqrt(0), 0)
        with self.assertRaises(ValueError):
            m.sqrt(-5)

    def test_isfinite(self):
        self.assertTrue(m.isfinite(5))
        self.assertFalse(m.isfinite(float('nan')))

    def test_pi(self):
        self.assertGreater(m.pi, 3.14)
        self.assertAlmostEqual(m.pi, 3.14159265359, places = 7)


if __name__ == '__main__':
    unittest.main(verbosity = 2)

