"""
Leia nome, idade e sexo de 4 pessoas e mostre estatísticas do grupo.
"""

soma = mulheres20 = idade = idadevelho = 0
homemvelho = ''

print('=' * 50)

for pessoa in range(1, 5):
    nome = str(input(f'Digite o nome da {pessoa}ª pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Informe o sexo da {pessoa}ª pessoa (m/f): ')).strip().lower()

    soma += idade

    if sexo == 'f' and idade < 20:
        mulheres20 += 1

    if pessoa == 1 and sexo == 'm':
        homemvelho = nome
        idadevelho = idade

    if sexo == 'm' and idade > idadevelho:
        idadevelho = idade
        homemvelho = nome

    print('=' * 50)

print(f'\033[32mA média de idade do grupo é {soma / 4:.2f} anos.'
      f'\nO homem com maior idade é {homemvelho}, com {idadevelho} anos.'
      f'\nHá {mulheres20} mulheres com menos de 20 anos.\033[m')