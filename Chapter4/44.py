"""
Question 44
"""

altura_degrau_escada = float(input('Entre com a altura do degrau da escada: '))
altura_desejada = float(input('Entre com a altura desejada: '))
quantidade_degraus = altura_desejada / altura_degrau_escada

print(f'O usuário deverá subir {int(quantidade_degraus)} degraus para atingir a altura desejada.')
