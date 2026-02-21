"""
Leia o ano de nascimento de sete pessoas e mostre quantas são maiores e menores de idade.
"""

from datetime import date
ano = date.today().year
maiores = menores = 0
for c in range (1, 8):
    n = int(input(f'Digite a data de nascimento da {c}º pessoa: '))
    if ano - n >= 21:
        maiores+=1
    else:
        menores+=1
print(f'Apenas {maiores} pessoas atingiram a maioridade, e {menores} ainda não.')
