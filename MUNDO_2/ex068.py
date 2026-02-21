"""
Jogue par ou ímpar com o computador até o jogador perder, mostrando vitórias consecutivas.
"""

from random import randint

titulo = 'PAR OU ÍMPAR?'
print(f'\033[35m{titulo:=^100}\033[m')

vitoria = '\033[32mVITÓRIA\033[m'
derrota = '\033[31mDERROTA\033[m'
vitorias_consecutivas = 0

while True:
    escolha = 'q'
    jogada = -1
    # É necessário reinicializar "escolha" e "jogada" dentro do loop,
    # pois essas variáveis mantêm o valor da rodada anterior.
    # Como os loops de validação só executam quando o valor é inválido,
    # sem a reinicialização a próxima rodada poderia não solicitar
    # novos dados ao jogador.

    computador = randint(0, 10)

    while escolha not in 'pi':
        escolha = str(input('Par ou ímpar [p/i]? ')).strip().lower()[0]

    while jogada < 0 or jogada > 10:
        jogada = int(input('Informe um número de 0 a 10: '))

    if (computador + jogada) % 2 == 0:
        if escolha == 'p':
            print('=' * 100)
            print(f'{vitoria:^100}')
            print(f'''Computador (ímpar) = {computador}
Jogador (par) = {jogada}
Soma = {computador + jogada}''')
            print('=' * 100)
            vitorias_consecutivas += 1
        else:
            print('=' * 100)
            print(f'{derrota:^100}')
            print(f'''Computador (par) = {computador}
Jogador (ímpar) = {jogada}
Soma = {computador + jogada}''')
            print('=' * 100)
            print(f'Você obteve \033[34m{vitorias_consecutivas}\033[m vitórias consecutivas.')
            print('=' * 100)
            break

    elif (computador + jogada) % 2 != 0:
        if escolha == 'i':
            print('=' * 100)
            print(f'{vitoria:^100}')
            print(f'''Computador (par) = {computador}
Jogador (ímpar) = {jogada}
Soma = {computador + jogada}''')
            print('=' * 100)
            vitorias_consecutivas += 1
        else:
            print('=' * 100)
            print(f'{derrota:^100}')
            print(f'''Computador (ímpar) = {computador}
Jogador (par) = {jogada}
Soma = {computador + jogada}''')
            print('=' * 100)
            print(f'Você obteve \033[34m{vitorias_consecutivas}\033[m vitórias consecutivas.')
            print('=' * 100)
            break