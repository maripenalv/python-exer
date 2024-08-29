tupla = "Maçã", 2.5, "Abacaxi", 7, "Uva", 4.25, "Melancia", 10    #essa foi a minha forma de fazer

print(43*"-")
print(11*" ", "LISTA DE PRODUTOS", 12*" ")
print(43*"-")
print(tupla[0], 28*".", "R$", tupla[1])
print(tupla[2], 25*".", "R$", tupla[3])
print(tupla[4], 29*".", "R$", tupla[5])
print(tupla[6], 24*".", "R$", tupla[7])
print(43*"-")


tupla = ("Maçã", 2.5, "Abacaxi", 7, "Uva", 4.25, "Melancia", 10)    #forma do professor

print(43 * "-")
print(11 * " " + "LISTA DE PRODUTOS" + 12 * " ")
print(43 * "-")
for item in range(0, len(tupla)):                 #usou o "for" para os produtos aparecerem por vez e o "range" pq ele queria
    if item % 2 == 0:                             #iterar/percorrer essa sequência de números; Você itera uma sequencia
        print(f"{tupla[item]:~<30}", end="")      #quando quer visitar cada elemento individualmente para realizar alguma
    else:                                         #operação(nesse caso, foi para encontrar os pares e ímpares)
        print(f"R${tupla[item]:>7.2f}")           #o "if" serve para, se o item estiver numa posição/for par, ficará à esquerda,
                                                  #onde ficam os nomes dos produtos. Perceba que ele foi 30 carateres alinhado
                                                  #à esquerda acompanhado de ondinhas
                                                  #caso o item estiver numa posição ímpar ele ficará à esquerda,
                                                  #onde ficam os preços. Perceba que os preços estão alinhados 7 carateres
                                                  #à direita além dos números apresentarem duas casas decimais pelo ".2f"