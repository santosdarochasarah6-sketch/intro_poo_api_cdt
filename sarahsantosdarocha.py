import requests

url_api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
response = requests.get(url_api)

resposta = requests.get (url_api)  

if respostas.status_code == 200:
    dados = resposta.json()
    print("conexão estabelecida com sucesso!")
else:
    print("erro na requisição:{resposta.status_code}")
    
contacao_dolar = dados["USDBRL"]["bid"]  
nome_moeda = dados["USDBRL"]["name"] 

print(f"moeda:{nome_moeda}")
print(f"valor atual de compra: R$ {float(contacao_dolar):.2f}")
    
