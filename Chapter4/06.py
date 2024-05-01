"""
Question 6:
"""

tem_graus_celsius = float(input("Entre com uma temperatura em graus Celsius: "))

tem_graus_fahrenheit = tem_graus_celsius * (9.0 / 5.0) + 32.0

print(f'A temperatura {tem_graus_celsius}ºC em graus Fahrenheit é: {tem_graus_fahrenheit.__round__(2)}ºF')
