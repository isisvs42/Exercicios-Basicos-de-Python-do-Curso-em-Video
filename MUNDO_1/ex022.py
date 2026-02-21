"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
(a) O nome com todas as letras maiúsculas e minúsculas.
(b) Quantas letras ao todo (sem considerar espaços).
(c) Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o seu nome completo: '))
nome = nome.strip()
print(nome.upper())
print(nome.lower())
nomelista = nome.split()
nome = ''.join(nomelista)
print(f'Seu nome completo tem {len(nome)} letras.')
print(f'Seu primeiro nome tem {len(nomelista[0])} letras.')
