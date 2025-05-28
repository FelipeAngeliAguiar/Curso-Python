'''Crie um programa que leia dois valores e mostre um menu na tela: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
   Seu programa deverá realizar a operação solicitada em cada caso.'''
   
c1 = 1
while c1 != 0:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro númer: '))
    c2 = 1
    while c2 != 0:
        print('\nAgora escolha uma das opções abaixo: \n[1] Somar \n[2] Multiplicar \n[3] Qual o maior \n[4] Novos números \n[5] Sair do Programa\n')
        opt = int(input('Qual você quer? '))
        
        if opt > 5 or opt < 0:
            print(f'\n{'#'*10} Opção Ínvalida, Tente Novamente {'#'*10}')
        elif opt == 1:
            print(f'\nO resultado de \n{n1} + {n2} = {n1+n2}')
        elif opt == 2:
            print(f'\nO resultado de \n{n1} x {n2} = {n1*n2}')
        elif opt == 3:
            if n1 > n2:
                print(f'\nO número {n1} é maior que o {n2}')
            if n2 > n1:
                print(f'\nO número {n2} é maior que o {n1}')
            else: 
                print(f'\nOs número são iguais')
        elif opt == 4:
            print('\nEscolha novos números: ')
            c2 = 0
        elif opt == 5:
            c2 = 0
            c1 = 0
            
print("Fim do Programa")