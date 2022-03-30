#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do catoto adjacente: '))
h = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(h))
'''h = (co**2 + ca**2) ** (1/2)'''

