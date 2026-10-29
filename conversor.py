import csv, json

dados = []
with open ("notas.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for aluno, nota1, nota2 in reader:
        nota1_n = float(nota1)
        nota2_n = float(nota2)

        dados.append({
            "aluno" : aluno.strip(),
            "nota1" : nota1_n,
            "nota2" : nota2_n
        })

with open("dados.json", "w", encoding="utf-8") as out:
    json.dump(dados, out, ensure_ascii=False, indent=2)

print(f"Convertido! {len(dados)} alunos salvos em dados.json")
print(json.dumps(dados, ensure_ascii=False, indent=2))