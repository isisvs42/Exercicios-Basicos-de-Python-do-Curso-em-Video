"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

n = int(input('Digite um número inteiro, de 0 a 9999: '))
unidades = n // 1 % 10
dezenas = n // 10 % 10
centenas = n // 100 % 10
milhares = n // 1000 % 10
print(f"""Unidades: {unidades}
Dezenas: {dezenas}
Centenas: {centenas}
Milhares: {milhares}""")
