"""
Leia vários números, mostrando média, maior e menor, perguntando se deseja continuar.
"""

r = 's'
s = c = 0
lista = []

while r != 'n':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Deseja continuar (s/n)? ')).strip().lower()

    c += 1
    s += n
    lista.append(n)

    if r not in 'sn':
        print('Resposta inválida. Reiniciando contadores...')
        s = c = 0
        lista.clear()

print(f'Foram digitados {c} números.')
print(f'A média é {s / c:.2f}.')
print(f'O maior número informado foi {max(lista)} e o menor foi {min(lista)}.')