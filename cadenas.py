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


texto = "Hola, ¿cómo estás?"
palabras = texto.split(" ")  # Divide en cada espacio
print(palabras)
# Resultado: ['Hola,', '¿cómo', 'estás?']
palabras = ["Hola", "¿cómo", "estás?"]
texto = " ".join(palabras)
print(texto)
# Resultado: "Hola ¿cómo estás?"

texto = "Hola, ¿cómo estás?"
nuevo_texto = texto.replace("Hola", "Buenas")
print(nuevo_texto)
# Resultado: "Buenas, ¿cómo estás?"

texto = "Hola, ¿Cómo Estás?"
print(texto.lower())  # "hola, ¿cómo estás?"
print(texto.upper())  # "HOLA, ¿CÓMO ESTÁS?"

texto = "   Hola, ¿cómo estás?   "
print(texto.strip())   # "Hola, ¿cómo estás?"
print(texto.lstrip())  # "Hola, ¿cómo estás?   "
print(texto.rstrip())  # "   Hola, ¿cómo estás?"

texto = "Hola, ¿cómo estás?"
posicion = texto.find("cómo")
print(posicion)  # Resultado: 6

texto = "Hola, ¿cómo estás? ¿cómo te ha ido?"
cantidad = texto.count("cómo")
print(cantidad)  # Resultado: 2


nombre = "Juan"
edad = 25
mensaje = f"Hola, {nombre}. Tienes {edad} años."
print(mensaje)
# Resultado: "Hola, Juan. Tienes 25 años."


nombre = "Juan"
edad = 25
mensaje = "Hola, {}. Tienes {} años.".format(nombre, edad)
print(mensaje)
# Resultado: "Hola, Juan. Tienes 25 años."


mensaje = "Hola, {1}. Tienes {0} años.".format(25, "Juan")
print(mensaje)
# Resultado: "Hola, Juan. Tienes 25 años."


pi = 3.14159
mensaje = f"El valor de pi es aproximadamente {pi:.2f}."
print(mensaje)
# Resultado: "El valor de pi es aproximadamente 3.14."


nombre = "Juan"
edad = 25
mensaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print(mensaje)
# Resultado: "Hola, Juan. Tienes 25 años."

