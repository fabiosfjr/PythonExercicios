#desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. no final,
#mostre os 10 primeiros termos dessa progressão.
print('=' * 40)
print('{:^40}'.format(' 10 TERMOS DE UMA P.A '))
print('=' * 40)
termo = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' - ')
print('ACABOU')

