#{} cria um dicionario "coleção de chave/valor atribuidos" 
cadastro_pessoa = {"nome": "Luiz", "idade": 38, "telefone": "3333-3333", "endereço": "Av. central"}

print(cadastro_pessoa)

#update atualiza as chaves, valores dentro do dicionario
cadastro_pessoa.update({"e-mail": "luiz@gmail.com"})

print(cadastro_pessoa)

#para imprimir chave e valor dentro do dicionario separado por linha
for chave, valor in cadastro_pessoa.items():
    print(chave, ":", valor)
