"""
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
"""

matriz = [[], [], []]
soma_pares = soma_terceira_coluna = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('=-'*50)
for linha in matriz:
    for valor in linha:
        print(f'[{valor: ^5}]', end='')
        if valor%2==0:
            soma_pares+=valor
        if linha[2] == valor:
            soma_terceira_coluna+=valor
    print()
print('=-'*50)
print(f'''A soma dos valores pares é \033[34m{soma_pares}\033[m.
A soma dos valores da terceira coluna é \033[34m{soma_terceira_coluna}\033[m.
O maior valor da segunda linha é \033[34m{max(matriz[1])}\033[m.''')
