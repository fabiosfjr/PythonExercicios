#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
nome = str(input('Qual seu nome: '))
altura = float(input('Qual sua altura em metros: '))
peso = float(input('Qual seu peso em kg: '))
imc = peso / (altura * altura)
print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('{}, você está ABAIXO DO PESO'.format(nome))
elif 18.5 <= imc < 25:
    print('{}, você está no PESO IDEAL'.format(nome))
elif 25 <= imc < 30:
    print('{}, você está no SOBREPESO'.format(nome))
elif 30 <= imc < 40:
    print('{}, você está na OBESIDADE'.format(nome))
elif imc > 40:
    print('{}, você está com OBESIDADE MÓRBIDA.'.format(nome))











