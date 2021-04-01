# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.
n1 = int(input("Digite um número inteiro :"))
n2 = int(input("Digite outro número inteiro :"))
n3 = float(input("Digite umnúmero real :"))
produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
potencia = n3 ** 3
print(f"O produto do dobro do primeiro número com metade do segundo número é : {produto}")
print(f"A soma do triplo do primeiro número com o terceiro número é : {soma}")
print(f"O terceiro número elevado ao cubo é : {potencia}")

