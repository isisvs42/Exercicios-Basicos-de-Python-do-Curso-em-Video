"""
Refaça o exercício 35 dos triângulos, acrescentando o tipo de triângulo formado.
"""

titulo = 'TRIÂNGULOS'
print(f'\033[36m{titulo:=^100}\033[m')
a = int(input('Digite o primeiro valor inteiro: '))
b = int(input('Digite o segundo valor inteiro: '))
c = int(input('Digite o terceiro valor inteiro: '))
maior = max(a, b, c) #verifica qual o maior lado
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Esses três números formam um \033[35mtriângulo equilátero\033[m.')
    elif a == b or a == c or b == c:
        print('Esses três números formam um \033[35mtriângulo isósceles\033[m.')
    else:
        print('Esses três números formam um \033[35mtriângulo escaleno\033[m.')
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Esse triângulo é também \033[35mretângulo\033[m.')
    elif maior**2 > (a**2 + b**2 + c**2 - maior**2):
        print('Esse triângulo é também \033[35mobtusângulo\033[m.')
    else:
        print('Esse triângulo é também \033[35macutângulo\033[m.')
else:
    print('\033[31mEsses três números não formam um triângulo.\033[m')
