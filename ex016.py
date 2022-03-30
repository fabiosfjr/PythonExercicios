#Crie um programa que leia um numero Real qualquer pelo teclado e digite a sua porção inteira
#Ex: Digite um numero: 6.127
#O número 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('Digite um numero: '))
print('O numero {} tem a sua porção inteira {}'.format(num, trunc(num)))



