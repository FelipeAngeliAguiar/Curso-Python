#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triânculo retângulo
#calcule e mostre o comprimento da hipotenusa

from math import hypot

catOp = float(input('Digite um comprimento para cateto oposto: '))
catAd = float(input('Digite um comprimento para cateto adjacente: '))

print(f'Medidas do Triângulo Retângulo: \nCateto Oposto: {catOp} \nCateto Adjacente: {catAd} \nHipotenusa: {hypot(catOp, catAd):.2f}')


