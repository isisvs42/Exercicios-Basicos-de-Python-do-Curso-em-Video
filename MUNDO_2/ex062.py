"""
Melhore a PA perguntando se o usuário quer mostrar mais termos.
"""

titulo = 'PROGRESSÃO ARITMÉTICA V.2.0'
print(f'{titulo:=^120}')

a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))

print('A seguir, os dez primeiros termos da progressão: ', end='')

quantidade_de_termos = 10
c = 1
c2 = 0

while quantidade_de_termos != 0:
    c2 += quantidade_de_termos

    while c <= quantidade_de_termos:
        print(f'\033[34m{a1} -> ', end='')
        a1 += r
        c += 1

    c = 1
    quantidade_de_termos = int(input('\033[mDeseja visualizar quantos termos adicionais? '))

print(f'Programa finalizado com \033[34m{c2} termos exibidos\033[m.')