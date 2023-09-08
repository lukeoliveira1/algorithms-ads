cont = 0
with open("control_f/corpus.txt", "r", encoding='utf-8') as document:
    #readlines return a list with each line inside the file
    for linha in document.readlines():
        #find return the index of first occurrence of a sub-string within a string
        if(linha.find('garrafa')> -1):
        #count return many times a substring occurs within a string
            cont += linha.count('garrafa') 
            # print index + line within occurrence of sub-string
            print(linha.find('garrafa'), linha) 

print("repetições: ", cont)
            
