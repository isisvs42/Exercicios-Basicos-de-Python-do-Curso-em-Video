"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input('Digite seu nome completo: '))
nome = nome.strip().lower()
print(f'O seu nome tem "Silva". {'silva' in nome}.')
