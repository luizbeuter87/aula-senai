import json

contato = [
    {"nome": "joao", "telefone": "3333-3333", "cidade": "natal"},
    {"nome": "ana", "telefone": "4444-4444", "cidade": "cuiaba"},
    {"nome": "luiz", "telefone": "5555-5555", "cidade": "sorocaba"},
    {"nome": "jose", "telefone": "6666-6666", "cidade": "curitiba"}
]

with open("contatos.json", "w", encoding="utf8") as file:
    json.dump(contato, file, indent=2, ensure_ascii=False)

busca = input("digite uma cidade: ").strip()

encontrados = []
with open("contatos.json", "r", encoding="utf-8") as file:
    lido = json.load(file)
    for b in lido:
        if b["cidade"].lower() == busca:
            encontrados.append(b)

    if encontrados:
        for b in encontrados:
            print(f'{b["nome"]} - {b["telefone"]} - {b["cidade"]}')
    else:
        print(f'nenhum contato encontrado na cidade de: {busca}')
