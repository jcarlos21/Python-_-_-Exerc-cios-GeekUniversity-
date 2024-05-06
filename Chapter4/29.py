"""
Question 29
"""

nota1 = float(input('Entre com a nota 1: '))
nota2 = float(input('Entre com a nota 2: '))
nota3 = float(input('Entre com a nota 3: '))
nota4 = float(input('Entre com a nota 4: '))

soma = nota1 + nota2 + nota3 + nota4
media_aritmetica = soma / 4.0

print(f'A média aritmética das notas é: {media_aritmetica}')

"""
nota = list()
soma = 0

for i in range(1, 5):
    aux = float(input(f'Entre com a nota {i}: '))
    nota.append(aux)
    soma = soma + nota[i-1]

media_aritmetica = soma / len(nota)

print(f'A média aritmética das notas é: {media_aritmetica}')
"""

