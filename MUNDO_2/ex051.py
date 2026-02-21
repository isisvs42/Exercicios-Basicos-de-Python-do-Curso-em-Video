"""
Leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos.
"""

titulo = 'PROGRESSÃO ARITMÉTICA'
print(f'{titulo:=^100}')
a1 = int(input('Digite o primeiro termo na P.A.: '))
r = int(input('Digite a razão dessa P.A.: '))
print('Os dez primeiros termos dessa P.A. são: ', end='')
for c in range (a1, a1+10*r, r): #o range conta do termo a1 até o termo imediatamente anterior ao a11 ou seja, a10
    if c != a1+9*r: #termos diferentes do décimo
        print(f'{c}, ', end='')
    else: #décimo termo
        print(f'{c}.')
print('='*100)
