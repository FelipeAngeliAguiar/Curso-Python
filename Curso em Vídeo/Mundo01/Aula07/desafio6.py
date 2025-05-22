#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))

print(f'Número: {n1} \nDobro: {n1*2}\nTriplo: {n1*3}\nRaiz Quadrada: {pow(n1, (0.5)):.2f}')