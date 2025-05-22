'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome'''

nome = str(input("Digite seu nome: ")).strip()

priNome = nome.split()

print(f'''{'-'*20} \nNome: {nome} \nLetras Maiúsculas: {nome.upper()} \nLetras Minúsculas: {nome.lower()}
Total de Letras: {len(nome.replace(' ', ''))} \nPrimeiro Nome Letras: {len(priNome[0])} \n{'-'*20}''')