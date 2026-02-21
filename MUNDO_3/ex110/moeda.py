def titulo(txt):
    tamanho = len(txt) + 50
    print('~' * tamanho)
    print(f'                         \033[34m{txt}\033[m')
    print('~' * tamanho)


def aumentar(valor=0, aumento=0, arrumar=False):
    fator = 1 + aumento*0.01
    if arrumar:
        return moeda(valor*fator)
    else:
        return valor*fator


def diminuir(valor=0, desconto=0, arrumar=False):
    fator = 1 - desconto*0.01
    if arrumar:
        return moeda(valor*fator)
    else:
        return valor*fator


def dobro(valor=0, arrumar=False):
    if arrumar:
        return moeda(valor*2)
    else:
        return valor*2


def metade(valor=0, arrumar=False):
    if arrumar:
        return moeda(valor/2)
    else:
        return valor/2


def moeda(valor=0.0, _moeda='R$'):
    valor = f'{valor:05.2f}'
    return f'R${valor.replace('.', ',')}'


def resumo(valor=0, _aumento=0, _desconto=0):
    titulo('RESUMO DO VALOR')
    dados = ('Preço analisado:', moeda(valor),
             'Dobro do preço:', dobro(valor, True),
             'Metade do preço:', metade(valor, True),
             f'{_aumento}% de aumento:', aumentar(valor, _aumento, True),
             f'{_desconto}% de redução:', diminuir(valor, _desconto, True))
    for chave, valor in enumerate(dados):
        if chave%2==0:
            print(f'{dados[chave]:.<54}', end='') # 55 supondo que o máximo que o usuário vai digitar terá o formato 000000.00
        else:
            print(f'{dados[chave]}') # daria também para ter usado o \t, q é a tabulação, fazendo os preços ficarem alinhados
    print('='*65)
