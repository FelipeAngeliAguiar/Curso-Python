'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares. '''
    
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
pares = ''

numeros = (n1, n2, n3, n4)

print(f'\nVocê digitou os número {', '.join(map(str, numeros))}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')

for cont in range (len(numeros)):
    if numeros[cont] % 2 == 0:
        pares += str(numeros[cont])
        
print(f'Os números pares foram {', '.join(pares)}')
        