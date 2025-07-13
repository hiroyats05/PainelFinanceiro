import requests

def obter_cotacao_usd ():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return float(resposta.json()['USDBRL']['bid'])
    return None