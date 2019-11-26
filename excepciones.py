# -*- coding: utf-8 -*-
"""
Uso básico de Excepción
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
"""
Excepciones Encadenadas
"""
try:
    f = open("test.txt", encoding='utf-8')
    # perform file operations
except:
    print("Fallo al abrir")
finally:
    try:
        f.close()
    except Exception as e:
        print("No se ha podido cerrar, porque no estaba abierto")
        print("Error:" + str(e))
"""
Captura de excepción ValueError
"""
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
    finally:
        print("Se ejecutaras siempre")
print("Great, you successfully entered an integer!")
"""
Uso de Else 
"""
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
"""
Uso de Finally
"""
try:
    x = float(input("Your number: "))
    print(x)
    inverse = 1.0 / x

except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")

"""
Elevar una excepción
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
"""
Acceso a parámetros de excepción
"""
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)

"""
Excepciones personalizadas
"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
"""
Excepciones personalizadas más completo
"""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


class HTTPExcepcion(Exception):

    def __init__(self, mensaje='HTTPERROR: ', status='400', url='telecable.es'):
        self.mensaje = mensaje
        self.status = status
        self.url = url

    def __str__(self):
        return self.mensaje


try:
    raise HTTPExcepcion("HTTPERROR: el servidor no responde", '500', "cursosdedesarrollo.com")
except HTTPExcepcion as e:
    print(e)
    print(e.mensaje)
    print(e.url)
    print(e.status)
