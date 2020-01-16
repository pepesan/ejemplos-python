import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        boolean = True
        self.assertTrue(boolean)
        boolean = False
        self.assertFalse(boolean)
        boolean2 = boolean
        self.assertIs(boolean, boolean2)
        boolean = None
        self.assertIsNone(boolean)
        cadena = "Hola"
        letra = "H"
        self.assertIn(letra, cadena)
        # self.assertIsInstance(cadena, cadena)

    def test_bad_type(self):
        data = "banana"
        # controla una excepción que salga
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()