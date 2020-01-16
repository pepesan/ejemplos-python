import unittest

from funciones import suma


class TestSuma(unittest.TestCase):
    def test_sumanumeros(self):
        self.assertEqual(suma(1,2),3,"Debería ser 3")