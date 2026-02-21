"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests
try:
    url = 'https://www.pudim.com.br/'
    acesso = requests.get(url)
    # ↘
    #   O Python está indo até o site (como se fosse um navegador) e pedindo para ver a página.
    #   Isso é chamado de requisição HTTP ("Me mostre essa página") do tipo GET, que basicamente significa:
    #   “Me envie os dados dessa página!”
    #    O conteúdo da resposta do site será armazenado na variável 'acesso'
    if acesso.status_code == 200:
        print('\033[32mO site \033[4;34mpudim.com\033[0;32m pode ser acessado pelo usuário! :)\033[m')
        # o 4 faz ficar sublinhado, e o 0 tira essa formatação
except requests.exceptions.RequestException:
    print('\033[31mO site \033[4;34mpudim.com\033[0;31m não está acessível :(\033[m')
