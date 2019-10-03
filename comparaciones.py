# -*- coding: utf-8 -*-

a = 21
b = 10

# Sentencia condicional, con parte del if y parte del else
# Comparamos dos valores, si a es igual a b
if ( a == b ):
   print ("Comparacion 1: a es igual a b")
else:
   print ("Comparacion 1: a y b no son iguales")

# Comparamos si son distintos valores
if ( a != b ):
   print ("Comparacion 2: a es distinto de b")
else:
   print ("Comparacion 2: a y b son iguales")

# Comparamos si a es menor que b
if ( a < b ):
   print ("Comparacion 3:  a es menor que b" )
else:
   print ("Comparacion 3: a no es menor que b")

# Comparamos si a es mayor que b
if ( a > b ):
   print ("Comparacion 4: a es mayor que b")
else:
   print ("Comparacion 4: a no es mayor que b")

# Comparamos si a es menor o igual que b
if ( a <= b ):
   print ("Comparacion 5: a es menor o igual que b")
else:
   print ("Comparacion 5: a no es ni menor ni igual a b, entonces a es mayor que b")

# Comparando si b es mayor o igual que a
if ( b >= a ):
   print ("Comparacion 6:  b es mayor o igual que a")
else:
   print ("Comparacion 6: b no es ni mayor ni igual a a, b es menor que a")

a = 21
b = 21.0
# b = "21" # en PHP, pero no en Python

# Comparamos dos valores, si a es igual a b
if ( a == b ):
   print ("Comparacion 7: a es igual a b")
else:
   print ("Comparacion 7: a y b no son iguales")

# Comparamos si b es idéntico a a
if ( a is b ):
   print ("Comparacion 8: a es b")
else:
   print ("Comparacion 8: a no es b")
#Comparamos si a no es b, identidad
if ( a is not b ):
   print ("Comparacion 9: a no es b")
else:
   print ("Comparacion 9: a es b")
