'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta3 >= (reta1 + reta2) or reta1 >= (reta2 + reta3) or reta2 >= (reta1 + reta3):
    print('Não dá para formar um triângulo!')
elif reta3 == reta2 == reta1:
    print('Dá para formar um triângulo equilátero!')
elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
    print('Dá para formar um triângulo isósceles!')
else:
    print('Dá para formar um triângulo escaleno!')