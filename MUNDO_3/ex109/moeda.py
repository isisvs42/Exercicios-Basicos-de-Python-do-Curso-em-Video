def aumentar(valor=0, aumento=0, arrumar=False):
    fator = 1 + aumento*0.01
    # res = valor*fator
    # return res if arrumar is False else moeda(res)
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
    return f'{_moeda}{valor.replace('.', ',')}'

# O valor padrão é 0.0 (float) em vez de 0 (int) por dois motivos:
# 1. A formatação com ":05.2f" espera um número de ponto flutuante (float), e usar um inteiro pode gerar resultados
#    inesperados.

# 2. O PyCharm (e outras IDEs com verificação de tipo) detecta que o valor passado para moeda() normalmente vem de ope-
#    rações como "valor * fator", que resultam em float. Se o parâmetro tiver valor padrão int (0), isso gera um aviso
#    de tipo: "Expected type 'int', got 'float' instead". Usar 0.0 como padrão evita esse conflito de tipos.

# 3. Apesar disso, em tempo de execução, o Python aceita perfeitamente valores float mesmo quando o valor padrão é int,
#    porque o tipo do valor passado na chamada da função substitui o padrão. O erro detectado é apenas estático (na IDE),
#    e não afeta a execução do programa. Por isso que, no programa "ex109", mesmo que o usuário digite "12.5", por exem-
#    plo, as funções "metade", "dobro" etc continuam funcionando
