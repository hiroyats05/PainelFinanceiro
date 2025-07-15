# 💰 Painel Financeiro com Dashboard de Ações (Flask)

Um painel moderno feito com **Python + Flask**, para controle financeiro pessoal e visualização de ações em tempo real com gráficos comparativos.

![Python](https://img.shields.io/badge/Feito%20com-Python%203.11-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-black)
![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20dados-lightgrey)
![API](https://img.shields.io/badge/Cota%C3%A7%C3%A3o-via%20API-orange)

---

## 🖼️ Interface

Dashboard com tema escuro e roxo inspirado em plataformas como XP Investimentos, Rico e etc:

- ✅ Interface moderna e responsiva
- ✅ Cartões informativos com saldo, dólar e bitcoin
- ✅ Tabelas com transações
- ✅ Gráficos interativos para ações e comparações

---

## 📦 Requisitos

- Python 3.11 ou 3.12 (⚠️ Python 3.13 pode gerar incompatibilidades!)
- Ambiente virtual (recomendado)
- Acesso à internet para consumir cotações via API

### 🧪 Principais pacotes:

- `flask==2.3.3`
- `requests==2.31.0`
- `yfinance==0.2.37`

---

## 🛠️ Como instalar

1. Clone este repositório:

```bash
git clone https://github.com/hiroyats05/painel-financeiro-flask.git
cd painel-financeiro-flask
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Ativação:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

Inicie o servidor local:

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000/
```

---

## ✅ Funcionalidades

- 💳 **Controle financeiro**: registre receitas e despesas
- 💰 **Saldo automático**
- 🌐 **Cotação em tempo real** de dólar (USD) e bitcoin (BTC)
- 📈 **Gráficos de ações** individuais
- 📊 **Comparação entre ações** com base em percentual
- 🔍 **Busca de ações específicas**

---

## 📊 Ações suportadas

- Tickers da B3 como `PETR4.SA`, `VALE3.SA`, `ITUB4.SA`
- Comparação lado a lado com histórico de 30 dias
- Visualização separada com gráficos individuais
- Filtro por nome, seleção dinâmica e adição manual

---

## 💡 Exemplo de uso

1. Registre uma nova entrada: "Salário", R$ 5.000
2. Registre uma saída: "Cartão de Crédito", R$ 2.500
3. Veja o saldo atualizado no topo
4. Navegue até **Ações** e visualize os gráficos interativos com histórico
5. Use a busca para comparar `PETR4.SA` com `VALE3.SA` e `ITUB4.SA`

---

## 🧑‍💻 Autor

Desenvolvido por: **Hiroshi Yatabe**  
GitHub: [@hiroyats05](https://github.com/hiroyats05)  
Finalidade: Aprendizado e aplicação prática com Flask e APIs .
