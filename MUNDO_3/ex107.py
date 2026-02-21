"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

o 'diminuir()', mesma coisa.

"""

from ex107 import moeda
n = float(input('Digite o valor que almeja calcular: R$'))
print(f'A metade de {n} é {moeda.metade(n)}.')
print(f'O dobro de {n} é {moeda.dobro(n)}.')
print(f'Com um aumento de 10%, o novo valor é {moeda.aumentar(n, 10)}.')
print(f'Com uma diminuição de 13%, o novo valor é {moeda.diminuir(n, 13)}.')
