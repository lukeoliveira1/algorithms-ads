# 1 - Leia uma
# matriz 8 x 8 e a transforme numa matriz triangular inferior , atribuindo
# zero a todos os elementos acima da diagonal principal, escrevendo-a ao
# final.

def one():

    matriz = [[0 for j in range(8)] for i in range(8)]

    for i in range(8):
        for j in range(8):
            if(i >= j):
                matriz[i][j] = 1

    for i in range(8):
        for j in range(8):
            print(matriz[i][j], end=" ")
        print("")

# 2 - Leia uma
# matriz 8x 8 e escreva o maior elemento da diagonal principal e a soma dos
# elementos da diagonal secundaria.
def two():
    import random

    matriz = [[random.randint(1 , 9) for j in range(8)] for i in range(8)]
    maior_num = 0;

    for i in range(8):
        for j in range(8):
            print(matriz[i][j], end=" ")
        print("")
            
    print("diagonal principal")
    for i in range(8):
            for j in range(8):
                if(i == j):
                    print(matriz[i][j], end=" ")
                    if matriz[i][j] > maior_num:
                        maior_num = matriz[i][j]

    print(f"o maior número: {maior_num}")

# 4 - Leia uma
# matriz 100 x 10 que se refere respostas de 10 questões de múltipla
# escolha, referentes a 100 alunos. Leia também um vetor de 10 posições
# contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa
# deverá comparar as respostas de cada candidato com o gabarito e emitir um
# vetor Resultado, contendo a pontuação correspondente. 
import random

respostas = ('A', 'B', 'C', 'D')

matriz_respostas = [[random.choice(respostas) for j in range(10)] for i in range(10)]

for i in range(8):
        for j in range(8):
            print(matriz_respostas[i][j], end=" ")
        print("")

matriz_gabarito = [['A' for j in range(10)] for i in range(10)]
print("\nGabarito: \n", matriz_gabarito[1], "\n")

quantos_acertos_por_linha = 0;

for i in range(8):
        for j in range(8):
             if matriz_respostas[i][j] == matriz_gabarito[i][j]:
                  quantos_acertos_por_linha += 1;
        print(f"linha {i} acertou {quantos_acertos_por_linha} questões")
        quantos_acertos_por_linha = 0