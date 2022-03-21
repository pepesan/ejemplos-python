# -*- coding: utf-8 -*-

var = 100

# Como var == 100 es como poner
# if(True):
# if(var == 100):
if var == 100:
    print("Sentencia 1: La variable vale 100")
    print("Sentencia 1: Dentro del if")

print("¡Adios!")

var1 = True
# if (var1):
if var1:
    print("Sentencia 2: Sólo de ejecuta si var  == True")
    print(var1)

print("Sentencia 2: Fuera del if")

var2 = 0
# 0 es False, 1 es True
if var2:
    print("Sentencia 3: sólo sale si var2 == True")
    print(var2)

var1 = 100
if var1:
    print("Sentencia 4: La variable existe y no es 0")
    print(var1)
else:
    print("Sentencia 4: La variable no existe o es 0")
    print(var1)

var2 = 1
if var2:
    print("Sentencia 5: Existe o no tiene valor 0")
    print(var2)
else:
    print("Sentencia 5: No existe o  tiene valor 0")
    print(var2)

# Sentencia condicional múltiple
var = 100
if var == 200:
    print("Sentencia 6: vale 200")
    print(var)
elif var == 150:
    print("Sentencia 6: vale 150")
    print(var)
elif var == 100:
    print("Sentencia 6: vale 100")
    print(var)
else:
    print("Sentencia 6: vale cualquier otra cosa ")
    print(var)
var = 100
# If anidados
if var < 200:
    print("Sentencia 7: menor que 200")
    if var == 150:
        print("Sentencia 7: es 150")
    elif var == 100:
        print("Sentencia 7: es 100")
    elif var == 50:
        print("Sentencia 7: es 50")
    else:
        print("Sentencia 7: No es ni 150, ni 100, ni 50, pero es menor a 200")
elif var > 200:
    print("Sentencia 7: es mayor a 200")
else:
    print("Sentencia 7: es 200")

# Sentencias Iterativas / Bucles
# Inicialización
count = 1
# Condición, Mientras que count valga menos que 3, sigue dando vueltas
# while (count < 3):
while count < 3:
    print('While 1, count vale: ', count)
    # Incremento
    count = count + 1

print("Salimos del bucle while")

## While con else
print("While-Else")
# Inicialización
count = 0
# Condición
while count < 2:
    print("While 2, count vale: ", count)
    # Incremento
    count = count + 1
# Else cuando salga del bucle
else:
    print("Caso del else")

# Recorrer un listado con un bucle for-in
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
    print('For-in Frutas 1, fruta actual :', fruit)

print("Bucle 2")
var = 4
print("Valor Variable:", var)

# Recorrer un listado pero teniendo acceso al índice
fruits = ['banana', 'apple', 'mango']
# for index in range (3): de 0 a 2, 0,1,2
for index in range(len(fruits)):
    print("For-in Frutas 2, indice:", index)
    print('For-in Frutas 2, con índice, fruta actual :', fruits[index])

## Recorro sacando el índice y el valor
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('For in 3, por posición:', index, ' :', fruits[index])

# Recorro una tupla con un for in, con índice
fruits = ('banana', 'apple', 'mango')
for index in range(len(fruits)):
    print('For in 4, Tupla: indice : ', index, 'Elemento :', fruits[index])

# Recorro un diccionario, por la clave
midict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for clave in midict:
    print("For in 5, clave: ", clave, ", Valor:", midict[clave])

# For anidados
n_vuelta = 0
for i in range(2):
    for j in range(3):
        print("For in 6: i:", i, ",j:", j)
        n_vuelta = n_vuelta + 1
        print("Numero de vuelta: ", n_vuelta)

# Código que busca números primos, si no es primo te dice porqué
for num in range(2, 20):  # to iterate between 2 to 19
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num / i  # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            break  # to move to the next number, the #first FOR
    else:  # else part of the loop
        print(num, 'is a prime number')

# Recorro una cadena de caracteres con un For in
for letter in 'Python':  # First Example
    print('For in 7: letra: ', letter)

# Recorro una cadena en base a su longitud y su índice
var = "Python"
for index in range(len(var)):  # First Example
   print('For in 7: indice: ', index, ' letra: ', var[index])
