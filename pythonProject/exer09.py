lista = []  #primeira forma de fazer
posicao = 0

for numero in range(0, 5):
    nmr = input("Digite um número: ")
    lista.append(nmr)
    posicao += 1
    print(f"Foi digitado {nmr} na posição {posicao}")
print(f"Os valores digitados em ordem crescente foram: {sorted(lista)}")


import bisect  #o "bisect" fornece funcionalidades para inserção ordenada em listas

lista = []

for numero in range(0,5):
    nmr = int(input("Digite um número: "))
    bisect.insort(lista, nmr)  #"bisect.insort" encontra a posição onde o numero deve ser inserido na lista para
                               #manter a ordem crescente e faz a inserção do número na lista, como vemos em "(lista, nmr)"
print(f"Os valores digitados em ordem crescente foram: {lista}")
