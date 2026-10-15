cadastro_pessoa = [
    {"nome": "Luiz", "idade": 38, "telefone": "3333-3333", "endereço": "Av. central"},
    {"nome": "Maria", "idade": 25, "telefone": "4444-4444", "endereço": "Rua das Flores"},
    {"nome": "João", "idade": 40, "telefone": "5555-5555", "endereço": "Travessa dos Sonhos"},
    {"nome": "Ana", "idade": 30, "telefone": "6666-6666", "endereço": "Avenida Brasil"},
    {"nome": "Carlos", "idade": 28, "telefone": "7777-7777", "endereço": "Rua das Palmeiras"}
]

def busca_pessoa(nome):
    for pessoa in cadastro_pessoa:
        if pessoa["nome"].lower() == nome.lower():    #lower() para ignorar maiúsculas e minúsculas
            return pessoa
    return None

if pessoa := busca_pessoa(input("Digite o nome da pessoa que deseja buscar: ")):
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Telefone: {pessoa['telefone']}")
    print(f"Endereço: {pessoa['endereço']}")
else:
    print("Pessoa não encontrada.")
