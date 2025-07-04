'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No final, mostre o conteúdo da estrutura na tela.'''
    
boletim = {'nome': str(input('Nome: '))}

while True:
    boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
    
    if boletim['media'] > 10 or boletim['media'] < 0:
        print('Média Ínvalida')
        del boletim['media']
    else:
        break

if boletim['media'] >= 7:
    boletim['resultado'] = 'Aprovado'
elif boletim['media'] <= 5:
    boletim['resultado'] = 'Reprovado'
else:
    boletim['resultado'] = 'Recuperação'
    
print(f'\n{'=-'*16} \n{f"BOLETIM DE {boletim["nome"].upper()}":^32} \n{'=-'*16} \nMédia: {boletim["media"]:>24} \nResultado: {boletim["resultado"]:>20}\n')

