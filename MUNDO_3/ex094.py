"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

pessoas = []
mulheres = []
pessoas_acima_da_media = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    resposta = pessoa['sexo'] = 'q'

    while pessoa['sexo'] not in 'MF':
        pessoa['sexo']  = str(input('Sexo [M/F]: ')).strip().upper()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma_idades += pessoa['idade']
    pessoas.append(pessoa.copy())

    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]? ')).upper()[0]

    if resposta == 'N':
        print('-=' * 30)
        break
    print('-=' * 30)

print(f'''- O grupo tem \033[34m{len(pessoas)}\033[m pessoas.
- A média de idade é de \033[34m{soma_idades / len(pessoas):.2f}\033[m anos.''')

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
print(f'- As mulheres cadastradas foram: \033[31m{", ".join(mulheres)}\033[m.')

for pessoa in pessoas:
    if pessoa['idade'] > soma_idades / len(pessoas):
        pessoas_acima_da_media.append(pessoa)
        
print(f'- Lista das pessoas que estão acima da média: ')
for pessoa in pessoas_acima_da_media:
    print('     ', end='')
    for k, v in pessoa.items():
        print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
