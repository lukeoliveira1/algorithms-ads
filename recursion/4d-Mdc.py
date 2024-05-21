#recursiva
def mdc(num_one, num_two):
    if(num_two == 0): #num_one=36 num_two=12
        return num_one ##segunda_rodada num_two==0, return num_one
    else:                                       
        return (num_two, num_one % num_two) #mdc(12, 0) primeira_rodada
  
print(mdc(36,48))
#dinâmica
num_one = int(input("número 1: "))
num_two = int(input("núemro 2: "))
mdc = 0
i = 1 #cont para as divisões

if(num_one > num_two):
    while i < num_one:
        if(num_one % i == 0 and num_two % i == 0):
            mdc = i
        i=i+1
else:
    while i < num_two:
        if(num_one % i == 0 and num_two % i == 0):
            mdc=i
        i=i+1

print(mdc)

