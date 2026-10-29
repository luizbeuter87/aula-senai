def e_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def calcular_imc(peso, altura):
    return peso / (altura**2)


ano = int(input("insira um ano para saber se é bissexto: "))

if e_bissexto(ano):
    print(f"o ano de {ano} é bissexto!")
else:
    print(f"o ano de {ano} não é bissexto!")

peso_t = input("insira seu peso: ").replace (",", ".")
peso = float(peso_t)
altura_t = input("insira sua altura em metros: ").replace (",", ".")
altura = float(altura_t)
imc = calcular_imc(peso, altura)

print (f"Seu imc é {imc:.2f}")  # .2f para mostrar apenas 2 casas decimais