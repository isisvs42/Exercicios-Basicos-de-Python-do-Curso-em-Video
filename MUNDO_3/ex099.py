"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep
def maior(*numeros):
    print('-='*25)
    print('Analisando dados...')
    sleep(0.75)
    for numero in numeros:
        print(numero, end=' ')
        sleep(0.5)
    print(f'Foram fornecidos {len(numeros)} números.')
    sleep(0.75)
    if len(numeros) == 0:
        print('O maior deles é 0.')
    else:
        print(f'O maior deles é {max(numeros)}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
