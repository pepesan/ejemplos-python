# -*- coding: utf-8 -*-

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]


print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


list = ['physics', 'chemistry', 1997, 2000]

print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001
print ("New value available at index 2 : ")
print (list[2])

x = [1, 2, 3]
x.append(4)
print (x)


print (list1)
del (list1[2])
print ("After deleting value at index 2 : ")
print (list1)




Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit=[]
for item in Celsius:
    i=((float(9)/5)*item + 32)
    Fahrenheit.append(i)

Fahrenheit = [ ((float(9)/5)*item + 32) for item in Celsius ]
print(Fahrenheit)


mitupla=[(x,y,z)
         for x in range(1,30)
         for y in range(x,30)
         for z in range(y,30)
         if x**2 + y**2 == z**2]
print(mitupla)


mi_listado=[ x for x in range(1,51)]
print(mi_listado)

listado=[1, 2, 3]
for x in listado:
    print (x)

if( 3 in listado):
    print ("Está vivo!!!!!")