if __name__ == '__main__':
    # Uso de yield para parar la ejecución de una función
    def simpleGeneratorFun():
        yield 1
        yield 2
        yield 3


    # Recorre todos los yield
    for value in simpleGeneratorFun():
        print(value)


    # Ejemplo de generador
    def gen_primos():
        """ Generador de números primos."""

        contador = 1
        lista_primos = []

        # Comienza un ciclo infinito.
        while True:
            es_primo = True
            contador += 1
            if len(lista_primos) > 0:
                for primo in lista_primos:
                    if contador % primo == 0:
                        es_primo = False
                        break
            if es_primo:
                lista_primos.append(contador)
                yield contador


    generador = gen_primos()
    print(next(generador))
    for i in range(5):
        print(next(generador))

    # square is a generator
    square = (i * i for i in range(10))
    # add the squares
    total = 0
    for i in square:
        total += i

