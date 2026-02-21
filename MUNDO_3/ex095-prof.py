time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='') # mostra o nome dos índices ('nome', 'gols', etc)
print()
print('-'*40)
for i, j in enumerate(time):
    print(f'{i:>4} ', end='') # mostra a numeração dos índices (0, 1, 2, ...)
    for v in j.values():
        print(f'{str(v):<15}', end='') # mostra o conteúdo dos índices de cada dicionário de jogadores (j) dentro da lista time
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, q in enumerate(time[busca]['gols']):
            print(f'    => Na partida {i+1}, fez {q} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
