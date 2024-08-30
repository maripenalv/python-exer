lista = []  
posicao = 0

for numero in range(0, 5):
    nmr = input("Digite um número: ")
    lista.append(nmr)
    posicao += 1
    print(f"Foi digitado {nmr} na posição {posicao}")
print(f"Os valores digitados em ordem crescente foram: {sorted(lista)}")



