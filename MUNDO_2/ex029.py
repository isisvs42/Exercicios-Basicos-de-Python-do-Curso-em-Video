"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
km acima do limite.
"""

velocidade = float(input('Qual a velocidade de seu carro em km/h? '))
if velocidade > 80:
    print(f'Você foi multado! A velocidade limite é de 80 km/h. Tu terá que pagar R${(velocidade-80)*7:.2f}!')
else:
    print('Você está dentro do limite de velocidade. Muito bem!')
