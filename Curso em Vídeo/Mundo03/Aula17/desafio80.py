'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
    já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.'''
    
lista = []
for c in range(0,5):
    num = int(input('Digite um número: '))
        
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista...')
        
    else:
        for cont, v in enumerate(lista):
            if num < v:
                lista.insert(cont, num)
                print(f'Número {num} adicionado na posição {cont}')
                break           

print(f'{"=-"*20}\nLista ordenada: \n{lista}')