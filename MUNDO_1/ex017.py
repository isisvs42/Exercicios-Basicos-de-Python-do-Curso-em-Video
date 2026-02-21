"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

titulo = 'TRIÂNGULO RETÂNGULO'
print(f'{titulo:=^70}')
from math import hypot
b = float(input('Digite o valor de um cateto: '))
c = (float(input('Digite o valor de outro cateto: ')))
print(f'O comprimento da hipotenusa é {hypot(b, c):.2f}')
