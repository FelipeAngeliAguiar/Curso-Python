#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o 
#nome dos quatro alunos e mostre a ordem sorteada

from random import sample

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

num = sample([n1,n2,n3,n4], k=4)

print(f'{'-'*20} \nOrdem da Apresentação: \nPrimeiro: {num[0]} \nSegundo: {num[1]} \nTerceiro: {num[2]} \nQuarto: {num[3]}')