from os import system as sy

sy('cls')
sg1 = float(input('Primeiro segmento: '))
sg2 = float(input('Segundo segmento: '))
sg3 = float(input('Terceiro segmento: '))

def funcao():
    if sg1 == sg2 == sg3:
        print(' EQUILÁTERO')

    elif sg1 != sg2 != sg3 != sg1:
        print(' ESCALENO')

    else:
        print(' ISÓSCELES')

if sg1 < sg2 + sg3 and sg2 < sg1 + sg3 and sg3 < sg1 + sg2:
    sy('cls')
    print('Os segmentos informados podem formar um triângulo', end=(''))
    funcao()

else: 
    sy('cls')
    print('NÃO PODEM FORMAR')
    exit