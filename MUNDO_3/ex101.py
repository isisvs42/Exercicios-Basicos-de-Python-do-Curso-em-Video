"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""

def titulo(txt):
    tamanho = len(txt) + 50
    print('~'*tamanho)
    print(f'                         \033[34m{txt}\033[m')
    print('~'*tamanho)


def voto(ano_de_nascimento):
    from datetime import datetime # importação local, economizando memória
    ano = datetime.now().year
    idade = ano - ano_de_nascimento
    if 16 <= idade < 18 or idade > 70:
        return idade, 'VOTO OPCIONAL' # retorna uma tupla com dois elementos
    elif idade >= 18:
        return idade, 'VOTO OBRIGATÓRIO'
    else:
        return idade, 'NÃO VOTA'


# Programa Principal
titulo('VOTO E IDADE')
dados = voto(int(input('Em que ano você nasceu? '))) # dados é uma tupla com dois elementos
print(f'Com {dados[0]} anos: {dados[1]}!')
