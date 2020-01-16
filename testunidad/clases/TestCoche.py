import unittest

from testunidad.clases.Coche import Coche


class TestCoche(unittest.TestCase):
    def setUp(self):
        self.objeto = Coche()
    def test_inicia_correcto_velocidad_a_cero(self):
        self.assertEqual(self.objeto.speed, 0, "Debería ser cero al velocidad")
    def test_inicia_correcto_destino_a_None(self):
        self.assertIsNone(self.objeto.destination, "Debería ser None")
        self.assertEqual(self.objeto.destination, None, "Debería ser None al velocidad")