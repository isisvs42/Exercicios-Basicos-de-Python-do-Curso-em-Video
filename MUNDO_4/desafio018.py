'''
Crie a classe Churrasco, onde seja possível
informar quantas pessoas vão participar e mostre
quanto de carne deve ser comprado, o total do
churrasco e o preço por pessoa.

Consumo padrão: 400g por pessoa
Preço: R$82,40/kg
'''
from rich import print
from rich.panel import Panel

class Churrasco():
    consumo_padrao = 0.400
    preco_quilo_padrao = 82.4

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

        self.quilos_totais = quantidade * self.consumo_padrao
        self.preco_por_pessoa = self.quilos_totais * self.preco_quilo_padrao / quantidade

    def analisar(self):
        analise = Panel(f'''
Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]
Para comprar os [red]{self.quilos_totais}kg [/] necessários, cada pessoa deve pagar [red]R${self.preco_por_pessoa:,.2f}[/].
''', title=self.titulo)
        print(analise)

c1 = Churrasco("Não Aconselho a ir nesse churrasco", 15)
c1.analisar()