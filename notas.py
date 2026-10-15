import csv

alunos_com_media = []

with open("notas.csv", newline="", encoding="utf-8") as n:
    for aluno in csv.DictReader(n):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        if media >= 7.0:
            situacao = "Aprovado(a)"
        else:
            situacao = "Reprovado(a)"
        print(aluno ["nome"], media, situacao)

        aluno["media"] = media
        aluno["situacao"] = situacao
        alunos_com_media.append(aluno)

with open("notas_com_media.csv", "w", newline="", encoding="utf-8") as i:
    fieldnames = ["nome", "nota1", "nota2", "media", "situacao"]
    escritor = csv.DictWriter(i, fieldnames=fieldnames)
    escritor.writeheader()
    escritor.writerows(alunos_com_media)
