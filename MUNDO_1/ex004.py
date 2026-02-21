"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ele.
"""

a = input('Digite qualquer coisa: ')
print(f'É um número. {a.isnumeric()}')
print(f'Possui somente letras. {a.isalpha()}')
print(f'Possui só letras e/ou números, sem caracteres especiais ou espaços. {a.isalnum()}')
print(f'Está somente com letras maiúsculas. {a.isupper()}')
print(f'Está somente com letras minúsculas. {a.islower()}')
print(f'Cada palavra começa com letra maíuscula e o resto é minúscula (formatação de título). {a.istitle()}')
print(f'Apenas contém letras do alfabeto inglês, números e/ou símbolos comuns. {a.isascii()}')
print(f'Possui somente dígitos de 0 a 9. {a.isdecimal()}')
print(f'Possui somente dígitos numéricos de 0 a 9 ou em outras línguas. {a.isdigit()}')
print(f'Essa palavra serviria como um identificador válido em um script, a exemplo de uma variável. {a.isidentifier()}')
print(f'Todos os caracteres são imprimíveis, ou seja, podem ser exibidos ou renderizados em uma tela/dispositivo grágico. {a.isprintable()}')
print(f'O texto é só um espaço em branco. {a.isspace()}')
