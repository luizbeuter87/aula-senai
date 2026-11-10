import re
import datetime

def nome_limpo(nome):
    return re.sub(r"\s+", " ", nome).strip().lower()

def telefone_valido(telefone):
    apenas_numeros = re.sub(r"\D", "", telefone)
    if len(apenas_numeros) == 11:
        return apenas_numeros
    return "telefone inválido"

def data_limpa(data):
    data = data.strip()
    try:
        dt = datetime.datetime.strptime(data, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except ValueError:
        return data

if __name__ == "__main__":
        # Testes simples: rode "python faxina.py" para conferir
        assert nome_limpo("  ana   SOUZA ") == "ana souza"
        assert telefone_valido("(48) 99999-1234") == "48999991234"
        assert telefone_valido("4833334444") == "telefone inválido"
        assert data_limpa("2025-03-05") == "05/03/2025"
        print("Todos os testes de faxina.py passaram.")