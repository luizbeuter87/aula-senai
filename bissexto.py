ano__txt = input('Insira um ano para saber se é bissexto: ')
ano = int(ano__txt)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano Bissexto!")
else:
    print("Não é um ano Bissexto!")