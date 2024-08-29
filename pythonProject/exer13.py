lista = []
contador = 0

while True:
    lista2 = []                             #criamos outra lista dentro do "while" e não fora dele pq assim criaremos
    nome = str(input("Digite um nome: "))   #uma nova lista cada vez que ocorre um loop, o que é necessário para armazenar os
    lista2.append(nome)                     #valores únicos de nome e peso para cada pessoa
    peso = float(input("Digite um peso: ")) #o motivo de adicionar os itens à "lista2" invés da "lista1" é estruturar os dados
    lista2.append(peso)                     #antes de adicioná-los à lista1, isso significa que cada elemento em "lista1" será
    lista.append(lista2)                    #uma lista contendo o nome e o peso de uma pessoa.
    contador += 1
    escolha = input("Deseja parar o código? (s/n) ")
    if escolha == 's':
        print(f"Código finalizado; veja a lista: {lista}")
        print(f"Houveram {contador} pessoas na lista")

        pesos = [pessoa[1] for pessoa in lista]  #cria uma nova lista chamada pesos, onde cada elemento é o da primeira posição(logo, os pesos) de cada lista interna da lista principal "lista"
        pesos.sort(reverse=True)                 #ordenamos a lista "pesos" em ordem decrescente
        print("Pesos ordenados do maior para o menor:")
        for peso in pesos:        #este loop itera sobre cada elemento na lista pesos(que agora está ordenada do maior
            print(peso, end=", ") #para o menor)

        pesos.sort()             #para conseguirmos os números na ordem crescente usaremos o ".sort" normal
        print("\nPesos ordenados do menor para o maior:")  #o "\n" servirá para pular uma linha(informações estavam vindo na mesma linha)
        for peso in pesos:
            print(peso, end=", ")
        break

    else:
        print("Vamos continuar o código")
        print(30 * "-")
