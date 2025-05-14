#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos Km foram percorridos com o carro: '))
dias = int(input('Digite por quantos dias o carro foi alugado: '))

print(f'{'-'*20} \nNota: \nCarro: Toyota \nPreço por Km: {km} x R$0,15 = R${km * 0.15:.2f} \nPreço por dias: {dias} x R$ 60 = R${dias * 60:.2f}') 
print(f'Total: R${(km * 0.15)+(dias * 60):.2f} \n {'-'*20}')