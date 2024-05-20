"""
Question 42
"""


salario_base = float(input('Entre com o salário-base do funcionário: '))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_bruto = salario_base + gratificacao - imposto

print(f'Gratificação: R$ {gratificacao.__round__(2)}')
print(f'Imposto: R$ {imposto.__round__(2)}')
print(f'O salário bruto que o funcionário irá receber,'
      f'considerando uma gratificação de 5% e o imposto de 7% é: R$ {salario_bruto.__round__(2)}')
