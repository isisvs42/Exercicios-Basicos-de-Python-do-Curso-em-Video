"""
Leia o peso de cinco pessoas e mostre o maior e o menor peso.
"""

comparacao = []
for c in range (1, 6):
    n = float(input(f'Digite o peso da {c}ª pessoa, em kg: '))
    comparacao.append(n)
print(f'O maior peso digitado foi {max(comparacao):.2f} kg, e o menor foi {min(comparacao):.2f} kg')
# outra forma de fazer:
# maior = menor = 0
# for c in range (1, 6):
#     peso = float(input(f'Digite o peso da {c}ª pessoa, em kg: '))
#     if c == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#            maior = peso
#         if peso < menor:
#             menor = peso
# print(maior)
# print(menor)
