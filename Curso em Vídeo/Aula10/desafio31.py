'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 
por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''


cores = {'limpa': '\033[m',
         'amarelosub': '\033[4;33m',
         'azul':'\033[34m',
         'ciano':'\033[36m'}

viagem = float(input(f'{cores["amarelosub"]}{'=-'*20}\nDigite quantos Km vai ser sua viagem:{cores["limpa"]}'))

if viagem <= 200:
    print(f'{cores["azul"]}Sua viagem de {viagem}Km \nVai custar R${viagem*0.50:.2f}{cores["limpa"]}')
else:
    print(f'{cores["ciano"]}Sua viagem de {viagem}Km \nVai custar R${viagem*0.45:.2f}{cores["limpa"]}')