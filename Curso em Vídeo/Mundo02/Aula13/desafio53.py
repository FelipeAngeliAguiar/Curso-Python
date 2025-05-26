'''Crie um programa que leia uma frase qualquer e diga se ela pe palíndromo, desconsiderando os espaços.
EX:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''

txt = str(input('Digite algo: ')).strip()
txt = txt.replace(' ', '')
txt = txt.lower()
newtxt = ''

for c in range(1, len(txt)+1):
    newtxt += txt[-c]
    
print(f'\nTexto digitado: {txt}', 
      f'\nTexto inverso: {newtxt}')
if txt == newtxt:
    print('\nÉ um Palíndromo\n')
else:
    print('\nNão é um Palíndromo\n')