#cria o arquivo diario.txt "w"
#with open("diario.txt", "w", encoding="utf-8") as arquivo:
#   arquivo.write("diario linha 01\n")    #\n pula pra próxima linha
#   arquivo.write("diario linha 02\n")
#   arquivo.write("diario linha 03\n")

#Adiciona ao final do arquivo as linhas com "a"
#with open("diario.txt", "a", encoding="utf-8") as arquivo:
#    arquivo.write("diario linha 04\n")
#    arquivo.write("diario linha 05\n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    contador = 1  # adiciona contador
    for linha in arquivo:
        print(contador, ":", linha.strip()) #strip retira o espaço a mais entre as linhas que já foi dado no \n
        contador = contador +1 

