#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Bem vind@s ao calculador de gorjeta")

#input do usuário para colocar o total da conta
conta = float(input("Qual foi o total da conta? R$ "))

#input da porcentagem desejada para gorjeta
gorjeta = int(input("Qual porcentagem de gorjeta gostaria de dar? 10, 12, ou 15? "))

#input de quantas pessoas o usuario ira dividir a conta em 
pessoas = int(input("Com quantas pessoas gostaria de dividir essa conta?"))

#divisão da porcentagem de gorjeta por 100
gorjeta_prct = gorjeta / 100

#multiplicação da conta total pelo valor da gorjeta_prct
conta_prct = conta * gorjeta_prct

#soma da conta com o valor da conta_prct
conta_soma = conta + conta_prct

#valor total da conta_soma com o total de pessoas a pagar a conta
total_div = conta_soma / pessoas

conta_final = round(total_div, 2)

#impressão do valor do final da conta divido pelo qtd de pessoas em que essa conta vai ser divida em 
print (f"Cada pessoa deve pagar: {conta_final}")

