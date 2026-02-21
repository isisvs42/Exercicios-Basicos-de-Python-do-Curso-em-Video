"""
Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""

def area(larg, comp):
    _area = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {_area:.1f}m².')


# Programa principal
print('Controle de terrenos-----------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
