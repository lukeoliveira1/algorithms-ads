# 1 - Crie uma matriz 10x10 com elementos aleatórios no intervalo [0,20]:
# a. Imprima todos os elementos
# b. Imprima todos os elementos de uma linha informada pelo usuário
# c. Imprima todos os elementos de uma coluna informada pelo usuário
# d. Imprima a soma dos elementos de uma linha informada pelo usuário
# e. Imprima a soma dos elementos de uma coluna informada pelo usuário
import random

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint(1, 8)

for i in range(10):
    for j in range(10):
        print(matriz[i][j], end=" ")
    print("")

choose_line = int(input("Escolha a linha para imprimir"))

for i in range(10):
    if i == choose_line:
        for j in range(10):
            print(matriz[i][j], end=" ")
        print("")

choose_col = int(input("Escolha a linha para imprimir"))

for i in range(10):
    for j in range(10):
        if i == choose_col:
            print(matriz[j][i], end=" ")
            print("")