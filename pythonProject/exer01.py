from numero_por_extenso import numero_por_extenso 

tupla = tuple(range(21))                 

while True:
    escolha = int(input("Escolha um número de 0 a 20: "))
    if escolha not in tupla:
        print("Escolha outro número dentro do intervalo de 0 a 20.")
    else:
        print(f"O número que você escolheu foi {escolha} e sua forma como número extenso é {numero_por_extenso.real(escolha)}.")
        break
