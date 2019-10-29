#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# é divisível somente por ele mesmo e por 1.
numero = int(input('Digite um número inteiro :'))
contador = 0
if (numero % 1) == 0 :
    for n in range(1,numero +1) :
        if (numero % n) == 0 :
           


else :
    print('Número inválido!')