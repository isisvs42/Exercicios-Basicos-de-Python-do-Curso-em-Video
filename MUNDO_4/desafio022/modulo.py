from rich import print
from rich.traceback import install
from rich.panel import Panel
install()

class ControleRemoto():
    def __init__(self):
        self.canais = [True, False, False, False, False]
        self.volume = [True, False, False, False, False]
        self.canalAtual = 1
        self.volumeAtual = 1
        self.tvLigada = True

    def mostrarCanais(self):
        canais_str = ""
        for n, canal in enumerate(self.canais):
            if canal:
                canais_str += f"[yellow]{n+1}[/] "
            else:
                canais_str += f"{n+1} "
        return canais_str

    def mostrarVolume(self):
        volume_str = ""
        for volume in self.volume:
            if volume:
                volume_str += "[yellow]▮[/]"
            else:
                volume_str += "▯"
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


controle = ControleRemoto()
controle.mostrarTv()