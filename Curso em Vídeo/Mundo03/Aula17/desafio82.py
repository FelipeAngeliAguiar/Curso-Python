'''Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.'''
    
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    
    while True:
        sn = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        if sn == 's' or sn == 'n':
            break
        else:
            print('Tente novamente!')
    
    if sn == 'n':
        break
    
print(f'{'=-'*20} \nLista completa é {lista}')

pares = []
impares = []
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista de pares é {pares} \nLista de ímpares é {impares}')
