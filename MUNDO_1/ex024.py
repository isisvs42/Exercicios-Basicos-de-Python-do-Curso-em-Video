"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

cidade = str(input('Digite o nome de uma cidade: ')).strip().lower()
print(f'O nome dela começa com "Santo". {cidade[:6] == 'santo '}. ')
