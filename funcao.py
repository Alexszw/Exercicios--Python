#Faça um programa para imprimir:
#  1
#  2   2
#  3   3   3
#  .....
#  n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


def sequencia(n_vezes):
    for i in range(1, n_vezes + 1):
        print(f'{i} ' * i)


numero = int(input('Informe um numero: '))
sequencia(numero)
