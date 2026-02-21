"""
Calcule o valor a ser pago por um produto, considerando o preço e a condição de pagamento.
"""

p = float(input('Informe o preço do produto: R$ '))
m = int(input("""Selecione a forma de pagamento:
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista (cartão)
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Opção: """))

if m == 1:
    print(f'Desconto de 10% aplicado. Valor final: '
          f'\033[32mR${p * 0.9:.2f}\033[m.')

elif m == 2:
    print(f'Desconto de 5% aplicado. Valor final: '
          f'\033[32mR${p * 0.95:.2f}\033[m.')

elif m == 3:
    print(f'Pagamento em 2 parcelas de R${p / 2:.2f}. '
          f'Valor total: \033[33mR${p:.2f}\033[m.')

elif m == 4:
    parcelas = int(input('Informe o número de parcelas: '))
    print(f'Pagamento em {parcelas} parcelas de '
          f'R${p * 1.2 / parcelas:.2f} com acréscimo de juros. '
          f'Valor total: \033[31mR${p * 1.2:.2f}\033[m.')

else:
    print('\033[31mOpção inválida.\033[m')