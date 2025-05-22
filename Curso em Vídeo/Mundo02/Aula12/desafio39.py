'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele *ainda vai se alistar* ao serviço militar.
- Se é a *hora de se alistar*.
- Se já *passou do tempo* do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc

if idade > 18:
    print (f'Já passou do tempor do Alistamento \nVocê tem {idade} anos \nFaz {idade - 18} anos que você se alistou')
elif idade < 18:
    print (f'Você ainda vai se alistar para o serviço militar \nVocê tem {idade} anos \nFalta {18 - idade} anos para você se alistar')
elif idade == 18:
    print (f'Está no ano de você se alistar \nVocê tem {idade} anos')