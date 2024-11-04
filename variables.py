# -*- coding: utf-8 -*-


if __name__ == '__main__':
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
    contador = 100  # un número entero
    sueldo = 35000.70  # coma flotante
    nombre = "David"  # Una cadena de caracteres
    booleano = True  # Un booleano

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
    print(sueldo)

    """
    Cuando un programa termina su ejecución se libera la memoria
    de la variables que estaban declaradas y en uso
    """
    print("Ejemplos de variables")
    print("Booleanos")
    # Declaración e inicilización de variable
    # boolean: True, False, None
    booleana = True
    # imprimir por pantalla variable
    print(booleana)

    print("Números Enteros")
    # Declaración de variable entera
    # enteros: numero naturales, positivos o negativos
    entero = 2
    # imprimir por pantalla variable
    print(entero)
    # cambiamos el valor de una variable
    entero = 3
    # imprimir por pantalla variable
    print(entero)
    # Definimos otra variable entera
    numero = 2
    # imprimir por pantalla variable
    print(numero)

    print("Números flotantes")
    # Declaración de variables de coma flotante
    flotante = +1.23
    # imprimir por pantalla variable
    print(flotante)
    # valor negativo
    flotante = -1.23
    # imprimir por pantalla variable
    print(flotante)
    # casting de entero a flotante
    entero = 2
    flotante = float(entero)
    # imprimir por pantalla variable
    print(flotante)
    # casting de flotante a entero
    entero = int(flotante)
    print(entero)

    # Números complejos
    print("Números complejos")
    # definimos parte real y parte imaginaria
    complejo = complex(2, 1)
    print(complejo)