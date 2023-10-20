from time import sleep as sl
from os import system as sy
from datetime import date as dt

ano_atual = dt.today().year


ano_nasc = int(input('Ano de Nascimento: '))

idade = ano_atual - ano_nasc

if idade <= 9:
    print('\033[31m' 'MIRIM' '\033[0m')

elif idade > 9 and idade <= 14:
    print('\033[36m' 'INFANTIL' '\033[0m')

elif idade > 14 and idade <= 19:
    print('\033[35m''JUNIOR' '\033[0m')

elif idade > 19 and idade <= 25:
    print('\033[34m' 'SÊNIOR' '\033[0m')
    
else:
    print('\033[33m' 'MASTER' '\033[0m')