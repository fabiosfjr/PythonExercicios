#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria de acordo com a idade:
#até 9 anos: MIRIM
#até 14 anos: INFANTIL
#até 19 anos: JUNIOR
#até 25 anos: SENIOR
#acima: MASTER
from datetime import date
ano = date.today().year
nascimento = int(input('Qual o ano do seu nascimento: '))
idade = ano - nascimento
if idade <= 9:
    print('O atleta tem {} anos. Classificação: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos. Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos. Classificação: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos. Classificação: SENIOR'.format(idade))
else:
    print('O atleta tem {} anos. CLassificação: MASTER'.format(idade))





