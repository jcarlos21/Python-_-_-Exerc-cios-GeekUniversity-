"""
Question 52
"""

aposta_1 = float(input('Entre com o valor da primeira aposta: '))
aposta_2 = float(input('Entre com o valor da segunda aposta: '))
aposta_3 = float(input('Entre com o valor da terceira aposta: '))
valor_premio = float(input('Entre com o valor do prêmio: '))

soma_apostas = aposta_1 + aposta_2 + aposta_3

apostador_1 = (aposta_1 / soma_apostas) * valor_premio
apostador_2 = (aposta_2 / soma_apostas) * valor_premio
apostador_3 = (aposta_3 / soma_apostas) * valor_premio

print(f'O primeiro apostador ganhará: R$ {apostador_1.__round__(2)}')
print(f'O segundo apostador ganhará: R$ {apostador_2.__round__(2)}')
print(f'O terceiro apostador ganhará: R$ {apostador_3.__round__(2)}')

print(f'Soma das premiações: {apostador_1 + apostador_2 + apostador_3}')
