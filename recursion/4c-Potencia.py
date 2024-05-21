#recursiva
def potencia (x, n):
    #condição de parada se expoente for 0 o resultado é 1
    if(n == 0):
        return 1
    elif(n < 0):
        #se for expoente negativo
        return 1 / potencia(x, -n)
    elif(n > 0):
        #se for positivo
        return x * potencia(x, n-1)

#print(potencia(2,4))

#dinâmica
x = int(input('base'))
n = int(input('expoente'))
fix = x
cont = 0

if(n>0):
    while cont < n-1:
        x = x * fix
        cont=cont+1

    print(x)
elif(n==0):
    print(1)
else:
    #transforma n em positivo pra poder fazer o mesmo cálculo
    n = n * (-1)
    while cont < n-1:
        x = x * fix
        cont=cont+1
    print(1/x)

