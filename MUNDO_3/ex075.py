"""
Leia quatro valores e guarde-os em uma tupla, mostrando estatísticas específicas.
"""

tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece pela primeira vez na {tupla.index(3)+1}ª posição.')
else:
    print(f'O número 3 não aparece em posição alguma.')
print('Os números pares digitados foram: ', end = '')
for numero in tupla:
    if numero%2==0:
        print(f'{numero}, ', end = '')

