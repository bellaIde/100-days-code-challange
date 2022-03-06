#input do usuário para saber qual ano ele deseja ver
ano = int(input("Que ano gostaria de checar? "))

#if e else aninhados checando de acordo com o fluxograma
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("É bissexto.")
        else:
            print("Não é bissexto.")
    else:
        print("É bissexto.")
else:
    print("Não é bissexto.")
