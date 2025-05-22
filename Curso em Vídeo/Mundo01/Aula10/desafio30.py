'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Ímpar.'''
cores = {'limpa':'\033[m',
         'sublinhado':'\033[4m',
         'ciano':'\033[36m',
         'roxo':'\033[35m'}

n1 = int(input(f'{cores["sublinhado"]}Digite um número: {cores["limpa"]}'))

if n1%2 == 0:
    print(f'{cores["ciano"]}{n1} é Par{cores["limpa"]}')
else:
    print(f'{cores["roxo"]}{n1} é Ímpar{cores["limpa"]}')