"""
Faça uma contagem regressiva de 10 até 0 com pausa de 1 segundo.
"""

from time import sleep
from emoji import emojize
print('CONTAGEM REGRESSIVA!')
sleep(1)
for c in range (10, -1, -1):
    print (f'{c:2}!')
    sleep(1)
print(emojize('\033[35m:fogos_de_artifício: BOOM! OS FOGOS ESTOURARAM! :fogos_de_artifício:\033[m', language='pt'))
