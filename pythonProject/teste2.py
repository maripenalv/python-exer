'''interactive help: a forma de conseguir ajuda interativa se usa a função "help()", veja abaixo:
voce pode entrar no console do python e escrever essa função, agora voce pode digitar qualuqer comando, como "len", "input", etc para conseguir seu manual
para sair, digite "quit. Também há como escrever na área que geralmente se coda um "help(pra qual comando voce quer um manual)"


docstring: é uma string de documentação, veja abaixo para entender.
Agora imagine que você fez o código pra outra pessoa e ela não sabe o que i, f ,p(inicio, fim, passo) significam.
Para isso você pode incuir um manual, você escreverá 3 aspas(que automaticamente escreverá 6) e apertará "enter", isso
dará um manual com frases pré-existentes mas você pode mudá-la e acrescentar outras coisas

def contador(i, f, p):
    c = i
    while c <= f:
        print(f"{c}")
        c += p

contador(2, 10, 2)


parametros opcionais: perceba que no código abaixo, quando se trata do último "somar" nós teríamos um problema: a variável que
fará a conta utiliza tres numeros e ele só tem dois, nessa hora que entra os parametros opcionais: ao lado do "c" na função, colocaremos "=0"
a adição do zero fará com que, caso o terceiro número não exista, "c" terá o valor de zero, além disso, nada impede de colocar a, b e c, todos eles, recebendo zero

def somar(a, b, c=0):
 s= a + b + c
 print(f"A soma vale {s}")
somar(3, 2, 5)
somar(8, 4)



escopos de variáveis/escopos de declarações: escopo é o lugar onde a variável vai existir e não vai mais
existir; veja abaixo.
Na primeira versão do código temos um escopo global: apesar do "n" ter sido definido depois
da função, ele funcionará dentro de todo o código. Na outra versão você perceberá que houve um errou pois "x" não foi declarado
fora da função, ela só funcionará dentro dela, não fora, ou seja "x" tem um escopo local.
Em resumo: variáveis escritas  fora de funções englobam ambas função em si quanto a área fora dela(o programa principal)
já variáveis criadas dentro de funções só englobam a função atenção! caso você crie uma variável "n" dentro de uma funçao o
código acabará com dois "n" com valores difentes! nao pense que o valor da função principal vai ser substituído quando a
função for chamada, entretanto, para burlar isso, pode-se escrever dentro da função "global n" junto do seu novo valor

def teste():
	print("Na função teste, n vale {n}")

n=2
print(f"No programa principal n tem o valor de {n}")
teste()

/////////////////////////////////////////////////////////
def teste():
	x = 8
	print(f"Na função teste, n vale {n}")
	print(f"Na função teste, x vale {x}")

n=2
print(f"No programa principal n tem o valor de {n}")
teste()
print(f"No programa principal n tem o valor de {n}")



retorno de valores: vamos ver o funcionamento do "return", veja abaixo, na segunda versão do código, o uso do return
basicamente ele o "s" retornará para os "somar" na forma de uma variável ou colocar dentro de um print

def somar(a=0, b=0, c=0):
s = a + b + c
print(f"A soma vale {s}")

somar(3, 2, 5)
somar(2, 2)
somar(6)
//////////////////////////////////////
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

calculo1 = somar(3, 2, 5)
calculo2 = somar(2, 2)
calculo3 = somar(6)

print(calculo1)  # Saída: 10
print(calculo2)  # Saída: 4
print(calculo3)  # Saída: 6

///////////////////////////////////////
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

calculo1 = somar(3, 2, 5)
calculo2 = somar(2, 2)
calculo3 = somar(6)

print(f"Os resultados foram: {calculo1}, {calculo2} e {calculo3}")

'''


