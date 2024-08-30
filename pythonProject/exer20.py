import random
from operator import itemgetter 
contador = 0

jogada1= random.randint(1, 6)
jogada2= random.randint(1, 6)
jogada3= random.randint(1, 6)
jogada4= random.randint(1, 6)

dicio= {"jogador1": jogada1, "jogador2": jogada2, "jogador3": jogada3, "jogador4": jogada4}

print(45*"-")
for k, v in dicio.items():
    print(f"{k} jogou e o número que caiu foi {v}")

                                                    
ordenado = sorted(dicio.items(), key=itemgetter(1), reverse=True)
                                                    
print(55 * "-")                                      
contador = 1                                       
for k, v in ordenado:  
    print(f"{contador}º lugar: {k} com {v} pontos")
    contador += 1







