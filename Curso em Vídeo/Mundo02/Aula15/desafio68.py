'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
    
from random import randint
vitoria = 0

print(f'{'=-'*20}\nVAMOS JOGAR PAR OU ÍMPAR \n{'=-'*20}')

while True:
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    
    if parimpar == 'P' or parimpar == 'I':
        player = int(input('Digite um valor: '))
        bot = randint(0,10)
        
        if parimpar == 'I':
            if (player + bot) % 2 == 1:
                print(f'\n{'=-'*20}\nVocê jogou: {player} \nBot jogou: {bot} \nTotal de {player + bot} deu ÍMPAR')
                print(f'{'=-'*20}\nVOCÊ GANHOU!\n{'=-'*20}')
                print('Vamos jogar novamente!...\n')
                vitoria += 1
            else:
                print(f'\n{'=-'*20}\nVocê jogou: {player} \nBot jogou: {bot} \nTotal de {player + bot} deu PAR')
                print(f'{'=-'*20}\nVOCÊ PERDEU!\n{'=-'*20}\n')
                break
            
        elif parimpar == 'P':
            if (player + bot) % 2 == 0:
                print(f'\n{'=-'*20}\nVocê jogou: {player} \nBot jogou: {bot} \nTotal de {player + bot} deu PAR')
                print(f'{'=-'*20}\nVOCÊ GANHOU!\n{'=-'*20}')
                print('Vamos jogar novamente!...\n')
                vitoria += 1
            else:
                print(f'\n{'=-'*20}\nVocê jogou: {player} \nBot jogou: {bot} \nTotal de {player + bot} deu ÍMPAR')
                print(f'{'=-'*20}\nVOCÊ PERDEU!\n{'=-'*20}\n')
                break
              
    else:         
        print(f'\n{'#'*20}\nOPÇÃO ÍNVALIDA!\n{'#'*20}\n')
            
print(f'GAME OVER! Você ganhou {vitoria} vezes!')