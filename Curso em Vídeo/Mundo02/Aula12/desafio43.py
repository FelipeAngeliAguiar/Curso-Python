'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade 
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

if imc <= 18.5:
    resultado = 'Abaixo do Peso'
elif imc > 18.5 and imc <= 25:
    resultado = 'Peso Ideal'
elif imc > 25 and imc <= 30:
    resultado = 'Sobrepeso'
elif imc > 30 and imc <= 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade Mórbida'
    
print(f'Seu IMC é: {imc:.2f} \nResultado: {resultado}')