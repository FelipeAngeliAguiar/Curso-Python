'''Crie um programa que tenha uma tupla totalmente preenchido com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
    
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    
    if n1 > 20 or n1 < 0:
         print('Tente Novamente')
    else:
        print(f'Você digitou o número {numeros[n1]}.')
        break