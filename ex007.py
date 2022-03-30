#Desenvolva um programa de veja as duas notas de um aluno, calcule e mostra sua média
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2
print('A nota 1 é {:.1f}, a nota 2 é {:.1f}. Portanto, sua média é {:.1f}'.format(n1, n2, m))

