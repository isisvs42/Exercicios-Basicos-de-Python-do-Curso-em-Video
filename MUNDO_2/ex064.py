"""
Leia números até o usuário digitar 999 e mostre a quantidade e a soma (desconsiderando 999).
"""

n = c = s = 0

while n != 999:
    n = int(input('Digite um número inteiro (999 para encerrar): '))
    if n != 999:
        s += n
        c += 1

print(f'Foram digitados {c} números válidos. A soma total é {s}.')

# Outra forma de implementar:

# n = c = s = 0
# n = int(input('Digite um número inteiro (999 para encerrar): '))
# while n != 999:
#     s += n
#     c += 1
#     n = int(input('Digite um número inteiro (999 para encerrar): '))
#
# print(f'Foram digitados {c} números válidos. A soma total é {s}.')