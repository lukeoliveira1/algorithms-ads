def fatorial_recursiva(n):
    if(n == 1):
        return 1
    else:
        return n * fatorial_recursiva(n-1)

print(fatorial_recursiva(4))

#dinâmica
cont = 0
n=5
fat=1
a=1
while(cont < n):
    fat = fat * a
    a=a+1
    cont=cont+1

print(fat)
