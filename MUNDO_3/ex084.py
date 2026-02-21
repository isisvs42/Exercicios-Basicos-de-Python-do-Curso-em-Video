"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.
"""

pessoas = []
maior_peso = menor_peso = 0

while True:
    pessoa = []
    r = 'q'

    pessoa.append(str(input('Nome: ')).title())
    pessoa.append(float(input('Peso (kg): ')))

    # Inicializa maior e menor peso na primeira inserção
    if len(pessoas) == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

    # Adiciona uma cópia da lista pessoa à lista principal
    pessoas.append(pessoa[:])

    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? ')).strip().lower()[0]

    if r == 'n':
        print('=' * 100)
        break

    print('=' * 100)

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior_peso:.2f} kg. Peso de ', end='')
for pessoa in pessoas:
    if maior_peso in pessoa:
        print(f'{pessoa[0]}', end='... ')

print(f'\nO menor peso foi de {menor_peso:.2f} kg. Peso de ', end='')
for pessoa in pessoas:
    if menor_peso in pessoa:
        print(f'{pessoa[0]}', end='... ')