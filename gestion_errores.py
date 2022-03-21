# -*- coding: utf-8 -*-




while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
    finally:
        print("Se ejecutaras siempre")
print ("Great, you successfully entered an integer!")



try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

try:
    x = float(input("Your number: "))
    print(x)
    inverse = 1.0 / x

except ValueError:
    print ("You should have given either an int or a float")
except ZeroDivisionError:
    print ("Infinity")
finally:
    print("There may or may not have been an exception.")

