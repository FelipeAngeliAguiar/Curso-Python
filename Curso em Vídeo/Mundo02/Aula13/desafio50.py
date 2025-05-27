'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar
desconsidere-o.'''

soma = 0
cont = []
for c in range(0,6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma += n1
        cont.append(str(n1))
        
if cont:
    print(f"\nA soma dos pares \n{' + '.join(cont)} = {soma}\n")
else:
    print("\nNenhum número par foi digitado\n")