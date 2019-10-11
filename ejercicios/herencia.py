class Persona:
    def __init__(self, nombre="", direccion=""):
        self.nombre = nombre
        self.direccion = direccion
        print("init de Persona")


paco = Persona()
paco.nombre = "Paco"
print(paco.nombre)
reme = Persona (nombre="Remedios")
print(reme.nombre)
class Empleado(Persona):
    def __init__(self, nombre="", direccion="", sueldo=0, cargo=""):
        super().__init__(nombre,direccion)
        self.sueldo = sueldo
        self.cargo = cargo
        print("init de Empleado")

ivan = Empleado("Ivan", "Futuro 22, 37770", 35000, "Desarrollador")
print(ivan.sueldo)

class Jefe(Empleado):

    def __init__(self, nombre="", direccion="",sueldo=0, cargo="",nombreDepartamento=""):
        super().__init__(nombre,direccion,sueldo, cargo)
        self.nombreDepartamento= nombreDepartamento
        print("init de Jefe")



rato=Jefe("Rodrigo","Soto del real",0,"Carcel", "Fraudes y estafas")
print(rato.nombreDepartamento)
