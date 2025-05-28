'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    No final, mostre quantos números foram digitados e qual foi a soma entre eles [desconsiderando o flag]'''
    
num = 1
a = 0
soma = 0
cont = []
while num != 999:
    num = int(input('Digite qualquer número: '))
    if num != 999:
        cont.append(str(num))
        a += 1
        soma += num

print(f'A soma dos {a} números é \n{' + '.join(cont)} = {soma}')