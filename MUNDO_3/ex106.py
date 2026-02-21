"""
Faça um minissistema que utilize o interactive help do Python

O usuário vai digitar o comando e o manual vai aparecer.

Quando o usuário digitar a palavra "FIM", o programa se encerrará!.

OBS: use cores.
"""

from time import sleep
cores = {
    'rosa': '\033[45;30m',  # Fundo rosa, texto preto
    'branco': '\033[107;30m',  # Fundo branco, texto preto
    'verde': '\033[42;30m',  # Fundo verde, texto preto
    'limpa': '\033[m'  # Código para resetar as cores
}

def titulo(cor, txt):
    tamanho = len(txt)
    print(cores[cor] + '~' * (tamanho + 4))  # Linha superior com cor
    print(f'  {txt}')  # Texto centralizado
    print('~' * (tamanho + 4))  # Linha inferior
    sleep(1)


def ajuda(enunciado):
    _comando = input(enunciado)

    # Se o usuário digitar "FIM", interrompemos retornando None explicitamente
    if _comando.strip().upper() == 'FIM':
        return None  # <- Aqui o None indica que o programa deve encerrar o loop principal

    titulo('rosa', f'Acessando o manual do comando {_comando}')
    print(cores['branco'])
    help(_comando)  # A função help() já imprime o manual diretamente no terminal; não precisa colocar no return
    sleep(1)
    return _comando  # Retorna o comando digitado para checar no laço principal


# Programa Principal
titulo('verde', 'SISTEMA DE AJUDA PyHELP')

while True:
    resultado = ajuda('\033[mFunção ou Biblioteca> ')

    # Se a função ajuda() retornar None (quando o usuário digita FIM), o loop é encerrado
    if resultado is None:
        break
