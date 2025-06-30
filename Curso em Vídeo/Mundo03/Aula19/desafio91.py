'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
    Guarde esses resultados em um dicionário.
    No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
    
from random import randint
from time import sleep
from operator import itemgetter

cont = 1

jogos = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}

print("Valores Sorteados: ")
for k, v in jogos.items():
    print(f"{f'O {k} tirou {v} no dado.':>30}")
    sleep(0.8)
    
print()
print("Ranking dos jogadores: ")
for k, v in sorted(jogos.items(), key=itemgetter(1), reverse=True):
    print(f"{f'{cont}° lugar: {k} com {v}':>26}")
    cont += 1
    sleep(0.8)