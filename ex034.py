#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário atual: '))
if salario > 1250.00:
    novo = salario + (salario * 0.10)
else:
    novo = salario + (salario * 0.15)
print('O seu salário teve um aumento, portanto será R$ {:.2f}'.format(novo))
