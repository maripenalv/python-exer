import moeda

nmr= float(input("Digite um preço:"))
print(f"Aumentando 10% de {nmr} temos {moeda.moeda(moeda.aumentar(nmr))}") 
print(f"Dimunindo 10% de {nmr} temos {moeda.moeda(moeda.diminuir(nmr))}")  
print(f"O dobro do número {moeda.moeda(nmr)} é {moeda.moeda(moeda.dobro(nmr))}")
print(f"A metade do número {nmr} é {moeda.moeda(moeda.metade(nmr))}")            
                                                                           
                                                                           
