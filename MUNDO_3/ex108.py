"""
Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.
"""

from ex108 import moeda
n = float(input('Digite o valor que almeja calcular: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'Com um aumento de 10%, o novo valor é {moeda.moeda(moeda.aumentar(n, 10))}.')
print(f'Com uma diminuição de 13%, o novo valor é {moeda.moeda(moeda.diminuir(n, 13))}.')
