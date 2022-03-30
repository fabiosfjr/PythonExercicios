#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
#a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$10 e $1.
print('=' * 30)
print('{:^30}'.format('BANCO FÁBIO FERREIRA'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        print(f'Total de {totcedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO FÁBIO FERREIRA. Tenha um bom dia!')
