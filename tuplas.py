#uma tupla () é imutavel
tupla_fim_semana = ("sexta", "sabado", "domingo")

#transforma em lista
lista_fim_semana = list(tupla_fim_semana)

#adiciona um dia
lista_fim_semana.append("segunda")

#transforma em tupla novamente
tupla_fim_semana_att = tuple(lista_fim_semana)

print(tupla_fim_semana_att)
