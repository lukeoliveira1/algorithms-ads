import random

def pesquisa_binaria(lista, item):
    baixo = 0;
    alto = len(lista)-1

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

minha_lista = [random.randint(1, 8) for j in range(10)]
print(minha_lista)
print(pesquisa_binaria(minha_lista, 8))


####












def pesquisa_binaria_new(arr):
    meio = len(arr) // 2
    