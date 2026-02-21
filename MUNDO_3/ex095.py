"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""

encerrado = '< \033[31mENCERRADO\033[m >'
jogadores = []

while True:
    r = 'q'

    jogador = {}  # dicionário para cada jogador registrado

    jogador['nome'] = str(input('Qual o \033[34mnome\033[m do jogador? ')).title()

    jogador['gols'] = []  # lista para armazenar os gols por partida

    partidas = int(input(f"Quantas \033[34mpartidas\033[m {jogador['nome']} jogou? "))

    jogador['partidas'] = partidas  # armazena o número de partidas

    for partida in range(partidas):
        jogador['gols'].append(
            int(input(f'     Quantos \033[34mgols\033[m ele fez na partida {partida}? '))
        )

    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)

    while r not in 'sn':
        r = str(input('\033[31mQuer continuar [s/n]?\033[m '))

    if r == 'n':
        print('=' * 100)
        break

    print('=' * 100)

print(f'{"cod":<5}{"nome":<15}{"gols":<30}{"total":>10}')
print('-' * 60)

for cod, jogador in enumerate(jogadores):
    gols_str = str(jogador["gols"])
    print(f'{cod:<5}{jogador["nome"]:<15}{gols_str:<30}{jogador["total"]:>10}')

print('-' * 60)

while True:
    print('=' * 100)
    jogador = int(input('Digite o código equivalente ao jogador cujos dados deseja ver (999 para parar): '))

    if jogador == 999:
        print(f'{encerrado:=^108}')
        break

    else:
        if jogador >= len(jogadores) or jogador < 0:
            print('\033[31mEsse jogador não existe!\033[m')
        else:
            print(f"O jogador \033[31m{jogadores[jogador]['nome']}\033[m jogou "
                  f"\033[31m{jogadores[jogador]['partidas']}\033[m partidas.")

            for partida, gols in enumerate(jogadores[jogador]['gols']):
                print(f'    => Na partida {partida}, fez {gols} gols.')