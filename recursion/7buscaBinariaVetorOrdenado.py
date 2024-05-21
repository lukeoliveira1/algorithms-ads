def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if A[meio] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 20))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 0))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 70))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 100))

def pesquisa_binaria(A, item):
    """Implementa pesquisa binária iterativamente."""
    #leva o item pro meio para ser retornado
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria(A, 20))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 0))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 70))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 100))