'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizadno um laço for'''

n1 = int(input('Digite um número que irei dizer a tabuada do mesmo: '))

for c in range(1, 11):
    print(f'{n1:<3} {'x':^3} {c:>3} {'=':^3} {c*n1 :>4}')