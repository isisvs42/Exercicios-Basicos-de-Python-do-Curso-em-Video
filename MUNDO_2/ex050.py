"""
Leia seis números inteiros e mostre a soma apenas dos pares.
"""
soma = 0
contador = 0
for c in range (0, 6):
    n = int(input('Digite um valor inteiro: '))
    if n%2 == 0:
        soma+=n
        contador+=1
print(f'A soma dos {contador} números pares fornecidos é {soma}.')
