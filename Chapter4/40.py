"""
Question 40
"""

valor_diaria_encanador = 30

dias_trabalhados = int(input('Entre com quantidade de dias que o encanador trabalhou: '))

quantia_liquida_com_imposto_descontado = (dias_trabalhados * valor_diaria_encanador) * 0.92

print(f'A quantia líquida a ser paga ao encanador pelos'
      f' {dias_trabalhados} com o desconto de '
      f'8% do IR é de: R$ {quantia_liquida_com_imposto_descontado.__round__(2)}')
