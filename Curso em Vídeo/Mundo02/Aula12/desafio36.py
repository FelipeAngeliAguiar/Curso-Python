'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o *valor da casa*, 
o *salário* do comprador e em *quantos anos* ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

cores = {'limpa':'\033[m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

valor = float(input(f'Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quanto anos deseja pagar a casa? '))


prestacao = valor / (anos * 12)

if (salario * 0.30) > prestacao:
    print(f"{cores['verde']}Empréstimo Aprovado{cores['limpa']}")
elif (salario * 0.30) <= prestacao:
    print(f"{cores['vermelho']}Empréstimo Negado{cores['limpa']}")