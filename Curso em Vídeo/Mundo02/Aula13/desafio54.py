'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''

from datetime import date

hoje = date.today().year
maioridade = 0
menoridade = 0
for c in range(1,8):
    ano = int(input('Digite o ano do seu nascimento: '))
    if ano > hoje or ano < 1900:
        print('Ano Ínvalido')
        
    else:
        if (hoje - ano) > 18:
            maioridade += 1
        else:
            menoridade += 1
            
print(f'Quantas pessoas tem mais de 18 anos: {maioridade} \nQuantas pessoas tem menos de 18 anos: {menoridade}')