#inserção das informações do usuário
altura = float(input("inserir sua altura em m: "))
peso = float(input("inserir seu peso em kg: "))

#Write your code below this line 👇
#calculo do imc 
imc = (round( peso / (altura ** 2)))

if imc < 18.5 :
    print(f"Seu IMC é {imc}, você está abaixo do peso.")
elif 18.5 < imc < 25:
    print(f"Seu IMC é {imc}, você possui um peso normal.")
elif 25 < imc < 30:
    print(f"Seu IMC é{imc}, você está levemente acima do peso.")
elif 30 < imc < 35:
    print(f"Seu IMC é {imc}, você está obeso.")
else:
    print(f"Seu IMC é{imc}, você está clinicamente obeso.")
