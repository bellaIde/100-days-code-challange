
print("Bem vind@s ao Love Calculator!")
nome1 = input("Qual é o seu nome? \n")
nome2 = input("Qual o nome dele/dela? \n")


#soma de ambas as strings
nome_total = nome1 + nome2
#transformando essa string em letras minusculas caso o usuário use uma letra maiuscula
nome_total_minusc = nome_total.lower()

#buscando se na string nome_total_minusc se há essas letras da palavra true =  verdadeiro
t = nome_total_minusc.count("t")
r= nome_total_minusc.count("r")
u = nome_total_minusc.count("u")
e = nome_total_minusc.count("e")

#somando toda a contagem dessas letras
soma_true = t + r + u + e

#buscando se na string nome_total_minusc se há essas letras da palavra love =  amor
l = nome_total_minusc.count("l")
o = nome_total_minusc.count("o")
v = nome_total_minusc.count("v")
em = nome_total_minusc.count("e")

#somando toda a contagem dessas letras
some_love = l + o + v + em

#somando o total de ambos mas em string, para que não seja uma soma e sim uma concatenação
total = int(str(soma_true) + str(some_love))

#else elif e else para verificar se a soma cai em alguma dessas condições
#para fazer a impressão de uma mensagem no terminal para o usuário
if (total < 10) or (total > 90):
    print(f"Sua pontuação é {total}, vocês são como romeu e julieta.")
elif (total >= 40) and (total <= 50):
    print(f"Sua pontuação é {total}, vocês são okay juntos.")
else:
    print(f"Sua pontuação é {total}.")
