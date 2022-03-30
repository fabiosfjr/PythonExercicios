#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido
from random import choice
a1 = str(input('Digite um nome: '))
a2 = str(input('Digite o segundo nome: '))
a3 = str(input('Digite o terceiro nome: '))
a4 = str(input('Digite o quarto nome: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido para apagar o quadro é {}!'.format(escolhido))




