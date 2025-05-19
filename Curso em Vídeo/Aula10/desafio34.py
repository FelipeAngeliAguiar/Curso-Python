'''Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite seu salário: R$'))

if salario <= 1250:
    print(f'PARABÉNS \nVocê ganhou um aumento de 15% \nSálario Antigo: R${salario:.2f} \nSálario Atual: R${salario * 1.15:.2f}')
else:
    print(f'PARABÉNS \nVocê ganhou um aumento de 10% \nSálario Antigo: R${salario:.2f} \nSálario Atual: R${salario * 1.10:.2f}')
