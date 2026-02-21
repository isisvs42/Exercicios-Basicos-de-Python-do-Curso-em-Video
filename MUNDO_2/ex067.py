"""
Mostre a tabuada de vários números até que seja digitado um número negativo.
"""

titulo = 'TABUADA v.3.0'
print(f'\033[35m{titulo:=^100}\033[m')
while True:
    n = int(input('Digite um número (negativo para parar): '))
    print('='*100)
    contador = 1 #faz com que o contador sempre volte a valer 1 quando a tabuada do primeiro n digitado se encerrar
    if n < 0:
        break
    while contador <= 10:
        print(f'{n:2} x {contador:2} = {n*contador:2}')
        contador += 1
    print('='*100)
print('\033[31mPROGRAMA ENCERRADO\033[m')
