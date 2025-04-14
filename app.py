#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

# Funções da calculadora
def calcular(a, b, operacao):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Erro: valores inválidos"

    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"

# Página principal
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ''
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        operacao = request.form.get('operacao')
        resultado = calcular(a, b, operacao)

    return f'''
    <html>
        <head>
            <title>Calculadora Flask</title>
        </head>
        <body>
            <h1>Calculadora Simples</h1>
            <form method="post">
                <input type="text" name="a" placeholder="Número 1" required>
                <select name="operacao">
                    <option value="soma">+</option>
                    <option value="subtracao">-</option>
                    <option value="multiplicacao">*</option>
                    <option value="divisao">/</option>
                </select>
                <input type="text" name="b" placeholder="Número 2" required>
                <button type="submit">Calcular</button>
            </form>
            <h2>Resultado: {resultado}</h2>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
