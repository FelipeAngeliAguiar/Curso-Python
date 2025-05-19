'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 
por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

viagem = float(input('Digite quantos Km vai ser sua viagem: '))

if viagem <= 200:
    print(f'Sua viagem de {viagem}Km \nVai custar R${viagem*0.50:.2f}')
else:
    print(f'Sua viagem de {viagem}Km \nVai custar R${viagem*0.45:.2f}')