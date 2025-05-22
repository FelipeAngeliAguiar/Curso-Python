'''
Escreva um programa que leia *dois números* inteiros e compare-os, mostrando na tela uma mensagem:
- O *primeiro valor* é Maior
- O *segundo valor* é Maior
- *Não existe* valor maior, os dois são Iguais
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que o {n1}')
else:
    print(f'{n1} é igual a {n2}')