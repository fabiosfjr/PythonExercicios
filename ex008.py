#Escreva um programa que leia o valor dele em metros e o exiba convertido em centímetros e milímetros
metro = int(input('Digite um número: '))
c = metro * 100
m = metro * 1000
print('Ele tem {} metros, portanto tem {} centrimetros e {} milimetros'.format(metro, c, m))
