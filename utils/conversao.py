import requests

def obter_cotacao_usd():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            return float(resposta.json()['USDBRL']['bid'])
    except Exception:
        pass
    return 0.0