def ficha(jogador="", gols=""):
    print(f"O jogador {jogador} fez {gols} gols")

jogador = str(input("Digite o nome do jogador: "))
gols = input("Qual a quantidade de gols?: ")


if jogador == "":
    jogador = "*campo desconhecido*"


if gols.isdigit(): 
    gols = int(gols) 
else:
    gols = "*campo desconhecido*" 


ficha(jogador, gols)
