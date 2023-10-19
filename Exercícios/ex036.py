import os

os.system('cls')
valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite seu salário: R$ "))
anos_pagamento = int(input("Em quantos anos pretende pagar o empréstimo: "))

# Pretação mensal 
prestacao_mensal = valor_casa / (anos_pagamento * 12)

# Limite da prestação 
limite_prestacao = salario_comprador * 0.3
os.system('cls')


print ('Para pagar uma casa de {:.2f} em {} anos a prestação mensal será de: {:.2f}.' .format(valor_casa, anos_pagamento, prestacao_mensal))

if prestacao_mensal <= limite_prestacao:
    print('Empréstimo Aprovado!')
else:
    print('Empréstimo Negado! A prestação mensal excede 30% do salário')