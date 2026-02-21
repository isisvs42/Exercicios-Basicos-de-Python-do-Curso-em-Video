"""
Leia 5 valores em uma lista e mostre o maior, o menor e suas posições.
"""

lista = []
for item in range(0, 5):
    lista.append(int(input(f'Digite o valor numérico da posição {item}: ')))
print('=-'*25)
print('Você digitou os valores: ', end='')
for item in range(0, 5):
    if item < 4:
        print(f'{lista[item]}, ', end='')
    else:
        print(f'{lista[item]}.')
print(f'O maior valor digitado foi {max(lista)}, nas posições ', end='')
for item in range(0, 5):
    if lista[item] == max(lista):
        print(f'{item}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)}, nas posições ', end ='')
for item in range(0, 5):
    if lista[item] == min(lista):
        print(f'{item}... ', end='')
