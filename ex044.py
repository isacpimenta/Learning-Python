from os import system as sy
from time import sleep as sp

sy('cls')

print('======= LOJAS ABREU =======')
compras = float(input('Preço das compras: R$ '))
sp(2)

print()
print('___________________________')
print('|   FORMAS DE PAGAMENTO   |')
print('|   [1] Dinheiro / Pix    |')
print('|   [2] à vista cartão    |')
print('|   [3] 2x no cartão      |')
print('|   [4] 3x ou mais        |')
opcao = int(input('> '))
sp(1)
sy('cls')

if opcao == 1:
    desconto = compras * 0.10 
    novo_valor = compras - desconto

    print('Você terá ' '\033[34m' '10%' '\033[0m' ' de desconto')
    sp(1)
    print('Sua compra de ' '\033[31m' 'R$ {:.2f}' '\033[0m' ' vai custar ' '\033[32m' 'R$ {:.2f}' '\033[0m' '.'.format(compras, novo_valor))

elif opcao == 2:
    desconto = compras * 0.05 
    novo_valor = compras - desconto

    print('Você terá ' '\033[34m' '5%' '\033[0m' ' de desconto')
    sp(1)
    print('Sua compra de ' '\033[31m' 'R$ {:.2f}' '\033[0m' ' vai custar ' '\033[32m' 'R$ {:.2f}' '\033[0m' '.'.format(compras, novo_valor))

elif opcao == 3:
    print('Você pagará o valor ' '\033[34m' 'FORMAL' '\033[0m' ' do produto')
    sp(1)
    print('Sua compra vai custar ' '\033[32m' 'R$ {:.2f}' '\033[0m' '.'.format(compras))

elif opcao == 4:
    juros = compras * 0.20
    novo_valor = compras + juros
    qtd_parcelas = 0
    parcelas = 0

    qtd_parcelas = int(input('Em quantas parcelas deseja pagar? '))

    parcelas = novo_valor / qtd_parcelas

    print('Você terá ' '\033[34m' '20%' '\033[0m' ' de juros acima do valor formal do produto!')
    sp(4)
    sy('cls')

    print('Sua compra foi parcelada em {}x de R${:.2f} COM JUROS'.format(qtd_parcelas, parcelas))
    print('Sua compra de ' '\033[32m' 'R$ {:.2f}' '\033[0m' ' vai custar ' '\033[31m' 'R$ {:.2f}' '\033[0m' '.'.format(compras, novo_valor))

else:
    print('\033[31m' 'OPÇÃO INVÁLIDA DE PAGAMENTO.' '\033[0m')