#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado.
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
r1 = int(input('Digite a medida da reta 1: '))
r2 = int(input('Digite a medida da reta 2: '))
r3 = int(input('Digite a medida da reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')


