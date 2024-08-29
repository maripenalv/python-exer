lista = []

while True:
    nmr = input("Digite um número: ")
    lista.append(int(nmr))                #se você quiser que o "if 5 in lista" funcione, você deve afirmar que as informações que
    escolha = input("Deseja continuar?")  #entrarão na lista são números, por isso usamos "int"
    if escolha == "s":
        print("Certo, vamos continuar")
    elif escolha == "n":
        print(f"Programa finalizado. Os números foram: {lista}")
        print(f"A quantidade de números foi: {len(lista)}")
        print(f"Os números em ordem decrescente: {sorted(lista, reverse=True)}")
        if 5 in lista:
            print("O número cinco está presente na lista")
        else:
            print("O número cinco não está presente na lista")
        break


