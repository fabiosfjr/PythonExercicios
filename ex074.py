#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão em tupla.
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}') #max mostra o maior numero aleatório de num
print(f'O menor valor sorteado foi {min(num)}') #min mostra o menor numero aleatório de num
