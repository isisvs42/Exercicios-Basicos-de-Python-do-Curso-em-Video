def aumentar(valor, aumento):
    fator = 1 + aumento*0.01 # transforma o parâmetro aumento em um número centesimal
    return valor*fator # calcula o aumento percentual


def diminuir(valor, desconto):
    fator = 1 - desconto*0.01
    return valor*fator


def dobro(valor):
    return valor*2


def metade(valor):
    return valor/2

