#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$ 0,50 por Km para viagens até 200km e R$ 0,45 para viagens mais longas
viagem = float(input('Digite a distânia da viagem em Km: '))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('O preço da passagem é R$ {:.2f}'.format(preço))
print('BOA VIAGEM!')
