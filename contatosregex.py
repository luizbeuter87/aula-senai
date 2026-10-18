#Cria o arquivo contatos.csv
#import csv

#with open("contatos.csv", "w", newline="", encoding="utf-8") as file:
#    writer = csv.writer(file)
#    writer.writerow(["Nome", "Telefone"])
#    writer.writerows([
#                    ["Joao", "(11) 98765-4321"],
#                    ["jose", "21 91234-5678"],
#                    ["maria", "(31) 998765432"],
#                    ["ana", "(41) 98765 4321"],
#                    ["carlos", "51 91245678"]
#])


#importando e configurando o regex para validar os telefones do arquivo contatos.csv
import re, csv

with open("contatos.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho
    for nome, telefone in reader:
        limpo = (re.sub(r"\D", "", telefone))  # Remove todos os caracteres que não são numeros do telefone)  

        if len(limpo) == 11:
            print("telefone valido", nome, "-", limpo)
        else:
            print("telefone invalido", nome, "-", limpo)
    