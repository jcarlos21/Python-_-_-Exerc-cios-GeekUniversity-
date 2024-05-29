"""
Question 48
"""

tempo_segundos = int(input('Entre com um valor inteiro em segundos: '))

hora = tempo_segundos // 3600
minuto = (tempo_segundos % 3600) // 60
segundo = (tempo_segundos % 3600) % 60

print(f'O valor {tempo_segundos} segundos equivalor'
      f'a {hora} horas, {minuto} minutos e {segundo} segundos.')
