class NombreClase:
    'Optional class documentation string'
    # class_suite


obj = NombreClase()


class Empleado:
    """Clase que maneja los datos de un empleado"""

    # comentario
    def __init__(self):
        self.nombre = ""
        self.salario = 0
        # return self


jorge = Empleado()
print(jorge.nombre)
jorge.nombre = "Jorge"
print(jorge.nombre)
print(jorge.salario)
jorge.salario = 45000
print(jorge.salario)

juan = Empleado()
juan.nombre = "Juan"
juan.salario = 15000
print(juan.nombre)
print(juan.salario)


class Empleado:
    """Clase que maneja los datos de un empleado"""

    # comentario
    def __init__(self, nombre="", salario=0):
        self.nombre = nombre
        self.salario = salario


isabel = Empleado()
# isabel = Empleado(nombre="Isabel", salario=5000)
print(isabel.salario)
isabel = Empleado("Isabel")
print(isabel.nombre)
print(isabel.salario)
isabel = Empleado("Isabel", 60000)
print(isabel.nombre)
print(isabel.salario)
isabel = Empleado(salario=60000)
print(isabel.salario)
isabel = Empleado(nombre="Isabel")
print(isabel.nombre)


class Empleado:
    """Clase que maneja los datos de un empleado"""

    # comentario
    def __init__(self, nombre="", salario=0):
        self.nombre = nombre
        self.salario = salario

    def incrementaSalario(self, valor):
        # self.__salario = self.__salario+valor
        # += -= *= /=
        self.salario += valor


maria = Empleado(nombre="Maria", salario=75000)
maria.incrementaSalario(1000)
print(maria.salario)


# maria.__salario= maria.__salario+10000
def incrementaSalario(salario, incremento):
    return salario + incremento


maria.salario = incrementaSalario(maria.salario, 10000)

maria.incrementaSalario(10000)
print(maria.salario)


class Empleado:
    """Clase que maneja los datos de un empleado"""

    # comentario
    def __init__(self, nombre="", salario=0):
        self.nombre = nombre
        self.__salario = salario

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario


maria = Empleado(nombre="Maria", salario=75000)
print(maria.getSalario())
maria.setSalario(15000)
print(maria.getSalario())


