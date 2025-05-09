#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu sálario: R$'))

print(f'Parabéns você ganho um aumento de 15% \nSálario Antigo: R${salario} \nSálario Atual: R${salario * (1.15):.2f}')