#zadanie 3
import math as m
import unittest

class TestListMethods(unittest.TestCase):

    def test_contains(self):
        lista = [float('nan')]
        self.assertTrue(float('nan') in lista)

if __name__ == '__main__':
    unittest.main(verbosity = 2)

