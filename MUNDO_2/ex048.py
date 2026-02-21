"""
Calcule a soma dos números ímpares múltiplos de três no intervalo de 1 até 500.
"""

titulo = 'SOMA DOS NÚMEROS ÍMPARES MÚLTIPLOS DE 3 NO INTERVALO DE 1 A 500'
print(f'{titulo:=^100}')
soma = 0
contador = 0
for c in range(1, 501):
    if c%3==0 and c%2!=0:
        soma+=c
        contador+=1
print(f'A soma dos {contador} valores socilitados é {soma}')
print('='*100)
