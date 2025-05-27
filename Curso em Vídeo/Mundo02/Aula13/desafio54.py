'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''

from datetime import date

hoje = date.today().year
maioridade = 0
menoridade = 0

for c in range(1,8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if ano > hoje or ano < 1900:
        print('Ano Ínvalido')
        
    else:
        if (hoje - ano) >= 21:
            maioridade += 1
        else:
            menoridade += 1
            
print(f'\nTem {maioridade} pessoas maior de idade \nTem {menoridade} pessoas menor de idade\n')