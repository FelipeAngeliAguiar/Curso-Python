#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
#pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Quantos metros de largura tem a parede? '))
altura = float(input('Quantos metros de altura tem a parede? '))

print(f'Sua parede tem a área de {(largura*altura)}m² \nEntão para pintar totalmente a sua parede vamos precisar de {(largura*altura)/2:.2f}L de tinta')