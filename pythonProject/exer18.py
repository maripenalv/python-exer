lista = []
contador = 0

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media]) #invés de colocar cada um dos itens dentro da lista, podemos colocar de vez dessa forma
    contador += 1

    escolha = input("Deseja parar o programa? (s/n): ")
    if escolha.lower() == "s":
        print("Programa finalizado.")
        break
    else:
        print("Vamos continuar o programa.")

for aluno in lista:
    print(f"O aluno(a) {aluno[0]} teve como média {aluno[3]:.2f}")

while True:
    try:
        aluno = int(input("Escolha um aluno pela sua posição para ver suas notas ou digite -1 para sair: "))
        if aluno == -1:
            print("Encerrando a visualização das notas.")
            break
        if 1 <= aluno <= contador: # "1 <= aluno" verifica se o índice aluno fornecido pelo usuário é maior ou igual a 1 e "aluno <= contador" verifica se o índice aluno fornecido pelo usuário é menor ou igual ao valor do contador, que representa o número total de alunos na lista
            print(f"As notas do(a) aluno(a) {lista[aluno - 1][0]} foram {lista[aluno - 1][1]} e {lista[aluno - 1][2]}")
        else:
            print("Índice inválido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
