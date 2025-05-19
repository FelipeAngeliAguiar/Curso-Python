'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi
o número escolhido pelo computador.
O Programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
n1 = randint(0,5)
n2 = int(input('Descubra qual o número que o computador escolheu entre 0 e 5 \n'))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print(f'{'-'*20} \nNúmero do Computador: {n1} \nSeu Número: {n2} \nVOCÊ GANHOU :D\n{'-'*20}')
else:
    print(f'{'-'*20} \nNúmero do Computador: {n1} \nSeu Número: {n2} \nVOCÊ PERDEU ;-; \n{'-'*20}')