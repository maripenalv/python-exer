lista = []

while True:
    nmr = input("Digite um número: ")
    lista.append(int(nmr))                
    escolha = input("Deseja continuar?")  
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


