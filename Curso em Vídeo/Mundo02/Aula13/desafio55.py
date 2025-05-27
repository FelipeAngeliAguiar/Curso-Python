'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

for c in range(1,6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    
    if c == 1:
        maiorp = peso
        menorp = peso
        p1 = c
        p2 = c
         
    if peso > maiorp:
        maiorp = peso
        p1 = c
    if peso < menorp:
        menorp = peso
        p2 = c
        
print(f'\nO Maior peso foi da {p1}° com {maiorp}Kg \nO Menor peso foi da {p2}° com {menorp}Kg')
    
    
    