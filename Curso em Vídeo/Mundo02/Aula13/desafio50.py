'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar
desconsidere-o.'''

soma = 0
for c in range(0,6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma += n1
        
print(f'\nA soma dos números pares foi : {soma}\n')