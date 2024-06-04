"""
Question 41
"""

valor_hora_trabalho = float(input('Entre com o valor da hora de trabalho do funcionário: '))
horas_trabalhadas = float(input('Entre com o número de horas trabalhadas: '))

valor_a_ser_pago = (valor_hora_trabalho * horas_trabalhadas) * 1.10

print(f'O valor da hora trabalhada com adição de 10% é: R$ {valor_a_ser_pago.__round__(2)}')
