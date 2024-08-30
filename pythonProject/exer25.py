def contador():
    print(40*"-")
    print(f"Assim ficou a contagem: ")
    print(f"Início: {escolha1}")
    print(f"Fim: {escolha2}")
    print(f"Espaçadas: {escolha3}")

print(f"Contagem de 1 até 10; de 1 em 1: ")
for nmr in range(1, 11):
    print(nmr, end=", ")
print() 

print(f"Contagem de 10 até 0; de 2 em 2: ")
for nmr in range(10, -1, -2): 
    print(nmr, end=", ")
print()

print(40*"-")
print("Agora é sua vez de personalizar a contagem=")
escolha1= int(input("Digite o número de início: "))
escolha2= int(input("Digite o número final: "))
escolha3= int(input("Digite qual o número de espaçamentos: "))
contador()

print(f"Contagem de {escolha1} até {escolha2}; de {escolha3} em {escolha3}: ")
for nmr in range(escolha1, escolha2, escolha3):
    print(nmr, end=", ")

