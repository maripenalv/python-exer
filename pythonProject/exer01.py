from numero_por_extenso import numero_por_extenso #vamos utilizar essa biblioteca para tornar os nmrs extensos

tupla = tuple(range(21))                 #se utilizarmos somente o "range(21)", ao printar, o resultado não daria certo
                                         #pois o range só printa um número por vez, por isso o uso de um loop se faz necessário.
                                         #Para burlar isso, adicionamos "tuple" para que o range funcione como uma tupla, ou seja,
                                         #para que todos os números de 0 a 20 sejam printados
while True:
    escolha = int(input("Escolha um número de 0 a 20: "))
    if escolha not in tupla:
        print("Escolha outro número dentro do intervalo de 0 a 20.")
    else:
        print(f"O número que você escolheu foi {escolha} e sua forma como número extenso é {numero_por_extenso.real(escolha)}.")
        break
