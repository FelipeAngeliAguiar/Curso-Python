'''Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista. (se for em qual posição ele está)'''

lista = []
while True:
    lista.append(int(input('\nDigite um valor: ')))

    while True:
        sn = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        if sn == 's' or sn == 'n':
            break
        else:
            print('Valor Ínvalido, tente novamente! ')
    
    if sn == 'n':
        break

lista.sort(reverse=True)
print(f'{'=-'*30}\nVocê digitou {len(lista)} elementos. \nOs valores em ordem decrescente são {lista}''')

if 5 not in lista:
    print('O valor 5 não foi encontrado na lista! ')
else:
    print(f'O valor 5 faz parte da lista e está {'na posição' if lista.count(5) == 1 else 'nas posições'}', end=' ')
    for c, v in enumerate(lista):
        if v == 5:
            print(f'{c+1}',end=('... '))