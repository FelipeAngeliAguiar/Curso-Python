'''Crie um programa que gerencie o aproveitamento der um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou. 
    Depois vai ler a quantidade de gols feitos em cada partida.
    No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {'nome': str(input('Nome do Jogador: '))}

while True:
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    if partidas < 0:
        print('Valor Ínvalido! ')
    else:
        break

gols = list()

for c in range(1, partidas+1):
    while True:
        gol = int(input(f'  Quantos gols na partida {c}? '))
        
        if gol < 0:
            print('Valor Ínvalido! ')
        else:
            break
    gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print(f'\n{'=-'*15}\n')
print(jogador)
print(f'\n{'=-'*15}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
    
print(f'{'=-'*20}')
print(f'O jogador {jogador["nome"]} jogou {partidas} {'partidas' if partidas > 1 else 'partida'}.')
print(f'{'=-'*20}')
for cont in range(0, partidas):
    print(f'{f' => Na partida {cont+1}, fez {jogador["gols"][cont]}':>30}')

print(f'Fez um total de {jogador["total"]} gols')