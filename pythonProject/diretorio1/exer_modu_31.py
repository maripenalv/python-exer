import moeda

nmr= float(input("Digite um preço:"))
print(f"Aumentando 10% de {nmr} temos RS{moeda.aumentar(nmr)}")
print(f"Dimunindo 10% de {nmr} temos RS{moeda.diminuir(nmr)}")
print(f"O dobro do número {nmr} é RS{moeda.dobro(nmr)}")
print(f"A metade do número {nmr} é RS{moeda.metade(nmr)}")