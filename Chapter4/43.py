"""
Question 43
"""

valor_venda = float(input('Entre com o valor da venda: '))

total_pagar_desconto = valor_venda * 0.90
parcelado_sem_juros = valor_venda / 3.0
comissao_vendedor_a_vista = 0.05 * total_pagar_desconto
comissao_vendedor_parcelado = 0.05 * valor_venda

print(f'O total a pagar com desconto de 10% é: R$ {total_pagar_desconto.__round__(2)}')
print(f'Valor do parcelamento em 3x sem juros: R$ {parcelado_sem_juros.__round__(2)}')
print(f'Comissão do vendedor, no caso de compra a vista '
      f'(5% sobre o valor com desconto): R$ {comissao_vendedor_a_vista.__round__(2)}')
print(f'Comissão do vendedor, no caso de compra parcelada '
      f'(5% sobre o total): R$ {comissao_vendedor_parcelado.__round__(2)}')
