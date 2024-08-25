# Grafos

# Algoritmo de Dijkstra:

# Qual o caminho mais curto (com menor peso) de A até B?

# Para grafos ponderados(com pesos), o algoritmo de Dijkstra é a melhor opção.
# Não funciona para grafos com pesos negativos.


# inicio -> a = 6
# inicio -> b = 2

# a -> fim = 1
# b -> fim = 5

# b -> a = 3

grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# a tabela de custos
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# a tabela de pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []


def encontrar_nodo_com_menor_custo(custos):
    menor_custo = float("inf")
    nodo_com_menor_custo = None
    # Percorrer cada nodo. (nodo = chave(ex. A, B))
    for nodo in custos:
        custo = custos[nodo]
        # Se for o menor custo até agora e ainda não foi processado...
        if custo < menor_custo and nodo not in processados:
            # ... defina-o como o novo nodo com menor custo.
            menor_custo = custo
            nodo_com_menor_custo = nodo
    return nodo_com_menor_custo


# Encontre o nodo com menor custo que ainda não foi processado.
nodo = encontrar_nodo_com_menor_custo(custos)
# Se você já processou todos os nodos, este loop while termina.
while nodo is not None:
    custo = custos[nodo]
    # Percorra todos os vizinhos deste nodo.
    vizinhos = grafo[nodo]
    for v in vizinhos.keys():
        novo_custo = custo + vizinhos[v]
        # Se for mais barato chegar a este vizinho passando por este nodo...
        if custos[v] > novo_custo:
            # ... atualize o custo para este nodo.
            custos[v] = novo_custo
            # Este nodo se torna o novo pai para este vizinho.
            pais[v] = nodo
    # Marque o nodo como processado.
    processados.append(nodo)
    # Encontre o próximo nodo para processar e continue o loop.
    nodo = encontrar_nodo_com_menor_custo(custos)

print("Custo do início para cada nodo:")
print(custos)
