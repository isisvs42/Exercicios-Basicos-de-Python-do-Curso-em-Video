from ex115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # a função 'open' abre um arquivo; rt = leitura em modo texto
        a.close() # fecha arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except OSError as erro:
        # OSError é uma exceção genérica que cobre erros relacionados a entrada e saída (I/O),
        # como: não conseguir abrir, criar, ler ou escrever em arquivos ou diretórios.
        #
        # A sintaxe "as erro" dá um nome ao objeto de exceção capturado,
        # permitindo que você acesse e exiba a mensagem detalhada do erro com print(erro)
        print(f'Houve um erro ao criar o arquivo: {erro}')

    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except OSError as erro:
    # OSError trata erros de arquivos (abrir, ler, escrever, etc.)
    # "as erro" permite acessar a mensagem da exceção com print(erro)
        print(f'Erro ao acessar o arquivo: {erro}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') # cria uma lista
            dado[1] = dado[1].strip()
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at') # a = append; at = adiciona mais dados como arquivo de texto
    except OSError as erro:
    # OSError trata erros de arquivos (abrir, ler, escrever, etc.)
    # "as erro" permite acessar a mensagem da exceção com print(erro)
        print(f'Erro ao acessar o arquivo: {erro}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora do arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

# Usar 'r' ou 'rt' (ou 'w'/'wt', 'a'/'at') dá o mesmo resultado na prática, quando você está lidando com arquivos de tex-
# to no Python em Linux/macOS/Windows.
# O programa do prof só adicionou o 't' para clareza, não por necessidade técnica.
