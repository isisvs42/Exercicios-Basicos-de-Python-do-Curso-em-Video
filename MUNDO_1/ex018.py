"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

titulo = 'SEN, COS, TG'
print(f'{titulo:=^70}')
from math import radians, sin, cos, tan
a = float(input('Digite o valor de um ângulo qualquer em graus: '))
A = radians(a) #converte para radianos
print(f'O ângulo de {a}º possui sen = {sin(A):.2f}, cos = {cos(A):.2f} e tg = {tan(A):.2f}')
