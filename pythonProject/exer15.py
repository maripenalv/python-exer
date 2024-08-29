lista = []  #meu jeito de fazer
lista2 = []
lista3= []

for numero in range(0, 3):
 nmr= int(input("Escolha os números da primeira linha: "))
 lista.append(nmr)
print(40*"-")

for numero in range(0, 3):
 nmr= int(input("Escolha os números da segunda linha: "))
 lista2.append(nmr)
print(40*"-")

for numero in range(0, 3):
 nmr= int(input("Escolha os números da terceira linha: "))
 lista3.append(nmr)
print(" ")

print("Veja a matriz: ")
print(lista)
print(lista2)
print(lista3)



