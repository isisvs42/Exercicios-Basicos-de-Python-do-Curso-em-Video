"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

futebol = {
    'nome': str(input('Qual o nome do jogador? ')).title(),
    'gols': []
}

partidas = int(input(f"Quantas partidas {futebol['nome']} jogou? "))

for partida in range(partidas):
    futebol['gols'].append(
        int(input(f"     Quantos gols ele fez na partida {partida}? "))
    )

futebol['total'] = sum(futebol['gols'])

print('-=' * 50)
print(futebol)
print('-=' * 50)

for k, v in futebol.items():
    print(f'O campo \033[35m{k}\033[m tem o valor \033[34m{v}\033[m.')

print('-=' * 50)

print(f"O jogador {futebol['nome']} jogou {partidas} partidas.")

for partida, gols in enumerate(futebol['gols']):
    print(f'    => Na partida {partida}, fez {gols} gols.')

print(f"Foi um total de {futebol['total']} gols.")