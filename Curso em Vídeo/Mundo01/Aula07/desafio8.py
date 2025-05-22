#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite um valor em metros: '))

print(f'{n1/10000:<10}km \n{n1/1000:<10}hm \n{n1/100:<10}dam \n{n1:<10}m \n{n1*10:<10}dm \n{n1*100:<10}cm \n{n1*1000:<10}mm')