'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
    O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
    cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

jogos = []
numjogos = []

print(f'{'='*50} \n{'JOGA NA MEGA SENA':^50} \n{'='*50}')

num = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range (1, num+1):
    while True:
        random = randint(1, 60)
        if numjogos.count(random) == 0:
            numjogos.append(random)
            
        if len(numjogos) == 6:
            break
    
    jogos.append(sorted(numjogos[:]))
    numjogos.clear()


txt = f' SORTEANDO {len(jogos)} {'JOGOS' if len(jogos) > 1 else 'JOGO'} '
print(f'\n{txt:=^50}')
for cont, v in enumerate(jogos):
    print(f'Jogo {cont+1}: {jogos[cont]}')
    sleep(1)

print(f'{' BOA SORTE! ':=^50}')