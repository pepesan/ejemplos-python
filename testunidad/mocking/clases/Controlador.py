from testunidad.mocking.clases.Modelo import Modelo


class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.value = 0
    def cogeDato(self):
        self.value = self.modelo.getData()
    def procesaDato(self):
        self.value += 2
    def imprimeDato(self):
        print(self.value)