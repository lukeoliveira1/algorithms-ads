## Fator de carga

# Nº de elementos / Nº de posições

# Ideal é que o fator de carga seja menor que 0.7

# Se o fator de carga for maior que 0.7, a tabela hash deve ser redimensionada

class TabelaHash:
    def __init__(self, tamanho_inicial):
        self.tamanho = tamanho_inicial
        self.tabela = [None] * tamanho_inicial
        self.num_elementos = 0  

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def _redimensionar(self):
        novo_tamanho = self.tamanho * 2
        nova_tabela = [None] * novo_tamanho

        for item in self.tabela:
            if item:
                chave, valor = item
                novo_index = hash(chave) % novo_tamanho
                nova_tabela[novo_index] = (chave, valor)

        self.tabela = nova_tabela
        self.tamanho = novo_tamanho

    def inserir(self, chave, valor):
        if self.num_elementos / self.tamanho > 0.7:  # Fator de carga
            self._redimensionar()

        index = self._hash(chave)
        self.tabela[index] = (chave, valor)
        self.num_elementos += 1

    def buscar(self, chave):
        index = self._hash(chave)
        par = self.tabela[index]
        if par and par[0] == chave:
            return par[1]
        return None

    def remover(self, chave):
        index = self._hash(chave)
        par = self.tabela[index]
        if par and par[0] == chave:
            self.tabela[index] = None
            self.num_elementos -= 1


hash_tabela = TabelaHash(4)
hash_tabela.inserir("chave1", "valor1")
hash_tabela.inserir("chave2", "valor2")
hash_tabela.inserir("chave3", "valor3")
hash_tabela.inserir("chave4", "valor4")  # Redimensionamento

print(hash_tabela.buscar("chave1"))  
print(hash_tabela.buscar("chave2"))  
