def media(notas):
    return sum(notas) / len(notas)

def desconto(preco, percentual=10):
    return preco - preco * percentual / 100

def estatistica(notas):
    return min(notas), media(notas), max(notas)

def situacao(media_valor):
    if media_valor >= 7:
        return "Aprovado!"
    return "Reprovado"

notas = [6.5, 8.5, 9.0, 5.5, 8.0]

valor_compra_t = input("qual valor da compra? ").replace(",", ".")
valor_compra = float(valor_compra_t)
desconto_padrao = desconto(valor_compra)
desconto_posicional = desconto(valor_compra, 25)
desconto_declarado = desconto(percentual=50, preco=valor_compra)
print(f"valor com o desconto padrao é {desconto_padrao}") 
print(f"valor com desconto posicional: {desconto_posicional}")
print(f"valor com desconto declarado: {desconto_declarado}")

nota_min, nota_media, nota_max = estatistica(notas)
print(f"\nnota minima: {nota_min}, nota média: {nota_media}, nota máxima: {nota_max}")
print("Sua média foi:", nota_media, "situação:", situacao(nota_media))