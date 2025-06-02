'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nõa continuar.
    No final, mostre: 
    A) Quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.'''
    
idade = maiordeidade = homens = mulheres = 0
sexo = ''

while True:
    print (f'{'='*50}\n{'CADASTRE UMA PESSOA':^50}\n{'='*50}')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':    
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        
    print (f'{'='*50}')
    if idade >= 18:
        maiordeidade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
           
    sn = ' '
    while sn not in 'SN': 
        sn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if sn == 'N':
        break
            
print(f'\n{'=-'*10} FIM DO PROGRAMA {'=-'*10}')
print(f'\nTotal de pessoas com mais de 18 anos: {maiordeidade} \nAo todo temos {homens} homens cadastrados \nE temos {mulheres} mulheres com menos de 20 anos.\n')
    
