"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite o último número inteiro: '))
# if a > b:
#     maior = a
#     menor = b
# else:
#     maior = b
#     menor = a
# if c > maior:
#     maior = c
# if c < menor:
#     menor = c
#outra forma de fazer também é:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior} e o menor é {menor}.')
