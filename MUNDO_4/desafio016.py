'''
Crie a classe Funcionario, onde podemos cadastrar
nome, setor e cargo. Crie também um método que 
permita ao funcionário se apresentar.
'''
from rich import print

class Funcionario():
    def __init__(self, nome='desconhecido', setor='desconhecido', cargo='desconhecido'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':waving_hand:Olá, sou [blue]{self.nome}[/] e eu sou {self.cargo} do setor {self.setor} da empresa'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
        
