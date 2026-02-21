"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
porção inteira. Exemplo: o número 6,127 tem a parte inteira 6.
"""

from math import trunc

n = float(input('Digite um número qualquer: '))
print(f'A parte inteira de {n} é {trunc(n)}')

# Também pode utilizar a função int():
# m = float(input('Digite um número qualquer: '))
# print(f'A parte inteira de {m} é {int(m)}')
