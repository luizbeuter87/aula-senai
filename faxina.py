import csv
import limpeza

dados = []
fieldnames = ["nome", "telefone", "data"]
with open ("sujo.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    cabecalho = next(reader, None)  # pula o cabeçalho
    
    for linha in reader:
        if not linha:
                continue
        nome, telefone, data = linha

        nome_limpo = limpeza.nome_limpo(nome)
        telefone_valido = limpeza.telefone_valido(telefone)
        data_limpa = limpeza.data_limpa(data)

        dados.append({
                 "nome": nome_limpo,
                 "telefone": telefone_valido,
                 "data": data_limpa
                 })

with open ("limpo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dados)