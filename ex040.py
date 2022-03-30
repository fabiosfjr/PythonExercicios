#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
#com a média atingida.
#Média abaixo de 5,0: REPROVADO
#Média entre 5,0 e 6,9: RECUPERAÇÃO
#Média 7,0 ou superior: APROVADO
nome = str(input('Qual seu nome? '))
n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, sua média é {:.1f}.'.format(n1, n2, media))
if media >= 7.0:
    print('Parabéns, {}. Você foi APROVADO'.format(nome))
elif media < 5.0:
    print('REPROVADO. {}, você precisa estudar mais.'.format(nome))
elif 7 > media >= 5:
    print('{}, você está de RECUPERAÇÃO!'.format(nome))
