"""
Mostre a tabuada de um número usando laço FOR.
"""

titulo = 'TABUADA v.2.0'
print(f'{titulo:=^100}')
n = int(input('Escolha um número inteiro: '))
for c in range (1, 11):
    print(f'{c:2} x {n:2} = {c*n:2}')
print('='*100)
