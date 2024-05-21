def fibonacci_recursivo(cont):
    #condição de parada cont == 1
    #se quiser o primeiro ou segundo termo de fibonacci o retorno é 1
    if(cont < 2):
        return 1
    else:
    #se quiser acima do segundo termo faz a soma dos anteriores
        return fibonacci_recursivo(cont-1) + fibonacci_recursivo(cont-2) 

print(fibonacci_recursivo(5))

print("\n")

#dinâmico
#imprimindo a sequencia até a posição desejada
fib = 1
a = 0
b = 1
cont = 0

while(cont < 5):
    print(fib)
    fib = a + b #fib 1
    a = b   #a 2
    b = fib #b 2
    cont=cont+1
