"""
Question 39
"""

importancia = 780_000

ganhador_1 = importancia * 0.46
ganhador_2 = importancia * 0.32
ganhador_3 = importancia - (ganhador_1 + ganhador_2)

print(f'O ganhador 1 receberá a quantia de: R$ {ganhador_1}')
print(f'O ganhador 2 receberá a quantia de: R$ {ganhador_2}')
print(f'O ganhador 3 receberá a quantia de: R$ {ganhador_3}')
