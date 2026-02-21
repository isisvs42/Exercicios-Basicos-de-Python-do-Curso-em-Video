'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = list()

while True:
    r = 'q'
    a = int(input('Digite um valor: '))

    # O método append() não retorna o valor inserido.
    # Caso fosse feito algo como:
    # a = lista.append(int(input('Digite um valor: ')))
    # a variável receberia None, comprometendo a lógica das
    # verificações condicionais realizadas abaixo.

    if a not in lista:
        lista.append(a)
        print('Valor adicionado com sucesso!')
    else:
        r = 's'  # evita a exibição da pergunta 'Quer continuar [s/n]?'
        print('Valor já adicionado! Tente novamente... ', end='')

    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? ')).strip().lower()[0]

    if r not in 'sn':
        print('Isso não é uma opção!')

    if r == 'n':
        break

print('Você digitou os números: ', end='')

for a in sorted(lista):
    if a != max(lista):
        print(f'{a}, ', end='')
    else:
        print(f'{a}.')