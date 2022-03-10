print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindos a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.") 

#Write your code below this line 👇
lado = input("Você está em uma bifurcação. Onde quer ir? Digite direita ou esquerda ")
lado_minusc = lado.lower()

if lado_minusc == "esquerda":
    transp = input("Você chegou em um lago. No meio desse lago há uma ilha. Digite -esperar- para esperar por um barco. Digite -nadar- para nadar através. ")
    transp_minusc = transp.lower()
    if transp_minusc == "esperar":
        porta = input("Você chegou em uma ilha intocada. Nela há três portas. Uma vermelha, um amarelo e outro azul. Qual cor você escolhe? ")
        porta_minusc = porta.lower()
        if porta_minusc == "amarelo":
            print("Você ganhou!!!!")
        elif porta_minusc == "azul":
            print("Você foi devorado por bestas perversas!!FIM DE JOGO")
        elif porta_minusc == "vermelha":
            print("Você foi queimado no fogo!!FIM DE JOGO")
        else:
            print("FIM DE JOGO")
    else:
        print("Você foi atacado por uma truta!!FIM DE JOGO")
else:
    print("Você foi atacado por uma truta. FIM DE JOGO!")

