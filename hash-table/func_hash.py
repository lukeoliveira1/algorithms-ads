hash_table = {}


def key_hash(number):
    return ((2 * number) + 5) % 11


def add_value(number):
    key = key_hash(number)

    if not key in hash_table:
        hash_table[key] = number
    else:
        current_value = hash_table[key]

        if type(current_value) == list:
            current_value.append(number)
        else:
            new_list = []
            new_list.append(current_value)
            new_list.append(number)
            hash_table[key] = new_list


values = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

for i in values:
    add_value(i)

print(hash_table.items()) 
