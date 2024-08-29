import re   #a biblioteca "re" procura padrões específicos em strings, como ocorrência de caracteres, palavras, etc

tupla = "tapete", "mesa", "carro", "uva"
print(re.findall('[aeiou]', tupla[0]))   #utilizamos o ".findall" e escolhemos vogais como o que ele devia procurar
print(re.findall('[aeiou]', tupla[1]))
print(re.findall('[aeiou]', tupla[2]))
print(re.findall('[aeiou]', tupla[3]))


import re  #outra forma de fazer, nesse mesmo código tbm podia usar lista mas ficaria muito longo e desnecessário

tupla = "tapete", "mesa", "carro", "uva"

for palavra in tupla:     #iremos fazer um loop de cada um dos itens da tupla
    vogais_encontradas = re.findall('[aeiou]', palavra)  #criamos a variável "vogais_encontradas" que será composta pelas vogais de cada item da tupla por vez
    print(f"Vogais encontradas em '{palavra}': {vogais_encontradas}")