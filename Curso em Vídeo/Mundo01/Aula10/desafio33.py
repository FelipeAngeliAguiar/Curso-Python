'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

cores = {'limpa':'\033[m',
         'amarelosub':'\033[4;33m',
         'verdeinv':'\033[7;1;32m',
         'vermelhoinv':'\033[7;1;31m',
         'invertido':'\033[7;1m'}

n1 = float(input(f"{cores['amarelosub']}{'=-'*20} \nDigite o primeiro número: "))
n2 = float(input(f"{'=-'*20} \nDigite o segundo número: "))
n3 = float(input(f"{'=-'*20} \nDigite o terceiro número: "))
print(f'{'=-'*20}{cores["limpa"]}')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
print(f'{cores["invertido"]}  Entre {n1}, {n2}, {n3}  ',
      f'\n{cores["verdeinv"]}     O Maior é {maior}     ',
      f'\n{cores["vermelhoinv"]}     O Menor é: {menor}     {cores["limpa"]}')