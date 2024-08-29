def aumentar(preco):
	conta= (preco*0.10)+preco
	return conta               #usamos o "return" pois ele permite que ele seja enviado pra qualquer lugar onde a função seja
                               #chamada, armazenando-o. em o return, a função executaria seus cálculos, mas não devolveria nenhum
	                           #valor ao ponto onde foi chamada. Como resultado, o valor calculado dentro da função não estaria
	                           #disponível fora dela, e qualquer tentativa de usar o valor retornado resultaria em "None"
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