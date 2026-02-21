"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se
já passou do tempo do alistamento.
"""

from datetime import date

ano = date.today().year
nascimento = int(input('Em qual ano você nasceu? '))

if 0 < ano - nascimento < 18:
    print(f'Você possui {ano - nascimento} anos. Ainda não é o momento de se alistar. '
          f'O alistamento será em {nascimento + 18}. '
          f'Faltam {nascimento + 18 - ano} anos.')

elif ano - nascimento == 18:
    print('Você completa 18 anos este ano. É necessário realizar o alistamento militar.')

else:
    if ano - nascimento - 18 > 1:
        print(f'Você possui {ano - nascimento} anos. '
              f'O período de alistamento ocorreu há {ano - nascimento - 18} anos, '
              f'em {nascimento + 18}.')
    elif ano - nascimento - 18 == 1:
        print(f'Você possui {ano - nascimento} anos. '
              f'O período de alistamento ocorreu há 1 ano, '
              f'em {ano - 1}.')
    else:
        print(f'A informação informada indica que o nascimento ocorrerá em {nascimento}. '
              f'O alistamento está previsto para {nascimento + 18}.')