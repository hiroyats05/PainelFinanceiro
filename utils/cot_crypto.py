import requests

def obter_cotacao_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            return float(resposta.json()['bitcoin']['brl'])
    except Exception:
        pass
    return 0.0
