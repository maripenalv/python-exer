nome_aluno = str(input('Qual o nome do aluno?: '))
media_aluno = float(input("Qual a média desse aluno?: "))

if media_aluno < 6:
    resultado_aluno = "O aluno foi reprovado"
else:
    resultado_aluno = "O aluno foi aprovado"

dicio = {"nome": nome_aluno, "media": media_aluno, "resultado": resultado_aluno}

for chave, valor in dicio.items():
    print(f"{chave} é igual a {valor}")