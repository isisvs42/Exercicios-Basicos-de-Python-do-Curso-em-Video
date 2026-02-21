"""
Leia nome e preço de vários produtos e mostre estatísticas no final.
"""

titulo = 'CONTROLE DE LOJA'
print(f'\033[31m{titulo:~^100}\033[m')

produto_mais_barato = ''
total = produtos_mais_1000 = preco_menor = c = 0

while True:
    continua = 't'
    produto = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$'))

    c += 1
    total += preco

    if c == 1 or preco < preco_menor:
        preco_menor = preco
        produto_mais_barato = produto

    if preco > 1000:
        produtos_mais_1000 += 1

    while continua not in 'sn':
        continua = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]

    if continua == 'n':
        break

    print('=' * 100)

print(f'O total acumulado foi de \033[31mR${total:.2f}\033[m.'
      f'\nAo todo, \033[31m{produtos_mais_1000}\033[m produtos custam mais de R$1000,00.'
      f'\nO produto com menor preço foi \033[31m{produto_mais_barato}\033[m, '
      f'custando \033[31mR${preco_menor:.2f}\033[m.')