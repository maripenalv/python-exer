from functools import reduce

lista = []
operacao = int(input("Escolha uma operação: \n 1.soma \n 2.subtração \n 3.multiplicação \n 4.divisão\n"))

if operacao == 1:
    print("Você escolheu a operação soma")
elif operacao == 2:
    print("Você escolheu a operação subtração")
elif operacao == 3:
    print("Você escolheu a operação multiplicação")
elif operacao == 4:
    print("Você escolheu a operação divisão")

while len(lista) <= 5:
    if len(lista) >= 2:
        while True:
            escolha = str(input("Deseja escolher mais um número? s/n: ")).lower()
            if escolha == "n":
                print(f"Operação finalizada. Veja a lista: {lista}")
                break
            elif escolha == "s":
                print("Por favor prossiga")
                break
            else:
                print("Erro. Digite apenas 's' ou 'n'.")
        if escolha == "n":
            break
    try:
        numero = int(input("Digite até seis números: "))
        lista.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    if len(lista) > 5:
        print(f"Operação concluída. A lista já tem seis dígitos: {lista}")
        break

while True:
    choice = str(input("Deseja mudar algum dos números da sua lista? s/n: ")).lower()
    if choice == "n":
        if operacao == 1:
            resultado = sum(lista)
            print(f"A soma dos números {lista} foi igual a {resultado}")
        elif operacao == 2:
            resultado = reduce(lambda x, y: x - y, lista)
            print(f"A subtração dos números {lista} foi igual a {resultado}")
        elif operacao == 3:
            resultado = reduce(lambda x, y: x * y, lista)
            print(f"A multiplicação dos números {lista} foi igual a {resultado}")
        elif operacao == 4:
            resultado = reduce(lambda x, y: x / y, lista)
            print(f"A divisão dos números {lista} foi igual a {resultado}")
        break
    elif choice == "s":
        pos = int(input(f"Por favor, escolha a posição do número a ser trocado (de 0 a {len(lista)-1}): "))
        if 0 <= pos <= len(lista)-1:
            novo = int(input("Escolha o novo número: "))
            lista[pos] = novo
            print(f"A lista final ficou assim: {lista}")
        else:
            print(f"Posição inválida. Escolha um número entre 0 e {len(lista)-1}.")
    else:
        print("Erro. Digite apenas 's' ou 'n'.")
