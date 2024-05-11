"""
Question 36
"""

import math as mt

altura_cilindro_circular = float(input('Entre com a altura do cilindro circular: '))

raio_cilindro_circular = float(input('Entre com o raio do cilindro circular: '))

volume_cilindro_circular = mt.pi * mt.pow(raio_cilindro_circular, 2) * altura_cilindro_circular

print(f'O volume do cilindro circular é: {volume_cilindro_circular.__round__(2)}m³')
