'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

a = 1

while a != 0:
    a1 = int(input('Digite o primeiro termo da PA: '))
    r = int(input('Digite a razão da PA: '))
    pa = []
    pa.append(str(a1))
    n1 = 10

    while n1 != 1:
        a1 += r
        pa.append(str(f'{a1}'))
        n1 -= 1

    print(' -> '.join(pa))
    b = 1
    while b != 0:
        sn = str(input(f'\nQuer ver outro PA? [S/N]: ')).upper()
        if sn == 'S':
            print("\nEntão digite novamente \n")
            b = 0     
        elif sn == 'N':
            print("\nAté a Próxima!")
            b=0
            a=0    
        else:
            print("\nOpção Invalida, Tente novamente!")