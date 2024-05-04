"""
Question 18:
"""

volume_m3 = float(input('Entre com um volume em metros cúbicos (m³): '))

volume_litro = 1000 * volume_m3

print(f'O volume {volume_m3}m³ em litros é: {volume_litro.__round__(2)} litros')


