'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
cores = {'limpa':'\033[m', 'amarelo':'\033[1;33m', 'vermelho':'\033[1;31m'}

n1 = int(input('Digite um número: '))
tot = 0
for c in range (1, n1 + 1):
    if n1 % c == 0:
        print(f'{cores["vermelho"]}', end='')
        tot +=1
    else:
        print(f'{cores["amarelo"]}', end='')
    print(f'{c}{cores["limpa"]}', end=' ')
    
print(f'\n\nO número {n1} foi dividível {tot} vezes')

if tot == 2:
    print(f'\nEntão {n1} é um número PRIMO\n')
else:
    print(f'\nEntão {n1} NÃO é um número primo\n')