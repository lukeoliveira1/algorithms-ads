# def inverter(lista):
#     if not lista: # lista vazia, retorna ela mesma
#         return lista
#     return lista[-1:] + inverter(lista[:-1])
#     #[-1:]constrói outra lista contendo apenas o último elemento de lista [5]
#     #[:-1]constrói outra lista contendo do primeiro ao penúltimo elemento de lista [1,2,3,4]
#     # pega o último elemento da lista e junta com o inverso do restante da lista.

# lista = inverter([1, 2, 3, 4, 5])
# print(lista) # [5, 4, 3, 2, 1]

import numpy as np

#recursivo
def inverter_vetor(arr, inicio, final):
    if(inicio == final):
        return arr
    else:
        if(inicio < final):
            aux = arr[inicio]
            arr[inicio] = arr[final]
            arr[final] = aux
            #print("inicio vetor: ", inicio)
            #print("final vetor: ", final)
            #inicio+=1
            #final-=1
            return inverter_vetor(arr, inicio+1, final-1)

total=10
arr = np.random.randint(1,10,size=total)
print(arr)
print(inverter_vetor(arr, 0, total))

#dinâmico
total=10
# + de 30min
arr = np.random.randint(1,10,size=total)
print(arr)

final_vetor= total-1
inicio_vetor = 0

while inicio_vetor != final_vetor: 
    if(inicio_vetor < final_vetor):
        aux = arr[inicio_vetor]
        arr[inicio_vetor] = arr[final_vetor]
        arr[final_vetor] = aux
        #print("inicio vetor: ", inicio_vetor)
        #print("final vetor: ", final_vetor)
        inicio_vetor+=1
        final_vetor-=1
    else:
        break;

print(arr)


