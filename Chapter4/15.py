"""
Question 15:
"""

import math

angulo_radianos = float(input('Entre com um ângulo em radianos: '))

angulo_graus = angulo_radianos * (180 / math.pi)

print(f'O ângulo {angulo_radianos} radianos em grau é: {angulo_graus.__round__(2)}º')
