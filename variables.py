# -*- coding: utf-8 -*-
"""
Sentencias con variables:

1- Declaración de una variable (Construcción) con el tipo de la variable
2- Inicialización de una variable (darle un valor inicial)
3- Cambiar el valor de una variable (asignación de un valor)
4- Liberar memoria (destruir) una variable
"""

"""
    Declaro una variable llamada counter, 
    del tipo número entero y 
    la inicializo con el valor 100
"""
contador = 100         # un número entero
sueldo = 35000.70      # coma flotante
nombre = "David"       # Una cadena de caracteres
booleano = True        # Un booleano

print(booleano)
print(sueldo)
print(nombre)
print(contador)

# Sentencia de asignación
# Asigna un valor nuevo a una variable
# cambia el valor almacenado en la variable
nombre = "Perro"
print(nombre)

# Python permite el tipado dinámico
# Una variable puede cambiar su tipo
sueldo = "Muchas"
print (sueldo)

"""
Cuando un programa termina su ejecución se libera la memoria
de la variables que estaban declaradas y en uso
"""