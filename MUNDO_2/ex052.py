"""
Leia um número inteiro e diga se ele é primo.
"""

n = int(input('Digite um número inteiro: '))
divisores = []

print('Listando os divisores: ', end='')

for c in range(1, n + 1):
    if n % c == 0:
        if c == n:
            print(f'\033[32m{c}\033[m.')
            divisores.append(c)
        else:
            print(f'\033[32m{c}\033[m, ', end='')
            divisores.append(c)
    else:
        print(f'{c}, ', end='')

if len(divisores) == 2:
    print(f'O número {n} é primo, pois possui apenas \033[32m2\033[m divisores: '
          f'\033[32m1\033[m e \033[32m{n}\033[m.')
else:
    print(f'O número {n} é composto, pois possui '
          f'\033[32m{len(divisores)}\033[m divisores: '
          f'\033[32m{", ".join(map(str, divisores))}\033[m.')

# A função map aplica uma função a todos os elementos de um iterável
# (como lista ou tupla) e retorna um iterador com os resultados.
#
# Exemplo:
# numeros = [1, 2, 3, 4, 5]
# numeros_str = map(str, numeros)
# print(list(numeros_str))  # Saída: ['1', '2', '3', '4', '5']
#
# O map retorna um objeto iterável do tipo map.
# Por isso, utiliza-se a função list() para visualizar os valores.