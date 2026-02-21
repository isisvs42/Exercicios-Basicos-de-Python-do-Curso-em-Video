def leiaInt(enunciado):
    while True:
        try:
            a = int(input(enunciado))
        except (ValueError, TypeError): # o que acontece enquanto um número inteiro não for digitado
            print('\033[31mERRO: por favor, digite um número INTEIRO válido.\033[m')
        else: # o loop só para quando o usuário digitar um número inteiro
            break
    return a