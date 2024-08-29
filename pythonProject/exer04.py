nmr1= int(input("Digite o primeiro número: "))
nmr2= int(input("Digite o segundo número: "))
nmr3= int(input("Digite o terceiro número: "))
nmr4= int(input("Digite o quarto número: "))

tupla = (nmr1, nmr2, nmr3, nmr4)
print(f"Os números digitados foram: {tupla}")
print(f"O número 9 aparece {tupla.count(9)} vezes") #usamos "count" para contar as ocorrências de um elemento específico
print(f"A posição do primeiro número 3 foi {tupla.index(3) +1}") #o index automaticamente encontra apenas a posiçao do primeiro número "tal" digitado

for numero in tupla:                            #podemos descobrir os números pares assim, porém eles aparecerão
    if numero % 2 ==0:                          #por vez
        print(f"O número {numero} é par")

lista = []                                      #dessa forma utilizamos uma lista, funcionará assim:
for numero in tupla:                            #criaremos um loop "for" que percorrerá cada elemento da tupla, em seguida, por
    if numero % 2 == 0:                         #meio do "if", os números que foram constatados que são pares serão anexados à uma
        lista.append(numero)                    #lista, logo, ao printá-la, printaremos de vez todos os números pares contidos nela
print(f"Os números pares são {lista}")