'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. 
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
    num = int(input('\nDigite um valor: '))
    
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado! Não vou inserir!')
        
    while True:
        sn = str(input('Quer continuar? [s/n] ')).strip().lower()
        if sn == 's' or sn == 'n':
            break
        else:
            print('Valor Ínvalido, tente novamente')
    
    if sn == 'n':
        break

print('=-'*20)
print(f'Você digitou os valores {sorted(lista)}')