'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a sua expressão: '))
lista = []

for digito in expressao:
    if digito == '(':
        lista.append(digito)

    elif digito == ')':
        if len(lista) > 0:
            lista.pop()  # Remove o último '(' armazenado
        else:
            # Situação inválida: há um ')' sem um '(' correspondente
            lista.append(')')  # Garante que len(lista) > 0 ao final
            break  # Não é necessário continuar a verificação

if len(lista) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está errada!')