#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar
#-Se é a hora de se alistar
#-Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano = date.today().year
nascimento = int(input('Qual o ano nascimento: '))
idade = ano - nascimento
if idade == 18:
    print('Quem nasceu em {} tem {} anos em 2021. Você tem que se alistar IMEDIATAMENTE.'.format(nascimento, idade))
elif idade > 18:
    print('Já passou o tempo do alistamento militar. Procure o EXÉRCITO BRASILEIRO!')
elif idade < 18:
    faltam = 18 - idade
    alistamento = nascimento + 18
    print('Quem nasceu em {} tem {} anos em 2021. Ainda faltam {} anos para o alistamento. Seu alistamento será em {}'.format(nascimento, idade, faltam, alistamento))
