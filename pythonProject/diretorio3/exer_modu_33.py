import moeda

nmr = float(input("Digite um preço: "))
print(f"Aumentando 10% de {moeda.moeda(nmr)} temos {moeda.aumentar(nmr, True)}") 
print(f"Diminuindo 10% de {moeda.moeda(nmr)} temos {moeda.diminuir(nmr, True)}") 
print(f"O dobro do número {moeda.moeda(nmr)} é {moeda.dobro(nmr, True)}")
print(f"A metade do número {moeda.moeda(nmr)} é {moeda.metade(nmr, True)}")
