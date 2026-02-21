'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista = []

for c in range(5):
    n = int(input('Digite um valor: '))

    if not lista:  # Se a lista estiver vazia, apenas adiciona o número
        lista.append(n)
        print('Esse valor foi adicionado na posição final da lista.')
    else:
        # Percorre a lista para localizar a posição correta de inserção
        for i in range(len(lista)):
            if n <= lista[i]:
                # Insere n na posição i caso seja menor ou igual ao elemento atual
                lista.insert(i, n)
                print(f'Esse valor foi adicionado na posição {i} da lista.')
                break  # Interrompe o laço após a inserção

        else:
            # Esse else pertence ao for: executa apenas se o laço terminar
            # sem encontrar posição (ou seja, sem executar o break).
            # Isso indica que o valor é maior que todos os existentes.
            lista.append(n)
            print(f'Esse valor foi adicionado na posição {lista.index(n)} da lista.')

print(f'Aqui está a lista em ordem crescente: {lista}')