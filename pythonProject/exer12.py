lista = []
escolha = input("Escreva uma expressão matemática com parenteses: ")

for caractere in escolha:   
    if caractere == '(':    
        lista.append(caractere)
    elif caractere == ')': 
        if not lista:       
            print("Os parênteses estão incorretamente posicionados.") 
            break
        lista.pop() 

if not lista:  
    print("Os parênteses estão corretamente posicionados.")
else:
    print("Os parênteses estão incorretamente posicionados.")
