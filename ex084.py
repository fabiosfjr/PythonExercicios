#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves
dados = list()
pessoas = list()
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados [1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maiorpeso} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menorpeso} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]} ', end='')