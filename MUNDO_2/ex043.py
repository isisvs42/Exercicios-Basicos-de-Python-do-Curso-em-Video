"""
Leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status.
"""

titulo = 'CÁLCULO DO IMC'
print(f'{titulo:=^100}')

peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em metros: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Classificação: abaixo do peso.')

elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Classificação: peso adequado.')

elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Classificação: sobrepeso.')

elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Classificação: obesidade.')

elif imc >= 40:
    print(f'Seu IMC é {imc:.1f}. Classificação: obesidade grau III.')