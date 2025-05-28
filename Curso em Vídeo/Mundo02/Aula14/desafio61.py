'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = []
pa.append(str(a1))
n1 = 10

while n1 != 1:
    a1 += r
    pa.append(str(f'{a1}'))
    n1 -= 1

print(' -> '.join(pa))