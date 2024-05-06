"""
Question 24
"""

area_m2 = float(input('Entre com uma área em m²: '))

area_acres = area_m2 * 0.000247

print(f'A área {area_m2}m² em acres é: {area_acres.__round__(2)} acres')