class Empleado:
    """Clase base de manejo de empleados"""
    # esta variable es estática y se comparte entre instancias de Employee
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Empleado.empCount += 1

    @classmethod
    def presenta(cls, dato):
        print("Hola, me llamo ", dato, "!")

    def displayCount(self):
        print("Total Employee %d" % Empleado.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"creamos el primero objeto"
emp1 = Empleado("Zara", 2000)
"creamos un segundo objeto de Empleado"
emp2 = Empleado("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Número de Empleados %d" % Empleado.empCount)
Empleado.presenta("")

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
print("Edad del empleado:", emp1.age)
# No funciona porque no tiene ese atributo
# print("Edad del empleado:",emp2.age)
del emp1.salary  # Delete 'salary' attribute.
# No funciona porque no tiene ese atributo
# print(emp1.salary)
print(emp2.salary)

# funciones de control de atributos
hasattr(emp1, 'age')  # Returns true if 'age' attribute exists
getattr(emp1, 'age')  # Returns value of 'age' attribute
setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
delattr(emp1, 'age')  # Delete attribute 'age'

print("Empleado.__doc__:", Empleado.__doc__)
print("Empleado.__name__:", Empleado.__name__)
print("Empleado.__module__:", Empleado.__module__)
print("Empleado.__bases__:", Empleado.__bases__)
print("Empleado.__dict__:", Empleado.__dict__)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


print("Ejemplos con Punto")
pt1 = Point()
pt1.x = 1
print(pt1.x)
pt2 = pt1
print(pt2.x)
pt2.x = 2
print(pt1.x)
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
del pt1
del pt2
del pt3


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y


punto = Point(12, 15)
print(punto.x)
print(punto.y)
punto.setX(10)
print(punto.x)
print(punto.getX())
print(punto)


class Empleado:
    'Clase que maneja los datos de un empleado'

    # comentario
    def __init__(self, nombre="", salario=0):
        self.nombre = nombre
        self.salario = salario

    def incSalario(self, valor):
        # self.salario=self.salario+valor
        self.salario += valor

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def __str__(self):
        return 'Empleado [nombre:' + self.nombre + ", salario:" + str(self.salario) + "]"


print("Ejemplo __str__")
emp1 = Empleado("Zara", 2000)
emp1.salario = 30000
emp1.setSalario(35000)
print(emp1.getSalario())
print(emp1)


class Madre:  # clase madre
    atributoEstatico = 100

    def __init__(self):
        print("Constructora de la Madre")
        self.atributoMadre = 100

    def metodoMadre(self):
        print('Método de la madre')

    def setAttr(self, attr):
        self.atributoMadre = attr

    def getAttr(self):
        return self.atributoMadre


class Hija(Madre):  # clase hija
    def __init__(self):
        super().__init__()
        print("Llamando a la constrctura de la hija")

    def metodoHija(self):
        print('llamando al método de la hija')


print("Datos de herencia")
Madre.atributoEstatico = 200
print(Madre.atributoEstatico)
print(Hija.atributoEstatico)
c = Hija()  # instancia hija
c.metodoHija()  # llama al método de la hija
c.metodoMadre()  # llama a método de la madre
c.setAttr(200)  # llama al método de la madre
print(c.getAttr())  # llama al método de la madre


class A:  # define your class A
    def __init__(self):
        self


class B:  # define your class B
    def __init__(self):
        self


class C(A, B):  # subclass of A and B
    def __init__(self):
        self


class Parent:  # define parent class
    def myMethod(self):
        print('Calling parent method')


class Child(Parent):  # define child class
    def myMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.myMethod()  # child calls overridden method


class Parent:
    def __init__(self):
        self.parameter = ""


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.attribute = ""


c = Child()
print(c.parameter)
print(c.attribute)


class Parent:
    def __init__(self, parameter=""):
        self.parameter = parameter

    def metodoMadre(self):
        print("Metodo madre en Madre")


class Child(Parent):
    def __init__(self, attribute="", parameter=""):
        self.attribute = attribute
        # self.parameter=parameter
        super(Child, self).__init__(parameter)

    def metodoHija(self):
        self.metodoMadre()

    def metodoMadre(self):
        print("Metodo Madre en Hija")
        super(self).metodoMadre()


c = Child("Hola")
print(c.parameter)
print(c.attribute)

c = Child("Hola", "Mundo")
print(c.parameter)
print(c.attribute)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()


# print (counter.__secretCount)


class Cliente:
    ""
    totalCotizaciones = 0

    def __init__(self, nombre="", direccion="", email="", tlf="", cotizacion=0):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.tlf = tlf
        self.cotizacion = cotizacion

    def setCotizacion(self, cotizacion):
        self.cotizacion = cotizacion
        self.totalCotizaciones += cotizacion

    def __str__(self):
        return "Cliente[nombre:" + self.nombre + "]"


indra = Cliente()
indra.setCotizacion(20000)
print(indra.cotizacion)
telefonica = Cliente(nombre="Telefónica")
print(telefonica.nombre)
print(telefonica.__str__())


class Figuras(object):
    __slots__ = ('dim1', 'dim2')

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print(('El área de la figura no esta definida.'))


class Rectangulo(Figuras):
    def __init__(self, dim1, dim2):
        super().__init__(dim1, dim2)

    def area(self):
        if self.dim1 != self.dim2:
            print(('El área del rectángulo es: '))
        else:
            print(('El área del cuadrado es:'))
        return (self.dim1 * self.dim2)

    def perimetro(self):
        print(('El perímetro del rectángulo es: '))
        return (2 * self.dim1 + 2 * self.dim2)


def main():
    F = Figuras(10, 10)
    R = Rectangulo(9, 5)


main()


class Persona:
    def __init__(self, nombre=""):
        self.nombre = nombre


class Empleado(Persona):
    def __init__(self, nombre="", sueldo=0):
        super().__init__(nombre)
        self.sueldo = sueldo


perso = Persona("personita")
emp1 = Empleado(nombre="Juan", sueldo=65000)

print(perso.nombre)
print(emp1.sueldo)
print(emp1.nombre)


class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
        print("init de Persona")

    def __str__(self):
        return "Persona[ nombre:" + self.nombre + ", edad:" + str(self.edad) + "]"


class Empleado(Persona):
    def __init__(self, nombre="", edad=0, sueldo=0):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        print("init de Empleado")


class Jefe(Empleado):

    def __init__(self, nombre="", edad=0, sueldo=0, departamento=""):
        super().__init__(nombre, edad, sueldo)
        self.departamento = departamento


perso = Persona("personita")
emp1 = Empleado(nombre="Juan", sueldo=65000)
jefecillo = Jefe("Rodrigo", 56, 0, "Carcel")

print(perso.nombre)
print(emp1.sueldo)
print(emp1.nombre)
print(jefecillo.nombre)
print(jefecillo.sueldo)
print(jefecillo.departamento)

emp2 = Empleado()
