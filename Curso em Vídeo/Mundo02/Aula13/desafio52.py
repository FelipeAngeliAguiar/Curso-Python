'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n1 = int(input('Digite um número: '))
if n1 > 1:
    for c in range (2, n1):
        if n1 % c == 0:
            print('Não é Número Primo')
            break
    else:
        print('É Número Primo')

else:
    print('Não é Número Primo')
    