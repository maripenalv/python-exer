import re   

tupla = "tapete", "mesa", "carro", "uva"
print(re.findall('[aeiou]', tupla[0]))  
print(re.findall('[aeiou]', tupla[1]))
print(re.findall('[aeiou]', tupla[2]))
print(re.findall('[aeiou]', tupla[3]))


