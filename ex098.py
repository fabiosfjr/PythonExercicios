# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for num in range(1, 11):
        print(f' {num} ', end='')
        sleep(1)
    print('FIM!')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(f' {c} ', end='')
        sleep(1)
    print('FIM!')
    print('-=' * 20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=' * 20)
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    for p in range(inicio, fim + 1, passo):
        print(f' {p} ', end='')
        sleep(1)
    print('FIM!')
    print('-=' * 20)


contador()
