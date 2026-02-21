"""
Leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
"""

from datetime import date

ano = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = ano - nascimento

if 0 < idade <= 9:
    print(f'Com {idade} anos, a categoria do atleta é MIRIM.')

elif idade <= 14:
    print(f'Com {idade} anos, a categoria do atleta é INFANTIL.')

elif idade <= 20:
    print(f'Com {idade} anos, a categoria do atleta é JUNIOR.')

elif idade <= 25:
    print('Com 20 anos, a categoria do atleta é SÊNIOR.')

elif 100 >= idade > 20:
    print(f'Com {idade} anos, a categoria do atleta é MASTER.')

else:
    print(f'Idade inválida informada: {idade} anos.')