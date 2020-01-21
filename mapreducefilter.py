if __name__ == '__main__':
    def multiply(x):
        return (x * x)


    def add(x):
        return (x + x)


    funcs = [multiply, add]
    for i in range(5):
        #mapea las dos funciones
        value = list(map(lambda x: x(i), funcs))
        print(value)

    number_list = range(-5, 5)
    # filtra aquellos que sean menor que cero
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)

    from functools import reduce
    # aplica una función por pares de números
    # primero multiplica los dos primeros luego el resto
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print(product)