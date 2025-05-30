'''Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
    
n1 = cont = maior = menor = soma = 0
lista = []

while n1 != 1:
    n2 = 0
    num = int(input('\nDigite um número: '))
    lista.append(str(num))
    cont += 1
    soma += num
    
    if cont == 1:
        maior = num
        menor = num
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
        
    while n2 != 1:
        n3 = 0
        sn = str(input('\nQuer digitar outro número? [S/N] ')).upper()
        
        if sn == 'S':
            n2 = 1
            
        elif sn == 'N':       
            media = soma / cont          
            print(f'\n{'=-'*20} \nSobre os números digitados: \nQuantidade: {cont} \nNúmeros: {' - '.join(lista)}\nSoma: {soma} \nMédia: {media:.2f} \nMaior: {maior} \nMenor: {menor} \n{'=-'*20}')
            
            while n3 != 1:
                sn = str(input('\nQuer continuar digitando outros números? [S/N] ')).upper()
                
                if sn == 'S':
                    n3 = 1
                    n2 = 1
                elif sn == 'N':
                    print('\nMuito Obrigado!')
                    n1 = 1
                    n2 = 1
                    n3 = 1
                else:
                    print(f'\n{'#'*10} Opção Ínvalida {'#'*10}\n')
                
        else:
            print(f'\n{'#'*10} Opção Ínvalida {'#'*10}\n')