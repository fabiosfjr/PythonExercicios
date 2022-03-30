# Faça um programa que leia nome e média de um aluno, guardando também a situação (APROVADO OU REPROVADO) em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('==' * 20)
for k, v in aluno.items():
    print(f' ==> {k} é igual {v}.')



