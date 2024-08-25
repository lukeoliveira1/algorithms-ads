import random


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = sorted([random.randint(1, 1000000) for _ in range(1000000)])

item = 200
result = pesquisa_binaria(minha_lista, item)
print(f"Índice de {item}: {result}")
