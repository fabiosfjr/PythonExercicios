#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for ímpar, desconsidero.
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print('Você informou {} numeros PARES e a soma dos do valores é {}'.format(cont, s))
