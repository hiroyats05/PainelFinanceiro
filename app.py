from flask import Flask, render_template, request, redirect
import sqlite3
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
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)