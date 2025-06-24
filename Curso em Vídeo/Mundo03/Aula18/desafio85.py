'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
    os valores pares e ímpares. No final, mostre os valores pares e ímapres em ordem crescente.'''
    
numero = [[], []]


for c in range (1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    
    if num % 2 == 0:
        numero[0].append(num)
    elif num % 2 == 1:
        numero[1].append(num)

print('=-'*20)
print(f'Os valores pares digitado foram: {sorted(numero[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numero[1])}')