# Iteradores
lista = ['1', 2, 'tres', 4.0]
print(lista)
iterador = iter(lista)
print(iterador)
print(next(iterador))
for i in iterador:
    print(i)

