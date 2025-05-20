'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.'''
from datetime import date

cores = {'limpa': '\033[m',
         'amarelosub': '\033[4;33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m'}

ano = int(input(f'{cores["amarelosub"]}Digite um ano, coloque 0 para o ano atual: {cores["limpa"]}'))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{cores["verde"]}{ano} é um ano Bissexto!{cores["limpa"]}')

else:
    print(f'{cores["vermelho"]}{ano} não é um ano Bissexto!{cores["limpa"]}')
    