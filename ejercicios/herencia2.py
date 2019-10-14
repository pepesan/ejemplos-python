class Vehiculo:
    def __init__(self, nombre="", matricula="", marca="", modelo="", numRuedas=0, caballos=0):
        self.nombre= nombre
        self.matricula= matricula
        self.marca= marca
        self.modelo= modelo
        self.numRuedas=numRuedas
        self.caballos= caballos
    def setNombre(self, nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def setMatricula(self, matricula):
        self.matricula=matricula
    def getMatricula(self):
        return self.matricula
    def setMarca(self, marca):
        self.marca=marca
    def getMarca(self):
        return self.marca
    def setModelo(self, modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def setNumRuedas(self, numRuedas):
        self.numRuedas=numRuedas
    def getNumRuedas(self):
        return self.numRuedas
    def setCaballos(self, caballos):
        self.caballos=caballos
    def getCaballos(self):
        return self.caballos
    def __str__(self):
        return "Vehiculo[ nombre: "+self.nombre+", matricula: "+self.matricula+", marca: "+self.marca+", modelo: "+self.modelo+", numRuedas: "+str(self.numRuedas)+", caballos: "+str(self.caballos)+"]"

hiro = Vehiculo(marca="Toyota", modelo="Auris", nombre="Hiro")
print(hiro)
pepo = Vehiculo(marca="Mercedes", modelo="190D", nombre="Pepo")
print(pepo)

class Moto(Vehiculo):

    def __init__(self, nombre="", matricula="", marca="", modelo="", numRuedas=2, caballos= 0,chuches=[]):
        super().__init__(nombre, matricula, marca, modelo, numRuedas, caballos)
        self.chuches=chuches
    def getChuches(self):
        return self.chuches
    def setChuches(self, chuches = []):
        self.chuches=chuches
    def addChuche(self, chuche):
        self.chuches.append(chuche)
    def quitarChuche(self, chuche):
        self.chuches.remove(chuche)
    def __str__(self):
        return "Moto[nombre: "+self.nombre+", matricula: "+self.matricula+", marca: "+self.marca+", modelo: "+self.modelo+", numRuedas: "+str(self.numRuedas)+", caballos: "+str(self.caballos)+", chuches : "+str(self.chuches)+"]"


ita= Moto()
print(ita.numRuedas)
ita = Moto(numRuedas=3)
print(ita)
print(ita.numRuedas)
ita.setCaballos(134)
ita.addChuche("Puños calefactables")
print(ita)
ita.quitarChuche("Puños calefactables")
print(ita)

class Coche(Vehiculo):
    def __init__(self, nombre="", matricula="", marca="", modelo="", numRuedas=4, caballos=0):
        super().__init__(nombre, matricula, marca, modelo, numRuedas, caballos)
    def __str__(self):
        return "Coche[ nombre: "+self.nombre+", matricula: "+self.matricula+", marca: "+self.marca+", modelo: "+self.modelo+", numRuedas: "+str(self.numRuedas)+", caballos: "+str(self.caballos)+"]"


hiro = Coche()
print(hiro.numRuedas)
print(hiro)