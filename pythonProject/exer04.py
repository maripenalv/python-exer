nmr1= int(input("Digite o primeiro número: "))
nmr2= int(input("Digite o segundo número: "))
nmr3= int(input("Digite o terceiro número: "))
nmr4= int(input("Digite o quarto número: "))

tupla = (nmr1, nmr2, nmr3, nmr4)
print(f"Os números digitados foram: {tupla}")
print(f"O número 9 aparece {tupla.count(9)} vezes") 
print(f"A posição do primeiro número 3 foi {tupla.index(3) +1}") 

for numero in tupla:                            
    if numero % 2 ==0:                          
        print(f"O número {numero} é par")

lista = []                                      
for numero in tupla:                            
    if numero % 2 == 0:                         
        lista.append(numero)                    
print(f"Os números pares são {lista}")
