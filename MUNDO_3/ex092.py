"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

from datetime import date

# Alternativa:
# from datetime import datetime
# ano_atual = datetime.now().year

ano_atual = date.today().year

individuo = {
    'Nome': str(input('Nome: ').title()),
    'Ano de Nascimento': int(input('Ano de Nascimento: ')),
    'CTPS': int(input('Carteira de Trabalho (digite 0 caso não tenha): '))
}

individuo['Idade'] = ano_atual - individuo['Ano de Nascimento']

if individuo['CTPS'] == 0:
    print('=' * 50)

    # Remove o ano de nascimento antes da exibição
    del individuo['Ano de Nascimento']

    for k, v in individuo.items():
        print(f'{k} tem o valor {v}.')

else:
    individuo['Ano de Contratação'] = int(input('Ano de Contratação: '))
    individuo['Salário'] = float(input('Salário: R$ '))

    # Cálculo da idade prevista para aposentadoria (35 anos de contribuição)
    aposentadoria = individuo['Ano de Contratação'] + 35 - individuo['Ano de Nascimento']
    individuo['Aposentadoria'] = aposentadoria

    print('=' * 50)

    # Remove o ano de nascimento antes da exibição
    del individuo['Ano de Nascimento']

    for k, v in individuo.items():
        print(f'{k} tem o valor {v}.')