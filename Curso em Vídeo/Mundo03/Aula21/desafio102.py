'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
    o primeiro que indique o número a calcular e o outro chamado show. que será um valor lógico (opcional)
    indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial (num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número inteiro do qual se deseja o fatorial (padrão é 1).
    :param show: Valor booleano que indica se deve mostrar ou não o processo (padrão é False).
    :return: O valor do fatorial de num.
    """
    
    if num < 0:
        print('Fatorial não aceita número negativo.')
        return None
    
    f = 1
    
    for c in range(num, 0 , -1):
        if show == True:
            print (c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
            
    return f
    
numero = int(input('Deseja ver fatorial de qual número? '))

while True:
    mostrar = str(input('Quer ver o processo? [S/N] ')).strip().lower()
    if mostrar == 's':
        show=True
        break
    elif mostrar == 'n':
        show=False
        break
    else:
        print('Valor Ínvalido! ')

print('-' * 50)
print(fatorial(numero, show))
print('-' * 50)
        
