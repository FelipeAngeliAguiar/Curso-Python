'''Crie um programa que tenha uma tupla com vários palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
    
dicionario = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

vogal = 'a', 'e', 'i', 'o', 'u'

for contD in range (len(dicionario)):
    vogais = ''
    palavra = (dicionario[contD])
    for contP in range (len(palavra)):
        for contV in range (len(vogal)):
            if palavra[contP] == vogal[contV]:
                vogais += vogal[contV]
    
    print(f'Na palavra {palavra.upper()} temos {' '.join(vogais)}')
        