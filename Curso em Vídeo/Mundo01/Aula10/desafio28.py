'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi
o número escolhido pelo computador.
O Programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'sublinhado': '\033[4m',
         'amarelo': '\033[33m',
         'vermelho': '\33[31m',
         'verde': '\033[32m',}

n1 = randint(0,5)
n2 = int(input(f'{cores["sublinhado"]}Descubra qual o número que o computador escolheu entre 0 e 5: {cores["limpa"]}'))
print(f'{cores['amarelo']}PROCESSANDO...{cores["limpa"]}')
sleep(2)
if n1 == n2:
    print(f'{cores["verde"]}{'=-'*20} \nNúmero do Computador: {n1} \nSeu Número: {n2} \nVOCÊ GANHOU :D\n{'=-'*20}{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}{'=-'*20} \nNúmero do Computador: {n1} \nSeu Número: {n2} \nVOCÊ PERDEU ;-; \n{'=-'*20}{cores["limpa"]}')