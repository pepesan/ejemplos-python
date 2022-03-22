class Persona:
    def __init__(self, nombre="", dni="", tlf="", email="", direccion="", direcciones=None):
        self.nombre = nombre
        self.dni = dni
        self.tlf = tlf
        self.email = email
        self.direccion = direccion
        if direcciones is not None:
            self.direcciones = direcciones
        else:
            self.direcciones = []
        if self.direccion != "":
            self.setDireccion(direccion)

    def setDireccion(self, direccion):
        self.direccion = direccion
        self.direcciones.append(self.direccion)


pepito = Persona()
pepito.nombre = "Pepito"
pepito.dni = "07977865A"
pepito.tlf = "945123456"
pepito.email = "pepito@gmail.com"
pepito.setDireccion("Castrourdiales 10")
print(pepito.direccion)
print(pepito.direcciones)

juanita = Persona(nombre="Juanita")
print(juanita.nombre)
juanita = Persona(dni="07888997A")
print(juanita.dni)
juanita = Persona("Juanita", "07998877A")
print(juanita.nombre)
print(juanita.dni)
print(juanita)
print(juanita.direcciones)
juanita.setDireccion("Una")
print(juanita.direcciones)
juanita.setDireccion("Dos")
print(juanita.direcciones)
