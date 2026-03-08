from rich import print
from rich.traceback import install
from rich.panel import Panel
install()

class ControleRemoto():
    def __init__(self):
        self.canais = [True, False, False, False, False]
        self.volume = [True, False, False, False, False]
        self.canalAtual = 0
        self.volumeAtual = 0
        self.tvLigada = False

    def mostrarCanais(self):
        canais_str = ""
        for n, canal in enumerate(self.canais):
            if canal:
                canais_str += f"[white on purple] {n+1} [/]"
            else:
                canais_str += f" {n+1} "
        return canais_str

    def mostrarVolume(self):
        volume_str = "[white on green]"
        for volume in self.volume:
            if volume:
                volume_str += " [/]"
            else:
                volume_str += " "
        return volume_str

    def mostrarTv(self):
        if self.tvLigada:
            tv = Panel(
                f"CANAL = {self.mostrarCanais()}\nVOLUME = {self.mostrarVolume()}",
                title="[ TV ]",
                width=30
            )
        else:
            tv = Panel(":x: [red]A TV está desligada[/]", title="[ TV ]", width=30)

        print(tv)

    def ligaDesliga(self):
        self.tvLigada = not self.tvLigada

    def avancarCanal(self):
        if not self.tvLigada:
            print('A TV está desligada!')
            return
        
        self.canalAtual = (self.canalAtual + 1) % 5 # quando o estado atual for 4 e avançarmos, teremos o resto de 5 dividido por 5 igual a 0, reiniciando

        for n in range(0, 5):
            if n == self.canalAtual:
                self.canais[n] = True
            
            else:
                self.canais[n] = False
    
    def voltarCanal(self):
        if not self.tvLigada:
            print('A TV está desligada!')
            return
        
        self.canalAtual = (self.canalAtual - 1) % 5
            # se estiver no canal 0 e voltar: 0 - 1 = -1 / 5 = 0 e resto -1 (ou seja, último item da lista)
            # a contagem pode ficar de trás para a frente: -1, -2, -3, -4...
            # quando chegar no -5: -5 / 5 = -1 e resto 0 (ou seja, o primeiro item da lista, que é o -5)
        
        for n in range(4, -1, -1):
            if n == self.canalAtual:
                self.canais[n] = True
            
            else:
                self.canais[n] = False
            
    def aumentarVolume(self): 
        if not self.tvLigada:
            print('A TV está desligada!')
            return
        
        if self.volumeAtual == 4:
            return
        else:
            self.volumeAtual +=1

        for n in range(0, 5):
            if n == self.volumeAtual:
                self.volume[n] = True
            
            else:
                self.volume[n] = False

    def diminuirVolume(self): 
        if not self.tvLigada:
            print('A TV está desligada!')
            return
        
        if self.volumeAtual == 0:
            return
        else:
            self.volumeAtual -=1

        for n in range(4, -1, -1):
            if n == self.volumeAtual:
                self.volume[n] = True
            
            else:
                self.volume[n] = False
