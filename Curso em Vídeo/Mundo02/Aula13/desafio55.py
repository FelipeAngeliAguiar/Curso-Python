'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maiorp = 0
menorp = 0

for c in range(1,6):
    peso = float(input('Digite seu peso: '))
    
    if c == 1:
        maiorp = peso
        menorp = peso
        
    if peso > maiorp:
        maiorp = peso
    elif peso < menorp:
        menorp = peso
        
print(f'\nO Maior peso foi: {maiorp}\nO Menor peso foi: {menorp}')
    
    
    