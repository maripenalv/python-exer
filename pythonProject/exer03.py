import random

tupla = random.sample(range(1, 101), 5)   
print(f"Os números sorteados foram: {tupla}") 
print(f"O maior valor da tupla foi {max(tupla)} e o menor, {min(tupla)}")
