'''
Crie a classe Caneta, que simula o funcionamento
de uma caneta colorida, podendo escrever frases
na cor relativa
'''
from rich import print

class Caneta():
    def __init__(self, cor):
        cor = cor.lower().strip()
        if cor == 'verde':
            self.cor = 'green'

        elif cor == 'vermelho':
            self.cor = 'red'

        elif cor == 'azul':
            self.cor = 'blue'

        else:
            print('Cor indisponível')

        self.tampada = True

    def destampar(self):
        self.tampada = False

    def quebrar_linha(self, linhas):
        for linha in range(linhas):
            print('\n')

    def escrever(self, frase):
        if not self.tampada:
            print(f'[{self.cor}]{frase}[/]', end='')

        else:
            print(f'A [{self.cor}]caneta[/] está tampada!')


c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')
c4 = Caneta('preta')
