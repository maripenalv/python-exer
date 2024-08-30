lista = []

while True:
    nmr=input("Digite um valor: ")
    if nmr not in lista: 
     lista.append(nmr)
    else:                
        print("Número repetido, escolha outro.")
    escolha = input("Deseja continuar?")
    if escolha == "n":
        print(f"Código finalizado, os números escolhidos em ordem crescente foram {sorted(lista)}")
        break
    elif escolha == "s":
        print("Certo, vamos continuar")
        print(30*"-")
