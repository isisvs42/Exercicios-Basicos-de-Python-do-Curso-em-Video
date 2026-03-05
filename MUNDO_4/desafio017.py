'''
Crie a classe Produto, onde podemos cadastrar nome e 
preço. Crie também um método que mostre uma etiqueta
de preço do produto.
'''
from rich import print
from rich.panel import Panel

class Produto():
    def __init__(self, nome='desconhecido', preco=0.00):
        self.nome = nome
        self.preco = preco
        self._etiqueta = Panel(f'{self.nome:^25}\n\n{'R$' + format(self.preco, ',.2f'):=^25}', title='Produto', width=30, height=5)
        
    def etiqueta(self):
        print(self._etiqueta)

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()
