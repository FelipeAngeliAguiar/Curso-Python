'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
print(f'{'-'*20} \nNome Completo: {' '.join(nome)} \nPrimeiro Nome: {nome[0]} \nÚltimo Nome: {nome[-1]}')