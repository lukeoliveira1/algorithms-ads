#n quantidade de discos
#a,b,c pinos
def mover( n, a, b, c):
    if (n > 0):          #1 rodada    ##2rodada 
        mover(n-1,a,c,b) #a1 b2 c3    ##a1 b3 c2
        print(a," -> ",b,"\n")
        mover(n-1,c,b,a); #a3 b2 c1   ##a2 b3 c1
       
n = 4; 
print("Numero de discos: ", n)
print("Solucao para ", n," discos: "); 
mover(n,1,3,2);  
