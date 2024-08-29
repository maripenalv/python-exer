import random

aposta = []
quant = int(input("Quantos jogos serão criados?: "))
contador = 1

while contador <= quant:
    contador += 1
    aposta.append(random.sample(range(1, 61), 6)) #pelo ".sample" e "range" geraremos 6 números que variam de 1 a 60
print(f"Os números sorteados foram: {aposta}")