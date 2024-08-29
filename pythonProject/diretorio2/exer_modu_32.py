import moeda

nmr= float(input("Digite um preço:"))
print(f"Aumentando 10% de {nmr} temos {moeda.moeda(moeda.aumentar(nmr))}") #Primeiro importamos do módulo "moeda" a
print(f"Dimunindo 10% de {nmr} temos {moeda.moeda(moeda.diminuir(nmr))}")  #função "moeda" que inclui a sigla "RS", o número
print(f"O dobro do número {moeda.moeda(nmr)} é {moeda.moeda(moeda.dobro(nmr))}") #em si e a formatação do ponto pra vírgula.
print(f"A metade do número {nmr} é {moeda.moeda(moeda.metade(nmr))}")            #Em seguida, aplicaremos essa formatação de
                                                                           #sigla e vírgula ao número que sofrerá uma das
                                                                           #operações matemáticas.