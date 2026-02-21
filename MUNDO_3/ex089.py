"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""

alunos = []
while True:
    aluno = []
    r='q'
    nome = str(input('Nome do aluno: ')).title()
    aluno.append(float(input('Nota 1: '))) # posição 0
    aluno.append(float(input('Nota 2: '))) # 1
    media = sum(aluno)/2
    aluno.append(nome) # 2
    aluno.append(media) # 3
    alunos.append(aluno)
    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
    if r =='n':
        print('='*50)
        break
    print('='*50)
print('Nº   NOME                MÉDIA')
print('-'*36)
for numero, aluno in enumerate(alunos):
    print(f'{numero: <5}{aluno[2]: <20}{aluno[3]:.2f}')
print('-'*36)
while True:
    n = int(input('Deseja ver as notas de qual aluno (999 para parar)? '))
    if n == 999:
        print('=' * 50)
        print('Finalizando programa... Volte sempre!')
        break
    print(f'As notas de \033[34m{alunos[n][2]}\033[m são \033[31m{alunos[n][0:2]}\033[m.')
    print('=' * 50)
