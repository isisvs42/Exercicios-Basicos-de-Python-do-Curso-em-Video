"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
from emoji import emojize
titulo = 'JOGO DA ADIVINHAÇÃO v.1.0'
print(f'{titulo:=^100}')
n = randint(1, 10)
m = int(input(emojize(':balão_de_pensamento: Pensei em um número inteiro de 1 a 10! Qual você acha que é? ', language='pt')))
if m == n:
    print(emojize(':rosto_saboreando_comida: Processando...', language='pt'))
    sleep(1.5)
    print(emojize(':marca_de_seleção_branca: Parabéns! Você acertou!', language='pt'))
else:
    print(emojize(':rosto_saboreando_comida: Processando...', language='pt'))
    sleep(1.5)
    print(emojize(f':xis: Errou! Eu tinha pensado no número {n}, não no {m}!', language='pt'))
