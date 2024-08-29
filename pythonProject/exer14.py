lista = []
lista2 = []
lista3 = []

for cont in range(0, 7):
    nmr = int(input("Digite um número: "))

    if nmr % 2 == 0:
        lista2.append(nmr)

    else:
        lista3.append(nmr)

lista.append(sorted(lista2))
lista.append(sorted(lista3))
print(f"Veja a lista dos pares: {sorted(lista2)}")
print(f"Veja a lista dos ímpares: {sorted(lista3)}")
print(f"A lista com pares e ímpares: {lista}")

