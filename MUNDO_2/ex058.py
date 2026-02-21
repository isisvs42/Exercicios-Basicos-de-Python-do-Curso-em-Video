"""
Melhore o jogo de adivinhação (0 a 10) até o usuário acertar, mostrando quantos palpites foram necessários.
"""

from random import randint
from time import sleep
from emoji import emojize

titulo = 'ADIVINHE O NÚMERO'
print(f'\033[35m{titulo:=^100}\033[m')

computador = randint(0, 10)
jogador = -1
tentativas = 0

print('Processando...', end=' ', flush=True) # Sem a quebra de linha do \n, o buffer enche. O flush obriga a mandar imediatamente para o terminal
sleep(0.3)

for balao in range(0, 6):
    print(emojize('\033[97m:balão_de_pensamento:\033[m', language='pt'),
      end='... ', flush=True)
    sleep(0.3)

print('Escolhi um número entre \033[34m0\033[m e \033[34m10\033[m.', end=' ')

while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1

    if jogador < computador:
        print('\033[31mIncorreto.\033[m O número escolhido é maior. Tente novamente.')
    elif jogador > computador:
        print('\033[31mIncorreto.\033[m O número escolhido é menor. Tente novamente.')

if tentativas == 1:
    print(f'\033[32mCorreto.\033[m Você acertou na primeira tentativa.')
else:
    print(f'\033[32mCorreto.\033[m Foram necessárias \033[34m{tentativas}\033[m tentativas.')

print('\033[35m=\033[m' * 100)

# Outra forma de implementar a lógica:
#
# vitoria = False
# while not vitoria:
#     jogador = int(input('Qual é o seu palpite? '))
#     tentativas += 1
#     if jogador == computador:
#         vitoria = True
#
# print(f'\033[32mCorreto.\033[m Foram necessárias \033[34m{tentativas}\033[m tentativas.')