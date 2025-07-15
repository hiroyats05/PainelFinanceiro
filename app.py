from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import requests
import yfinance as yf
from datetime import datetime
from utils.conversao import obter_cotacao_usd
from utils.cot_crypto import obter_cotacao_btc

app = Flask(__name__)

def init_db():
    with sqlite3.connect('finac.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                valor REAL NOT NULL,
                descricao TEXT,
                data TEXT NOT NULL
            )
        ''')

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

def calcular_saldo():
    with sqlite3.connect('finac.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT tipo, valor from transacoes')
        transacoes = cursor.fetchall()
        saldo = 0
        for tipo, valor in transacoes:
            if tipo == 'receita':
                saldo += valor
            elif tipo == 'despesa':
                saldo -= valor
        return saldo
        
@app.route('/')
def index():
    with sqlite3.connect('finac.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT tipo, valor, descricao, data FROM transacoes ORDER BY data DESC")
        transacoes = cursor.fetchall()

    saldo = calcular_saldo()
    cotacao_usd = obter_cotacao_usd()
    cotacao_btc = obter_cotacao_btc()
    now= datetime.now()

    return render_template('index.html', transacoes=transacoes, saldo=saldo, cotacao_usd=cotacao_usd, cotacao_btc=cotacao_btc, now=now)

@app.route('/registrar', methods = ['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        tipo = request.form['tipo']
        valor = float(request.form['valor'])
        descricao = request.form['descricao']
        data = datetime.now().strftime('%d-%m-%Y')

        with sqlite3.connect('finac.db') as conn:
            conn.execute('INSERT INTO transacoes (tipo, valor,descricao, data) VALUES (?, ?, ?, ?)', (tipo, valor, descricao, data))
        
        return redirect ('/')
        
    return render_template('registrar.html')
    
acoes_comparar = ['PETR4.SA', 'VALE3.SA']

@app.route('/api/acoes_comparadas')
def api_acoes_comparadas():
    dados = {}
    datas = []

    for ticker in acoes_comparar:
        acao = yf.Ticker(ticker)
        historico = acao.history(period="1mo")
        if historico.empty:
            continue

        if not datas:
            datas = [str(d.date()) for d in historico.index]

        precos = historico['Close'].tolist()
        base = precos[0]
        normalizado = [round((p / base) * 100, 2) for p in precos]

        dados[ticker] = normalizado

    return jsonify({"datas": datas, "series": dados})

@app.route('/investimentos')
def investimentos():
    return render_template('investimentos.html')

@app.route('/api/acao/<ticker>')
def dados_acao(ticker):
    acao = yf.Ticker(ticker)
    historico = acao.history(period="1mo")
    dados = historico[['Close']].reset_index()
    resultado = [
        {"data": str(row['Date'].date()), "preco": round(row['Close'], 2)}
        for _, row in dados.iterrows()
    ]
    return jsonify(resultado)

@app.route('/acoes')
def acoes():
    return render_template('acoes_multiplas.html')

@app.route('/api/acoes')
def api_multiplas_acoes():
    tickers = request.args.get('tickers')  # Ex: PETR4.SA,VALE3.SA,ITUB4.SA
    tickers_lista = tickers.split(',')
    dados = {}
    datas = []

    for ticker in tickers_lista:
        acao = yf.Ticker(ticker)
        historico = acao.history(period="1mo")
        if historico.empty:
            continue

        if not datas:
            datas = [str(d.date()) for d in historico.index]

        dados[ticker] = [round(p, 2) for p in historico['Close']]

    return jsonify({"datas": datas, "series": dados})

acoes_fixas = [
    'PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA',
    'MGLU3.SA', 'WEGE3.SA', 'BBAS3.SA', 'GGBR4.SA', 'RADL3.SA',
    'JBSS3.SA', 'SUZB3.SA', 'LREN3.SA', 'HYPE3.SA', 'B3SA3.SA'
]

@app.route('/api/acoes_separadas')
def api_acoes_separadas():
    tickers_param = request.args.get('tickers')
    if tickers_param:
        tickers_lista = [t.strip().upper() for t in tickers_param.split(',')]
    else:
        tickers_lista = acoes_fixas

    dados = {}
    for ticker in tickers_lista:
        try:
            acao = yf.Ticker(ticker)
            historico = acao.history(period="1mo")
            if historico.empty:
                continue
            datas = [str(d.date()) for d in historico.index]
            precos = [round(p, 2) for p in historico['Close']]
            dados[ticker] = {"datas": datas, "precos": precos}
        except Exception as e:
            print(f"Erro ao obter dados da ação {ticker}: {e}")
            continue

    return jsonify(dados)

@app.route('/acoes_separadas')
def pagina_acoes_separadas():
    return render_template('acoes_multiplas.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=False)