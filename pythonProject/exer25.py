def contador():
    print(40*"-")
    print(f"Assim ficou a contagem: ")
    print(f"Início: {escolha1}")
    print(f"Fim: {escolha2}")
    print(f"Espaçadas: {escolha3}")

print(f"Contagem de 1 até 10; de 1 em 1: ")
for nmr in range(1, 11):
    print(nmr, end=", ")
print() #precisamos incluir esse print pois ele vazio define o pulo de uma linha, sem ele, os resultados entre ambos os prints e for's se misturariam

print(f"Contagem de 10 até 0; de 2 em 2: ")
for nmr in range(10, -1, -2): #utilizamos o range com inicio, fim e espaçadas; nesse caso, o início é o número "10", o fim é o número "-1" pois queremos o "0"(o número -1 não será incluído pelas regras do python, e se o número antes dele) e as espaças do número de início até o final é "-2" pois queremos uma contagem decrescente e de 2 em 2
    print(nmr, end=", ")
print()

print(40*"-")
print("Agora é sua vez de personalizar a contagem=")
escolha1= int(input("Digite o número de início: "))
escolha2= int(input("Digite o número final: "))
escolha3= int(input("Digite qual o número de espaçamentos: "))
contador()

print(f"Contagem de {escolha1} até {escolha2}; de {escolha3} em {escolha3}: ")
for nmr in range(escolha1, escolha2, escolha3): #utilizamos o range com inicio, fim e espaçadas; nesse caso, o início é o número "10", o fim é o número "-1" pois queremos o "0"(o número -1 não será incluído pelas regras do python, e se o número antes dele) e as espaças do número de início até o final é "-2" pois queremos uma contagem decrescente e de 2 em 2
    print(nmr, end=", ")


'''                                         forma do gpt
                                     
def contador(inicio, fim, passo): #essa função realizará a contagem com início, fim e passo fornecidos
    print(40 * "-")
    print(f"Assim ficou a contagem: ")
    print(f"Início: {inicio}")
    print(f"Fim: {fim}")
    print(f"Espaçamento: {passo}")

    if inicio < fim:  #se o número inicial for menor que o final(ex: 5, 10) se trata de uma contagem crescente
        if passo < 0: #se "0" for maior que o passo a ser tomado, ele é um número negativo
            passo = -passo #para uma contagem crescente, precisamos de um número negativo, logo, caso seja positivo, tornaremos-o negativo
        for nmr in range(inicio, fim + 1, passo): #adicionamos "+1" a "fim" pois o python exclui o número final e nós queremos incluí-lo
            print(nmr, end=", ")
    elif inicio > fim:  #sentido oposto ao pensamento de cima
        if passo > 0:
            passo = -passo
        for nmr in range(inicio, fim - 1, passo):
            print(nmr, end=", ")
    print()

# Contagem padrão de 1 até 10, de 1 em 1
print("Contagem de 1 até 10; de 1 em 1:")
for nmr in range(1, 11):
    print(nmr, end=", ")
print()

print("Contagem de 10 até 0; de 2 em 2:")
for nmr in range(10, -1, -2):
    print(nmr, end=", ")
print()

print(40 * "-")
print("Agora é sua vez de personalizar a contagem:")
inicio = int(input("Digite o número de início: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o número de espaçamentos: "))

contador(inicio, fim, passo)    
'''