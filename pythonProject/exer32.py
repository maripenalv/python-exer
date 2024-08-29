import requests

def verificar_acesso(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return f"A URL '{url}' pode ser acessada com sucesso."
		else:
			return f"Falha ao acessar a URL '{url}'. Código de status: {response.status_code}"
	except requests.exceptions.RequestException as e:
		return f"Erro ao tentar acessar a URL '{url}': {e}"

url = "https://www.example.com"
resultado = verificar_acesso(url)
print(resultado)
