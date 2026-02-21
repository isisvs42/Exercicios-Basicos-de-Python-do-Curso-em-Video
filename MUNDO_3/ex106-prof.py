from time import sleep
c = ('\033[m', # 0 - limpa
     '\033[30;41m', # 1 - vermelho
     '\033[30;42m', # 2 - verde
     '\033[30;43m', # 3 - amarelo
     '\033[30;44m', # 4 - azul
     '\033[30;45m', # 5 - roxo
     '\033[30;107m'   # 6 - branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
titulo('SISTEMA DE AJUDA', 2)
comando = ''
while True:
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)