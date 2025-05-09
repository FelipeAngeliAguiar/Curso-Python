#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = input("Digite o produto desejado: ")
preco = float(input(f"Digite o preço do {produto}: R$"))

print(f'{'-'*20} \nProduto: {produto} \nPreço: R${preco} \nPreço com 5% de desconto: R${preco * 0.95:.2f} \n{'-'*20}')