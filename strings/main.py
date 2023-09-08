import re

def change_text(string):
    string = str(input())

    #alterando a string 
    string = re.sub("o", "0", string) 
    string = re.sub("O", "0", string)
    string = re.sub("l", "1", string)
    string = re.sub("L", "1", string)
    string = re.sub(",", "", string)
    string = re.sub(" ", "", string)

    print(string)

## outra

import re
import textwrap #para edições no texto

def text_to_html(text: str) -> str:

    #default configuration
    # replace_whitespace substituirá cada caractere de espaço em branco por um único espaço
    wrapper = textwrap.TextWrapper(width=80, replace_whitespace="")

    #alterações na string
    text = re.sub("[ ]?<hr>[ ]?", "\n" + "-" * 80 + "\n", text)

    text = re.sub("[ ]?<br>[ ]?", "\n", text)

    new_text = wrapper.fill(text) #criando uma nova string com as configurações do wrapper

    return new_text

text = "Hallo, dies ist eine ziemlich lange Zeile, die in Html aber nicht umgebrochen wird. <br> Zwei <br> <br>  produzieren zwei Newlines. Es gibt auch noch das tag <hr> was einen Trenner darstellt. Zwei <hr> <hr> produzieren zwei   Horizontal Rulers. Achtung mehrere Leerzeichen irritieren Html genauso wenig wie mehrere Leerzeilen."
# print(text_to_html(text))

# outra

import re

# input_one = "7a5a6adfg4a4adsfgsd9fg6aa904aa91#$%11.23" 
input_one = "11#$%11111*&¨1111&*(1198-=&8789.\"34\"8" 

#pegar padrão com ponto na entrada 
list_input_cpf_and_rest = re.findall('[\d\.]', input_one) 
#transformando a lista de cima em string 
string_list_input_cpf_and_rest = "".join(list_input_cpf_and_rest)
#tirando os 11 primeiros 
list_resto = re.sub('[\d]{11}', "", string_list_input_cpf_and_rest)

#criando strings vazias para receber o cpf e o restante que sobrar da entrada
string_cpf = ""
string_rest = ""

for i in list_input_cpf_and_rest:
    #enquanto o cpf tiver menos de 11 caracteres ele vai ser preenchido
    if(len(string_cpf) < 11):
        string_cpf += i

    #função count para ver se tem mais de um ponto
    if (list_input_cpf_and_rest.count(".") > 1):
        print("invalid input, should be less than one comma")
        exit()

#preenchendo o resto
for i in list_resto:
    string_rest += i

#Deixar apenas duas casas decimais
rest_float = float(string_rest) 
#joga as duas casas decimais para esquerda e ignora o restante que ficar em casas decimais
rest_without_decimal_places = int(rest_float * 100)
#deixa só as duas casas decimais que eu quero
result_rest = rest_without_decimal_places / 100

print('cpf: ', string_cpf)
print('rest: ', result_rest)

# input_two = "42**&774667" 
input_two = "%(&567.22%99"

list_input_two = re.findall('[\d\.]', input_two)  

#string vazia para receber o número da entrada dois
string_input_two = ""

for i in list_input_two:

    #preenchendo a string do número da entrada dois    
    string_input_two += i

    #função count para ver se tem mais de um ponto
    if (list_input_two.count(".") > 1):
        print("invalid input, should be less than one comma")
        exit()

#Deixar apenas duas casas decimais
input_two_float = float(string_input_two) 
#joga as duas casas decimais para esquerda e ignora o restante que ficar em casas decimais
input_two_without_decimal_places = int(input_two_float * 100)
#deixa só as duas casas decimais que eu quero
result_input_two = input_two_without_decimal_places / 100

#soma
print("sum: ", float(result_rest) + float(result_input_two))