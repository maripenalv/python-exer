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