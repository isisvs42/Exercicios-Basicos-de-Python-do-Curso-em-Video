"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

from operator import itemgetter
from random import randint
from time import sleep

jogadores = {
    'Antôin': randint(1, 6),
    'Junin': randint(1, 6),
    'Binha': randint(1, 6),
    'Sonynha': randint(1, 6)
}

print('Valores sorteados:')
sleep(0.75)

for jogador, dado in jogadores.items():
    print(f'    {jogador} tirou {dado} no dado.')
    sleep(0.75)

print('\nRanking dos jogadores:')
sleep(0.75)

posicao = 1

for jogador, dado in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'    O {posicao}º lugar pertence a {jogador}, que tem {dado} pontos.')
    sleep(0.75)
    posicao += 1

# No sorted(), o parâmetro key recebe uma função utilizada para
# extrair o valor que servirá como critério de ordenação.
#
# itemgetter() é uma função do módulo operator.
# itemgetter(1) indica que o elemento de índice 1 (valor do dicionário)
# será utilizado como base para a ordenação.
#
# reverse=True inverte a ordem da classificação (do maior para o menor).
#
# sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# retorna uma nova lista ordenada.