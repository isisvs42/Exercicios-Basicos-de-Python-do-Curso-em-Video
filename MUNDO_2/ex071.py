"""
Simule um caixa eletrônico com cédulas de R$50, R$20, R$10 e R$1.
"""

titulo = 'BANCO'
print(f'{titulo:=^100}')

cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
valor = int(input('Informe o valor a ser sacado: R$'))

while True:
    if valor >= 50:
        while valor >= 50:
            valor -= 50
            cedulas50 += 1

    elif valor >= 20:
        while 50 > valor >= 20:
            valor -= 20
            cedulas20 += 1

    elif valor >= 10:
        while 20 > valor >= 10:
            valor -= 10
            cedulas10 += 1

    elif valor > 0:
        while 10 > valor > 0:
            valor -= 1
            cedulas1 += 1

    else:  # valor == 0
        print('=' * 100)
        break

print('Distribuição das cédulas:')
if cedulas50 > 0:
    print(f'\033[31m{cedulas50}\033[m cédulas de R$50,00')
if cedulas20 > 0:
    print(f'\033[31m{cedulas20}\033[m cédulas de R$20,00')
if cedulas10 > 0:
    print(f'\033[31m{cedulas10}\033[m cédulas de R$10,00')
if cedulas1 > 0:
    print(f'\033[31m{cedulas1}\033[m cédulas de R$1,00')

print('=' * 100)

# Outra forma de implementar:

# while True:
#     if valor >= 50:
#         cedulas50 = valor // 50
#         valor = valor % 50
#     if valor >= 20:
#         cedulas20 = valor // 20
#         valor = valor % 20
#     if valor >= 10:
#         cedulas10 = valor // 10
#         valor = valor % 10
#     if valor >= 1:
#         cedulas1 = valor // 1
#         valor = valor % 1
#     if valor == 0:
#         break

# Outra alternativa:

# cedula = 50
# total_cedulas = 0
# while True:
#     if valor >= cedula:
#         valor -= cedula
#         total_cedulas += 1
#     else:
#         if total_cedulas > 0:
#             print(f'Total de {total_cedulas} cédulas de R${cedula}.')
#         if cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 1
#         total_cedulas = 0
#         if valor == 0:
#             break