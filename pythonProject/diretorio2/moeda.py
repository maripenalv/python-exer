def aumentar(preco):
	conta= (preco*0.10)+preco
	return conta               
def diminuir(preco):
	conta= preco-(preco*0.10)
	return conta
def dobro(preco):
	conta= 2*preco
	return conta
def metade(preco):
	conta= preco//2
	return conta

def moeda(preco=0, sigla= "RS"):                           #criaremos dois parametros: "preco" que já existe e um novo, "moeda2"
     return f"{sigla}{preco}".replace(".",",") #caso o valor de preço não seja informado, será igual a "0", caso o
                                                            #valor de moeda2 não for informado, receberá "RS"
                                                            #Por fim, retornaremos a sigla da moeda seguido do preço e pedimos
	                                                        #para que o programa mudasse os pontos(do padrão americano) pra vírgula(do brasileiro)
