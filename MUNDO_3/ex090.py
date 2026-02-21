"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

dicionario = {
'Nome':str(input('Nome do aluno: ')).title().strip(),
'Média':float(input('Média do aluno: '))
}
print('='*50)
if dicionario['Média'] < 5:
    dicionario['Situação'] = 'REPROVADO'
    print('\033[31mALUNO REPROVADO!\033[m')
elif dicionario['Média'] < 7:
    dicionario['Situação'] = 'RECUPERAÇÃO'
    print('\033[33mALUNO EM RECUPERAÇÃO!\033[m')
else:
    dicionario['Situação'] = 'APROVADO'
    print('\033[32mALUNO APROVADO!\033[m')
for chave, valor in dicionario.items():
    print(f'{chave} é igual a {valor}.')
