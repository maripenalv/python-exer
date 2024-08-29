def ficha(jogador="", gols=""):
    print(f"O jogador {jogador} fez {gols} gols")

jogador = str(input("Digite o nome do jogador: "))
gols = input("Qual a quantidade de gols?: ")


if jogador == "":
    jogador = "*campo desconhecido*"


if gols.isdigit(): #primeiro verificamos se o input que "goals" recebe é composto por algum número. Caso sim, o input de "goals"
    gols = int(gols) #(perceba que ele não recebeu nenhum tipo primitivo anteriormente) será convertido pra um número inteiro
else:
    gols = "*campo desconhecido*" #se "goals" não recebeu nenhum dígito, ele será igual a "*campo desconhecido*"


ficha(jogador, gols)
