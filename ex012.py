# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: '))
d = p - (p * 0.05)
print('Preço do produto: {:.2f}\n Preço com desconto de 5%: {:.2f}'.format(p, d))


