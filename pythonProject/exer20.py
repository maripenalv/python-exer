import random
from operator import itemgetter #a biblioteca "operator" tem o "itemgetter" útil para funções como o "sorted" pois define a partir de qual posição o sorted agirá
contador = 0

jogada1= random.randint(1, 6)
jogada2= random.randint(1, 6)
jogada3= random.randint(1, 6)
jogada4= random.randint(1, 6)

dicio= {"jogador1": jogada1, "jogador2": jogada2, "jogador3": jogada3, "jogador4": jogada4}

print(45*"-")
for k, v in dicio.items():
    print(f"{k} jogou e o número que caiu foi {v}")

                                                     #criamos a variável "ordenado" que com o "sorted" irá ordenar
ordenado = sorted(dicio.items(), key=itemgetter(1), reverse=True) #números. "dicio.items()" aplica que levaremos em consideração as
                                                     #chaves(jogador1) e os valores(5, 3, 1, etc) do dicionário. "key=itemgetter(1)" fará
print(55 * "-")                                      #com que o sorted seja aplicado no item na posição 1 do dicionário, logo, nos
contador = 1                                         #valores(5, 3, 1, etc). "reverse=True" faz com que a ordenação seja em ordem decrescente
for k, v in ordenado:  #"ordenado" não é um dicionário por isso não há a necessidade de "ordenado.items"
    print(f"{contador}º lugar: {k} com {v} pontos")
    contador += 1







