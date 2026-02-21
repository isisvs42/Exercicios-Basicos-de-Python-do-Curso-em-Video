"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem final de acordo com a média atingida.
"""

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'verde': '\033[32m',
    'magenta': '\033[35m'
}

titulo = 'RESULTADO DA MÉDIA'
print(f"{cores['magenta']}{titulo:=^100}{cores['limpa']}")

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if 0 <= media < 5:
    print(f"{cores['vermelho']}REPROVADO{cores['limpa']} "
          f"Sua média foi {cores['vermelho']}{media:.1f}{cores['limpa']}, abaixo de 5,0.")

elif 5 <= media < 7:
    print(f"{cores['amarelo']}RECUPERAÇÃO{cores['limpa']} "
          f"Sua média foi {cores['amarelo']}{media:.1f}{cores['limpa']}, "
          f"dentro da faixa de 5,0 a 6,9.")

elif 10 >= media >= 7:
    print(f"{cores['verde']}APROVADO{cores['limpa']} "
          f"Sua média foi {cores['verde']}{media:.1f}{cores['limpa']}.")

else:
    print(f"Valor inválido. A média calculada foi "
          f"{cores['vermelho']}{media:.2f}{cores['limpa']}.")