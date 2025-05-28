'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
    Ex: 5! = 5x4x3x2x1 = 120'''
    

fator = int(input('Digite um valor: '))

n1 = fator
cont = []
while n1 != 0:
    cont.append(str(n1))
    n1 = n1 - 1
    if n1 != 0:
        fator = fator * n1
    
print(f'{cont[0]}! = {' x '.join(cont)} = {fator}')
