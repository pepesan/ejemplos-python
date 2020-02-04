# -*- coding: utf-8 -*-

def procedimiento():
    print("procedimiento")

procedimiento()

def suma(x, y):
    """Devuelve x + y"""
    print("x:",x)
    print("y:", y)
    return x + y

suma(4,7)
# res = 5
res=suma(2,3)
print("Resultado: ",res)

res=suma(4,9)
print(res)

res=suma (2,y=3)
print(res)

res=suma (x=2,y=3)
print(res)

res=suma (y=3,x=2)
print(res)



def resta(x, y=1):
    """parámetro opcional"""
    return x - y

# x=5, y=1
res=resta(5)
print(res)
res=resta(5,2)
print(res)
res=resta(y=5,x=2)
print(res)

def restaTres(x=0,y=0,z=0):
    return x-y-z

# x=0, y=0,z=0
print(restaTres())
# x=2, y=0,z=0
print(restaTres(2))
# x=2, y=3,z=0
print(restaTres(2, 3))
# x=2, y=3,z=4
print(restaTres(2, 3, 4))
#y=2
print(restaTres(y=2))
#z=2
print(restaTres(z=2))



def multi(x=2,y=3):
    return x*y

# x=2 , y=3
res=multi()
print(res)
# x=4 , y=3
res=multi(4)
print(res)
# x=4 , y=5
res=multi(4,5)
print(res)

# x=3 , y=5
res=multi(3,5)
print(res)

# x=2 , y=3
res=multi(y=3)
print(res)


# def a(c=None):
def a(c=0):
    return 100 + c

# def b(n=120):
def b(n=a(20)):
    return n + 50

# imprime 70
print(b(20))

# imprime 170
print(b())



def f(*args):
    return args

print("Parámetros variable en número",f(1, 5, True, False, "Hello, world!"))

print("Parámetros variable en número",f(1, 5))


def f(*args, **kwargs):
    return args, kwargs

args, kwargs = f(True, False, 3.5, message="Hello, world!", year=2014)
print(args)
#(True, False, 3.5)
print(kwargs)
#{'message': 'Hello, world!', 'year': 2014}


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(2))

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

print(factorial(5))


def sumados(x):
    x = x+2
    return x
res=sumados(3)
print("resultado:",res)
x=3
res= sumados(x)
print("X:",x)
print("resultado:",res)

def restados(x):
    x = x-2

res= restados(3)
print("Res:", res)

print("Resta:",restados(4))

print("Resta:",restados(7))