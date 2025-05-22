'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''


cores = {'sublinhado': '\033[4m',
         'vermelho': '\033[31m',
         'verde': '\033[33m',
         'limpo': '\033[m'}

vel = float(input(f'{cores["sublinhado"]}Digite a velocidade do seu carro: {cores["limpo"]}'))

if vel > 80:
    print(f'{cores["vermelho"]}{'=-'*20} \nVocê foi multado por ter ultrapassado 80Km/h \nPreço da Multa: R${(vel - 80)*7:.2f} \n{'=-'*20}{cores["limpo"]}')
else:
    print(f'{cores["verde"]}{'=-'*20} \nTenha um bom dia! Dirija com segurança! \n{'=-'*20}{cores["limpo"]}')