#Refaça o ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando uma laço for
n = int(input('Digite um número para ver sua tabuada: '))
print('{:=^20}'.format(' TABUÁDA '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('=' * 20)

