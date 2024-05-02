"""
Question 6:
"""

temp_graus_celsius = float(input("Entre com uma temperatura em graus Celsius: "))

temp_graus_fahrenheit = temp_graus_celsius * (9.0 / 5.0) + 32.0

print(f'A temperatura {temp_graus_celsius}ºC em graus Fahrenheit é: {temp_graus_fahrenheit.__round__(2)}ºF')
