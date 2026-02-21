"""
Leia um número n e mostre os n primeiros termos da sequência de Fibonacci.
"""

titulo = 'SEQUÊNCIA DE FIBONACCI'
print(f'\033[35m{titulo:=^100}\033[m')

quantidade_de_termos = int(input('Quantos termos da Sequência de Fibonacci deseja visualizar? '))

a1 = a1_antigo = contador = 0
a2 = 1

while quantidade_de_termos != 0:

    while contador < quantidade_de_termos:
        print(f'\033[34m{a1} -> ', end='')
        contador += 1
        a1 = a1_antigo + a2
        a2 = a1_antigo
        a1_antigo = a1

    print('Processamento concluído.', end='')
    quantidade_de_termos = int(input('\033[m\nQuantos termos adicionais deseja visualizar? '))

'''
Representação da lógica de atualização das variáveis:

a1        0   a1_antigo + a2   1   1   2   3   5
a2        1   a1_antigo        0   1   1   2   3
---------------------------------------------------
resultado 1                   1   2   3   5   8

Fórmula utilizada:
s = a1_antigo + a2
'''