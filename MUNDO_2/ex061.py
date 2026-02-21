"""
Refaça a PA usando estrutura WHILE.
"""

titulo = 'PROGRESSÃO ARITMÉTICA V.2.0'
print(f'{titulo:=^120}')
n = 1
a1 = int(input('Digite o primeiro termo de sua P.A.: '))
r = int(input('Digite a razão de sua P.A.: '))
print('Eis aqui os dez primeiros termos de sua P.A: ', end='')
while n <= 10:
    print(f'{a1} -> ', end='')
    a1+=r
    n += 1
print('FIM! ')
print('='*120)
