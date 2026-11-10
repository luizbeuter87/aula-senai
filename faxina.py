import re, csv
from datetime import datetime

dados = []
fieldnames = ["nome", "telefone", "data"]
with open ("sujo.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for nome, telefone, data in reader:
        nome_limpo = (re.sub(r"\s+", " ", nome)).strip().lower()
        telefone_limpo = (re.sub(r"\D", "", telefone))
        if len(telefone_limpo) == 11:
             telefone_valido = telefone_limpo
        else:
             "telefone invalido" 
        data_limpa = data.strip()
        try:
            dt = datetime.strptime(data_limpa, "%Y-%m-%d")
            data_formatada = dt.strftime("%d/%m/%Y")
        except ValueError:
            data_formatada = data_limpa

        dados.append({
                 "nome": nome_limpo,
                 "telefone": telefone_valido,
                 "data": data_formatada
        })

with open ("limpo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dados)