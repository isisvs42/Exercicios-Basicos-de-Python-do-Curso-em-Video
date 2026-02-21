"""
Crie uma tupla com palavras e mostre as vogais de cada uma.
"""

palavras = ('Urso', 'Computador', 'Dedo', 'Cookie', 'Guerra', 'Emocional', 'Cantar', 'Gato', 'Fantasma', 'Escola')
for palavra in palavras:
    if palavra == 'Urso':
        print(f'A palavra {palavra.upper()} possui as seguintes vogais: ', end = '')
        for letra in palavra.lower():
            if letra in 'aeiou':
                print(letra, end=' ')
    else:
        print(f'\nA palavra {palavra.upper()} possui as seguintes vogais: ', end = '')
        for letra in palavra.lower():
            if letra in 'aeiou':
                print(letra, end=' ')
