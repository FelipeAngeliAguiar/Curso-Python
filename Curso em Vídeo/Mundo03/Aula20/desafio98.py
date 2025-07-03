'''Faça um programa que tenha uma função chamada contador(), 
    que recebe três parâmetro: início, fim e passo e realize a contagem.
    Seu programa tem que realizar três contagens através da função criada:
    a) De 1 até 10, de 1 em 1
    b) De 10 até 0, de 2 em 2
    c) Uma contagem personalizada'''
from time import sleep

def contador(inicio, fim, passo):
    print('=-'*20)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.2)
            
    if fim < inicio:
        for c in range(inicio, fim-1, (passo * -1)):
            print(c, end=' ', flush=True)
            sleep(0.2)
    
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('=-'*20)
print('Agora é sua vez de personalizar a contagem! ')
contador(int(input(f'{'Início: ':<10}')),
         int(input(f'{'Fim: ':<10}')),
         int(input(f'{'Passo: ':<10}')))
