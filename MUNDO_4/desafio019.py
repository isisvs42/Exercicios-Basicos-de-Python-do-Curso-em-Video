'''
Crie a classe Livro, que vai simular a passagem de páginas
de um livro, considerando também se o usuário chegou ao
fim da leitura
'''
from time import sleep
from rich import print

class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f'Você acabou de abrir o livro {self.titulo}. Você está na página {self.pagina_atual}')

    def avancar_paginas(self, quantidade):
        for pagina in range(self.pagina_atual, quantidade+1):
            if pagina > self.paginas:
                print('Você não pode avançar mais nas páginas. O livro acabou.')
                break

            else:
                if pagina < self.paginas:
                    print(f'Página {pagina}', end=' > ', flush=True)
                    sleep(0.3)

                if pagina == quantidade:
                    self.pagina_atual = pagina
                    print(f"Parabéns! Agora, você está na página {self.pagina_atual}")

                if pagina == self.paginas:
                    print(f"Parabéns, você chegou ao final do livro! Você está na página {pagina}")
                
                
l1 = Livro('O Pequeno Príncipe', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(30)
 