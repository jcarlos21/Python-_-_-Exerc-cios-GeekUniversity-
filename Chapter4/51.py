"""
Question 51
"""

import math as mt

coord_x = float(input('Entre com a coordenada x: '))
coord_y = float(input('Entre com a coordenada y: '))

dist_origem = mt.sqrt(mt.pow((coord_x - 0), 2)+mt.pow((coord_y - 0), 2))

print(f'A distância para as coordenadas do ponto à origem (0,0) é: {dist_origem.__round__(2)}')
