'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999.
    que é a condição de parada. No final, mostre quantos números foram digitados e qual foi  a soma entre eles 
    (desconsiderando o flag)'''

soma = contador = 0
numeros = []

while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    
    if n1 == 999:
        break
    
    numeros.append(str(n1))
    soma += n1
    contador += 1

print(f'\nA soma dos {contador} valores é igual a: \n{' + '.join(numeros)} = {soma}! \n')