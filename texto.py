import re
import datetime

def so_digitos(texto):
    return re.sub(r"\D", "", texto)

def normalizar_nome(nome):
    return re.sub(r"\s+", " ", nome).strip().title()

def formatar_data(texto):
    return datetime.datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")

if __name__ == "__main__": # Este bloco só roda quando o arquivo é executado direto (python texto.py),
    # e NÃO quando ele é importado por outro arquivo.
    print(so_digitos("(48) 99999-1234"))
    print(normalizar_nome("  ana   SOUZA "))
    print(formatar_data("05/03/2025"))