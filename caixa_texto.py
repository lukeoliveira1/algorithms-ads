def criar_caixa(largura, altura, mensagem):
    if len(mensagem) > largura - 2:
        mensagem = mensagem[:largura - 3] + "..."
    print('*' * (largura + 2))
    for _ in range(altura):
        print('*' + ' ' * largura + '*')
    print('* ' + mensagem.center(largura) + ' *')
    for _ in range(altura):
        print('*' + ' ' * largura + '*')
    print('*' * (largura + 2))

def main():
    largura = int(input("Digite a largura da caixa (em caracteres): "))
    altura = int(input("Digite a altura da caixa (em linhas): "))
    mensagem = input("Digite a mensagem de linha única: ")
    criar_caixa(largura, altura, mensagem)

if __name__ == "__main__":
    main()
