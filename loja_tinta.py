#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
#cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float(input("Informe a área a ser pintada em metros quadrados : "))
import math
quantidade_de_latas = math.ceil((area / 3) / 18)
preco_total = quantidade_de_latas * 80
print(f"A quantidade de latas a serem compradas é : {quantidade_de_latas}")
print(f"E o preço total é de : R$ {preco_total} ")
