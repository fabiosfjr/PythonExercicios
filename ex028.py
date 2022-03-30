#Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5 e peça para o usuário tentar
#descobrir qual o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário perdeu ou vendeu
import random
num = random.randint(0, 5)
escolhido = int(input('Digite o numero de 0 a 5 que você acha que foi escolhido pelo programa: '))
print('O numero escolhido pelo programa foi {}'.format(num))
if escolhido == num:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')
