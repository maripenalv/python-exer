import random

placar = []
tentativa = 3
jogo_num = 1
ponto = 0
total_pontos = 0

print("Bem-vindo ao jogo de adivinhação!")
print("O jogo tem apenas três regras:")
print("1. Você tem três tentativas")
print("2. O número é um inteiro natural")
print("3. O número vai de 1 a 10")
print("Boa sorte!\n")

while True:
	cont = 0
	alea = random.randint(1, 10)

	while cont < tentativa:
		try:
			nmr = int(input("Qual número você escolhe?: "))
			if nmr > 10 or nmr < 1:
				print("Número fora de intervalo. Escolha um dígito entre 1 e 10.")
				continue
		except ValueError:
			print("Entrada inválida. Por favor, insira um número inteiro.")
			continue

		if alea == nmr:
			print("Você acertou, parabéns!")
			ponto += 1
			break
		elif alea == nmr+1:
			print("Você está próximo! Uma dica: qual o antônimo de menos?")
		elif alea == nmr-1:
			print("Você está próximo! Talvez você deva repensar e dar um passo pra tras...")
		else:
			cont += 1
			print(f"Você errou, você está na {cont}ª tentativa")

	if cont == tentativa and alea != nmr:
		print(f"Você usou todas as suas tentativas. O número correto era {alea}.")

	placar.append((jogo_num, ponto))
	total_pontos += ponto

	while True:
		try:
			print()
			escolha = input("Deseja jogar outra vez? s/n: ").lower()
			if escolha == "n":
				print("O jogo chegou ao fim. Veja o seu placar abaixo:")
				for jogo, pontos in placar:
					print(f"Jogo {jogo}: {pontos} pontos")
				print(f"Soma total dos pontos: {total_pontos}")
				break
			elif escolha == "s":
				jogo_num += 1
				print(f"\nVamos continuar com o jogo.")
				print(40 * "-")
				ponto = 0
				break
			else:
				print("Erro. Escolha apenas s ou n.")
		except ValueError:
			print("Erro. Escolha apenas s ou n.")
			continue

	if escolha == "n":
		break
