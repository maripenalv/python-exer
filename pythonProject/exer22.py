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

for partidas, gols in enumerate(lista): 
    print("-->" ,f"Na partida {partidas + 1} o jogador fez {gols} gols") 
                                                                  
