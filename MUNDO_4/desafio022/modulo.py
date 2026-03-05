from rich import print
from rich.panel import Panel

class ControleRemoto():
    def __init__(self):
        self.canais = [True, False, False, False, False]
        self.volume = [True, False, False, False, False]
        self.canalAtual = 1
        self.volumeAtual = 1
        self.tvLigada = False

    def mostrarTv(self):
        if self.tvLigada:
            tv = Panel(f'''
CANAL = [{'yellow' if self.canais[0] else '/'}] 1 [/] [{'yellow' if self.canais[1] else '/'}] 2 [/] [{'yellow' if self.canais[2] else '/'}] 3 [/] [{'yellow' if self.canais[3] else '/'} 4 [/] [{'yellow' if self.canais[4] else '/'}] 5 [/]
VOLUME = [{'yellow' if self.canais[0] else '/'}]   [{'yellow' if self.canais[1] else '/'}]   [{'yellow' if self.canais[2] else '/'}]   [{'yellow' if self.canais[3] else '/'}   [{'yellow' if self.canais[4] else '/'}]   [/]''',
title = '[ TV ]')
            
        else:
            tv = Panel(f':x: [red]A TV está desligada[/]', title = '[ TV ]') 
        print(tv)

    