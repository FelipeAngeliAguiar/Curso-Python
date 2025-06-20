'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
    
numeros = []

for cont in range(1, 6):
    numeros.append(int(input(f'Digite o {cont}° número: ')))

print(f'\nVocê digitou os valores: {numeros}')

print(f'\nO maior número é o: {max(numeros)}\nQue está nas posiçãos: ',end='')

for c, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{c+1}',end=('...'))
    
print(f'\nO menor número é o: {min(numeros)}\nQue está nas posiçãos: ',end='')

for c, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{c+1}',end=('...'))
