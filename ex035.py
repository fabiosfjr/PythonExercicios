#Desenvolva um programa que leia o comprimento de três retas e diga ou não se elas podem formar um triangulo
r1 = int(input('Digite a medida da reta 1: '))
r2 = int(input('Digite a medida da reta 2: '))
r3 = int(input('Digite a medida da reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triângulo')

