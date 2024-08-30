lista = []
contador = 0

while True:
    lista2 = []                             
    nome = str(input("Digite um nome: "))   
    lista2.append(nome)                    
    peso = float(input("Digite um peso: "))
    lista2.append(peso)
    lista.append(lista2)                    
    contador += 1
    escolha = input("Deseja parar o código? (s/n) ")
    if escolha == 's':
        print(f"Código finalizado; veja a lista: {lista}")
        print(f"Houveram {contador} pessoas na lista")

        pesos = [pessoa[1] for pessoa in lista]  
        pesos.sort(reverse=True)                
        print("Pesos ordenados do maior para o menor:")
        for peso in pesos:        
            print(peso, end=", ") 

        pesos.sort()             
        print("\nPesos ordenados do menor para o maior:")  
        for peso in pesos:
            print(peso, end=", ")
        break

    else:
        print("Vamos continuar o código")
        print(30 * "-")
