# -*- coding: utf-8 -*-

var = 100



if ( var  == 100 ) : print ("Value of expression is 100")

print ("Good bye!")


var1 = False
if var1:
   print ("1 - Got a true expression value")
   print (var1)

print("fuera del if")

var2 = 0
if var2:
   print ("2 - The var exists")
   print (var2)



var1 = 100
if var1:
   print ("1 - The var exists")
   print (var1)
else:
   print ("1 - The var not exists")
   print (var1)

var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
else:
   print ("2 - Got a false expression value")
   print (var2)

var = 100
if var == 200:
   print ("1 - Got a true expression value")
   print (var)
elif var == 150:
   print ("2 - Got a true expression value")
   print (var)
elif var == 100:
   print ("3 - Got a true expression value")
   print (var)
else:
   print ("4 - Got a false expression value")
   print (var)


if var < 200:
   print ("Expression value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   else:
      print("No es ni 150, ni 100, ni 50, pero es menor a 200")
elif var > 200:
   print ("Expression value greater than 200")
else:
   print ("Expression value is 200")

count = 1
while (count < 9):
   print ('The count is:', count)
   count = count +1


count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print ('Current fruit :', fruit)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
   print('Current fruit :', fruits[index])

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Fruit at position:',index,' :', fruits[index])

# Código que busca números primos, si no es primo te dice porqué
for num in range(2,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')