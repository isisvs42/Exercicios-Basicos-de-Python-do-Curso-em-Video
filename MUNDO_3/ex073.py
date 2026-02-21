"""
Trabalhe com os 20 primeiros colocados do Campeonato Brasileiro e mostre informações solicitadas.
"""
times = ("Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Corinthians",
    "Bahia",
    "Cruzeiro",
    "Vasco da Gama",
    "Vitória",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Juventude",
    "Red Bull Bragantino",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá")

titulo = 'CAMPEONATO BRASILEIRO DE FUTEBOL 2024'
print(f'{titulo:=^350}')

print(f'\033[32mOs vinte primeiros colocados do Campeonato Brasileiro são: ', end='')
for time in times:
    if time != 'Cuiabá':
        print(f'{time}, ', end='')
    else:
        print(f'{time}.')

print('\033[m-=' * 175)

print(f'\033[33mOs cinco primeiros colocados são: ', end='')
for time in times[:5]:
    if time != 'Internacional':
        print(f'{time}, ', end='')
    else:
        print(f'{time}.')

print('\033[m-=' * 175)

print(f'\033[34mOs quatro últimos colocados são: ', end='')
for time in times[-4:]:
    if time != 'Cuiabá':
        print(f'{time}, ', end='')
    else:
        print(f'{time}.')

print('\033[m-=' * 175)

print(f'\033[32mOs times em ordem alfabética: ', end='')
for time in sorted(times):
    if time != 'Vitória':
        print(f'{time}, ', end='')
    else:
        print(f'{time}.')

print('\033[m-=' * 175)

print(f'\033[33mO Vasco da Gama está na {times.index("Vasco da Gama") + 1}ª posição.')

print('\033[m=' * 350)