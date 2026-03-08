'''
Crie a classe ControleRemoto, onde vamos simular
o funcionamento de um controle simples (canal,
volume e liga/desliga)

@ = liga/desliga
< e > = avançar/voltar nos canais
+ e - = aumentar/diminuir volume

0 para sair do programa
'''
from modulo import ControleRemoto
import os

controle = ControleRemoto()

while True:
    os.system('clear')

    controle.mostrarTv()
    entrada = input(f'< CH{controle.canalAtual+1} > - VOL{controle.volumeAtual+1} +    ')
    

    if entrada == '@':
        controle.ligaDesliga()

    elif entrada == '>':
        controle.avancarCanal()

    elif entrada == '<':
        controle.voltarCanal()

    elif entrada == '+':
        controle.aumentarVolume()

    elif entrada == '-':
        controle.diminuirVolume()

    elif entrada == '0':
        break
