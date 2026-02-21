"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione também as docstrings da função
"""

def notas(*nota, sit=False):
    """
    Função que avalia notas e a situação dos alunos.

    :param nota: uma ou mais notas dos alunos (permite receber múltiplos valores)
    :param sit: parâmetro opcional que define se a situação deve ser incluída na análise
    :return: retorna um dicionário contendo diversas informações sobre o desempenho da turma
    """
    dicionario = {}
    s = c = maior = menor = 0
    for aluno in nota: # aluno representa cada nota entre os parâmetros de "*nota"
        s+=aluno
        if c == 0:
            maior = menor = aluno
        else:
            if aluno > maior:
                maior = aluno
            if aluno < menor:
                menor = aluno
        c += 1
    dicionario['total'] = c
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['média'] = s/c
    if sit: # == True
        if dicionario['média'] < 7:
            dicionario['situação'] = 'RUIM'
        elif 5 <= dicionario['média'] < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOA'
    return dicionario


# Programa Principal
print('-'*35)
print(notas(1, 5, 2, 4, 0))
print('-'*35)
print(notas(5.5, 9.5, 10, 6.5, sit=True))
print('-'*35)
lista = []
while True:
    r = 'q'
    _aluno = float(input('Digite uma nota: '))
    lista.append(_aluno)
    while r not in 'sn':
        r = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
    if r == 'n':
        break
while True:
    situation = str(input('Quer ver a sua situação também [s/n]? ')).strip().lower()[0]
    if situation in 'sn':
        break
if situation == 's':
    situation = True
else:
    situation = False
final = notas(*lista, sit=situation) # o asterisco desempacota a lista
print('-'*35)
print(final)
print('-'*35)
help(notas)

# Rsolução do prof
# def notas(*n, sit=False):
#     """
#         -> Função para analisar notas e situações
#         :param n: uma ou mais notas dos alunos (aceita várias)
#         :param sit: valor opcional, indicando se deve ou não adicionar a situação
#         :return: dicionário com várias informações sobre a situação da turma
#         """
#     r = dict()
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['menor'] = min(n)
#     r['média'] = sum(n)/len(n)
#     if sit:
#         if r['média'] >= 7:
#             r['situação'] = 'BOA'
#         elif r['média'] >= 5:
#             r['situação'] = 'RAZOÁVEL'
#         else:
#             r['situação'] = 'RUIM'
#     return r
