#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número: '))

cont = 1
print(f"Tabuada de {n1}\n{'='*20}")

while cont<=10:
    print(f'{cont:2} x {n1} = {cont*n1}')
    cont += 1

print('='*20)