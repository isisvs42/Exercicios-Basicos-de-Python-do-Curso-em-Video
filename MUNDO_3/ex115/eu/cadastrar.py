lista = []
from time import sleep
# Tenta abrir o arquivo de cadastros existentes
try:
    with open('cadastros.txt', 'r', encoding='utf-8') as _arquivo:
        # open('cadastros.txt', 'r', encoding='utf-8')
        # → Abre o arquivo chamado cadastros.txt no modo de leitura ('r' = read).
        # → O argumento encoding='utf-8' garante que acentos e caracteres especiais sejam lidos corretamente.
        #
        # with ... as _arquivo:
        # → Cria um bloco de leitura seguro:
        # as → é uma palavra-chave do Python que dá um nome ao recurso que está sendo aberto (neste caso, o _arquivo).
        # _arquivo → é apenas o nome (apelido) que você escolhe para acessar o arquivo dentro do bloco; é o apelido do
        # arquivo aberto — você usa _arquivo.read(), _arquivo.readline() ou percorre for linha in _arquivo.
        # O with garante que o arquivo será fechado automaticamente no final do bloco, mesmo se ocorrer erro.

        for linha in _arquivo:
            nome, idade = linha.strip().split(';')  # Suponha que 'linha' seja algo como: "Carlos Eduardo Martins Silva;34\n"
                                                    # 1. .strip() remove espaços e o '\n' no fim da linha
                                                    # 2. .split(';') divide a string (onde há um ';') em uma lista com duas partes: nome e idade
                                                    # 3. nome, idade = ... faz o "desempacotamento", colocando a primeira parte em 'nome' e a segunda em 'idade'
                                                    # A linha:
                                                    # nome, idade = ["Carlos Eduardo Martins Silva", "34"]
                                                    # é o que chamamos de desempacotamento de lista (ou de tupla). Ela atribui cada valor a uma variável:
                                                    # nome = "Carlos Eduardo Martins Silva"
                                                    # idade = "34"

            lista.append(nome)                      # Adiciona o nome à lista
            lista.append(int(idade))                # Adiciona a idade convertida em inteiro
except FileNotFoundError:
    # Se o arquivo não existir, usamos os 10 cadastros fictícios
    lista = [ 'Ana Beatriz Souza Lima', 29,
              'Carlos Eduardo Martins Silva', 34,
              'Juliana Cristina Pereira Rocha', 26,
              'Rafael Augusto Oliveira Santos', 41,
              'Fernanda Maria Costa Almeida', 37,
              'Lucas Gabriel de Souza', 22,
              'Patrícia Renata Lima Cardoso', 31,
              'Roberto Henrique Silva Júnior', 28,
              'Isabela Carolina Monteiro Almeida', 25,
              'Vinícius José da Silva', 33]

    # Como o arquivo não existia, salvamos esses cadastros no arquivo
    with open('cadastros.txt', 'w', encoding='utf-8') as arquivo:
        # 'w' = write (escrita)
        # → Abre o arquivo para escrever do zero.
        # ⚠️ Se o arquivo já existir, ele será APAGADO e reescrito.
        # Também usa encoding='utf-8' para manter compatibilidade com acentos.
        # with ... as arquivo: de novo garante que o arquivo será fechado corretamente após a escrita.
        for i in range(0, len(lista), 2):           # Percorre a lista de 2 em 2, garantindo que lista[i] seja o nome e lista[i+1] seja a idade
            arquivo.write(f'{lista[i]};{lista[i+1]}\n')   # Escreve no arquivo no formato nome;idade
                                                          # O arquivo cadastros.txt tem uma estrutura como esta:
                                                          # Ana Beatriz Souza Lima;29
                                                          # Carlos Eduardo Martins Silva;34
                                                          # ...

def novo_cadastro():
    print('-'*50)
    print(f'{'NOVO CADASTRO': ^50}')
    print('-'*50)
    while True:
        try:
            _nome = str(input('Nome: ')).strip().title()
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite o nome de verdade da pessoa que deseja cadastrar\033[m')
        else:
            break
    while True:
        try:
            _idade = int(input('Idade: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido para a idade\033[m')
        else:
            break
    lista.append(_nome)
    lista.append(_idade)
    # ⬇ Aqui é onde o cadastro fica salvo para sempre
    with open('cadastros.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{_nome};{_idade}\n')


def mostrar_cadastrados():
    print('-'*50)
    print(f'{'PESSOAS CADASTRADAS': ^50}')
    print('-'*50)
    for posicao, informacao in enumerate(lista):
        if posicao%2==0:
            print(f'{informacao: <43}', end='')
        else:
            print(f'{informacao} anos')


