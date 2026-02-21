"""
Leia idade e sexo de várias pessoas e mostre estatísticas no final.
"""

maiores = homens = mulheres20 = 0
while True:
    sexo = escolha = 'L'
    print('='*100)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiores+=1
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo [m/f]: ')).strip().lower()[0]
    if sexo == 'm':
        homens+=1
    if sexo == 'f' and idade < 20:
        mulheres20+=1
    while escolha not in 'sn':
        escolha = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
    if escolha == 'n':
        print('='*100)
        break
print(f'{maiores} pessoas têm mais de 18 anos.\n{homens} homens foram cadastrados.\n{mulheres20} mulheres têm menos de 20 anos.')
