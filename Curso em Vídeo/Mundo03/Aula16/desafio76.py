'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

mercado = ('Lápis', 1.75, 
           'Borracha', 2.00, 
           'Caderno', 15.90, 
           'Estojo', 25.00, 
           'Transferidor', 4.20, 
           'Compasso', 9.99, 
           'Mochila', 120.32, 
           'Canetas', 22.30, 
            'Livro', 34.90)

print(f'{'='*50}\n{'LISTAGEM DE PREÇO':^50}\n{'='*50}')

for cont in range (len(mercado)):
    if cont % 2 == 0:
        print(f'{mercado[cont]:.<40}R${mercado[cont+1]:>8.2f}')
        
print('='*50)
    
    