'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
    Caso esteja errado, peça a  digitação nomcamente até ter um valor correto.'''
    
n = 1
while n != 0:
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        print(f'Sexo Masculino registrado com sucesso')
        n = 0
    elif sexo == 'F':
        print(f'Sexo Feminino registrado com sucesso')
        n = 0
    else:
        print('Resposta ìnvalida! Tente novamente')
