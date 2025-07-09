'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
    o nome de um jogador e quantos gols ele marcou.
   O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''
   

def ficha(nome='', gols=0):
    """
    -> Função que retorna a ficha de um jogador.
    :param nome: Nome do jogador (opcional).
    :param gols: Quantidade de gols marcados (opcional).
    :return: String com a ficha do jogador.
    """
    
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
        
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato')



jogador = str((input('Nome do Jogador: '))).strip()
num = input('Números de Gols: ')

if num.isnumeric():
    num.int(num)
else:
    num = 0

ficha(jogador, num)