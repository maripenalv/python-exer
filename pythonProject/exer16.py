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

for numero in lista + lista2 + lista3:   # "lista + lista2 + lista3" concatena lista, lista2 e lista3 em uma única lista
    if numero % 2 == 0:
        soma.append(numero)         #se um dos numeros contidos nessas listas for par ele será adicionado à lista "soma"
print(f"A soma dos números pares da matriz foi igual a {sum(soma)}")        #por fim, faremos a soma de todos os numeros
                                                                            #contidos na lista "soma"
soma_terceira = lista[2] + lista2[2] + lista3[2] #não poderíamos criar essa lista junto das outras no início pois até então
print(f"A soma dos números da terceira coluna foi: {soma_terceira}") #as listas citadas nao foram criadas
                                                                     #perceba que aqui não estamos concatenando listas, mas sim, fazendo a soma dos seus números na posição 2
print(f"O maior valor da segunda linha foi {max(lista2)}") #utilizaremos a função "max" pra descobrir qual o maior número
