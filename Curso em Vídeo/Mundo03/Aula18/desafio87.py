'''Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.'''

matriz = [[], [], []]
somapares = somacol3 = maiorvalor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(num)
        
        if num % 2 == 0:
            somapares += num
            
        if coluna == 2:
            somacol3 += num
            
print('=-'*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end=' ')
    print('\n')

print('=-'*20)
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somacol3}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

