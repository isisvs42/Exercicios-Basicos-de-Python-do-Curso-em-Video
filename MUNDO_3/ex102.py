"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def titulo(txt):
    tamanho = len(txt) + 50
    print('~'*tamanho)
    print(f'                         \033[34m{txt}\033[m')
    print('~'*tamanho)


def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número n
    """
    numeros = []
    conta = 1
    while numero > 0:
        numeros.append(numero)
        conta *= numero
        numero -= 1
    if show: # == True
        return f"{' x '.join(map(str, numeros))} = {conta}"
    else:
        return conta


# Programa Principal
titulo('FATORIAL')
n = int(input('Digite um número para ver a conta: '))
q = 'q'
a = None
while q not in 'sn':
    q = str(input('Quer ver a conta [s/n]? ')).strip().lower()[0]
print('-'*50)
if q == 'n':
    print(fatorial(n))
if q == 's':
    print(fatorial(n, show=True))
print('-'*50)
help(fatorial)

# Resolução do prof:
# def fatorial(n, show=False):
#     """
#     -> Calcula o fatorial de um número
#     :param numero: o número a ser calculado
#     :param show: (opcional) mostrar ou não a conta
#     :return: o valor do fatorial de um número n
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *=c
#     return f