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

        alunos_com_media.append({
            "nome" : aluno["nome"],    
            "media" : media,
            "situacao" : situacao
})

with open("notas_com_media.csv", "w", newline="", encoding="utf-8") as m:
    escritor = csv.DictWriter(m, fieldnames=["nome", "media", "situacao"])
    escritor.writeheader()
    escritor.writerows(alunos_com_media)
    