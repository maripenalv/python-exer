lista = []
escolha = input("Escreva uma expressão matemática com parenteses: ")

for caractere in escolha:   #vai percorrer cada caractere escrito
    if caractere == '(':    #se o caracter atual a ser analisado é "(" entao será adicionado à lista
        lista.append(caractere)
    elif caractere == ')':  #se o caractere atual for ')' será feita uma verificação.
        if not lista:       #se a lista estiver vazia, isso significa que encontramos um ')' sem seu par correspondente '('.
            print("Os parênteses estão incorretamente posicionados.") #logo, os parenteses estão incorretamente posicionados
            break
        lista.pop()  #assim, removeremos o  '(' correspondente da lista

if not lista:  #após percorrer toda a expressão, verifica-se se a lista, usada como uma pilha para rastrear os parênteses de abertura, está vazia. Se estiver, significa que todos os parênteses de abertura encontraram seus pares de fechamento. Durante a iteração, parênteses de abertura são adicionados à pilha e, quando encontramos um parêntese de fechamento, retiramos o parêntese de abertura correspondente da pilha, se houver. Isso garante que os parênteses estejam balanceados.
    print("Os parênteses estão corretamente posicionados.")
else:
    print("Os parênteses estão incorretamente posicionados.")