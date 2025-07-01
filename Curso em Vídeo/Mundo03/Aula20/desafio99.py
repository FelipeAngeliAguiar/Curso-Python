'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
 
def maior(*lista):
    print('=-'*20)
    print('Analisando os valores passados...')
    
    if lista == 0:
        lista = 0
    for v in lista:
        print(v, end=' ', flush=True)
        sleep(0.2)
        
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista) if len(lista) != 0 else 0}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

    
