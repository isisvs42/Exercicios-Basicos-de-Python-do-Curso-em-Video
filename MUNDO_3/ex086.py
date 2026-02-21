"""
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
"""

matriz = [[],
          [],
          []]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('=-'*50)
for linha in matriz: # para cada linha na matriz
    for valor in linha: # imprime cada valor em cada linha da matriz
        print(f'[{valor: ^5}]', end='')
    print() # terminado o loop de uma linha, pula uma linha no terminal
# outra forma de mudar seria:
# for linha in range(3):
#     for coluna in range(3):
#         print(f'[{matriz[linha][coluna]: ^5}]', end='')
#     print()
