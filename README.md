# 💰 Painel Financeiro em Flask

Um painel simples feito com **Python + Flask** para registrar transações financeiras, visualizar saldo e consultar cotações de USD e Bitcoin em tempo real.

![Python](https://img.shields.io/badge/Feito%20com-Python%203.11-blue?style=flat&logo=python)  
![Flask](https://img.shields.io/badge/Flask-2.3.3-black)  
![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20dados-lightgrey)  
![API](https://img.shields.io/badge/Cota%C3%A7%C3%A3o-via%20API-orange)

---

## 📦 Requisitos

- Python 3.11 ou 3.12 (⚠️ Python 3.13 pode gerar incompatibilidades!)
- Ambiente virtual (recomendado)
- Acesso à internet para consumir cotações via API

### Pacotes usados:

- flask==2.3.3  
- requests==2.31.0  

---

## 🛠️ Como instalar

1. Clone este projeto:

```bash
git clone https://github.com/hiroyats05/painel-financeiro-flask.git
cd painel-financeiro-flask
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

```bash
.env\Scriptsctivate        # Windows
source venv/bin/activate      # Linux/macOS
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

1. Inicie o servidor:

```powershell
python app.py
```

2. Acesse no navegador:

```
http://127.0.0.1:5000/
```

---

## ✅ Funcionalidades

- Registro de transações (entrada e saída)  
- Cálculo automático do saldo  
- Visualização de transações em tabela  
- Cotações atualizadas de USD e BTC  
- Interface limpa com HTML + CSS puro  
- Salário com cálculo automático de imposto  
- Responsivo e simples de usar  

---

## 💡 Exemplo de uso

Você pode registrar entradas (salário, vendas) ou saídas (compras, contas) com data, descrição e valor. O sistema calcula automaticamente o saldo e mostra o salário líquido com desconto de impostos.

---

## 👨‍💻 Autor

Criado por: Hiroshi Yatabe  
GitHub: https://github.com/hiroyats05  
Finalidade: Aprendizado com Flask e integração de APIs.

---

## 📝 Licença

Este projeto é livre para uso pessoal, educacional e não comercial.
