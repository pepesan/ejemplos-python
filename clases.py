class ClassName:
   'Optional class documentation string'
   #class_suite

obj= ClassName()

class Employee:
    'Clase que maneja los datos de un empleado'
    #comentario
    def __init__(self):
        self.name=""
        self.salary=0
        # return self

jorge=Employee()
print(jorge.name)
jorge.name="Jorge"
print(jorge.name)
jorge.salary=45000
print(jorge.salary)

juan=Employee()
juan.name="Juan"
juan.salary=15000
print(juan.name)
print(juan.salary)


class Employee:
    'Clase que maneja los datos de un empleado'
    #comenatrio
    def __init__(self, name="",salary=0):
        self.name=name
        self.salary=salary

isabel=Employee()
print(isabel.salary)
isabel=Employee(salary=60000)
print(isabel.salary)
isabel=Employee(name="Isabel")
print(isabel.name)
isabel=Employee("Isabel",60000)
print(isabel.name)
print(isabel.salary)
isabel=Employee("Isabel")
print(isabel.name)
print(isabel.salary)

class Employee:
    'Clase que maneja los datos de un empleado'
    #comenatrio
    def __init__(self, name="",salary=0):
        self.name=name
        self.salary=salary

    def incSalary(self,valor):
        #self.salary=self.salary+valor
        self.salary+=valor

maria=Employee(name="Maria",salary=75000)
maria.incSalary(10000)
print(maria.salary)


class Employee:
    'Common base class for all employees'
    #esta variable es estática y se comparte entre instancias de Employee
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @classmethod
    def introduce(cls):
        print("Hello, I am %s!" % cls)

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)



emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.salary  # Delete 'salary' attribute.


hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
delattr(emp1, 'age')    # Delete attribute 'age'


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)


class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt2.x=2
print(pt1.x)
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the objects
del pt1
del pt2
del pt3


class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    def getX(self):
        return self.x
    def setX(self,x):
        self.x=x
punto=Point(12,15)
print(punto.x)
print(punto.y)
punto.setX(10)
print(punto.x)
print(punto.getX())

class Employee:
    'Clase que maneja los datos de un empleado'
    #comenatrio
    def __init__(self, name="",salary=0):
        self.name=name
        self.salary=salary

    def incSalary(self,valor):
        #self.salary=self.salary+valor
        self.salary+=valor

    def setSalary(self,salary):
        self.salary=salary

    def getSalary(self):
        return self.salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


emp1 = Employee("Zara", 2000)
emp1.salary=30000
emp1.setSalary(35000)
print(emp1.getSalary())

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


class A:        # define your class A
    def __init__(self):
        self

class B:         # define your class B
    def __init__(self):
        self


class C(A, B):   # subclass of A and B
    def __init__(self):
        self


class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


class Parent:
    def __init__(self):
        self.parameter=""

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.attribute=""


c=Child()
print(c.parameter)
print(c.attribute)

class Parent:
    def __init__(self,parameter=""):
        self.parameter=parameter

class Child(Parent):
    def __init__(self,attribute="",parameter=""):
        self.attribute=attribute
        super(Child, self).__init__(parameter)


c=Child("Hola")
print(c.parameter)
print(c.attribute)

c=Child("Hola","Mundo")
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
print (v1 + v2)


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)


class Cliente:
    ""
    totalCotizaciones = 0

    def __init__(self,nombre="",direccion="",email="",tlf="",cotizacion=0):
        self.nombre=nombre
        self.direccion=direccion
        self.email=email
        self.tlf=tlf
        self.cotizacion=cotizacion

    def setCotizacion(self,cotizacion):
        self.cotizacion=cotizacion
        self.totalCotizaciones+=cotizacion

    def __str__(self):
        return "Cliente[nombre:"+self.nombre+"]"


indra=Cliente()
indra.setCotizacion(20000)
print(indra.cotizacion)
telefonica=Cliente(nombre="Telefónica")
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
        self.nombre=nombre

class Empleado(Persona):
    def __init__(self, nombre="",sueldo=0):
        super().__init__(nombre)
        self.sueldo=sueldo

perso=Persona("personita")
emp1=Empleado(nombre="Juan",sueldo=65000)

print(perso.nombre)
print(emp1.sueldo)
print(emp1.nombre)

emp2=Empleado()