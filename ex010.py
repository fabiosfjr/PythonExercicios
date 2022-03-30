#Crie um programa que mostre quanto dinheiro ela tem na carteira e mostre quantos dolores (US$ 1.00 = R$ 3,27) ela pode comprar
reais = float(input('Digite quantos reais você tem na carteira: R$ '))
dolar = reais / 3.27
print('Você pode comprar {:.2f} dolares'.format(dolar))
