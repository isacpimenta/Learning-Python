from time import sleep as sl
from os import system as sy

sy('cls')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
sy('cls')

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média é {}.')
    sl(1) 
    print('Você está ' '\033[31m' 'REPROVADO' '\033[0m' '.')

elif media >= 5 and media <= 6.9:
    print('Sua média é {}.'.format(media))
    sl(1) 
    print('Você está na ' '\033[33m' 'RECUPERAÇÃO' '\033[0m' '.')

elif media >= 7:
    print('Sua média é {}.'.format(media))
    sl(1) 
    print('Você está ' '\033[32m' 'APROVADO' '\033[0m' '.')