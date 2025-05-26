'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.'''

soma = 0
maisvelho = 0
menos20 = 0

for c in range(1,5):
    print(f'\n{'=-'*20}')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    print('[ 0 ] Feminino \n[ 1 ] Masculino \n')
    sexo = int(input( 'Qual seu sexo? ' ))
    
    if sexo == 1 and maisvelho < idade:
        n1 = nome
        maisvelho = idade
        
    if sexo == 0 and idade < 20:
        menos20 += 1
        
    soma += idade

print(f'\n{'=-'*20} \nFicha Final \nMédia de idade do grupo: {soma/4:.2f} \nO homem mais velho é o {n1} com {maisvelho} anos. \nE tem {menos20} mulheres com menos de 20 anos.\n{'=-'*20}')