from unittest import mock
from unittest.mock import Mock

import unittest

from testunidad.mocking.clases.Controlador import Controlador


class TestControlador(unittest.TestCase):

    @mock.patch('testunidad.mocking.clases.Modelo.Modelo.getData')
    def test_classmethod(self, mock_class_method):
        mock_class_method.return_value = 3
        c = Controlador()
        c.cogeDato()
        self.assertEqual(c.value, 3)
        c.procesaDato()
        self.assertEqual(c.value, 5)