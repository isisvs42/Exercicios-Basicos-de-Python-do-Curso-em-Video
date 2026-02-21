"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

from emoji import emojize

cores = {
    'limpa': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco_brilhante': '\033[97m'
}

titulo = 'ANÁLISE DE APROVAÇÃO DE EMPRÉSTIMO'
print(f"{cores['magenta']}{titulo:=^100}{cores['limpa']}")

valor_casa = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe o seu salário mensal: R$ '))
anos = float(input('Em quantos anos pretende pagar? '))

limite = salario * 0.3
meses = anos * 12
prestacao = valor_casa / meses

if prestacao > limite:
    print(emojize(
        f"{cores['vermelho']}:xis: Empréstimo não aprovado{cores['limpa']}. "
        f"A prestação seria de {cores['vermelho']}R${prestacao:.2f}{cores['limpa']}, "
        f"valor superior a 30% do salário ({cores['vermelho']}R${limite:.2f}{cores['limpa']}).",
        language='pt'
    ))

elif prestacao == limite:
    print(emojize(
        f"{cores['amarelo']}:rosto_amedrontado: Empréstimo aprovado no limite permitido{cores['limpa']}. "
        f"A prestação será de {cores['amarelo']}R${prestacao:.2f}{cores['limpa']}, "
        f"correspondente a 30% do salário.",
        language='pt'
    ))

else:
    print(emojize(
        f"{cores['verde']}:marca_de_seleção_branca: Empréstimo aprovado{cores['limpa']}. "
        f"A prestação será de {cores['verde']}R${prestacao:.2f}{cores['limpa']}.",
        language='pt'
    ))