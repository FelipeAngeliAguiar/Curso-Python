'''Faça um programa que tenha uma função chamada area()
    que receba as dimensões de um terreno retangular (largura e comprimento)
    e mostre a área do terreno.'''
    
def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg} x {comp} é de {a}m²')

print(f'\n{'Controle de Terrenos':^25} \n{'-'*25}')
largura = float(input(f'{'LARGURA (m): ':<20}'))
comprimento = float(input(f'{'COMPRIMENTO (m): ':<20}'))
area(largura, comprimento)