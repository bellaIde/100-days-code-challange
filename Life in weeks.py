#Essa é uma calculadora que faz a contagem estimada
#de acordo com a sua idade atual e retorna a quantidade
#de dias,semanas e meses que o usuário ainda possui
age = input("Qual sua idade?")


new_age = int(age)

qtd_anos = 90 - new_age

qtd_dias = qtd_anos * 365
qtd_semanas = qtd_anos * 52
qtd_meses = qtd_anos * 12

#impressao para o usuário de dias semanas e meses que ele ainda tem de vida
print(f"Você tem {qtd_dias} dias, {qtd_semanas} semanas, e {qtd_meses} meses restantes")