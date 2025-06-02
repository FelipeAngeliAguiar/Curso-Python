'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será interrompido quando o número solicitado for negativo.'''
    
while True:
    print(f'\n{'=-'*20}\n')
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print(f'\n{'=-'*20}\n')
    
    if tabuada < 0:
        break
    
    for c in range(1, 11):
        print(f'{c} x {tabuada} = {c * tabuada}')
        
print('Programa encerrado!')