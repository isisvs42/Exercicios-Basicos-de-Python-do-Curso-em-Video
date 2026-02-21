"""
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:

~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def escreva(texto):
    caracteres = len(texto)+4
    for digito in range(caracteres):
        print('~', end='')
    print(f'\n  {texto}')
    for digito in range(caracteres):
        print('~', end='')


# Programa Principal
escreva('Ísis Valois Sampaio')
print()
escreva('Curso de Python no YouTube')
print()
escreva('Flor')
print()
escreva('Engenharia da Computação')

# Uma forma mais simples de ter feito o programa era:
# def escreva(msg):
#     tamanho = len(msg)+4
#     print('~'*tamanho)
#     print(f'  {msg}')
#     print('~'*tamanho)
