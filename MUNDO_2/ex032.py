"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

from datetime import date
ano = int(input('Digite um ano (digite zero para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print(f'Olha só! {ano} é um ano bissexto!')
        else:
            print('Ah... não é bissexto :(')
    else:
        print('Olha só! Um ano bissexto!')
else:
    print(f'Ah... {ano} não é bissexto :(')
#outra forma seria:
# if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
#     print('Olha só! Um ano bissexto!')
# else:
#     print('Ah... não é bissexto :(')
