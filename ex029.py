#Escreva um programa que que leia a velocidade de um carro. Se ele ultrapassar a velocidade de 80km/h, mostre uma
#mensagem que ele foi multado. A multa vai custar R$ 7,00  por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro: '))
if velocidade >80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
else:
    print('Parabéns, você está na velocidade permitida pela via!')
