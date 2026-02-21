"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples.

O sistema só vai ter duas opções: cadastrar uma nova pessoa
e listar as pessoas cadastradas
"""

from ex115.eu.cadastrar import *

while True:
    print('-' * 50)
    print(f'{'MENU PRINCIPAL': ^50}')
    print('-' * 50)
    print('''\033[93m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[93m2\033[m - \033[34mCadastrar nova pessoa\033[m
\033[93m3\033[m - \033[34mSair do sistema\033[m''')
    print('-' * 50)
    try:
        opcao = int(input('\033[93mSua Opção:\033[m '))
        if opcao not in (1, 2, 3):
            raise ValueError  # Se o usuário digitar 9, por exemplo, isso não causa um erro naturalmente — int('9')
                              # funciona. Mas como 9 não é uma opção válida, usamos raise ValueError para forçar o progra-
                              # ma a agir como se fosse erro e cair no except.
    except (ValueError, TypeError):
        print('-' * 50)
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
    else:
        if opcao == 1:
            mostrar_cadastrados()
            sleep(2)
        elif opcao == 2:
            novo_cadastro()
            sleep(2)
        else:
            sleep(2)
            print('-' * 50)
            print(f'{'Saindo do sistema... Até logo!': ^50}')
            print('-' * 50)
            break

