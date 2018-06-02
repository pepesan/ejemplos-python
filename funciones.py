# -*- coding: utf-8 -*-


def suma(x, y):
    """Devuelve x + y"""
    print("x:",x)
    print("y:", y)
    return x + y

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

res=resta(5)
print(res)
res=resta(5,2)
print(res)
res=resta(y=5,x=2)
print(res)


def multi(x=2,y=3):
    return x*y

res=multi()
print(res)

res=multi(2)
print(res)

res=multi(2,3)
print(res)

res=multi(3,5)
print(res)

res=multi(y=3)
print(res)


# def a(c=None):
def a(c=0):
    return 100 + c

def b(n=a(20)):
    return n + 50

print(b(20))

print(b())



def f(*args):
    return args

print(f(1, 5, True, False, "Hello, world!"))

print(f(1, 5))


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

print(factorial(5))

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

print(factorial(5))