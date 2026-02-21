"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal.
"""

from emoji import emojize

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'azul': '\033[34m',
    'magenta': '\033[35m'
}

titulo = 'CONVERSOR DE BASE NUMÉRICA'
print(f"{cores['magenta']}{titulo:=^100}{cores['limpa']}")

numero = int(input('Digite um número inteiro: '))

base = int(input("""Selecione a base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
[ 4 ] Todas as opções
Opção desejada: """))

if base == 1:
    resultado = bin(numero)
    print(f"Número {cores['azul']}{numero}{cores['limpa']} em binário: "
          f"{cores['azul']}{resultado[2:]}{cores['limpa']}")

elif base == 2:
    resultado = oct(numero)
    print(f"Número {cores['azul']}{numero}{cores['limpa']} em octal: "
          f"{cores['azul']}{resultado[2:]}{cores['limpa']}")

elif base == 3:
    resultado = hex(numero)
    print(f"Número {cores['azul']}{numero}{cores['limpa']} em hexadecimal: "
          f"{cores['azul']}{resultado[2:]}{cores['limpa']}")

elif base == 4:
    binario = bin(numero)
    octal = oct(numero)
    hexadecimal = hex(numero)

    print(f"""Número {cores['azul']}{numero}{cores['limpa']} convertido:
-> Binário: {cores['azul']}{binario[2:]}{cores['limpa']}
-> Octal: {cores['azul']}{octal[2:]}{cores['limpa']}
-> Hexadecimal: {cores['azul']}{hexadecimal[2:]}{cores['limpa']}""")

else:
    print(emojize(
        f"{cores['vermelho']}:xis: Opção inválida ({base}). "
        f"Selecione uma alternativa válida.{cores['limpa']}",
        language='pt'
    ))