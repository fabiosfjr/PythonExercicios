#Faça um programa que leia o ângulo qualquer e mostre na sua tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
a = float(input('Digite um angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O valor do angulo é {}, portanto o seno é {:.2f}, o cosseno {:.2f} e o tangente {:.2f}'.format(a, s, c, t))

