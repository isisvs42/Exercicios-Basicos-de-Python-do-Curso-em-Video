def aumentar(valor=0, aumento=0):
    fator = 1 + aumento*0.01
    return valor*fator


def diminuir(valor=0, desconto=0):
    fator = 1 - desconto*0.01
    return valor*fator


def dobro(valor=0):
    return valor*2


def metade(valor=0):
    return valor/2

def moeda(valor=0, _moeda='R$'):
    valor = f'{valor:05.2f}' # transforma o valor em uma string formatada
    return f'{_moeda}{valor.replace('.', ',')}' # troca ponto por vírgula
# - 05.2f:
#   - 0: preenche com zeros à esquerda
#   - 5: largura mínima dee 5 caracteres para aí preencher (00.00, total de 5 contando com o ".")
#   - .2f: mostra duas casas decimais, ponto flutuante

# também poderia ter colocado simplesmente:
# return f'{_moeda}{valor:05.2f}'.replace('.', ',')
