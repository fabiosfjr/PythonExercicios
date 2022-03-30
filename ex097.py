# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(texto):
    print(f'~' * len(texto))
    print(texto)
    print(f'~' * len(texto))


escreva(' Gustavo Guanabara ')
escreva(' Curso de Python no Youtube ')
escreva(' CeV ')
