"""
Question 10:
"""

velocidade_km_por_hora = float(input('Entre com um valor de velocidade km/h: '))

velocidade_m_por_segundo = velocidade_km_por_hora / 3.6

print(f'A velocidade {velocidade_km_por_hora} km/h em m/s é: {velocidade_m_por_segundo.__round__(2)} m/s')
