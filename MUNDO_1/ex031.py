"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o
preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para
viagens mais longas.
"""

d = float(input('Digite a distância de sua viagem em km: '))
if d <= 200:
    preco = 0.5*d
else:
    preco = 0.45*d
print(f'Sua passagem custará R${preco:.2f}.')
