"""
Faça um programa que leia uma frase pelo teclado e mostre:
(a) Quantas vezes aparece a letra "A".
(b) Em que posição ela aparece pela primeira vez.
(c) Em que posição ela aparece pela última vez.
"""

frase = str(input('Digite uma frase: ')).strip().lower()

frase_sem_espacos = ''.join(frase.split())

print(f'Nessa frase, a letra "a" aparece {frase_sem_espacos.count("a")} vezes.')
print(f'Na primeira ocorrência, corresponde à {frase_sem_espacos.find("a") + 1}ª letra (ou {frase.find("a") + 1}ª posição considerando os espaços).')
print(f'Na última ocorrência, corresponde à {frase_sem_espacos.rfind("a") + 1}ª letra (ou {frase.rfind("a") + 1}ª posição considerando os espaços).')