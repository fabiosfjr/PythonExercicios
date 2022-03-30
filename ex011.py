#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quantidade de tinta, sabendo que cada litro de tinta pinta uma area de 2m²
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A area da parede é {}m², portanto será necessário {} litros de tinta para pintar a parede.'.format(area, tinta))


