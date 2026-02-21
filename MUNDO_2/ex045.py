"""
Crie um programa que faça o computador jogar JOKENPÔ com o usuário.
"""

from random import randint
from emoji import emojize
from time import sleep

titulo = 'JOKENPÔ'
print(f'\033[38;5;206m{titulo:~^100}\033[m')

computador_escolha = [':pedra:', ':página_voltada_para_cima:', ':tesoura:']
jogador_escolha = [':punho_levantado:', ':mão_levantada:', ':mão_em_v_de_vitória:']

computador = randint(0, 2)

jogador = int(input(emojize("""Escolha uma das opções:
\033[94m[ 1 ] :pedra: Pedra :punho_levantado:\033[m
\033[91m[ 2 ] :página_voltada_para_cima: Papel :mão_levantada:\033[m
\033[92m[ 3 ] :tesoura: Tesoura :mão_em_v_de_vitória:\033[m
Opção: """, language='pt')))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)

print('\033[35m=\033[m' * 50)

print(emojize(f"""\033[35mComputador: {computador_escolha[computador]}
Jogador: {jogador_escolha[jogador - 1]}\033[m""", language='pt'))

print('\033[35m=\033[m' * 50)

if computador == 0:
    if jogador == 1:
        print(emojize('\033[33mEmpate. O computador também escolheu pedra. :pedra:\033[m', language='pt'))
    elif jogador == 2:
        print(emojize('\033[32mVitória do jogador. Papel cobre pedra. :pedra:\033[m', language='pt'))
    elif jogador == 3:
        print(emojize('\033[31mVitória do computador. Pedra quebra tesoura. :pedra:\033[m', language='pt'))
    else:
        print('\033[31mOpção inválida.\033[m')

elif computador == 1:
    if jogador == 1:
        print(emojize('\033[31mVitória do computador. Papel cobre pedra. :página_voltada_para_cima:\033[m', language='pt'))
    elif jogador == 2:
        print(emojize('\033[33mEmpate. O computador também escolheu papel. :página_voltada_para_cima:\033[m', language='pt'))
    elif jogador == 3:
        print(emojize('\033[32mVitória do jogador. Tesoura corta papel. :página_voltada_para_cima:\033[m', language='pt'))
    else:
        print('\033[31mOpção inválida.\033[m')

else:
    if jogador == 1:
        print(emojize('\033[32mVitória do jogador. Pedra quebra tesoura. :tesoura:\033[m', language='pt'))
    elif jogador == 2:
        print(emojize('\033[31mVitória do computador. Tesoura corta papel. :tesoura:\033[m', language='pt'))
    elif jogador == 3:
        print(emojize('\033[33mEmpate. O computador também escolheu tesoura. :tesoura:\033[m', language='pt'))
    else:
        print('\033[31mOpção inválida.\033[m')

rosaforte = '\033[38;5;206m'
print(f'{rosaforte}~\033[m' * 100)