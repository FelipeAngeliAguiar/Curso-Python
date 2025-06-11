'''Crie um programa que tenha uma tupla com vários palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
    
dicionario = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in dicionario:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')