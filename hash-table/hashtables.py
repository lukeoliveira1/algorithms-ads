class Component:
    def __init__(self, id, status, location):
        self.id = id
        self.status = status
        self.location = location

    def __str__(self) -> str:
        return f"{self.id} - {self.status} - {self.location}"


hash_components = {}


def add_component(id, status, location):
    component = Component(id, status, location)
    hash_components[id] = component


def update_component(id, new_status, nova_location):
    if id in hash_components:
        hash_components[id].status = new_status
        hash_components[id].location = nova_location
    else:
        print("Component não encontrado.")


def delete_component(id):
    if id in hash_components:
        del hash_components[id]


def get_component(id):
    return hash_components.get(id, "Component não encontrado.")


def get_all_components():
    for i in hash_components:
        print(hash_components[i])


add_component(1, "Em produção", "Setor A")
add_component(2, "Em produção", "Setor B")
add_component(3, "Em produção", "Setor C")
update_component(1, "Finalizado", "Estoque")
delete_component(1)
get_all_components()

# Colisões

# As colisões ocorrem quando dois elementos precisam ser inseridos na mesma posição em uma tabela hash.

# Como, por exemplo, temos o valor 'Abacate' na chave '1' e precisamos inserir o valor 'Abacaxi' na mesma chave.

# Para contornar esse problema é criado uma lista na posição 1, e os dois valores podem ser inseridos na mesma chave.

# Logo, ao acessar o valor 1 na hash será retornado a lista ['Abacate', 'Abacaxi']
