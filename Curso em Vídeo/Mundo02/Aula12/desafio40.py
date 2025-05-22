'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media <= 5.0:
    resultado = 'REPROVADO'
elif media >= 7.0:
    resultado = 'APROVADO'
else: 
    resultado = 'RECUPERAÇÃO'
    
print(f'{'=-'*20} \nStatus do aluno:\nPrimeira Nota: {nota1:.2f} \nSegunda Nota: {nota2:.2f} \nMédia: {media:.2f}',
      f'\nResultado Final: {resultado} \n{'=-'*20}')