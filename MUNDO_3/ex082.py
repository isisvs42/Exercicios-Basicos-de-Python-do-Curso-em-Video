'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []

while True:
    r = 'q'
    n = int(input('Digite um valor inteiro: '))
    lista.append(n)

    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? '))[0]

    if r == 'n':
        break

pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'''A lista completa é {lista}
A lista de pares é {pares}
A lista de ímpares é {impares}''')