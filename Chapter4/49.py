"""
Question 49
"""

hora = int(input('Entre com a hora de ínício: '))
minuto = int(input('Entre com os minutos: '))
segundo = int(input('Entre com os segundo: '))

tempo_segundos = int(input('Entre com um valor inteiro, correspondente ao'
                           ' tempo de duração do experimento, em segundos: '))

hora_add = tempo_segundos // 3600
minuto_add = (tempo_segundos % 3600) // 60
segundo_add = (tempo_segundos % 3600) % 60

nova_hora = hora + hora_add
novo_minuto = minuto + minuto_add
novo_segundo = segundo + segundo_add

print(f'O término do experimento foi às {nova_hora}:{novo_minuto}:{novo_segundo}.')
