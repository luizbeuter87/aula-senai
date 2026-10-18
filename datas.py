from datetime import datetime

nascimento_txt =  input("Digite sua data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(nascimento_txt, "%d/%m/%Y")
hoje = datetime.now()
idade_dias = (hoje - nascimento).days // 365
natal = datetime(2026, 12, 25) #por padrao a data é yyyy/mm/dd
proximo_natal = natal - hoje

dia_semana_nascimento = nascimento.weekday()
dia_semana_natal = natal.weekday()

weekdays = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"] #cria uma lista com os dias da semana, iniciando por segunda-feira indice 0.

print("Você tem", idade_dias, "anos.")
print("Você nasceu ", weekdays[dia_semana_nascimento])
print("Faltam", proximo_natal.days, "dias para o próximo Natal.")  #proximo_natal.days retorna a quantidade de dias que faltam para o próximo Natal sem as horas
print("O próximo Natal será ", weekdays[dia_semana_natal])
