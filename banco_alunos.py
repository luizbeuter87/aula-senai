alunos = [
    {"nome": "Luiz", "nota": 8.5},
    {"nome": "Marcos", "nota": 9.0},
    {"nome": "Ana", "nota": 6.5},
    {"nome": "Julia", "nota": 7.0}
]

contador_aprovados = 0

for aluno in alunos:
    if aluno["nota"] >= 7 :
        print(aluno["nome"], "Aprovado(a)")
        contador_aprovados = contador_aprovados + 1
    
print("\nAlunos aprovados: ", contador_aprovados)
    