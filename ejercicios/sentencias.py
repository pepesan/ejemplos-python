# -*- coding: utf-8 -*-
"""
Fichero principal de python
Autor: David Vaquero <pepesan@gmail.com>
"""
"""
Ejercicios Complementarios de la Unidad
1.- Sobr"e el mismo proyecto anterior resolveremos estos ejercicios

2.- Crea un nuevo fichero llamado sentencias.py
"""
"""
3.- Crea un  diccionario con los datos de un cliente: nombre, dirección, tlf, email
"""
diccionario = {
    'nombre':"Pepe",
    'direccion':"mi casa que es particular",
    'tlf':"945123456",
    'email':"p@p.cpm"}
"""
4.- Recorre la variable y vete presentando los datos por pantalla 
"""
for clave in diccionario:
    print(clave+":"+diccionario[clave])
"""
5.- Añade un nuevo campo al diccionario: facturacion total
"""
diccionario['facturacion_total'] = 35000.0
"""

6.- Vuelve a recorrer el diccionario para ver si están o no los datos introducidos
"""
for clave in diccionario:
    print(clave+":"+str(diccionario[clave]))
"""
7.- Crea un bucle while que de 10 vueltas, en cada una de esas vueltas imprime el número de vuelta
"""
i = 0
while(i<10):
    print("Numero: ", i+1)
    i = i +1

"""
8.- Crea un bucle for in que de 10 vueltas, en cada una de esas vueltas imprime el número de vuelta
"""
for item in range(10):
    print("For in numero: ", item+1)
"""
9.- Crea una variable del tipo tupla, otra de tipo cadena, otra de tipo listado 
y otra de tipo diccionario.
"""
tupla = (1,2)
cadena = "mi mensaje"
listado = [1,2,3,4]
diccionario = {
    'nombre':"Pepe",
    'direccion':"mi casa que es particular",
    'tlf':"945123456",
    'email':"p@p.cpm"}
"""
10.- Recorre los 4 tipos de datos con  bucle e imprime el índice y el valor para cada posición del dato
"""
for indice in range(len(tupla)):
    print("indice:", indice, ":", tupla[indice])
for indice in range(len(cadena)):
    print("indice:", indice, ":", cadena[indice])
for indice in range(len(listado)):
    print("indice:", indice, ":", listado[indice])
for clave in diccionario:
    print("indice:", clave, ":", diccionario[clave])
"""
11.- Define una cadena de caracteres larga (loren ipsum)
"""
loremIpsum ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu consequat dolor, sit amet sagittis mi. Vestibulum nibh arcu, rhoncus congue convallis eget, accumsan tempor neque. Nulla quis sollicitudin massa. Phasellus volutpat augue ac mauris scelerisque, nec laoreet mauris sagittis. Nulla accumsan, massa id aliquam consequat, turpis urna elementum augue, in scelerisque nibh tortor in ligula. Quisque id erat imperdiet, mattis est ut, gravida augue. Maecenas magna ipsum, mollis at commodo sed, vestibulum vitae nisi. Duis faucibus, massa a mattis porta, nulla justo elementum metus, eu condimentum est felis et enim. Ut posuere hendrerit sodales. Fusce pellentesque nisi et lorem hendrerit ultricies. Suspendisse potenti. Duis pulvinar quam nec faucibus fermentum. Pellentesque non orci enim. Etiam vel facilisis risus. Duis ac mi sed nisl aliquet elementum et at orci. Morbi fringilla ullamcorper ante ut ullamcorper"
"""

12.- Recorre la cadena para presentar todas la letras que la conforman y decir al final el número de letras que contiene, verifica que es el número correcto
"""
i=0
# while(i<len(loremIpsum)):
for letter in loremIpsum:
    #print(loremIpsum[i])
    print(letter)
    i=i+1

print("Caracteres sumados: ",i)
print(len(loremIpsum))
"""
13.- Busca dentro de la cadena del loren ipsum, ejercicio 11, 
y mediante bucles comprueba que incluye la palabra "ipsum", 
sin importar las mayúsculas o minúsculas. 
Imprime un mensaje por pantalla indicando si se ha encontrado 
o no ese texto dentro de la cadena
"""
cadena ="lorem IPsum no cuetator cosas"
contador=0
contador_letra=0
ipsum="ipsum"
encontrado=False
for letra in cadena:
    if(letra.lower()==ipsum[0]):
        contador_letra=1
        petado=False
        while(contador_letra<len(ipsum)):
            if(not(cadena[contador+contador_letra].lower()==ipsum[contador_letra].lower())):
                petado=True
                break
            contador_letra=contador_letra+1
        if(not(petado)):
            encontrado=True
    contador=contador +1

# Trapi
for i in range(1):
    for index in range (1):
        cadena2= cadena.lower()
        if (cadena2.find(ipsum)>=0 ):
            encontrado = True
        else:
            encontrado = False

if(encontrado):
    print("Hemos encontrado el ipsum")
else:
    print("No hemos encontrado el ipsum")

