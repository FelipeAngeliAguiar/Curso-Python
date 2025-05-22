'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''

nome = str(input('Digite seu nome: ')).strip()
nome = nome.title()

if ('Silva' in nome) == True:
    print(f'{nome} tem Silva no nome')
    
else:
    print(f'{nome} não tem Silva no nome')