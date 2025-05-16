'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ele aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()

print(f'Frase: {frase.title()} \nQuantidades  de A: {frase.count('a')} \nPrimeiro A: {frase.find('a')+1} \nÚltimo A: {frase.rfind('a')+1}')