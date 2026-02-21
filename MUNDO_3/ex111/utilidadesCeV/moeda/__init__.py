def titulo(txt):
    tamanho = len(txt) + 50
    print('~' * tamanho)
    print(f'                         \033[34m{txt}\033[m')
    print('~' * tamanho)


def aumentar(valor, aumento, arrumar=False):
    fator = 1 + aumento*0.01
    if arrumar:
        return moeda(valor*fator)
    else:
        return valor*fator


def diminuir(valor, desconto, arrumar=False):
    fator = 1 - desconto*0.01
    if arrumar:
        return moeda(valor*fator)
    else:
        return valor*fator


def dobro(valor, arrumar=False):
    if arrumar:
        return moeda(valor*2)
    else:
        return valor*2


def metade(valor, arrumar=False):
    if arrumar:
        return moeda(valor/2)
    else:
        return valor/2


def moeda(valor):
    valor = f'{valor:05.2f}'
    return f'R${valor.replace('.', ',')}'


def resumo(valor, _aumento, _desconto):
    titulo('RESUMO DO VALOR')
    dados = ('Preço analisado:', moeda(valor),
             'Dobro do preço:', dobro(valor, True),
             'Metade do preço:', metade(valor, True),
             f'{_aumento}% de aumento:', aumentar(valor, _aumento, True),
             f'{_desconto}% de redução:', diminuir(valor, _desconto, True))
    for chave, valor in enumerate(dados):
        if chave%2==0:
            print(f'{dados[chave]:.<54}', end='')
        else:
            print(f'{dados[chave]}')
    print('='*65)
