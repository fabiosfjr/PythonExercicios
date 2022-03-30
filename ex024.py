#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cidade = str(input('Digite o nome da cidade onde você mora: ')).strip()
print(cidade[:5].upper() == 'SANTO')
