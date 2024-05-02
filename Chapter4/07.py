"""
Question 7:
"""

temp_graus_fahrenheit = float(input('Entre com uma temperatura em graus Fahrenheit: '))

temp_graus_celsius = 5.0 * (temp_graus_fahrenheit - 32.0) / 9.0

print(f'A temperatura {temp_graus_fahrenheit}ºF em graus Celsius é: {temp_graus_celsius.__round__(2)}ºC')
