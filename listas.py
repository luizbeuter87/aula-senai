lista_compras = ["café", "refri", "arroz"]

#append adifiona ao fim da lista
lista_compras.append("banana")
lista_compras.append("cerveja")
lista_compras.append("leite")

#sort organiza a lista no caso a > z
lista_compras.sort()

#pop remove item do indice, começando por 0
lista_compras.pop(3)

print(lista_compras)

#len conta quantos itens tem na lista
print(len(lista_compras), "itens")

