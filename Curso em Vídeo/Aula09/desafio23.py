'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Ex: Digite um número 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1'''

num = int(input('Digite um número entre 0 e 9999: '))

if num > 9999 or num < 0:
    print("Número maior que 9999 ou menor que 0")
else:
    num = str(num)
    num = f'{num:>4}'
    num = num.replace(' ', '0')
    print(f'''{'-'*20}
    Número: {num}
    Unidade: {num[3]}
    Dezena: {num[2]}
    Centena: {num[1]}
    Milhar: {num[0]}
    ''')