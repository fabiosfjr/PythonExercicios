# elabore um programa que calcule o valor a ser pago por um produto considerando o seu PREÇO NORMAL e CONDIÇÃO DE
# PAGAMENTO.
# À vista no dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GUANABARA '))
p = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
o = int(input('Qual a opção? '))
if o == 1:
    desconto = p - (p * 0.10)
    print('A sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, desconto))
elif o == 2:
    desconto = p - (p * 0.05)
    print('A sua compra de R${:.2f} vai custar R${:.2f} no final'.format(p, desconto))
elif o == 3:
    parcela = p / 2
    print('A sua compra {:.2f} será parcelada em 2x de {:.2f} SEM JUROS.'.format(p, parcela))
elif o == 4:
    q = int(input('Quantas parcelas? '))
    total = p + (p * 0.20)
    parcela = total / q
    print('''A sua compra será parcelada em {}x de R${:.2f} COM JUROS.
Sua compra de R${:.2f} vai custar R${:.2f} no final.'''.format(q, parcela, p, total))



