"""Reescreva a função `leiaInt()` que fizemos no desafio 104,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""

from ex111.utilidadesCeV.dado import leia_int, leia_float
z = leia_int('Digite um número inteiro: ')
r = leia_float('Agora, digite um número real: ')
print(f'O número inteiro digitado foi {z} e o real, {r}.')
