'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"'''

cidade = str(input('Digite um nome de uma cidade: ')).strip()
cidade = cidade.title()

if (cidade[:5] == 'Santo') == True:
    print(f'{cidade} começa com Santo no nome')
    
else:
    print(f'{cidade} não começa com Santo no nome')