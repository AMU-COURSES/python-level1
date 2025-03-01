# -*- coding: utf-8 -*-
"""
Module de test de mymodule
@author: arrivault
"""
import unittest
import random
from mymodule import create_complex


class TestMymodule(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(create_complex(), complex(0, 0),
                         "Test d'initialisation")

    def test_random(self):
        r = 100 * (random.random() - 0.5)
        i = 100 * (random.random() - 0.5)
        self.assertEqual(create_complex(r, i), complex(r, i), "Test random")

    def test_fail(self):
        self.assertEqual(create_complex(1, 2), complex(1, 3),
                         "Test faux pour l'exemple")

if __name__ == '__main__':
    unittest.main()
