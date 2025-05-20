'''Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

cores = {'limpa':'\033[m',
         'amarelosub':'\033[4;33m',
         'azulbold':'\033[1;34m',
         'cianobold':'\033[1;36m'}

salario = float(input(f'{cores["amarelosub"]}Digite seu salário: R$'))
print(f'{cores["limpa"]}')

if salario <= 1250:
    print(f'{cores["azulbold"]}PARABÉNS \nVocê ganhou um aumento de 15% \nSálario Antigo: R${salario:.2f} \nSálario Atual: R${salario * 1.15:.2f}{cores["limpa"]}')
else:
    print(f'{cores['cianobold']}PARABÉNS \nVocê ganhou um aumento de 10% \nSálario Antigo: R${salario:.2f} \nSálario Atual: R${salario * 1.10:.2f}{cores["limpa"]}')
