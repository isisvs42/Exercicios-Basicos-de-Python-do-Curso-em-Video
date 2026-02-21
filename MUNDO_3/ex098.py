"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""

from time import sleep
def contador(inicio, fim, passo):
    print('-='*50)
    if passo == 0: # isso aqui faz com que o passo mostrado no print do else seja "1" se o usuário digitar "0"
        passo = 1
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*(-1)} em {passo*(-1)}: ')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    sleep(0.5)

    if inicio > fim and passo > 0: # caso o usuário digite o passo positivo querendo uma contagem regressiva
         passo*=-1
    if passo > 0:
        for numero in range(inicio, fim+1, passo): #o "fim+1" é para que a contagem não vá além do fim determinado pelo usuário
            print(numero, end=' ')
            sleep(0.5)
        print('FIM!')
    else: # se o passo for negativo
        for numero in range(inicio, fim-1, passo):
            print(numero, end=' ')
            sleep(0.5)
        print('FIM!')

# # Solução do professor:
# def contador(i, f, p):
#     if p < 0:
#         p*=-1
#     if p == 0:
#         p = 1
#     print('-='*20)
#     print(f'Contagem de {i} até {f} de {p} em {p}:')
#     sleep(1)
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='')
#             sleep(0.5)
#             cont+=p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='')
#             sleep(0.5)
#             cont-=p
#          print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*50)
print('Agora é a sua vez de personalizar a contagem!')
_inicio = int(input('Início: '))
_fim = int(input('Fim: '))
_passo = int(input('Passo: '))
contador(_inicio, _fim, _passo)
