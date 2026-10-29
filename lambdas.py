alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
    {"nome": "Carla", "nota": 7.0},
    {"nome": "Diego", "nota": 5.5},
    {"nome": "Elisa", "nota": 8.2},
]

ordem_decrescente = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
print("notas em ordem Decrescente:")
for aluno in ordem_decrescente:
    print("-", aluno["nome"], aluno["nota"])

nota_maior_7 = list(filter(lambda aluno: aluno["nota"] >= 7, ordem_decrescente))
print("Aprovados:", [aluno["nome"] for aluno in nota_maior_7])