lista = []
def maior():
    print(f"O maior número da lista {lista} foi {max(lista)}")

nmr1= int(input("Escolha um número: "))
lista.append(nmr1)

while True:
    escolha= str(input("Deseja escolher outro número? (s/n)"))
    if escolha == "s":
        nmr2= int(input("Escolha outro número: "))
        lista.append(nmr2)
    if escolha != "s" and "n":
        print("Erro de digitação. Tente novamente.")
    if escolha == "n":
        print("Certo, vamos fechar a lista.")
        print(50 * "-")
        break

maior()
