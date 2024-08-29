import random

tupla = random.sample(range(1, 101), 5)   #a função "random.sample" escolhe aleatoriamente números dentro de um certo
print(f"Os números sorteados foram: {tupla}") #intervalo(nesse caso entre 1 e 100) e pede a quantidade de nmrs que devem
                                             #ser escolhidos(nesse caso, 5)

print(f"O maior valor da tupla foi {max(tupla)} e o menor, {min(tupla)}")