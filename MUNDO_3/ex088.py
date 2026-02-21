"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

titulo = ' < MEGA SENA > '
print(f'{titulo:=^100}')
from random import sample # escolhe um número k de itens de uma lista, sem repetição (ao contrário do choices)
from time import sleep
numeros = range(1, 61)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-'*50)
for jogo in range(1, n+1):
    print(f'Jogo {jogo}: {sorted(sample(numeros, k=6))}')
    sleep(0.75)
print('=-'*50)
