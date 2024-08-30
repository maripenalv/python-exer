lista = []
lista2 = []
lista3 = []
soma = []


for numero in range(0, 3):
    nmr = int(input("Escolha os números da primeira linha: "))
    lista.append(nmr)
print(40 * "-")

for numero in range(0, 3):
    nmr = int(input("Escolha os números da segunda linha: "))
    lista2.append(nmr)
print(40 * "-")

for numero in range(0, 3):
    nmr = int(input("Escolha os números da terceira linha: "))
    lista3.append(nmr)
print(" ")

print("Veja a matriz: ")
print(lista)
print(lista2)
print(lista3)

for numero in lista + lista2 + lista3:  
    if numero % 2 == 0:
        soma.append(numero)        
print(f"A soma dos números pares da matriz foi igual a {sum(soma)}")        
soma_terceira = lista[2] + lista2[2] + lista3[2] 
print(f"A soma dos números da terceira coluna foi: {soma_terceira}") 
                                                                     
print(f"O maior valor da segunda linha foi {max(lista2)}") 
