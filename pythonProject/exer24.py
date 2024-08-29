def escreva():
    print(20*"-")

lista= []
frase1= str(input("Escreva uma frase: "))
lista.append(frase1)

while True:
    escolha= str(input("Você deseja escrever algo mais? s/n"))
    if escolha == "s":
        frase2= str(input("Escolha outra frase: "))
        lista.append(frase2)
    elif escolha == "n":
        print("Código finalizado, veja o resultado abaixo")
        break

escreva()
for frase in lista:
    print(frase)
escreva()