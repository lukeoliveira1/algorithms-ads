def soma(x, y):
    print(x + y)

    k = input("Digite 1 se desejar executar o programa novamente: ")
    if(k == '1'):
        return soma(x, y)
    else:
        exit()

soma(4, 3)