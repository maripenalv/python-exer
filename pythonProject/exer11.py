lista = []
impar = []
par = []

while True:
    nmr = int(input("Digite um número: "))
    lista.append(nmr)
    if nmr % 2 == 0:
        par.append(nmr)
    else:
        impar.append(nmr)
    escolha = input("Deseja finalizar a lista? (s/n): ")
    if escolha == "s":
        print(f"Certo, os números digitados foram: {lista}")
        print(f"Os números pares foram: {par}")
        print(f"Os números ímpares foram: {impar}")
        break
    elif escolha == "n":
        print("Certo, vamos continuar.")
