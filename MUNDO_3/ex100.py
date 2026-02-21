"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando os cinco valores...')
    sleep(0.5)
    for item in range(5):
        a = randint(0, 11)
        lista.append(a)
        print(a, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    sleep(1)
def somapares(lista):
    s=0
    for numero in lista:
        if numero%2==0:
            s+=numero
    print(f'Somando os valores pares de {numeros}, temos \033[31m{s}\033[m.')


# Programa principal
numeros = []
sorteia(numeros)
somapares(numeros)
