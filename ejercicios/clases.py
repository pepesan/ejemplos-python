class Cliente:
    def __init__(self, nombre="", direccion="", tlf="", email="", cotizacion=0,total_cotizaciones=0):
        self.nombre=nombre
        self.direccion=direccion
        self.tlf=tlf
        self.email=email
        self.cotizacion=cotizacion
        self.total_cotizaciones=total_cotizaciones
    def setCotizacion(self, dato):
        self.cotizacion=dato
        self.total_cotizaciones+=dato

indra=Cliente()
print(indra)
indra.nombre="Indra"
indra.direccion="Anabel Segura 23"
indra.tlf="9123354355"
indra.email="info@indra.es"
print(indra.email)
indra.setCotizacion(200)
print(indra.cotizacion)
bbva=Cliente(nombre="BBVA")
print(bbva.nombre)
santander=Cliente(nombre="Santander", tlf="9123434535")
print(santander.nombre)
print(santander.tlf)
iberdrola= Cliente(email="info@iberdrola.es")
print(iberdrola.email)


