'''Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.'''

a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))

for c in range(1,11):
    print (f'{a1 + (c-1) * r}')