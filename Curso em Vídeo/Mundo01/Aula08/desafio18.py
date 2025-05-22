#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import tan, sin, cos, radians

ang = float(input("Digite qualquer ângulo: "))

print(f"Valor do Seno: {sin(radians(ang)):.2f} \nValor do Cosseno: {cos(radians(ang)):.2f} \nValor da Tangente: {tan(radians(ang)):.2f}")
