"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar. Considere U$$1,00 = R$3,37.
"""

n = float(input('Quanto que tu tem na sua carteira? R$'))
print(f'Em 2017, você poderia ter comprado {n/3.27:.2f} dólares.\nCom a cotação atual, você só pode comprar {n/5.71:.2f}!')
#O ":.2f" arredonda o número flutuante para duas casas decimais.
#se você colocasse ":2", iria formatar para q o número tivesse 2 caracteres. Assim, o 9 iria aparecer como " 9", não como "9"