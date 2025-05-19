'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Ímpar.'''

n1 = int(input('Digite um número: '))

if n1%2 == 0:
    print(f'{n1} é Par')
else:
    print(f'{n1} é Ímpar')