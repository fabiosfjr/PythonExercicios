#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informçãoes possíveis sobre ela.
n1 = (input('Digite algo: '))
print('O tipo primitivo desse valor é', type(n1))
print('Só tem espaços ?', n1.isspace())
print('É um número? ', n1.isnumeric())
print('É alfabético? ', n1.isalpha())
print('É alfanumérico? ', n1.isalnum())
print('Está em maiúsculas? ', n1.isupper())
print('Está em minusculas? ', n1.islower())
print('Está capitalizada? ', n1.istitle())











