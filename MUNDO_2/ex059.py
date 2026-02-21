"""
Leia dois valores e mostre um menu de operações (somar, multiplicar, maior, novos números, sair).
"""

from time import sleep

escolha = 0
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

while escolha != 5:
    escolha = int(input('''Escolha uma das opções a seguir:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Informar o maior número
[ 4 ] Redefinir números
[ 5 ] Sair
\033[34mOpção escolhida\033[m: '''))

    if escolha == 1:
        print('=' * 50)
        print(f'{a} + {b} = \033[31m{a + b}\033[m')
        print('=' * 50)

    elif escolha == 2:
        print('=' * 50)
        print(f'{a} x {b} = \033[31m{a * b}\033[m')
        print('=' * 50)

    elif escolha == 3:
        print('=' * 50)
        if a > b:
            print(f'O maior número é \033[31m{a}\033[m.')
        else:
            print(f'O maior número é \033[31m{b}\033[m.')
        print('=' * 50)

    elif escolha == 4:
        print('=' * 50)
        print('Reiniciando valores...')
        sleep(0.5)
        for c in range(1, 4):
            print(f'{c}... ', end='', flush=True)
            sleep(0.5)
        print()
        a = int(input('Digite um número inteiro: '))
        b = int(input('Digite outro número inteiro: '))

    elif escolha < 1 or escolha > 5:
        print('=' * 50)
        print('\033[31mOpção inválida.\033[m')
        print('=' * 50)

print('\033[31mPrograma encerrado.\033[m')