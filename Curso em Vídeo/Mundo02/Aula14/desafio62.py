'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

a = 10
p1 = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
print(f'{'=-'*20}')
cont = []
contador = 0

while a != 0:
    cont.append(str(p1))
    p1 += r
    a -= 1
    contador += 1
    
    if a == 0:
        print(f'\n{' -> '.join(cont)}\n')
        a = int(input('Quantos termos você quer mostrar a mais? '))
        
        if a == 0:
            print(f'\nProgressão Finalizada! com {contador} termos mostrados. \n')