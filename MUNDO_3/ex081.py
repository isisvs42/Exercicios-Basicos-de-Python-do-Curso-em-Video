'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
contador = 0

while True:
    r = 'q'
    n = int(input('Digite um valor inteiro: '))
    lista.append(n)
    contador += 1

    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
        if r not in 'sn':
            print('Opção inválida! ', end='')

    if r == 'n':
        break

print('=' * 50)

print(f'Você digitou {contador} elementos.')

print('Os valores em ordem decrescente são: ', end='')
print(', '.join(map(str, sorted(lista, reverse=True))) + '.')

# 1. sorted(lista, reverse=True): ordena a lista em ordem decrescente
# 2. map(str, ...): converte cada número da lista para string
# 3. ', '.join(...): concatena os elementos usando vírgula e espaço como separador
# 4. + '.': adiciona um ponto final ao final da string

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')