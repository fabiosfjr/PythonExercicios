#faça um programa que leia um numero de 0 a 9999 e mostre cada um dos digitos separados
#ex: Digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
#forma matemática
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



