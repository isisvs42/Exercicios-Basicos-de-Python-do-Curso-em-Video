"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def titulo(txt):
    tamanho = len(txt) + 50
    print('~'*tamanho)
    print(f'                         \033[34m{txt}\033[m')
    print('~'*tamanho)


def ficha(jogador='', gols=''):
    if jogador=='':
        jogador='<desconhecido>'
    if gols=='' or gols.isnumeric() == False:
        gols='0'
    return jogador, gols


# Programa Principal
print('-'*35)
nome = str(input('Nome do Jogador: ')).strip().title()
n_gols = str(input('Quantidade de Gols: ')).strip()
ficha_tupla = ficha(nome, n_gols)
print(f'O jogador {ficha_tupla[0]} fez {ficha_tupla[1]} gol(s) no campeonato.')

# Resolução do professor
# def ficha(jog='<desconhecido>', gols=0):
#     print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')
#
#
# n = str(input('Nome do Jogador: '))
# g = str(input('Número de Gols: '))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gols=g)
# else:
#     ficha(n, g)
