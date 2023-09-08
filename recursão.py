def somatorio(n):
    #condição de parada n == 1
    #se for n==2, faz 2 + n-1(1)
    #se for n==3, faz 3 + n-1(2) + n-1(1)
    #se for n==4, faz 4 + n-1(3) + n-1(2) + n-1(1)
    if(n==1):
        return 1
    else:
        return n + somatorio(n-1)

# print(somatorio(5))

import random

def procura(x, v, n):
    #procurando do final pro começo do vetor
    try:    
        #condição de parada se a posição do vetor for x
        if(v[n] == x):
            #retorna a posição
            return n;
        else:
            return procura(x, v, n-1)
    except:
        return "number wasn't found"

n = 20
v = [random.randint(1, 20) for i in range(20)]

# print(v, " ")
# x = 18
# #preencher vetor e testar
# print("posição do elemento no vetor: ",procura(x, v,    n-1))
    
def fibonacci_recursivo(n):
    if n < 2:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
# print(fibonacci_recursivo(4))

def fatorial_recursivo(n):
    if n < 2:
        return 1
    else:
        return n * fatorial_recursivo(n-1)

# print(fatorial_recursivo(5))

def potencia_recursiva(base, expoente):
    if expoente < 2:
        return base
    else:
        return base * potencia_recursiva(base, expoente-1)

# print(potencia_recursiva(4, 3))

def mdc(num1, num2):
    cont = 1
    mdc = 0

    if num1 > num2:
        while cont < num1:
            if num1 % cont == 0 and num2 % cont == 0:
                mdc = cont
            cont += 1
    else:
        while cont < num2:
            if num1 % cont == 0 and num2 % cont == 0:
                mdc = cont
            cont += 1
    return mdc

# print(mdc(10, 20))

def mdc_recursivo(num1, num2):
    if(num2 == 0): #num1=36 num2=12
        return num1 ##segunda_rodada num2==0, return num1
    else:                                       
        return mdc_recursivo(num2, num1 % num2) #mdc(12, 0) primeira_rodada
    
# print(mdc_recursivo(10, 20))

def pesquisa_binaria_recursiva(A, esquerda, direita, item):
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


