def somatorio(n):
    #condição de parada n == 1
    #se for n==2, faz 2 + n-1(1)
    #se for n==3, faz 3 + n-1(2) + n-1(1)
    #se for n==4, faz 4 + n-1(3) + n-1(2) + n-1(1)
    if(n==1):
        return 1
    else:
        return n + somatorio(n-1)

print(somatorio(5))