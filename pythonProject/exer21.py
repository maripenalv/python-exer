di_nome= str(input("Digite o nome: "))
di_ano= int(input("Qual o ano de nascimento?"))
di_carteira= int(input("Qual o número da carteira? Escreva 0 se não tem: "))
di_idade= 2024-di_ano
di_contra= int(input("Digite o ano de contratação: "))
di_salario= float(input("Digite qual o salário: "))
di_sexo= str(input("Sexo masculino ou feminino(m/f): "))

if di_sexo == "m":
    di_aposen= di_idade+35
elif di_sexo == "f":
    di_aposen= di_idade+30

if di_carteira != 0:
    dicio = {"nome": di_nome, "idade": di_idade, "carteira": di_carteira,
             "ano do contrato": di_contra, "salario": di_salario, "idade da aposentadoria": di_aposen}
else:
   dicio= {"nome": di_nome, "idade": di_idade, "carteira": di_carteira}

print(30*"-")
for k, v in dicio.items():
    print(f"{k} tem o valor de {v}")