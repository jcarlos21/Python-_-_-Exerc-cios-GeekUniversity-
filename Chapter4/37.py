"""
Question 37
"""

valor_produto = float(input('Entre com o valor do produto: '))
valor_produto_desconto = valor_produto - (valor_produto * 0.12)

print(f'O valor do produto com desconto de 12% é: R$ {valor_produto_desconto.__round__(2)}')
