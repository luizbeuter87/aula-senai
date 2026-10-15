import csv

with open("notas.csv", newline="", encoding="utf-8") as n:
    for aluno in csv.DictReader(n):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        if media >= 7.0:
            situacao = "Aprovado(a)"
        else:
            situacao = "Reprovado(a)"
        print(aluno ["nome"], media, situacao)
