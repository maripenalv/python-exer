def leiaInt():
	while True:
		try:
			nmr_int = int(input("Digite um número inteiro: "))
		except:
			print("Erro. Digite um número inteiro.")
		else:
			print("Número correto.")
			break

def leiaFloat():
	while True:
		try:
			nmr_float = float(input("Digite um número real: "))
		except:
			print("Erro. Digite um número real.")
		else:
			print("Número correto.")
			break

leiaInt()
print(30*"-")
leiaFloat()





