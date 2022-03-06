# 🚨 Don't change the code below 👇
print("Bem-vindo a pizzaria Python deliveries!")
size = input("Que tamanho de pizza você gostaria? S, M, or L ")
add_pepperoni = input("Você gostaria de pepperoni? Y or N ")
extra_cheese = input("Você gostaria de queijo extra? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conta = 0

if size == "S":
    conta += 15
elif size == "M":
    conta += 20
else:
    conta += 25

if add_pepperoni == "Y":
    if size == "S":
        conta += 2
    else:
        conta += 3
   

if extra_cheese == "Y":
    conta += 1

print(f"Sua conta final é de R${conta}")