"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvido no desafio 108.
"""

from ex109 import moeda
n = float(input('Digite o valor que almeja calcular: R$'))
print('-'*65)
print(f'A metade de \033[34m{moeda.moeda(n)}\033[m é \033[32m{moeda.metade(n, True)}\033[m.')
print('-'*65)
print(f'O dobro de \033[34m{moeda.moeda(n)}\033[m é \033[32m{moeda.dobro(n, True)}\033[m.')
print('-'*65)
print(f'Com um \033[34maumento de 10%\033[m, o novo valor é \033[32m{moeda.aumentar(n, 10, True)}\033[m.')
print('-'*65)
print(f'Com uma \033[34mdiminuição de 13%\033[m, o novo valor é \033[31m{moeda.diminuir(n, 13)}\033[m.') # sem formatação
print('-'*65)
