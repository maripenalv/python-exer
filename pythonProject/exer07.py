lista = []   

for nmr in range(0, 5):  
 escolha= int(input("Digite um valor: "))
 lista.append(escolha)

print(lista)
print(f"O maior valor da lista foi {max(lista)} e o menor {min(lista)}", end=" ")
print(f"e suas respectivas posições na lista foram {lista.index(max(lista)) + 1} e {lista.index(min(lista)) + 1}")
