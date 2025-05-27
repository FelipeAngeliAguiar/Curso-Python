'''Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artifício, ido de 10 até 0,
com uma pausa de 1 segundo entre eles.'''

from time import sleep

cores = {'vermelho': '\033[1;31m','amarelo': '\033[1;33m','verde':'\033[1;32m','limpa': '\033[m'}

print('O FOGOS DE ARTIFÍCIO VÃO COMEÇAR EM:')

for c in range(10, 0, -1):
    if c > 6:
        print(f'{cores["verde"]}{c}{cores["limpa"]}')
    elif c >3:
        print(f'{cores["amarelo"]}{c}{cores["limpa"]}')
    else:
        print(f'{cores["vermelho"]}{c}{cores['limpa']}')
    sleep(1)

print(f'{cores["verde"]}FELIZ ANO NOVO!!!{cores["limpa"]}')