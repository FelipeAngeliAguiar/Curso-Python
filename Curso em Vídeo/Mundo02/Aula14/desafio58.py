'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
    
from random import randint

cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m'}

n = 1
p = 0
print(f"\n{cores['amarelo']}Tente adivinhar o número que o computador pensou, um número de 0 a 10, Boa sorte! {cores['limpa']}\n")
while n != 0:
    numBot = randint(0,10)
    numPlayer = int(input(f'\n{cores["amarelo"]}Número: {cores["limpa"]}'))
    
    if numPlayer > 10 or numPlayer < 0:
        print(f"{cores["vermelho"]}{'#'*10} Número Ínvalido, tente novamente {'#'*10}{cores["limpa"]}")
    elif numPlayer == numBot:
        p += 1
        print(f'{cores["verde"]}{'=-'*10} \nNúmero do bot: {numBot} \nNúmero do Player: {numPlayer} \nVOCÊ GANHOU PARABÉNS!!! \n{'=-'*10} \nTentativas: {p}{cores["limpa"]}')
        n = 0
    elif numPlayer != numBot:
        print(f'{cores["vermelho"]}{'=-'*10} \nNúmero do bot: {numBot} \nNúmero do Player: {numPlayer} \nVocê Perdeu... Tente novamente \n{'=-'*10}{cores["limpa"]}')
        p += 1
