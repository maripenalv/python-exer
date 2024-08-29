import random

lista1 = []
lista2 = []

def sorteia():
    for nmr in range(5):
        nmrs = random.randint(1, 100)
        lista1.append(nmrs)
    print(f"Os números sorteados foram {lista1}")

def somaPar():
    for nmr in lista1:
        if nmr % 2 == 0:
            lista2.append(nmr)
            soma = sum(lista2)
    print(f"Os números pares foram {lista2}")
    print(f"A soma dos números pares foi {soma}")

sorteia()
somaPar()