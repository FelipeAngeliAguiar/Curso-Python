'''
Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu Preço Normal e Condição de Pagamento:
- À vista *dinheiro/cheque*: 10% de desconto
- À vista no *cartão*: 5% de desconto
- Em até *2x no cartão*: preço normal
- *3x ou mais* no cartão: 20% de juros
'''
print(f'{ ' LOJAS FELIPE ' :=^40}')
valor = float(input('Digite o valor do produto: R$'))
print('Qual vai ser a forma de pagamento? \n1- À vista (dinheiro/cheque) \n2- À vista (cartão) \n3- Em até 2x no cartão \n4- Em até 3x ou mais no cartão \n')
pgmnt = int(input('Qual a sua opção? '))

if pgmnt == 1:
    forma = 'À vista (dinheiro/cheque)'
    final = valor * 0.90
    parcelas = None
    
elif pgmnt == 2:
    forma = 'À vista (cartão)'
    final = valor * 0.95
    parcelas = None
    
elif pgmnt == 3:
    forma = 'Em até 2x no cartão'
    final = valor
    parcelas = 2
    
elif pgmnt == 4:
    forma = 'Em até 3x ou mais no cartão'
    parcelas = int(input('Quantas parcelas? '))
    final = valor * 1.20
    
else:
    forma = None
    print('Forma de pagamento inválido')

if forma != None:
    if parcelas != None:
        print(f'{'=-'*20}\nNota \nValor do produto: R${valor:.2f} \nForma de Pagamento: {forma} \nValor das Parcelas: {parcelas}x de R${final/parcelas:.2f}\nValor Final: R${final:.2f}\n{'=-'*20}')
    else:
        print(f'{'=-'*20}\nNota \nValor do produto: R${valor:.2f} \nForma de Pagamento: {forma}\nValor Final: R${final:.2f}\n{'=-'*20}')
else:
    print('Tente novamente')