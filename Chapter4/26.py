"""
Question 26
"""

area_m2 = float(input('Entre com uma área em m²: '))

area_hectar = area_m2 * 0.0001

print(f'A área {area_hectar}m² em hectar é: {area_hectar.__round__(4)} hectar')
