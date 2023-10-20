from os import system as sy
from time import sleep as sp

sy('cls')
peso = float(input('Informe seu peso (KG): '))
altura = float(input('Informe sua altura (M): '))
imc = 0

imc = peso / (altura ** 2)

sy('cls')
if imc < 18.5:
    print('O IMC dessa pessoa é:' '\033[33m' ' {:.2f}' '\033[0m'.format(imc))
    print('Ela está ' '\033[34m' 'ABAIXO DO PESO' '\033[0m')    # 35 é ROSA     34 é LILÁS  32 é VERDE 33 é AMARELO

elif imc >= 18.5 and imc < 25:
    print('O IMC dessa pessoa é:' '\033[33m' ' {:.2f}' '\033[0m'.format(imc))
    print('Ela está no ' '\033[32m' 'PESO IDEAL' '\033[0m')    # 35 é ROSA     34 é LILÁS  32 é VERDE  33 é AMARELO
    
elif imc >= 25 and imc < 30:
    print('O IMC dessa pessoa é:' '\033[33m' ' {:.2f}' '\033[0m'.format(imc))
    print('Ela está em ' '\033[33m' 'SOBREPESO' '\033[0m')    # 35 é ROSA     34 é LILÁS  32 é VERDE   33 é AMARELO

elif imc >= 30 and imc <= 40:
    print('O IMC dessa pessoa é:' '\033[33m' ' {:.2f}' '\033[0m'.format(imc))
    print('Ela está na ' '\033[31m' 'OBESIDADE' '\033[0m')    # 35 é ROSA     34 é LILÁS  32 é VERDE   33 é AMARELO

elif imc > 40:
    print('O IMC dessa pessoa é:' '\033[33m' ' {:.2f}' '\033[0m'.format(imc))
    print('Ela está em ' '\033[36m' 'OBESIDADE MÓRBIDA' '\033[0m')    # 35 é ROSA     34 é LILÁS  32 é VERDE   33 é AMARELO
