"""
Question 34
"""

import math as mt

raio_circulo = float(input('Entre com o rádio de um círculo: '))

area_circulo = mt.pi * mt.pow(raio_circulo, 2)

print(f'A área do círculo é: {area_circulo.__round__(2)}m²')
