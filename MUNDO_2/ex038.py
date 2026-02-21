"""
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela
uma mensagem adequada.
"""

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
if a > b:
    print(f'O primeiro valor ({a}) é o maior.')
elif a < b:
    print(f'O segundo valor ({b}) é o maior.')
else:
    print('Não existe valor maior. Os dois são iguais.')
