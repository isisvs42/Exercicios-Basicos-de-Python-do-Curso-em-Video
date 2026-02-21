"""
Mostre um número por extenso (0 a 20) usando tupla.
"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('Esse número não está no intervalo de 0 a 20. Tente novamente: '))
print(f'Você digitou o número {numeros[n]}.')
