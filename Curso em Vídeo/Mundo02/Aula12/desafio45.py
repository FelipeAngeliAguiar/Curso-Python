'''
Crie um programa que faça o computador jogar *Jokenpô* com você.
'''

from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'amarelosub': '\033[4;33m',
         'amarelobold': '\033[1;33m',
         'vermelhobold': '\033[1;31m',
         'whitebold': '\033[1m',
         'verdebold': '\033[1;32m'}

print(f'\n{cores["amarelosub"]}{ ' JOKENPO ':=^40}\n{cores["limpa"]}')

bot = randint(1,3)
jogadas = {1 : 'Pedra',
           2 : 'Papel',
           3 : 'Tesoura'}

print(f'{cores["whitebold"]}Escolha uma opção: \n1 - PEDRA \n2 - PAPEL\n3 - TESOURA')
player = int(input('Qual vai ser a sua jogada? '))
print(f'{cores["limpa"]}')

print(f'{cores["vermelhobold"]}JO{cores["limpa"]}')
sleep(1)
print(f'{cores['amarelobold']}KEN{cores["limpa"]}')
sleep(1)
print(f'{cores["verdebold"]}PO!!!{cores["limpa"]} \n')
sleep(1)
if player == 1 or player == 2 or player == 3:
    alt = {1 : f'{cores["verdebold"]}{'=-'*20} \n{f'{'Player:':<10} {f'{jogadas[player]}':>10}':^40} \n{f'{'Bot:':<10} {f'{jogadas[bot]}':>10}':^40}\n{'=-'*20} \n{f'JOGADOR VENCEU':^40}{cores["limpa"]}\n',
           2 : f'{cores["vermelhobold"]}{'=-'*20} \n{f'{'Player:':<10} {f'{jogadas[player]}':>10}':^40} \n{f'{'Bot:':<10} {f'{jogadas[bot]}':>10}':^40}\n{'=-'*20} \n{f'JOGADOR PERDEU':^40}{cores["limpa"]}\n'}

    if player == bot:
        print(f'{cores["amarelobold"]}{'=-'*20} \n{f'{'Player:':<10} {f'{jogadas[player]}':>10}':^40} \n{f'{'Bot:':<10} {f'{jogadas[bot]}':>10}':^40}\n{'=-'*20} \n{f'EMPATE':^40}{cores["limpa"]}\n')
    elif player == 1 and bot == 2:
        print(f'{alt[2]}')
    elif player == 1 and bot == 3:
        print(f'{alt[1]}')
    elif player == 2 and bot == 1:
        print(f'{alt[1]}')
    elif player == 2 and bot == 3:
        print(f'{alt[2]}')
    elif player == 3 and bot == 1:
        print(f'{alt[2]}')
    elif player == 3 and bot == 2:
        print(f'{alt[1]}')
else:
    print(f'{cores["vermelhobold"]}{' Número Ínvalido ':#^40}{cores["limpa"]}\n')
    