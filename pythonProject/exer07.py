lista = []   #primeira forma de fazer

nmr1= input("Digite o primeiro número: ")
lista.append(nmr1)
nmr2= input("Digite o segundo número: ")
lista.append(nmr2)
nmr3= input("Digite o terceiro número: ")
lista.append(nmr3)
nmr4= input("Digite o quarto número: ")
lista.append(nmr4)
nmr5= input("Digite o quinto número: ")
lista.append(nmr5)

print(lista)
print(f"O maior valor da lista foi {max(lista)} e o menor {min(lista)}", end=" ")
print(f"e suas respectivas posições na lista foram {lista.index(max(lista)) + 1} e {lista.index(min(lista)) + 1}")  #usamos o ",index" para achar a posição de um determinado item na lista e o +1 para que ela não comece pelo 0, como acontece no python


lista = []   #segunda forma de fazer

for nmr in range(0, 5):   #o loop "for" continuará até que 5 valores sejam digitados
 escolha= int(input("Digite um valor: "))
 lista.append(escolha)

print(lista)
print(f"O maior valor da lista foi {max(lista)} e o menor {min(lista)}", end=" ")
print(f"e suas respectivas posições na lista foram {lista.index(max(lista)) + 1} e {lista.index(min(lista)) + 1}")
