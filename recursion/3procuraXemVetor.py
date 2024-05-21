import numpy as np

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
v = np.random.randint(1, 20, n)
print(v, " ")
x = 18
#preencher vetor e testar
print("posição do elemento no vetor: ",procura(x, v,    n-1))