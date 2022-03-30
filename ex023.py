#faça um programa que leia um numero de 0 a 9999 e mostre cada um dos digitos separados
#ex: Digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
num = int(input('Digite um número: '))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))







