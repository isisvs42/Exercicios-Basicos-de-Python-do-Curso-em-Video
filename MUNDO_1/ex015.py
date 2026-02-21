"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 por km rodado.
"""

d = int(input('Por quantos dias você alugou esse carro? '))
km = float(input('E quantos quilômetros você rodou com ele? '))
p = 60*d + 0.15*km
print(f'Você terá que pagar R${p:.2f} de aluguel desse carro.')
