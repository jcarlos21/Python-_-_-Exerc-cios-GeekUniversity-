"""
Question 35
"""

import math as mt

cateto_oposto = float(input('Entre com o valor do cateto oposto: '))
cateto_adjacente = float(input('Entre com o cateto adjacente: '))

hipotenusa = mt.sqrt((mt.pow(cateto_oposto, 2))+(mt.pow(cateto_adjacente, 2)))

print(f'O valor da hipotenusa é: {hipotenusa.__round__(2)}')
