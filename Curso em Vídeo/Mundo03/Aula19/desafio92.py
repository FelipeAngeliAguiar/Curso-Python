'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionário
    se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

cadastro = {'nome': str(input('Nome: ')),
            'idade': (datetime.now().year - int(input('Ano de Nascimento: ')))}

ctps = int(input('Carteira de Trabalho (0 não tem): '))

if ctps == 0:
    cadastro['ctps'] = 0
else:
    cadastro['contratacao'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratacao'] + 35) - datetime.now().year + cadastro['idade']

print('-='*20)
for k, v in cadastro.items():
    print(f'{k} tem valor {v}')
    