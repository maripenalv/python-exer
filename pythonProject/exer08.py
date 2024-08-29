lista = []

while True:
    nmr=input("Digite um valor: ")
    if nmr not in lista: #se o número não estiver contido na lista, será adicionado a ela
     lista.append(nmr)
    else:                #caso contrário, uma mensagem de aviso será printada
        print("Número repetido, escolha outro.")
    escolha = input("Deseja continuar?")
    if escolha == "n":
        print(f"Código finalizado, os números escolhidos em ordem crescente foram {sorted(lista)}")
        break
    elif escolha == "s":
        print("Certo, vamos continuar")
        print(30*"-")
