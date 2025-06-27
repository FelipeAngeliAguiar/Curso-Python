'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
    e todos os dicionários em uma lista.
    No final mostre:
        A) Quantas pessoas foram cadastradas;
        B) A média de idade do grupo;
        C) Uma lista com todas as mulheres;
        D) Uma lista com todas as pessoas com idade acima da média.'''

grupo = list()
total = 0
while True:
    pessoa = {'nome': str(input('Nome: '))}
    
    while True:
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            pessoa['sexo'] = sexo
            break
        else:
            print('Valor Ínvalido! ')
    
    while True:
        idade = int(input('Idade: '))
        if idade < 150 and idade > 0:
            pessoa['idade'] = idade
            total += idade
            break
        else:
            print('Valor Ínvalido! ')
    
    grupo.append(pessoa)
    while True:
        sn = str(input('Quer continuar? [S/N] ')).strip().lower()
        if sn == 's' or sn == 'n':
            break
        else:
            print('Valor Ínvalido! ')
    if sn == 'n':
        break
    
print('=-'*30)
print(f'- O grupo tem {len(grupo)} {'pesssoas' if len(grupo) > 1 else 'pessoa'}.')
print(f'- A média de idade do grupo é de {total/len(grupo):.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')

for m in range(0, len(grupo)):
    if grupo[m]['sexo'] == 'F':
        print(grupo[m]['nome'], end=' ')
        
print()
print(f'- Lista das pessoas que estão acima da média: ')

for i in range(0, len(grupo)):
    if grupo[i]['idade'] > total/len(grupo):
        print(f'\nNome = {grupo[i]['nome']}; sexo = {grupo[i]['sexo']}; idade: {grupo[i]['idade']};')

print('<< ENCERRADO >>')
