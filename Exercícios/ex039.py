from time import sleep
from os import system as os
from datetime import date as dt

os('cls')
ano_atual = dt.today().year

ano_nascimento = int(input('Informe seu ano de nascimento: '))
sleep(1)
os('cls')

# Lógica
idade = ano_atual - ano_nascimento
resposta = 18 - idade

if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento,idade, ano_atual))
    sleep(3)
    os('cls')
    print('Você tem que se alistar ' '\033[31m' 'IMEDIATAMENTE' '\033[0m' '.')

elif idade < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_atual))
    sleep(3)
    os('cls')
    print('Ainda faltam ' '\033[31m' '{}' '\033[0m' ' anos para seu alistamento.'.format(resposta))
    sleep(3)
    print('Seu alistamento será em ' '\033[31m' '{}' '\033[0m' '.'.format(ano_atual + resposta))

elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, ano_atual))
    sleep(3)
    os('cls')
    print('Você já deveria ter se alistado há ' '\033[31m' '{}' '\033[0m' ' anos.'.format(abs(resposta)))
    sleep(3)
    print('Seu alistamento foi em ' '\033[31m' '{}' '\033[0m' '.'.format(ano_atual - abs(resposta)))