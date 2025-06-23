'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves. '''
    
grupo = list()
pessoa = list()
maior = menor = 0

while True:
    pessoa.append(str(input('\nNome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    
    while True:
        sn = str(input('Quer continuar? [s/n] ')).strip().lower()
        if sn == 's' or sn == 'n':
            break
        else:
            print('Tente novamente! ')
            
    if sn == 'n':
        break

print('=-'*20)
print(f'\n{len(grupo)} {'pessoas foram cadastradas. ' if len(grupo) > 1 else 'pessoa foi cadastrada.'}')

for c, v in enumerate(grupo):
    if c == 0:
        maior = v[1]
        menor = v[1]
    elif v[1] > maior:
        maior = v[1]
    elif v[1] < menor:
        menor = v[1]

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')

for c, v in enumerate(grupo):
    if maior == v[1]:
        print(f'{v[0]} ', end='')
        
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')

for c, v in enumerate(grupo):
    if menor == v[1]:
        print(f'{v[0]} ', end='')