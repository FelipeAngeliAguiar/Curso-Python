'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

cores = {'limpa':'\033[m',
         'amarelosub':'\033[4;33m',
         'vermelhobold':'\033[1;31m',
         'verdebold':'\033[1;32m'}

reta1 = float(input(f'{cores["amarelosub"]}Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
print(f'{cores["limpa"]}')

if (reta1 + reta2) <= reta3 or (reta1 + reta3) <= reta2 or (reta3 + reta2) <= reta1:
    print(f'{cores["vermelhobold"]}Não dá para formar um triângulo!{cores["limpa"]}')

else:
    print(f'{cores["verdebold"]}Dá para formar um triângulo!{cores["limpa"]}')