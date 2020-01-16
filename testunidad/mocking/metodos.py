import unittest
from unittest import mock

class Empleado:
    'Clase base de manejo de empleados'
    #esta variable es estática y se comparte entre instancias de Employee
    empCount = 0

    def __init__(self, name = '', salary = '') :
        self.name = name
        self.salary = salary
        Empleado.empCount += 1

    @classmethod
    def presenta(cls, dato):
        print("Hola, me llamo ", dato,"!")

    def displayCount(self):
        print ("Total Employee %d" % Empleado.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name



class TestSum(unittest.TestCase):
    def test_foo(self):
        with mock.patch.object(Empleado, 'getName', return_value=None) as mock_method:
            instance = Empleado()
            instance.getName()
            mock_method.assert_called()

    def test_setget(self):
        with mock.patch.object(Empleado, 'getName', return_value=None) as mock_method:
            instance = Empleado()
            instance.setName("Pepe")
            self.assertEqual(instance.getName(), None)

    @mock.patch('testunidad.mocking.metodos.Empleado.getName')
    def test_classmethod(self, mock_class_method):
        mock_class_method.return_value = "foobar"
        emp = Empleado()
        self.assertEqual(emp.getName(), "foobar")

    @mock.patch('testunidad.mocking.metodos.Empleado')
    def test_class(self, mock_emp):
        class NewEmp(object):
            def getName(self):
                return 'Pepe'

        mock_emp.return_value = NewEmp()
        self.assertEqual("Pepe", mock_emp().getName())


if __name__ == '__main__':
    unittest.main()