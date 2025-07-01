'''Faça um programa que tenha uma função chamada escreva,
    que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável'''
    
def escreva(txt):
    comp = len(txt)+4
    print(f'{'~'*comp}')
    print(f'{txt:^{comp}}')
    print(f'{'~'*comp}')

texto = str(input('Digite qualquer texto: ')).strip()
escreva(texto)