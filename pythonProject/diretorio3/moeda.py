def aumentar(preco, format=False):
    conta = (preco * 0.10) + preco
    return conta if format is False else moeda(conta) 
                                                      
def diminuir(preco, format=False):                    
    conta = preco - (preco * 0.10)
    return conta if format is False else moeda(conta)

def dobro(preco, format=False):
    conta = 2 * preco
    return conta if format is False else moeda(conta)

def metade(preco, format=False):
    conta = preco / 2  # Use divisão normal para obter um resultado decimal
    return conta if format is False else moeda(conta)

def moeda(preco=0, sigla="RS"):
    return f"{sigla}{preco:.2f}".replace(".", ",")
