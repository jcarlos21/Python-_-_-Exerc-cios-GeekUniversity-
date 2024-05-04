"""
Question 14:
"""

import math

angulo_graus = float(input('Entre com um ângulo em graus: '))

angulo_radianos = angulo_graus * (math.pi / 180)

print(f'O ângulo {angulo_graus}º em radianos é: {angulo_radianos.__round__(2)} radianos')

