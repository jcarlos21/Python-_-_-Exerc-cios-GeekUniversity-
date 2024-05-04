"""
Question 19:
"""

volume_litro = float(input('Entre com um valor en litros: '))

volume_m3 = volume_litro / 1000

print(f'O valor {volume_litro} litros em méetros cúbicos é: {volume_m3.__round__(2)}m³')
