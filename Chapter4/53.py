"""
Question 53
"""

comprimento = float(input('Entre com o comprimento do terreno: '))
largura = float(input('Entre com a largura do terreno: '))
preco_tela_metro = float(input('Entre com o preço do metro de tela: '))

preco_para_cercar = ((comprimento * 2) + (largura * 2)) * preco_tela_metro

print(f'O custo para cercar o terreno {comprimento}x{largura}m² é de: R$ {preco_para_cercar.__round__(2)}')
