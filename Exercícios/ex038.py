import os
from time import sleep

os.system('cls')
valor1 = float(input('Digite o ' '\033[36m' 'primeiro' '\033[0m' ' valor: '))
valor2 = float(input('Digite o ' '\033[31m' 'segundo' '\033[0m' ' valor: '))

# CARREGANDO...
sleep(1)
os.system('cls')

# Lógica
if valor1 > valor2:
    print('O ' '\033[36m' 'primeiro' '\033[0m' ' valor é maior')
elif valor1 < valor2:
    print('O ' '\033[31m' 'segundo' '\033[0m' ' valor é maior')
else:
    print('Os valores são ' '\033[33m' 'iguais' '\033[0m')