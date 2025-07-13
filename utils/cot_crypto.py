import requests

def obter_cotacao_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()['bitcoin']['brl']
    return None    