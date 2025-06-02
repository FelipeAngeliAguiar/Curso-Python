'''Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar.
    No final, mostre:
    A) Qual é o total gasto na compra:
    B) Quantos produtos custam mais de R$1000.
    C) Qual é o nome do produto mais barato.'''

produto = baratoNome = ''
total = caros = baratoPreco = contador = 0

print(f'{'='*30}\n{'LOJAS AGUIAR':^30}\n{'='*30}')

while True:
    produto = str(input('\nNome do Produto: '))
    preco = float(input('Preço: R$'))
    
    contador += 1
    total += preco
    
    if contador == 1 or preco < baratoPreco:
        baratoPreco = preco
        baratoNome = produto
        
    if preco >= 1000:
        caros += 1
    
    sn = ' '
    while sn not in 'SN': 
        sn = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    
    if sn == 'N':
        break
    
print(f'\n{'=-'*10} FIM DO PROGRAMA {'=-'*10}\n')
print(f'O total da compra foi R${total:.2f} \nTemos {caros} produtos custando mais de R$ 1000,00 \nO produto mais barato foi {baratoNome} que custa R${baratoPreco:.2f}\n')