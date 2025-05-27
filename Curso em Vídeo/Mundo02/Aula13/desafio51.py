'''Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = a1 + (10 - 1) * r
cont = []
for c in range(a1, decimo + r, r):
    cont.append(str(c))
    
print(' -> '.join(cont))