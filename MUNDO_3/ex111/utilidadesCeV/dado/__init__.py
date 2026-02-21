def leia_dinheiro(enunciado):
    while True:
        lista_sem_ponto = []
        a = input(enunciado).strip()
        b = a.replace(',', '.') # troca a vírgula por ponto
        for digito in b:
            if digito not in '.':
                lista_sem_ponto.append(digito)
        if ''.join(lista_sem_ponto).isnumeric(): # esse metodo nn funciona com num flutuante, por isso a lista
            break
        else:
            print(f'\033[31mERRO: "{a}" é um preço inválido!\033[m')
    return float(b) # agora '4.2' é 4.2

# o "return float(a)" é necessário para que a função retorne o valor digitado corretamente para quem chamou a função.
# sem ele, o valor lido ficaria preso dentro da função e não poderia ser usado no restante do programa


# o "return float(a)" não pode ficar dentro do while True porque isso dificultaria a clareza do fluxo e poderia permitir o
# retorno antes da validação completa;

# ele também não pode ficar dentro do if, pois isso tornaria o 'break' um código inalcançável, já que o return encerra a
# função imediatamente (e vice-versa, se inverter a ordem das linhas em que apareceriam);

# colocar o 'return' fora o while garante que  o programa só devolva o valor depois de validdá-lo corretamente.

def leia_int(enunciado):
    while True:
        try:
            a = int(input(enunciado))
        except (ValueError, TypeError): # o que acontece enquanto um número inteiro não for digitado
            print('\033[31mERRO: por favor, digite um número INTEIRO válido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
        else: # o loop só para quando o usuário digitar um número inteiro
            break
    return a


def leia_float(enunciado):
    while True:
        try:
            a = float(input(enunciado))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número REAL válido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    return a
