"""
Question 30
"""

valor_real = float(input('Entre com um valore em reais: '))

cotacao_dolar = float(input('Entre com a cotação do dólar: '))

valor_dolar = valor_real / cotacao_dolar

print(f'O valor R$ {valor_real} em dólar é: $ {valor_dolar.__round__(2)}')
