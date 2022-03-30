#Faça um programa que faça o computador jogar JOKENPÔ com você.
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual sua jogada? '))
print('''JO
KEN
PÔ!!!''')
print('-=' * 15)
import random
computador = random.randint(0, 2)
if jogada == 0 and computador == 2:
    print('''Computador jogou TESOURA
Jogador jogou PEDRA''')
    print('-=' * 15)
    print('JOGADOR VENCE')
elif jogada == 0 and computador == 1:
    print('''Computador jogou PAPEL
Jogador jogou PEDRA''')
    print('-=' * 15)
    print('COMPUTADOR VENCE')
elif jogada == 0 and computador == 0:
    print('''Computador jogou PEDRA
Jogador jogou PEDRA''')
    print('-=' * 15)
    print('EMPATE')
elif jogada == 1 and computador == 2:
    print('''Computador jogou TESOURA
Jogador jogou PAPEL''')
    print('-=' * 15)
    print('COMPUTADOR VENCE')
elif jogada == 1 and computador == 1:
    print('''Computador jogou PAPEL
Jogador jogou PAPEL''')
    print('-=' * 15)
    print('EMPATE')
elif jogada == 1 and computador == 0:
    print('''Computador jogou PEDRA
Jogador jogou PAPEL''')
    print('-=' * 15)
    print('JOGADOR VENCE')
elif jogada == 2 and computador == 2:
    print('''Computador jogou TESOURA
Jogador jogou TESOURA''')
    print('-=' * 15)
    print('EMPATE')
elif jogada == 2 and computador == 1:
    print('''Computador jogou PAPEL
Jogador jogou TESOURA''')
    print('-=' * 15)
    print('JOGADOR VENCE')
elif jogada == 2 and computador == 0:
    print('''Computador jogou PEDRA
Jogador jogou TESOURA''')
    print('-=' * 15)
    print('COMPUTADOR VENCE')
