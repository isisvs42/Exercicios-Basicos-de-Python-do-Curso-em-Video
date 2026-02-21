"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""

def leia_int(enunciado):
    while True:
        a = input(enunciado) # mesmo que a = input('Digite um número: '); veja o programa principal
        if a.isnumeric():
            break
        else:
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
    return a


# Programa Principal
print('-'*35)
n = leia_int('Digite um número: ') # a string 'Digite um número: ' equivale à variável "enunciado"
print(f'Você acabou de digitar o número {n}.')

# Resolução do professor:
# def leiaInt(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[31mERRO! Digite um número inteiro válido.\033[m')
#         if ok:
#             break
#     return valor
