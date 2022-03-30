#Crie um programa completo que leia o nome completo da pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas as letras minisculas
#quantas letras ao todo sem condiderar espaços
#Quantas letras tem o primeiro nome#
nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em maiusculas é {}'.format(nome.upper()))
print('O seu nome em minusculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))



















