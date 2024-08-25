# Grafos

# Pesquisa em largura:
# Existe algum caminho de A até B?
# Qual o caminho mínimo de A até B?

from collections import deque

grafo = {}
grafo["luke"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedora(name):
    return name[-1] == "m"


def fila_de_pesquisa(name):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[name]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedora(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False


fila_de_pesquisa("luke")
