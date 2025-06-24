'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
from time import sleep

boletim = []

while True:
    nome = str(input('Nome: '))
    
    while True:
        nota1 = float(input('Nota 1: '))
        
        if nota1 > 10 or nota1 < 0:
            print('Nota Ínvalida! ')
        else:
            break
        
    while True:
        nota2 = float(input('Nota 2: '))
        
        if nota2 > 10 or nota2 < 0:
            print('Nota Ínvalida! ')
        else:
            break
    
    boletim.append([nome, [nota1, nota2]])
    
    while True:
        sn = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if sn == 's' or sn == 'n':
            break
        else:
            print('Tente Novamente! ')
    
    if sn == 'n':
        break

print(f'\n{'=-'*36}')
print(f'{'No':<3}{'NOME':<20} Média')
print(f'-'*36)

for c , v in enumerate(boletim):
        print(f'{c:<3}{boletim[c][0]:<20} {(boletim[c][1][0]+boletim[c][1][1])/2:.1f}')

print(f'-'*36)

while True:
    num = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if num == 999:
        print('FINALIZANDO...')
        sleep(2)
        print('< VOLTE SEMPRE! >')
        break
    elif num < 0 or num >= len(boletim):
        print('Número Ínvalido!')
    else:
        print(f'Notas de {boletim[num][0]} são {boletim[num][1]}')
        print(f'-'*36)