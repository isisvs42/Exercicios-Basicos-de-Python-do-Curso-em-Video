"""
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

titulo = 'SORTEIO DE ORDEM DE ALUNOS'
print(f'{titulo:=^70}')
from random import shuffle
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o do segundo: ')
c = input('Terceiro: ')
d = input('Último: ')
alunos = [a, b, c , d]
shuffle (alunos)
print(f'A ordem de apresentação será: {alunos}')
