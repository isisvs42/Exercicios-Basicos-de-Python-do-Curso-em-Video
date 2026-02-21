"""
Leia uma frase e diga se ela é um palíndromo.
"""

titulo = 'PALÍNDROMOS'
print(f'{titulo:=^100}')

frase = str(input('Digite uma palavra ou uma frase: ')).strip().upper()
palindromo = []

for c in range(len(frase), 0, -1):  # percorre a frase de trás para frente
    if frase[c - 1] != ' ':  # ignora espaços em branco
        palindromo.append(frase[c - 1])

print(f'O inverso de {"".join(frase.split())} é {"".join(palindromo)}!')

if ''.join(palindromo) == ''.join(frase.split()):
    print('A sequência informada é um palíndromo, pois sua leitura é idêntica nos dois sentidos.')
else:
    print('A sequência informada não é um palíndromo.')

print('=' * 100)

# Outra forma de construir o palíndromo seria utilizando string:
#
# palindromo = ''
# frase = ''.join(frase.split())  # remove os espaços internos
# for letra in range(len(frase) - 1, -1, -1):
#     palindromo += frase[letra]
# if palindromo == frase:
#     seria um palíndromo
#
# Outra alternativa mais simples:
# palindromo = frase[::-1]