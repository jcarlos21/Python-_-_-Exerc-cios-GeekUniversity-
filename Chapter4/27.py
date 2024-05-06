"""
Question 27
"""

area_hectar = float(input('Entre com uma área em hectar: '))

area_m2 = area_hectar * 10000

print(f'A área {area_hectar} hectar em m² é: {area_m2.__round__(4)}m²')
