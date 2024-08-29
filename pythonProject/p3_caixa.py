lista = []
cont = 0

print(50 * "-")
print(" " * 15 + "CAIXA ELETRÔNICO")

while True:
	try:
		print(50 * "-")
		esc = int(input(
			"Para prosseguir, escolha uma das opções abaixo: \n1. Sacar dinheiro \n2. Depositar dinheiro \n3. Verificar o saldo \n4. Sair\nDeseja prosseguir com qual operação?: "))

		if esc == 1:
			print("\nVocê escolheu sacar dinheiro")
			print(f"Seu saldo atual é de R${cont:.2f}")
			if cont == 0:
				print("Seu saldo está zerado. Primeiramente, deposite dinheiro na conta.")
			else:
				sacar = float(input("Digite o valor que você deseja sacar: "))
				if sacar > cont:
					print("Saldo insuficiente para o saque.")
				else:
					cont -= sacar
					print(f"Dinheiro sacado. Seu saldo atual é de R${cont:.2f}")
					lista.append(cont)

		elif esc == 2:
			print("\nVocê escolheu depositar dinheiro.")
			depositar = float(input("Digite o valor que você deseja depositar: "))
			cont += depositar
			print(f"Dinheiro depositado. Seu saldo atual é de R${cont:.2f}")
			lista.append(cont)

		elif esc == 3:
			print("\nVocê escolheu verificar seu saldo")
			if lista:
				print(f"Seu saldo inicial era de R${lista[0]:.2f}")
				print(f"Seu saldo atual é de R${lista[-1]:.2f}")
			else:
				print("Seu saldo inicial é de R$0")

		elif esc == 4:
			print("\nVocê escolheu sair do programa.")
			print("Programa finalizado.")
			break

		else:
			print("\nOpção inválida. Escolha a opção 1, 2, 3 ou 4.")
			continue

	except ValueError:
		print("\nErro por opção inválida. Tente novamente.")
		continue
