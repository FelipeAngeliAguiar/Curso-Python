'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de um Sequência de Fibonacci.
    Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
    
n1 = int(input('Digite até onde você quer ver a sequência de Fibonacci: '))
a1 = 0
a2 = 1
fi = []

while n1 != 0:
    fi.append(str(a1))
    total = a1 + a2
    a2 = a1
    a1 = total
    n1 -= 1
    
print(f'\n{' -> '.join(fi)}\n')