'''
Crie a classe Gamer, onde podemos cadastrar nome,
nick e os jogos favoritos de uma pessoa. Crie
também um método que permita mostrar a ficha
desse gamer.
'''
from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nomeReal, nomeJogo):
        self.nome = nomeReal
        self.nick = nomeJogo
        self.favoritos = []

    def add_favoritos(self, nomeDoJogo):
        jogo = f'\n:video_game: [blue]{nomeDoJogo}[/]'
        self.favoritos.append(jogo)
        self.favoritos.sort()

    def ficha(self):
        favoritos = ''.join(self.favoritos)
        ficha = Panel(f'''
Nome real: [black on blue]{self.nome}[/]
Jogos favoritos: {favoritos}''', title=f'Jogador <{self.nick}>', width=50)        
        print(ficha)


j1 = Gamer('Jean Dias', 'destruidor_de_series')
j1.add_favoritos('Red Dead Redemption 2')
j1.add_favoritos('The Last of Us')
j1.add_favoritos('Bully')
j1.add_favoritos('GTA VI')
j1.add_favoritos('Super Meat Boy')
j1.add_favoritos('Final Fantasy VII Remake')
j1.add_favoritos('Super Mario Galaxy')

j1.ficha()
