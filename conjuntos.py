if __name__ == '__main__':
    # Creación de un conjunto con elementos únicos
    conjunto = {1, 2, 3, 4}
    print(conjunto)
    # Resultado: {1, 2, 3, 4}

    # También puedes crear un conjunto desde una lista, eliminando duplicados automáticamente
    lista = [1, 2, 2, 3, 4, 4]
    conjunto = set(lista)
    print(conjunto)
    # Resultado: {1, 2, 3, 4}

    # Usando add() para agregar un elemento
    conjunto = {1, 2, 3}
    conjunto.add(4)
    print(conjunto)
    # Resultado: {1, 2, 3, 4}

    # Usando remove() para eliminar un elemento (lanza un error si no existe)
    conjunto.remove(3)
    print(conjunto)
    # Resultado: {1, 2, 4}

    # Usando discard() para eliminar un elemento (no lanza error si no existe)
    conjunto.discard(5)
    print(conjunto)
    # Resultado: {1, 2, 4} (sin error)

    # Usando clear() para vaciar el conjunto
    conjunto.clear()
    print(conjunto)
    # Resultado: set()



    conjunto1 = {1, 2, 3}
    conjunto2 = {3, 4, 5}
    union = conjunto1.union(conjunto2)
    print(union)
    # Resultado: {1, 2, 3, 4, 5}

    interseccion = conjunto1.intersection(conjunto2)
    print(interseccion)
    # Resultado: {3}

    diferencia = conjunto1.difference(conjunto2)
    print(diferencia)
    # Resultado: {1, 2}

    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
    print(diferencia_simetrica)
    # Resultado: {1, 2, 4, 5}

    conjunto_a = {1, 2}
    conjunto_b = {1, 2, 3, 4}
    es_subconjunto = conjunto_a.issubset(conjunto_b)
    print(es_subconjunto)
    # Resultado: True

    es_superconjunto = conjunto_b.issuperset(conjunto_a)
    print(es_superconjunto)
    # Resultado: True

    conjunto = {1, 2, 3, 4}
    for elemento in conjunto:
        print(elemento)
    # Imprime cada elemento en el conjunto (el orden no está garantizado)

    conjunto = {1, 2, 3}
    lista = list(conjunto)
    print(lista)
    # Resultado: [1, 2, 3]

