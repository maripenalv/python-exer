times = ("Flamengo", "Atlético Mineiro", "São Paulo", "Palmeiras", "Internacional", "Fluminense",
                      "Athletico Paranaense", "Ceará", "Santos", "Fortaleza", "Atlético Goianiense", "Corinthians",
                      "Juventude", "Bahia", "América Mineiro", "Sport Recife", "Cuiabá", "Grêmio", "Chapecoense", "São Paulo")

print(f"Os 5 primeiros colocados foram: {times[0:5]}")
print(f"Os 4 últimos colocados foram: {times[15:20]}")
print(f"Os times por ordem alfabética são: {sorted(times)}")
print(f"A posiçao do Chapecoense é a {times.index("Chapecoense") +1}") #vamos usar o index pra procurar a posição de uma palavra
                                                                       #e vamos adiconar o "+1" para adicionar 1 às posições
                                                                       #caso contrário, a exemplo do Flamengo, a sua posição
                                                                       #seria a 0, o que não faz sentido.