"""
Leia números até 999 e mostre quantidade e soma (desconsiderando 999).
"""

contador = soma = 0
while True:
    n = int(input('Digite um valor inteiro [999 para parar]: '))
    if n == 999:
        break
    contador+=1
    soma+=n
print(f'Você digitou {contador} números, que somados dão {soma}.')
