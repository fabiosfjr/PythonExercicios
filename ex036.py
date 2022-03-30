#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
#não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor do casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Quantos anos de financiamento? '))
pr = casa / (anos * 12)
if pr <= salario - (salario * 0.30):
    print('O seu empréstimo bancário foi APROVADO. A sua parcela será de R$ {:.2f} e você pagará em {} anos.'.format(pr, anos))
else:
    print('EMPRÉSTIMO NEGADO! O valor da parcela ultrapassa 30% do valor do seu salário')
print('OBRIGADO PELA PREFERÊNCIA EM SOLICITAR O EMPRÉSTIMO CONOSCO')


