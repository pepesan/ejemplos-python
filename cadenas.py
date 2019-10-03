# -*- coding: utf-8 -*-


cadena ="lorem Ipsum no cuetator cosas"
# Longitud de cadena
print("Logintud de la cadena:",len(cadena))
# Convertir a mayúsculas
print("Cadena en mayúsculas: ",cadena.upper())
# Convertir a minúsculas
print("Cadena en minúsculas: ",cadena.lower())
cadena2 = " cx xc xc xc  otra cadena"
# Concatenar
cadena3= cadena + cadena2
print(cadena3)
# encontrar una subcadena
res= cadena3.find("otra")
print("Resultado: Índice donde ha encontrado la subcadena:",res)

# Reemplazar un valor en una cadena por otro valor
res= cadena3.replace("otra","esta")
print("Resultado: cadena cambiada:",res)
# Reemplaza un número de veces, 2 en este caso
res= cadena3.replace("xc","22",2)
print("Resultado: cadena cambiada:",res)

res= cadena3.index("xc")
print("Resultado: indice:",res)
