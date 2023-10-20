import os
import time

inteiro = 0
base_desejada = 0

os.system('cls')
inteiro = int(input('Digite um número inteiro: '))

time.sleep(1)
os.system('cls')

print('\nPara qual base decimal deseja converter?')
print('|--------------------|')
print('|  \033[36m[1] Hexadecimal\033[0m   |')  # Azul ciano
print('|  \033[32m[2] Octal\033[0m         |')  # Verde
print('|  \033[35m[3] Binário\033[0m       |')  # Magenta
print('|--------------------|\n')

base_desejada = int(input('> '))
time.sleep(1)
os.system('cls')

if base_desejada == 1:
    hex_value = hex(inteiro)[2:]  # Remove o prefixo "0x"
    print('Opção selecionada: \033[36mHexadecimal\033[0m')
    print('\033[36m', hex_value, '\033[0m')  # Hexadecimal em azul ciano
    
elif base_desejada == 2:
    oct_value = oct(inteiro)[2:]  # Remove o prefixo "0o"
    print('Opção selecionada: \033[32mOctal\033[0m')
    print('\033[32m', oct_value, '\033[0m')  # Octal em verde

elif base_desejada == 3:
    bin_value = bin(inteiro)[2:]  # Remove o prefixo "0b"
    print('Opção selecionada: \033[35mBinário\033[0m')
    print('\033[35m', bin_value, '\033[0m')  # Binário em magenta

else:
    print(
        '\033[31m''Opção Inválida.''\033[0m'
    )
    time.sleep(1)
    os.system('cls')
    print(
        'Tente novamente'
    )