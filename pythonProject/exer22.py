di_nome= str(input("Qual o nome do jogador: "))
di_partida= int(input("Quantidade de partidas jogadas: "))
cont = 1
contador= 0
lista= []

for quantidade in range(di_partida):
    di_gol= int(input(f"Quantos gols ele fez na partida {cont}?"))
    cont+=1
    lista.append(di_gol)
di_gol_total=sum(lista)

dicio= {"campo nome do jogador": di_nome, "campo partidas totais": di_partida, "campo gols totais": di_gol_total}

print(40*"-")
for k, v in dicio.items():
    print(f"O {k} tem o valor {v}")

for partidas, gols in enumerate(lista): #"enumerate" corre uma lista e obtém a posição de cada item que a compõe e os itens em si
    print("-->" ,f"Na partida {partidas + 1} o jogador fez {gols} gols") #no caso, "partidas" representa as posições(0 ao número que o usuário escolheu)
                                                                  #e "gols" representa os itens em si da lista, no caso, os números de gols que escolhemos anteriormente