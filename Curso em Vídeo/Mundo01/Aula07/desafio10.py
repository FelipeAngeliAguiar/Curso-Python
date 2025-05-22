#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,65 ;-;

n1 = float(input("Digite quanto você tem na carteira: R$"))

print(f'Você tem R${n1:.2f} \nE pode comprar US${n1/5.65:.2f}')