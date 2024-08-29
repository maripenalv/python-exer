def leiaInt(nmr):                                           #veja o exer29 para tirar possívei dúvidas
    print(f"Você acabou de digitar o número {nmr}")

while True:
    nmr = input("Digite um número: ")
    if nmr.isdigit():
        break
    else:
        print("Por favor, forneça um número")

leiaInt(nmr)
