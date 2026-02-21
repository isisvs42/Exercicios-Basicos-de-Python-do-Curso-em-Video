"""
Crie uma tupla com nomes de produtos e preços e mostre em formato tabular.
"""

compras = ('Arroz (pacote de 5kg)', 25,
           'Feijão carioca (pacote de 1kg)', 3.50,
           'Leite integral (1 litro)', 4.35,
           'Pão francês (1kg)', 15,
           'Carne bovina (1kg)', 32,
           'Peito de frango (1kg)', 12,
           'Banana prata (1kg)', 5,
           'Tomate (1kg)', 6.5,
           'Batata inglesa (1kg)', 4,
           'Chocolate ao leite (barra de 100g)', 7)

titulo = 'LISTA DE COMPRAS'
print('=' * 50)
print(f'{titulo:^50}')
print('=' * 50)

total = 0

# Outra forma de construir o for seria:
# for compra in range(0, len(compras)):

for posicao, compra in enumerate(compras):
    if posicao % 2 == 0:
        print(f'{compra:.<43}', end='')
    else:
        print(f'R${compra:05.2f}')
        total += compra
        # 0  → preenche com zeros à esquerda
        # 5  → largura total do campo
        # .2f → duas casas decimais

# Outra alternativa:

# for compra in range(0, len(compras), 2):
#     print(f'{compras[compra]:.<43}', end='')
#     print(f'R${float(compras[compra+1]):05.2f}')
#     total += float(compras[compra+1])

# O passo 2 é utilizado porque os dados estão organizados em pares (nome + preço).
# Isso garante que cada iteração acesse corretamente um produto e seu respectivo valor.

"""
i = 0  → compras[compra] = 'Arroz',   compras[compra+1] = 25
i = 2  → compras[compra] = 'Feijão',  compras[compra+1] = 3.50
i = 4  → compras[compra] = 'Leite',   compras[compra+1] = 4.35
...
"""

print('=' * 50)

final = 'TOTAL'
print(f'{final:.<42}', end='')
print(f'R${total:05.2f}')

print('=' * 50)