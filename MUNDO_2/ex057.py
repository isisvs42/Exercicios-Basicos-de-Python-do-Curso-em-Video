"""
Leia o sexo de uma pessoa, aceitando apenas "M" ou "F".
"""

sexo = 'd'

while sexo != 'f' and sexo != 'm':
    sexo = str(input('Informe seu sexo (f/m): ')).strip().lower()[0]  
    # Considera apenas o primeiro caractere digitado

    if sexo not in 'fm':
        print('Valor inválido. Por favor, informe "f" ou "m".')
    else:
        print('Entrada registrada com sucesso.')

# Outra forma de implementar:

# sexo = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]
# while sexo not in 'mf':
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
# print(f'Sexo "{sexo}" registrado com sucesso.')