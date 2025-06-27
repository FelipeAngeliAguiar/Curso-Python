'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
    de detalhe do aproveitamento de cada jogador.'''
    
time = list()
gols = list()


while True:
    print('\n')
    jogador = {'nome': str(input('Nome do Jogador: '))}
    total = 0
    
    while True:
        partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        
        if partidas >= 0:
            jogador['partidas'] = partidas
            break
        else:
            print('Valor Ínvalido! ')
    
    for c in range(1, partidas+1):
        while True:
            gol = int(input(f'Quantos gols na partida {c}? '))
            
            if gol >= 0:
                gols.append(gol)
                total += gol
                break
            else:
                print('Valor Ínvalido! ')
                
    jogador['gols'] = gols[:]
    jogador['total'] = total
    gols.clear()
    time.append(jogador)
             
    while True:
        sn = str(input('Quer continuar? [S/N] ')).strip().lower()
        if sn == 'n' or sn == 's':
            break
        else:
            print('Valor Ínvalido! ')
    if sn == 'n':
        break
    
print('=-'*25)
print(f'{'cod':>3} {'nome':<20}{'gols':<15}{'total':<5}')
print('-'*45)
for c in range(0, len(time)):
    print(f'{c:>3} {time[c]["nome"]:<20}{f'{time[c]["gols"]}':<15}{time[c]["total"]:<5}')
print('-'*45)

while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    
    if dados == 999:
        print('<< VOLTE SEMPRE >>')
        break
    
    if 0 <= dados < len(time):
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["nome"].upper()}')
        for cont in range(0, len(time[dados]["gols"])):
            print(f'{f'No jogo {cont+1} ele fez {time[dados]["gols"][cont]} {"gol" if time[dados]["gols"][cont] == 1 else "gols"}.':>28}')
        print("-"*45)
    else:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente \n{"-"*45}')