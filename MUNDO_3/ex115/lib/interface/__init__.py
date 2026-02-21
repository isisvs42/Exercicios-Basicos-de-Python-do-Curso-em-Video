from ex111 import leiaInt


def linha(tam = 42):
    return '-' * tam, tam


def cabecalho(txt):
    print(linha()[0])
    print(txt.center(linha()[1]))
    print(linha()[0])


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha()[0])
    opc = leiaInt('\033[33mSua Opção\033[m: ')
    return opc

