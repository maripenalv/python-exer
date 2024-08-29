from datetime import datetime

dicio = {}
print()
print("Bem vindo ao sistema da Biblioteca da Cidade")
print(45 * "=")
print(12 * " ", "O P E R A Ç Õ E S")
print(45 * "=")

while True:
    try:
        print()
        opera = int(input(
            "Escolha uma das operações abaixo: \n1. Cadastrar livros \n2. Buscar livro por nome \n3. Buscar livro por autor \n4. Emprestar livro \n5. Devolução de livro \n6. Ver livros no sistema \n7. sair\n"))
        print(45 * "=")
        if opera < 1 or opera > 7:
            print("Erro. Escolha apenas o número de uma das operações.")
            print()
        elif opera == 1:
            print("Cadastre o nome do livro, o autor e o ano que foi escrito")
            cad_nome = input("Digite o nome do livro: ")
            cad_autor = str(input("Digite o nome do autor: "))
            cad_ano = int(input("Digite o ano de publicação do livro: "))
            if cad_nome in dicio:
                print("Esse livro já está cadastrado!")
            else:
                dicio[cad_nome] = {"autor": cad_autor, "ano": cad_ano}
                print(f"O livro '{cad_nome}' foi cadastrado com sucesso!")
        elif opera == 2:
            while True:
                try:
                    nome = str(input("Digite o nome do livro: "))
                    if nome not in dicio:
                        print(f"Esse livro não existe nos acervos da biblioteca.")
                    else:
                        print(f"Livro encontrado: Nome: {nome}, Autor: {dicio[nome]['autor']}, Ano: {dicio[nome]['ano']}")
                    break  # Sai do loop após uma busca bem-sucedida
                except Exception as e:
                    print(f"Erro: {e}. Tente novamente.")
        elif opera == 3:
            livros_encontrados = []
            autor = str(input("Digite o nome do autor: "))
            for k, v in dicio.items():
                if v['autor'].lower() == autor.lower():
                    livros_encontrados.append(k)
            if livros_encontrados:
                print("Livros encontrados:")
                for k in livros_encontrados:
                    print(f"Nome: {k}, Autor: {dicio[k]['autor']}, Ano: {dicio[k]['ano']}")
            else:
                print(f"Nenhum livro do autor '{autor}' foi encontrado.")
        elif opera == 4:
            while True:
                try:
                    livro = str(input("Digite o nome do livro a ser emprestado: "))
                    if livro in dicio:
                        pessoa = str(input("Por favor, escreva o nome e sobrenome da pessoa que ficará com o livro: "))
                        hoje = datetime.now()
                        hoje_str = hoje.strftime("%d/%m/%Y")
                        print(f"Data de hoje: {hoje_str}")
                        data = input(f"Digite a data de devolução do livro (formato dd/mm/aaaa): ")
                        data_devolucao = datetime.strptime(data, "%d/%m/%Y")
                        if data_devolucao < hoje:
                            print("Erro. A data de devolução não pode ser anterior à data de hoje.")
                        else:
                            print(f"Nome: {pessoa}. Livro: {livro}. Data de devolução: {data_devolucao.strftime('%d/%m/%Y')}.")
                            break  # Sai do loop se tudo estiver correto
                    else:
                        print(f"O livro '{livro}' não está disponível no acervo.")
                        break  # Sai do loop se o livro não estiver disponível
                except Exception as e:
                    print(f"Erro: {e}. Tente novamente.")
        elif opera == 5:
            livro = str(input("Digite o nome do livro a ser devolvido: "))
            if livro in dicio:
                print(f"O livro '{livro}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{livro}' não está registrado no acervo.")
        elif opera == 6:
            if not dicio:
                print("Nenhum livro cadastrado no sistema.")
            else:
                print("Livros cadastrados no sistema:")
                for nome, info in dicio.items():
                    print(f"Nome: {nome}, Autor: {info['autor']}, Ano: {info['ano']}")
        elif opera == 7:
            print("Saindo do sistema.")
            break

    except ValueError:
        print("Erro. Digite um número inteiro.")
        print()
        continue
