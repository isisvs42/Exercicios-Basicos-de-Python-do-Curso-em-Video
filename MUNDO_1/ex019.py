"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
"""

titulo = 'SORTEIO DE ALUNOS'
print(f'{titulo:=^70}')
from random import choice
a = input('Digite o nome de seu primeiro aluno: ')
b = input('Agora, o do próximo: ')
c = input('Mais um aluno: ')
d = input('Digite o nome do último aluno: ')
print(f'O aluno escolhido foi {choice([a, b, c, d])}.')
