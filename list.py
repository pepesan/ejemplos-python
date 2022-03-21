# -*- coding: utf-8 -*-

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

newlist = ['physics', 'chemistry', 1997, 2000]

print("Value available at index 2 : ")
print(newlist[2])
newlist[2] = 2001
print("New value available at index 2 : ")
print(newlist[2])

x = [1, 2, 3, 4]
# Añade un elemento al final del listado
print(x)  # [1, 2, 3, 4]

print(list1)
del (list1[2])
print("After deleting value at index 2 : ")
print(list1)

print("Suma de dos listados en uno: ")
list2 = list1 + x
print(list2)

Celsius = [25.0, 36.5, 37.3, 37.8]
UnFahrenheit = ((float(9) / 5) * Celsius[0] + 32)
print("Celsius", Celsius)
print("UnFahrenheit", UnFahrenheit)
# En cada una de las vueltas elemento vale en cada vuelta un valor distinto
# Empezando por el primer valor de listado
# Y terminando por el último valor del listado
for elemento in Celsius:
    print(elemento)

Fahrenheit = []
for item in Celsius:
    i = ((float(9) / 5) * item + 32)
    Fahrenheit.append(i)
    print(i)
    print(Fahrenheit)

print(Fahrenheit)
"""
for (int i=0;i<10;i++){
    cosa 1; 
    cosa 2;
}
"""

Fahrenheit = [((float(9) / 5) * item + 32) for item in Celsius]
print(Fahrenheit)

mitupla = [(x, y, z)
           for x in range(1, 30)
           for y in range(x, 30)
           for z in range(y, 30)
           if x ** 2 + y ** 2 == z ** 2]
print(mitupla)

# Seleccionamos con un rango de 1 a 50
mi_listado = [x for x in range(1, 51)]
print("range(1, 51)", mi_listado)
# Seleccionamos con un rango de 0 a 49
mi_listado = [x for x in range(50)]
print(range(50), mi_listado)
print(len(mi_listado))

listado = [1, 2, 3]
for x in listado:
    print(x)

if (3 in listado):
    print("Está vivo!!!!!")

holas = ['Hi!'] * 4  # ['Hi!', 'Hi!', 'Hi!', 'Hi!']
print(4 * holas)
