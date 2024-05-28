"""
Question 47
"""

num_int = int(input('Entre com um número inteiro de 4 dígitos (de 1000 a 9999): '))
aux = num_int
resto = 0

for i in range(0, 4):
    resto = aux % 10
    print(f'Num: {resto}')
    aux = aux // 10
