"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
"""

titulo = 'CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO'
print(f'{titulo:=^100}')
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite o último número inteiro: '))
if a < b + c and b < a + c and c < a + b:
    print('Olha só! Esses três números formam um triângulo!')
else:
    print('Ah... não formariam um triângulo :(')
