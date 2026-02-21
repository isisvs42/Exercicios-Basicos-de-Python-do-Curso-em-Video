"""
Leia um número e mostre seu fatorial.
"""

from math import factorial
n = int(input('Digite um valor para saber o seu fatorial: '))
antecessores = n
print(f'{n}! = ', end='')
while antecessores != 0:
    if antecessores > 1:
        print(f'{antecessores}', end=' x ')
    else:
        print('1', end='')
    antecessores -= 1
print(f' = {factorial(n)}')
