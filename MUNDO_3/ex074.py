"""
Gere cinco números aleatórios em uma tupla e mostre o menor e o maior.
"""

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print('Os cinco números sorteados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}.\nO menor número sorteado foi {min(numeros)}.')
