#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte.
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
digite = int(input('Digite um número entre 0 e 20: '))
while digite > 20 or digite < 0:
    digite = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num[digite]}')
