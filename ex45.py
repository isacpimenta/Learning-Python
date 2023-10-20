from os import system as sy
from time import sleep as sp
import random

def cabecalho():
    
    sy('cls')
    print('\033[33m','=========','\033[0m','PEDRA, PAPEL E TESTOURA','\033[33m','=========' '\033[0m')
    print('\033[33m', 7*'=','\033[0m' 'Pressione ' '\033[34m' 'ENTER' '\033[0m' ' para iniciar', '\033[33m', 7*'=' ,'\033[0m')
    input('> ')

    sp(2)
    sy('cls')

def jogo_maquina():
    global jogada
    jogada = random.randrange( 1, 4)

def logica():
    sp(3)
    sy('cls')
    
    if jogada == opcao:
        print('EMPATE')
    elif jogada == 1 and opcao == 3:
        print('PC GANHOU')
        print('PC: PEDRA | PLAYER: TESOURA')
    elif jogada == 2 and opcao == 1:
        print('PC GANHOU')
        print('PC: PAPEL | PLAYER: PEDRA')
    elif jogada == 3 and opcao == 2:
        print('PC GANHOU')
        print('PC: TESOURA | PLAYER: PAPEL')
    else:
        print('O PLAYER VENCEU')

def jogo_player():
    global opcao

    print('SUAS OPÇÕES:')
    print('[1] PEDRA')
    print('[2] PAPEL')
    print('[3] TESOURA')
    print()
    opcao = int(input('> '))

jogo_maquina()
cabecalho()
jogo_player()
logica()