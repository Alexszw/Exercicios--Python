#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
#cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quantidade = int(input('Qual a quantidade de CDs de sua coleção :'))
valor_total = 0
valor_unitario = 0
for n in range(0,quantidade) :
    valor_unitario = float(input('Digite o valor de um CD :'))
    valor_total += valor_unitario
media = valor_total/quantidade
print(f'A média do valor dos CDs é {media} e o valor total é {valor_total}')