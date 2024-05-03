"""
Question 11:
"""

velocidade_m_por_segundo = float(input('Entre com um valor de velocidade m/s: '))

velocidade_km_por_hora = velocidade_m_por_segundo * 3.6

print(f'A velocidade {velocidade_m_por_segundo} m/s em km/h é: {velocidade_km_por_hora.__round__(2)}')
