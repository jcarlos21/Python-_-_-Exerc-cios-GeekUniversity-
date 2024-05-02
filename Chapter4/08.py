"""
Question 8:
"""

temp_graus_kelvin = float(input('Entre com uma temperatura em graus Kelvin: '))

temp_graus_celsius = temp_graus_kelvin - 273.15

print(f'A temperatura {temp_graus_kelvin}K em graus Celsius é: {temp_graus_celsius.__round__(2)}ºC')
