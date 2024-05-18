"""
Question 38
"""

salario_funcionario = float(input('Entre com o salário do funcionário: '))
aumento_salario = salario_funcionario * 1.25

print(f'O salário do funcionário, acrescido de 25%, é: R$ {aumento_salario.__round__(2)}')
