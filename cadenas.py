# -*- coding: utf-8 -*-


cadena ="lorem Ipsum no cuetator cosas"
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

if(encontrado):
    print("Hemos encontrado el ipsum")
else:
    print("No hemos encontrado el ipsum")