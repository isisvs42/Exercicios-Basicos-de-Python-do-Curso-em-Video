"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual é o seu salário? R$ '))
if salario > 1250:
    print(f'Seu aumento será de 10%. Logo, seu novo salário é R${salario*1.1:.2f}')
else:
    print(f'Seu aumento será de 15%. Logo, seu novo salário é R${salario*1.15:.2f}')
