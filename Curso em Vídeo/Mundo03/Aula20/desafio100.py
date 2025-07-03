'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
    entre todos os valores PARES sorteados pela função anterior.'''
from time import sleep
from random import randint

numeros = list()

def sorteio(vezes, lista):
    print(f'Sorteando {vezes} valores da lista: ', end='')
    
    for c in range(0, vezes):
        sorteado = randint(1, 10)
        lista.append(sorteado)
        print(f'{sorteado}', end=' ', flush=True)
        sleep(0.3)
    
    print('PRONTO!')
        
    
def somaPar(lista):
    soma = 0
    
    print(f'Somando os valores pares de {lista}, temos... ', end='', flush=True)
    sleep(0.5)
    for v in lista:
        if v % 2 == 0:
            soma += v
    
    print(soma)
        
print()
sorteio(5, numeros)
somaPar(numeros)
print()